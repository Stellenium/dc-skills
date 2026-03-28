#!/usr/bin/env python3
"""PUE Calculator -- eng-power-model bundled script.

Calculates Power Usage Effectiveness from component-level losses.
Produces PUE with uncertainty ranges for data center power modeling.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 pue-calculator.py --it-load 10000 --cooling-load 2500 --lighting 150 --losses 500
    python3 pue-calculator.py --input power-inputs.json --output pue-results.json
    python3 pue-calculator.py --help
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict


@dataclass
class PUEResult:
    """Result of a PUE calculation with uncertainty range."""
    it_load_kw: float
    total_facility_kw: float
    pue: float
    pue_range_low: float
    pue_range_high: float
    breakdown: dict


def calculate_pue(
    it_load_kw: float,
    cooling_kw: float,
    lighting_kw: float = 0.0,
    distribution_losses_kw: float = 0.0,
    uncertainty_pct: float = 0.05,
) -> PUEResult:
    """Calculate PUE from component-level power loads.

    Args:
        it_load_kw: IT equipment load in kW.
        cooling_kw: Cooling system load in kW (CRAC/CRAH, chillers, pumps, towers).
        lighting_kw: Lighting and miscellaneous facility load in kW.
        distribution_losses_kw: Electrical distribution losses in kW
            (transformer, UPS, PDU losses).
        uncertainty_pct: Uncertainty band as a fraction (default 0.05 = +/-5%).

    Returns:
        PUEResult with calculated PUE and uncertainty range.

    Raises:
        ValueError: If it_load_kw is zero or negative.
    """
    if it_load_kw <= 0:
        raise ValueError(f"IT load must be positive, got {it_load_kw} kW")

    total = it_load_kw + cooling_kw + lighting_kw + distribution_losses_kw
    pue = total / it_load_kw

    if pue < 1.0:
        print(
            f"WARNING: Calculated PUE {pue:.3f} is below 1.0, which is physically "
            "impossible. Check input values.",
            file=sys.stderr,
        )

    return PUEResult(
        it_load_kw=it_load_kw,
        total_facility_kw=round(total, 2),
        pue=round(pue, 3),
        pue_range_low=round(pue * (1 - uncertainty_pct), 3),
        pue_range_high=round(pue * (1 + uncertainty_pct), 3),
        breakdown={
            "cooling_kw": cooling_kw,
            "lighting_kw": lighting_kw,
            "distribution_losses_kw": distribution_losses_kw,
            "cooling_pct_of_total": round(cooling_kw / total * 100, 1),
            "distribution_pct_of_total": round(
                distribution_losses_kw / total * 100, 1
            ),
        },
    )


def main():
    parser = argparse.ArgumentParser(
        description="Calculate PUE from component-level power loads.",
        epilog="Part of eng-power-model skill (stellenium/dc-skills).",
    )
    parser.add_argument(
        "--it-load", type=float, help="IT equipment load in kW"
    )
    parser.add_argument(
        "--cooling-load", type=float, help="Cooling system load in kW"
    )
    parser.add_argument(
        "--lighting",
        type=float,
        default=0,
        help="Lighting/misc facility load in kW (default: 0)",
    )
    parser.add_argument(
        "--losses",
        type=float,
        default=0,
        help="Electrical distribution losses in kW (default: 0)",
    )
    parser.add_argument(
        "--uncertainty",
        type=float,
        default=0.05,
        help="Uncertainty band as fraction (default: 0.05 = +/-5%%)",
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
        # Map JSON keys to function parameters
        mapped = {
            "it_load_kw": data.get("it_load_kw", data.get("it_load")),
            "cooling_kw": data.get("cooling_kw", data.get("cooling_load")),
            "lighting_kw": data.get("lighting_kw", data.get("lighting", 0)),
            "distribution_losses_kw": data.get(
                "distribution_losses_kw", data.get("losses", 0)
            ),
            "uncertainty_pct": data.get(
                "uncertainty_pct", data.get("uncertainty", 0.05)
            ),
        }
        result = calculate_pue(**mapped)
    elif args.it_load is not None and args.cooling_load is not None:
        result = calculate_pue(
            args.it_load,
            args.cooling_load,
            args.lighting,
            args.losses,
            args.uncertainty,
        )
    else:
        parser.error("Provide either --input FILE or both --it-load and --cooling-load")

    output = json.dumps(asdict(result), indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
