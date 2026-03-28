#!/usr/bin/env python3
"""Sustainability Calculator -- comp-sustainability-reporting bundled script.

Calculates Scope 1/2/3 carbon emissions, PUE/WUE/CUE efficiency metrics, and
benchmark comparisons for data center facilities. Supports location-based and
market-based Scope 2 accounting per GHG Protocol.

Methodology:
  - Scope 1: On-site combustion emissions (gas/diesel generators).
    Gas: 0.91 lbs CO2/kWh * gen_mw * gen_hours * 0.000453592 = tCO2e.
    Diesel: 1.21 lbs CO2/kWh equivalent.
  - Scope 2 (location-based): grid_carbon_intensity * total_facility_mw * 8760 / 1000.
    Grid carbon intensities from POWER-TARIFFS.md regional data.
  - Scope 2 (market-based): location_based - (rec_mwh * grid_intensity / 1000).
    Cannot go below zero.
  - PUE: Input validated (must be >= 1.0, flagged if > 2.0).
  - WUE: water_gallons * 3.78541 / (it_load_mw * 8760 * 1000) = L/kWh.
  - CUE: scope_1_tco2e * 1000 / (it_load_mw * 8760) = kgCO2/kWh.

Data sources:
  - Grid carbon intensity: Representative values from IEA, EPA eGRID, EEA.
  - Emission factors: EPA Emission Factors Hub (2024).
  - WUE benchmarks: The Green Grid, Uptime Institute Annual Survey.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 sustainability-calculator.py --help
    python3 sustainability-calculator.py \\
        --it-load-mw 10 --pue 1.3 --location US-TX \\
        --water-gallons 50000000 --gen-type gas --gen-mw 5 \\
        --gen-hours 8760 --cooling-type hybrid --rec-mwh 0
"""

import argparse
import json
import sys


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Representative grid carbon intensities (kg CO2/MWh) by region.
# Sources: IEA World Energy Outlook 2024, EPA eGRID 2023, EEA 2023.
GRID_CARBON_INTENSITY = {
    "US-TX": 380,    # ERCOT (gas-heavy)
    "US-VA": 310,    # PJM (mixed)
    "US-CA": 210,    # CAISO (renewables + gas)
    "US-GA": 370,    # SERC (coal + gas)
    "US-IL": 280,    # MISO (nuclear + gas + wind)
    "US-WA": 80,     # Pacific NW (hydro-dominant)
    "US-OR": 120,    # Pacific NW (hydro + gas)
    "EU-DE": 350,    # Germany (coal phase-out in progress)
    "EU-FR": 55,     # France (nuclear-dominant)
    "EU-NO": 15,     # Norway (hydro-dominant)
    "EU-SE": 25,     # Sweden (hydro + nuclear)
    "EU-NL": 330,    # Netherlands (gas-heavy)
    "EU-IE": 290,    # Ireland (gas + wind)
    "EU-ES": 170,    # Spain (renewables growth)
    "EU-PL": 650,    # Poland (coal-dominant)
    "UK": 200,       # UK (gas + wind + nuclear)
    "SG": 400,       # Singapore (gas-dominant)
    "JP": 450,       # Japan (LNG + coal)
    "AU": 550,       # Australia (coal + gas)
    "IN": 700,       # India (coal-dominant)
    "BR": 80,        # Brazil (hydro-dominant)
    "CL": 300,       # Chile (coal + solar growth)
    "ZA": 900,       # South Africa (coal-dominant)
    "AE": 420,       # UAE (gas-dominant)
    "SA": 500,       # Saudi Arabia (oil + gas)
    "KE": 100,       # Kenya (geothermal + hydro)
}

# European residual mix for market-based Scope 2 when no RECs are purchased
EU_RESIDUAL_MIX_KG_PER_MWH = 450

# Emission factors for on-site generation
GAS_LBS_CO2_PER_KWH = 0.91
DIESEL_LBS_CO2_PER_KWH = 1.21
LBS_TO_TONNES = 0.000453592  # lbs to metric tonnes

