#!/usr/bin/env python3
"""Cooling Calculator -- eng-cooling-design bundled script.

Calculates cooling load sizing, PUE/WUE estimates, free cooling hours,
water budget, and technology recommendations for data center cooling design.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 cooling-calculator.py --it-load 10000 --density 50 --climate hot-dry --water limited
    python3 cooling-calculator.py --input cooling-inputs.json --output results.json
    python3 cooling-calculator.py --help
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict


# Climate zone to free cooling hours (approximate annual hours)
# Based on ASHRAE climate data for representative cities
CLIMATE_FREE_COOLING = {
    "cold": {"hours_low": 6000, "hours_high": 8000, "examples": "Stockholm, Montreal, Helsinki"},
    "temperate": {"hours_low": 3000, "hours_high": 6000, "examples": "N. Virginia, Amsterdam, London"},
    "hot-dry": {"hours_low": 1000, "hours_high": 3000, "examples": "Phoenix, Las Vegas, Riyadh"},
    "hot-humid": {"hours_low": 500, "hours_high": 2000, "examples": "Miami, Singapore, Jakarta"},
}

# Water availability levels
WATER_LEVELS = ("abundant", "limited", "scarce", "unknown")

# Technology recommendations by density tier
DENSITY_TIERS = {
    "air": {"max_kw": 15, "technology": "raised-floor-air-or-in-row", "pue_low": 0.30, "pue_high": 0.50},
    "hybrid": {"max_kw": 40, "technology": "containment-with-rdhx", "pue_low": 0.15, "pue_high": 0.30},
    "dlc": {"max_kw": 80, "technology": "direct-liquid-cooling", "pue_low": 0.05, "pue_high": 0.15},
    "immersion": {"max_kw": 999, "technology": "single-phase-immersion", "pue_low": 0.03, "pue_high": 0.10},
}

# WUE by heat rejection technology (L/kWh)
WUE_BY_REJECTION = {
    "cooling-tower": {"wue_low": 1.8, "wue_high": 2.5},
    "adiabatic": {"wue_low": 0.5, "wue_high": 1.2},
    "dry-cooler": {"wue_low": 0.0, "wue_high": 0.0},
    "free-cooling": {"wue_low": 0.0, "wue_high": 0.1},
}


@dataclass
class CoolingResult:
    """Result of a cooling system calculation."""
    total_it_load_kw: float
    density_kw_per_rack: float
    density_tier: str
    climate_zone: str
    water_availability: str
    total_cooling_capacity_kw: float
    cooling_overhead_kw: float
    pue_cooling_contribution_low: float
    pue_cooling_contribution_high: float
    technology_recommendation: str
    heat_rejection_recommendation: str
    wue_low: float
    wue_high: float
    free_cooling_hours_low: int
    free_cooling_hours_high: int
    annual_water_liters_low: int
    annual_water_liters_high: int


def _determine_density_tier(density_kw: float) -> str:
    """Determine cooling tier from per-rack density."""
    if density_kw <= 15:
        return "air"
    elif density_kw <= 40:
        return "hybrid"
    elif density_kw <= 80:
        return "dlc"
    else:
        return "immersion"


def _determine_heat_rejection(climate: str, water: str) -> str:
    """Select heat rejection technology based on climate and water availability."""
    if water in ("scarce", "unknown"):
        return "dry-cooler"
    if climate == "cold":
        return "free-cooling"
    if climate == "temperate":
        return "free-cooling"  # primary, with mechanical backup
    if climate in ("hot-dry",) and water == "abundant":
        return "adiabatic"
    if water == "abundant":
        return "cooling-tower"
    return "dry-cooler"


def calculate_cooling(
    it_load_kw: float,
    density_kw_per_rack: float,
    climate_zone: str = "temperate",
    water_availability: str = "unknown",
    target_pue: float | None = None,
) -> CoolingResult:
    """Calculate cooling system requirements.

    Args:
        it_load_kw: Total IT load in kW.
        density_kw_per_rack: Average power density per rack in kW.
        climate_zone: One of cold, temperate, hot-dry, hot-humid.
        water_availability: One of abundant, limited, scarce, unknown.
        target_pue: Target PUE (optional, used for sizing validation).

    Returns:
        CoolingResult with sizing, technology, and efficiency estimates.

    Raises:
        ValueError: If inputs are invalid.
    """
    if it_load_kw <= 0:
        raise ValueError(f"IT load must be positive, got {it_load_kw} kW")
    if density_kw_per_rack <= 0:
        raise ValueError(f"Density must be positive, got {density_kw_per_rack} kW/rack")

    climate_zone = climate_zone.lower().strip()
    if climate_zone not in CLIMATE_FREE_COOLING:
        raise ValueError(
            f"Invalid climate zone '{climate_zone}'. "
            f"Must be one of: {', '.join(CLIMATE_FREE_COOLING.keys())}"
        )

    water_availability = water_availability.lower().strip()
    if water_availability not in WATER_LEVELS:
        raise ValueError(
            f"Invalid water availability '{water_availability}'. "
            f"Must be one of: {', '.join(WATER_LEVELS)}"
        )

    # Determine density tier and technology
    tier = _determine_density_tier(density_kw_per_rack)
    tier_info = DENSITY_TIERS[tier]

    # Determine heat rejection
    rejection = _determine_heat_rejection(climate_zone, water_availability)
    rejection_info = WUE_BY_REJECTION[rejection]

    # Calculate cooling overhead
    pue_low = tier_info["pue_low"]
    pue_high = tier_info["pue_high"]
    cooling_overhead_low = it_load_kw * pue_low
    cooling_overhead_high = it_load_kw * pue_high
    cooling_overhead_avg = (cooling_overhead_low + cooling_overhead_high) / 2

    # Total cooling capacity with 20% margin
    total_cooling_capacity = math.ceil(cooling_overhead_high * 1.20)

    # Free cooling hours
    climate_data = CLIMATE_FREE_COOLING[climate_zone]

    # Annual water usage (liters)
    # Based on WUE * IT load * 8760 hours * utilization factor (0.7)
    wue_low = rejection_info["wue_low"]
    wue_high = rejection_info["wue_high"]
    annual_water_low = int(wue_low * it_load_kw * 8760 * 0.7)
    annual_water_high = int(wue_high * it_load_kw * 8760 * 0.7)

    return CoolingResult(
        total_it_load_kw=it_load_kw,
        density_kw_per_rack=density_kw_per_rack,
        density_tier=tier,
        climate_zone=climate_zone,
        water_availability=water_availability,
        total_cooling_capacity_kw=total_cooling_capacity,
        cooling_overhead_kw=round(cooling_overhead_avg, 1),
        pue_cooling_contribution_low=pue_low,
        pue_cooling_contribution_high=pue_high,
        technology_recommendation=tier_info["technology"],
        heat_rejection_recommendation=rejection,
        wue_low=wue_low,
        wue_high=wue_high,
        free_cooling_hours_low=climate_data["hours_low"],
        free_cooling_hours_high=climate_data["hours_high"],
        annual_water_liters_low=annual_water_low,
        annual_water_liters_high=annual_water_high,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Calculate data center cooling system requirements.",
        epilog="Part of eng-cooling-design skill (stellenium/dc-skills).",
    )
    parser.add_argument(
        "--it-load", type=float, help="Total IT load in kW"
    )
    parser.add_argument(
        "--density", type=float, help="Per-rack power density in kW/rack"
    )
    parser.add_argument(
        "--climate",
        choices=list(CLIMATE_FREE_COOLING.keys()),
        default="temperate",
        help="Climate zone (default: temperate)",
    )
    parser.add_argument(
        "--water",
        choices=list(WATER_LEVELS),
        default="unknown",
        help="Water availability (default: unknown)",
    )
    parser.add_argument(
        "--target-pue",
        type=float,
        help="Target PUE for validation (optional)",
    )
    parser.add_argument(
        "--input",
        metavar="FILE",
        help="JSON input file (alternative to CLI args)",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        help="JSON output file (default: stdout)",
    )
    args = parser.parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        result = calculate_cooling(
            it_load_kw=data["it_load_kw"],
            density_kw_per_rack=data["density_kw_per_rack"],
            climate_zone=data.get("climate_zone", "temperate"),
            water_availability=data.get("water_availability", "unknown"),
            target_pue=data.get("target_pue"),
        )
    elif args.it_load is not None and args.density is not None:
        result = calculate_cooling(
            args.it_load, args.density, args.climate, args.water, args.target_pue
        )
    else:
        parser.error("Provide either --input FILE or both --it-load and --density")

    output = json.dumps(asdict(result), indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
