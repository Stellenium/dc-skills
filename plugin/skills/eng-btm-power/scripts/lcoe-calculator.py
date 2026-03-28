#!/usr/bin/env python3
"""LCOE Calculator -- eng-btm-power bundled script.

Unified Levelized Cost of Energy calculator for behind-the-meter data center
power generation. Supports natural gas, solar PV, wind, BESS, fuel cells,
and SMR. Models hybrid configurations with blended LCOE, ITC/PTC tax credit
optimization, and grid cost comparison.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 lcoe-calculator.py --help
    python3 lcoe-calculator.py --input btm-inputs.json --output btm-results.json
    python3 lcoe-calculator.py --facility-load-mw 20 --grid-tariff 65
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Post-OBBBA (effective July 4, 2025) default rates with prevailing wage
DEFAULT_ITC_RATE = 0.30        # 30% ITC for solar, BESS, fuel cells
DEFAULT_PTC_RATE_MWH = 28.60   # $/MWh PTC for wind (2025 inflation-adjusted)
DEFAULT_DISCOUNT_RATE = 0.08   # 8% WACC

# ITC-eligible source types (receive upfront capex reduction)
ITC_ELIGIBLE = {"solar", "bess", "fuel_cell"}
# PTC-eligible source types (receive per-MWh credit)
PTC_ELIGIBLE = {"wind", "smr"}

# MACRS 5-year depreciation schedule (percentages)
MACRS_5YR = [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class EnergySource:
    """A single BTM energy source configuration."""
    source_type: str          # gas, solar, wind, bess, fuel_cell, smr
    capacity_mw: float        # nameplate capacity in MW
    capex_per_kw: float       # capital cost $/kW
    opex_per_kw_yr: float     # annual O&M $/kW/yr
    fuel_cost_per_mwh: float = 0.0   # fuel cost $/MWh (gas, fuel_cell)
    capacity_factor: float = 0.0     # 0-1.0 (not applicable to BESS)
    degradation_rate: float = 0.005  # annual degradation (default 0.5%)
    lifetime_years: int = 25         # project/asset lifetime
    storage_hours: float = 0.0       # BESS: duration in hours
    cycles_per_year: float = 0.0     # BESS: charge/discharge cycles


@dataclass
class BTMInput:
    """Complete input for a BTM power assessment."""
    facility_load_mw: float = 10.0
    sources: list = field(default_factory=list)  # list of EnergySource dicts
    discount_rate: float = DEFAULT_DISCOUNT_RATE
    itc_rate: float = DEFAULT_ITC_RATE
    ptc_rate_per_mwh: float = DEFAULT_PTC_RATE_MWH
    grid_tariff_per_mwh: float = 65.0   # grid cost $/MWh
    escalation_rate: float = 0.03        # annual grid cost escalation
    corporate_tax_rate: float = 0.21


@dataclass
class SourceResult:
    """LCOE result for a single energy source."""
    source_type: str
    capacity_mw: float
    lcoe_per_mwh: float
    annual_generation_mwh: float
    total_capex: float
    annual_opex: float
    annual_fuel: float
    tax_credit_type: str        # "ITC", "PTC", or "none"
    tax_credit_value: float     # total ITC $ or annual PTC $
    lcoe_before_credits: float
    lcoe_after_credits: float


@dataclass
class BTMResult:
    """Complete BTM assessment result."""
    source_lcoes: dict                # source_type -> LCOE $/MWh
    blended_lcoe: float
    grid_lcoe: float
    savings_vs_grid_pct: float
    itc_benefit_total: float
    ptc_benefit_annual: float
    total_btm_capacity_mw: float
    total_annual_generation_mwh: float
    total_capex: float
    recommended_config: str
    confidence_range_low: float
    confidence_range_high: float
    source_details: list              # list of SourceResult dicts
    hybrid_blended_lcoe: float


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_crf(discount_rate: float, lifetime_years: int) -> float:
    """Capital Recovery Factor: r(1+r)^n / ((1+r)^n - 1)."""
    if discount_rate <= 0:
        return 1.0 / lifetime_years
    r = discount_rate
    n = lifetime_years
    numerator = r * (1 + r) ** n
    denominator = (1 + r) ** n - 1
    return numerator / denominator


def calculate_source_lcoe(
    source: EnergySource,
    itc_rate: float,
    ptc_rate_per_mwh: float,
    discount_rate: float,
    corporate_tax_rate: float,
) -> SourceResult:
    """Calculate LCOE for a single energy source.

    LCOE = (CapEx * CRF + Annual OpEx + Annual Fuel - Amortized Tax Credits)
           / Annual Generation

    ITC reduces effective capex upfront; PTC reduces cost per MWh over lifetime.
    """
    capacity_kw = source.capacity_mw * 1000
    total_capex = capacity_kw * source.capex_per_kw
    annual_opex = capacity_kw * source.opex_per_kw_yr
    lifetime = source.lifetime_years

    crf = calculate_crf(discount_rate, lifetime)

    # Annual generation accounting for degradation (average over lifetime)
    if source.source_type == "bess":
        # BESS: generation = capacity * hours * cycles * (1 - avg degradation)
        avg_degradation = 1 - (source.degradation_rate * lifetime / 2)
        annual_generation = (
            source.capacity_mw * source.storage_hours
            * source.cycles_per_year * avg_degradation * 1000  # MWh
        )
        if annual_generation <= 0:
            # Fallback: assume 365 cycles, 4-hour duration
            hours = source.storage_hours if source.storage_hours > 0 else 4.0
            cycles = source.cycles_per_year if source.cycles_per_year > 0 else 365
            avg_deg = 1 - (source.degradation_rate * lifetime / 2)
            annual_generation = source.capacity_mw * hours * cycles * avg_deg
    else:
        # Standard generation source
        hours_per_year = 8760
        avg_degradation = 1 - (source.degradation_rate * lifetime / 2)
        annual_generation = (
            source.capacity_mw * source.capacity_factor
            * hours_per_year * avg_degradation
        )

    if annual_generation <= 0:
        return SourceResult(
            source_type=source.source_type,
            capacity_mw=source.capacity_mw,
            lcoe_per_mwh=float("inf"),
            annual_generation_mwh=0,
            total_capex=total_capex,
            annual_opex=annual_opex,
            annual_fuel=0,
            tax_credit_type="none",
            tax_credit_value=0,
            lcoe_before_credits=float("inf"),
            lcoe_after_credits=float("inf"),
        )

    # Annual fuel cost
    annual_fuel = source.fuel_cost_per_mwh * annual_generation

    # LCOE before tax credits
    annualized_capex = total_capex * crf
    lcoe_before = (annualized_capex + annual_opex + annual_fuel) / annual_generation

    # Tax credits
    tax_credit_type = "none"
    tax_credit_value = 0.0
    annual_tax_credit = 0.0

    if source.source_type in ITC_ELIGIBLE:
        tax_credit_type = "ITC"
        tax_credit_value = total_capex * itc_rate
        # ITC reduces depreciable basis by 50% of credit
        # Amortize the net capex reduction over lifetime
        annual_tax_credit = tax_credit_value * crf
    elif source.source_type in PTC_ELIGIBLE:
        tax_credit_type = "PTC"
        annual_tax_credit = ptc_rate_per_mwh * annual_generation
        tax_credit_value = annual_tax_credit  # annual value

    # LCOE after tax credits
    lcoe_after = (
        (annualized_capex + annual_opex + annual_fuel - annual_tax_credit)
        / annual_generation
    )
    lcoe_after = max(lcoe_after, 0)  # floor at zero

    return SourceResult(
        source_type=source.source_type,
        capacity_mw=source.capacity_mw,
        lcoe_per_mwh=round(lcoe_after, 2),
        annual_generation_mwh=round(annual_generation, 1),
        total_capex=round(total_capex, 2),
        annual_opex=round(annual_opex, 2),
        annual_fuel=round(annual_fuel, 2),
        tax_credit_type=tax_credit_type,
        tax_credit_value=round(tax_credit_value, 2),
        lcoe_before_credits=round(lcoe_before, 2),
        lcoe_after_credits=round(lcoe_after, 2),
    )


def calculate_blended_lcoe(source_results: List[SourceResult]) -> float:
    """Compute generation-weighted blended LCOE across all sources."""
    total_gen = sum(s.annual_generation_mwh for s in source_results)
    if total_gen <= 0:
        return 0.0
    weighted = sum(
        s.lcoe_per_mwh * s.annual_generation_mwh for s in source_results
        if s.lcoe_per_mwh != float("inf")
    )
    return round(weighted / total_gen, 2)


def calculate_btm(inputs: BTMInput) -> BTMResult:
    """Run the full BTM power assessment calculation."""
    # Parse sources
    sources = []
    for s in inputs.sources:
        if isinstance(s, dict):
            sources.append(EnergySource(**s))
        elif isinstance(s, EnergySource):
            sources.append(s)

    if not sources:
        return BTMResult(
            source_lcoes={},
            blended_lcoe=0,
            grid_lcoe=inputs.grid_tariff_per_mwh,
            savings_vs_grid_pct=0,
            itc_benefit_total=0,
            ptc_benefit_annual=0,
            total_btm_capacity_mw=0,
            total_annual_generation_mwh=0,
            total_capex=0,
            recommended_config="No BTM sources configured",
            confidence_range_low=0,
            confidence_range_high=0,
            source_details=[],
            hybrid_blended_lcoe=0,
        )

    # Calculate LCOE for each source
    results = []
    for source in sources:
        result = calculate_source_lcoe(
            source=source,
            itc_rate=inputs.itc_rate,
            ptc_rate_per_mwh=inputs.ptc_rate_per_mwh,
            discount_rate=inputs.discount_rate,
            corporate_tax_rate=inputs.corporate_tax_rate,
        )
        results.append(result)

    # Aggregate results
    source_lcoes = {r.source_type: r.lcoe_per_mwh for r in results}
    blended = calculate_blended_lcoe(results)

    total_capacity = sum(r.capacity_mw for r in results)
    total_generation = sum(r.annual_generation_mwh for r in results)
    total_capex = sum(r.total_capex for r in results)

    itc_total = sum(
        r.tax_credit_value for r in results if r.tax_credit_type == "ITC"
    )
    ptc_annual = sum(
        r.tax_credit_value for r in results if r.tax_credit_type == "PTC"
    )

    # Grid comparison
    grid_lcoe = inputs.grid_tariff_per_mwh
    savings_pct = 0.0
    if grid_lcoe > 0 and blended > 0:
        savings_pct = round((grid_lcoe - blended) / grid_lcoe * 100, 1)

    # Recommend configuration
    if blended > 0 and blended < grid_lcoe:
        best_sources = sorted(results, key=lambda r: r.lcoe_per_mwh)
        config_parts = [f"{r.source_type} ({r.capacity_mw}MW)" for r in best_sources[:3]]
        recommended = f"BTM recommended: {' + '.join(config_parts)}, blended LCOE ${blended}/MWh vs grid ${grid_lcoe}/MWh"
    elif blended > 0:
        recommended = (
            f"Grid power is more economical (${grid_lcoe}/MWh vs BTM ${blended}/MWh). "
            "Consider BTM for reliability, sustainability, or tax credit benefits."
        )
    else:
        recommended = "Insufficient data for recommendation"

    # Confidence range (+/- 10% reflects resource assessment uncertainty)
    uncertainty = 0.10
    confidence_low = round(blended * (1 - uncertainty), 2) if blended > 0 else 0
    confidence_high = round(blended * (1 + uncertainty), 2) if blended > 0 else 0

    return BTMResult(
        source_lcoes=source_lcoes,
        blended_lcoe=blended,
        grid_lcoe=grid_lcoe,
        savings_vs_grid_pct=savings_pct,
        itc_benefit_total=round(itc_total, 2),
        ptc_benefit_annual=round(ptc_annual, 2),
        total_btm_capacity_mw=round(total_capacity, 2),
        total_annual_generation_mwh=round(total_generation, 1),
        total_capex=round(total_capex, 2),
        recommended_config=recommended,
        confidence_range_low=confidence_low,
        confidence_range_high=confidence_high,
        source_details=[asdict(r) for r in results],
        hybrid_blended_lcoe=blended,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Unified LCOE calculator for behind-the-meter data center power. "
            "Supports gas, solar, wind, BESS, fuel cells, and SMR with "
            "ITC/PTC tax credit modeling and hybrid blending."
        ),
        epilog=(
            "Examples:\n"
            "  python3 lcoe-calculator.py --input btm-inputs.json --output results.json\n"
            "  python3 lcoe-calculator.py --facility-load-mw 20 --grid-tariff 65\n"
            "\nPart of eng-btm-power skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--input", metavar="FILE",
        help="JSON input file with BTMInput fields and sources array",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )

    # Quick-run CLI args
    parser.add_argument(
        "--facility-load-mw", type=float, default=10.0,
        help="Facility IT load in MW (default: 10)",
    )
    parser.add_argument(
        "--grid-tariff", type=float, default=65.0,
        help="Grid electricity tariff in $/MWh (default: 65)",
    )
    parser.add_argument(
        "--discount-rate", type=float, default=DEFAULT_DISCOUNT_RATE,
        help=f"Discount rate / WACC (default: {DEFAULT_DISCOUNT_RATE})",
    )
    parser.add_argument(
        "--itc-rate", type=float, default=DEFAULT_ITC_RATE,
        help=f"ITC rate for eligible sources (default: {DEFAULT_ITC_RATE})",
    )
    parser.add_argument(
        "--ptc-rate", type=float, default=DEFAULT_PTC_RATE_MWH,
        help=f"PTC rate $/MWh for eligible sources (default: {DEFAULT_PTC_RATE_MWH})",
    )
    parser.add_argument(
        "--escalation", type=float, default=0.03,
        help="Annual grid cost escalation rate (default: 0.03)",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = BTMInput(
            facility_load_mw=data.get("facility_load_mw", 10.0),
            sources=data.get("sources", []),
            discount_rate=data.get("discount_rate", DEFAULT_DISCOUNT_RATE),
            itc_rate=data.get("itc_rate", DEFAULT_ITC_RATE),
            ptc_rate_per_mwh=data.get("ptc_rate_per_mwh", DEFAULT_PTC_RATE_MWH),
            grid_tariff_per_mwh=data.get("grid_tariff_per_mwh", 65.0),
            escalation_rate=data.get("escalation_rate", 0.03),
            corporate_tax_rate=data.get("corporate_tax_rate", 0.21),
        )
    else:
        inputs = BTMInput(
            facility_load_mw=args.facility_load_mw,
            grid_tariff_per_mwh=args.grid_tariff,
            discount_rate=args.discount_rate,
            itc_rate=args.itc_rate,
            ptc_rate_per_mwh=args.ptc_rate,
            escalation_rate=args.escalation,
        )

    result = calculate_btm(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"BTM results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