# WUE benchmarks by cooling type (L/kWh)
WUE_BENCHMARKS = {
    "air": {"low": 0.0, "high": 0.5, "label": "Air-cooled"},
    "liquid": {"low": 0.0, "high": 0.3, "label": "Direct liquid cooling"},
    "hybrid": {"low": 0.5, "high": 1.5, "label": "Hybrid air + liquid"},
    "evaporative": {"low": 1.5, "high": 2.5, "label": "Evaporative/adiabatic"},
    "immersion": {"low": 0.0, "high": 0.2, "label": "Immersion cooling"},
}

HOURS_PER_YEAR = 8760


# ---------------------------------------------------------------------------
# Calculation functions
# ---------------------------------------------------------------------------

def calculate_scope_1(gen_type: str, gen_mw: float, gen_hours: float) -> float:
    """Calculate Scope 1 emissions from on-site combustion (tCO2e).

    Args:
        gen_type: Generator fuel type ('gas', 'diesel', 'none').
        gen_mw: Generator capacity in MW.
        gen_hours: Annual operating hours.

    Returns:
        Scope 1 emissions in metric tonnes CO2 equivalent.
    """
    if gen_type == "none" or gen_mw <= 0 or gen_hours <= 0:
        return 0.0

    if gen_type == "gas":
        emission_factor = GAS_LBS_CO2_PER_KWH
    elif gen_type == "diesel":
        emission_factor = DIESEL_LBS_CO2_PER_KWH
    else:
        # Unknown type -- use gas as conservative estimate
        emission_factor = GAS_LBS_CO2_PER_KWH

    # gen_mw * 1000 (kW) * gen_hours * emission_factor (lbs/kWh) * lbs_to_tonnes
    generation_kwh = gen_mw * 1000 * gen_hours
    emissions_lbs = generation_kwh * emission_factor
    return round(emissions_lbs * LBS_TO_TONNES, 2)


def calculate_scope_2(
    it_load_mw: float,
    pue: float,
    location: str,
    rec_mwh: float,
) -> dict:
    """Calculate Scope 2 emissions -- location-based and market-based (tCO2e).

    Args:
        it_load_mw: IT load in MW.
        pue: Power Usage Effectiveness (>= 1.0).
        location: Region code matching GRID_CARBON_INTENSITY keys.
        rec_mwh: Renewable Energy Certificates purchased (MWh/year).

    Returns:
        Dict with location_based_tco2e, market_based_tco2e, grid_intensity.
    """
    total_facility_mw = it_load_mw * pue
    annual_mwh = total_facility_mw * HOURS_PER_YEAR

    # Grid carbon intensity lookup
    grid_intensity = GRID_CARBON_INTENSITY.get(location, 400)  # default 400 if unknown

    # Location-based: grid_intensity (kg/MWh) * annual_mwh / 1000 (kg to tonnes)
    location_based = grid_intensity * annual_mwh / 1000

    # Market-based: location_based minus REC offsets
    rec_offset = rec_mwh * grid_intensity / 1000
    market_based = max(location_based - rec_offset, 0)

    return {
        "location_based_tco2e": round(location_based, 2),
        "market_based_tco2e": round(market_based, 2),
        "grid_intensity_kg_per_mwh": grid_intensity,
        "annual_facility_mwh": round(annual_mwh, 1),
    }


def calculate_wue(
    water_gallons: float,
    it_load_mw: float,
) -> float:
    """Calculate Water Usage Effectiveness (L/kWh).

    Args:
        water_gallons: Annual water consumption in US gallons.
        it_load_mw: IT load in MW.

    Returns:
        WUE in liters per kWh.
    """
    if it_load_mw <= 0:
        return 0.0
    water_liters = water_gallons * 3.78541
    it_energy_kwh = it_load_mw * HOURS_PER_YEAR * 1000
    return round(water_liters / it_energy_kwh, 4)


def calculate_cue(scope_1_tco2e: float, it_load_mw: float) -> float:
    """Calculate Carbon Usage Effectiveness (kgCO2/kWh).

    Args:
        scope_1_tco2e: Scope 1 emissions in metric tonnes CO2e.
        it_load_mw: IT load in MW.

    Returns:
        CUE in kg CO2 per kWh of IT energy.
    """
    if it_load_mw <= 0:
        return 0.0
    scope_1_kg = scope_1_tco2e * 1000
    it_energy_kwh = it_load_mw * HOURS_PER_YEAR
    return round(scope_1_kg / it_energy_kwh, 4)


def validate_inputs(
    it_load_mw: float,
    pue: float,
    location: str,
    cooling_type: str,
    wue: float,
) -> list:
    """Validate inputs and return list of warnings."""
    warnings = []

    if pue < 1.0:
        warnings.append(
            f"PUE {pue} is below 1.0 (physically impossible). "
            "Check input -- PUE must be >= 1.0."
        )
    elif pue > 2.0:
        warnings.append(
            f"PUE {pue} is unusually high (>2.0). "
            "Verify this is correct -- modern facilities typically achieve 1.1-1.6."
        )

    if location not in GRID_CARBON_INTENSITY:
        warnings.append(
            f"Location '{location}' not in grid intensity lookup table. "
            f"Using default 400 kg CO2/MWh. Known locations: {', '.join(sorted(GRID_CARBON_INTENSITY.keys()))}"
        )

    if cooling_type in WUE_BENCHMARKS:
        bench = WUE_BENCHMARKS[cooling_type]
        if wue > bench["high"] * 1.5:
            warnings.append(
                f"WUE {wue:.4f} L/kWh is significantly above typical range for "
                f"{bench['label']} ({bench['low']}-{bench['high']} L/kWh). "
                "Verify water consumption input."
            )
    elif cooling_type not in WUE_BENCHMARKS:
        warnings.append(
            f"Cooling type '{cooling_type}' not recognized. "
            f"Known types: {', '.join(WUE_BENCHMARKS.keys())}"
        )

    if it_load_mw <= 0:
        warnings.append("IT load must be greater than 0 MW.")

    return warnings


def run_calculation(args: argparse.Namespace) -> dict:
    """Execute the full sustainability calculation.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Complete results dict suitable for JSON serialization.
    """
    it_load_mw = args.it_load_mw
    pue = args.pue
    location = args.location
    water_gallons = args.water_gallons
    gen_type = args.gen_type
    gen_mw = args.gen_mw
    gen_hours = args.gen_hours
    cooling_type = args.cooling_type
    rec_mwh = args.rec_mwh

    # Calculate total facility power
    total_facility_mw = it_load_mw * pue

    # Scope 1: on-site combustion
    scope_1 = calculate_scope_1(gen_type, gen_mw, gen_hours)

    # Scope 2: grid electricity
    scope_2 = calculate_scope_2(it_load_mw, pue, location, rec_mwh)

    # Efficiency metrics
    wue = calculate_wue(water_gallons, it_load_mw)
    cue = calculate_cue(scope_1, it_load_mw)

    # Validate inputs
    warnings = validate_inputs(it_load_mw, pue, location, cooling_type, wue)

    # Total carbon (using location-based Scope 2 for total)
    total_location = scope_1 + scope_2["location_based_tco2e"]
    total_market = scope_1 + scope_2["market_based_tco2e"]

    # WUE benchmark comparison
    wue_benchmark = "unknown"
    if cooling_type in WUE_BENCHMARKS:
        bench = WUE_BENCHMARKS[cooling_type]
        if wue <= bench["low"] + (bench["high"] - bench["low"]) * 0.33:
            wue_benchmark = "excellent"
        elif wue <= bench["high"]:
            wue_benchmark = "good"
        else:
            wue_benchmark = "above_average"

    # PUE benchmark
    if pue < 1.2:
        pue_benchmark = "excellent"
    elif pue <= 1.4:
        pue_benchmark = "good"
    elif pue <= 1.6:
        pue_benchmark = "average"
    else:
        pue_benchmark = "below_average"

    return {
        "carbon": {
            "scope_1_tco2e": scope_1,
            "scope_2_location_tco2e": scope_2["location_based_tco2e"],
            "scope_2_market_tco2e": scope_2["market_based_tco2e"],
            "scope_3_tco2e": None,  # Requires additional data; not calculated by this script
            "total_location_tco2e": round(total_location, 2),
            "total_market_tco2e": round(total_market, 2),
            "grid_intensity_kg_per_mwh": scope_2["grid_intensity_kg_per_mwh"],
        },
        "efficiency": {
            "pue": pue,
            "pue_benchmark": pue_benchmark,
            "wue_l_per_kwh": wue,
            "wue_benchmark": wue_benchmark,
            "cue_kg_per_kwh": cue,
        },
        "facility": {
            "it_load_mw": it_load_mw,
            "total_facility_mw": round(total_facility_mw, 2),
            "annual_facility_mwh": scope_2["annual_facility_mwh"],
            "location": location,
            "cooling_type": cooling_type,
            "water_gallons_per_year": water_gallons,
            "on_site_generation": {
                "type": gen_type,
                "capacity_mw": gen_mw,
                "annual_hours": gen_hours,
            },
            "rec_mwh": rec_mwh,
        },
        "benchmarks": {
            "pue_range": "1.1-1.6 (modern DC typical)",
            "wue_range_for_cooling": (
                f"{WUE_BENCHMARKS[cooling_type]['low']}-{WUE_BENCHMARKS[cooling_type]['high']} L/kWh"
                if cooling_type in WUE_BENCHMARKS
                else "unknown cooling type"
            ),
            "cue_range": "0.00-0.20 kgCO2/kWh (lower is better)",
        },
        "warnings": warnings,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Sustainability calculator for data center carbon accounting and "
            "efficiency metrics. Calculates Scope 1/2 emissions, PUE, WUE, CUE."
        ),
        epilog=(
            "Examples:\n"
            "  python3 sustainability-calculator.py --it-load-mw 10 --pue 1.3 "
            "--location US-TX --water-gallons 50000000 --gen-type gas --gen-mw 5 "
            "--gen-hours 8760 --cooling-type hybrid --rec-mwh 0\n"
            "\n"
            "  python3 sustainability-calculator.py --it-load-mw 50 --pue 1.15 "
            "--location EU-NO --water-gallons 5000000 --gen-type none --cooling-type liquid\n"
            "\nPart of comp-sustainability-reporting skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--it-load-mw", type=float, required=True,
        help="IT load in MW",
    )
    parser.add_argument(
        "--pue", type=float, required=True,
        help="Power Usage Effectiveness (>= 1.0)",
    )
    parser.add_argument(
        "--location", type=str, required=True,
        help=(
            "Region code for grid carbon intensity "
            f"(known: {', '.join(sorted(GRID_CARBON_INTENSITY.keys()))})"
        ),
    )
    parser.add_argument(
        "--water-gallons", type=float, default=0,
        help="Annual water consumption in US gallons (default: 0)",
    )
    parser.add_argument(
        "--gen-type", type=str, choices=["gas", "diesel", "none"], default="none",
        help="On-site generator fuel type (default: none)",
    )
    parser.add_argument(
        "--gen-mw", type=float, default=0,
        help="On-site generator capacity in MW (default: 0)",
    )
    parser.add_argument(
        "--gen-hours", type=float, default=0,
        help="Annual generator operating hours (default: 0)",
    )
    parser.add_argument(
        "--cooling-type", type=str,
        choices=list(WUE_BENCHMARKS.keys()),
        default="air",
        help=f"Cooling system type (default: air)",
    )
    parser.add_argument(
        "--rec-mwh", type=float, default=0,
        help="Renewable Energy Certificates purchased annually in MWh (default: 0)",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()
    result = run_calculation(args)
    output_json = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
