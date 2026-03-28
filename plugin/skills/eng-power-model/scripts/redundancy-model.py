#!/usr/bin/env python3
"""Redundancy Model -- eng-power-model bundled script.

Models data center power redundancy configurations from N (no redundancy)
through 2N+1 (fault tolerant with spare). Maps Uptime Tier classifications
to component redundancy configurations and calculates module requirements.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 redundancy-model.py --tier III --load 10000 --module-size 2000
    python3 redundancy-model.py --input redundancy-inputs.json --output results.json
    python3 redundancy-model.py --help
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict


# Tier to redundancy mapping per Uptime Institute definitions
TIER_MAP = {
    "I": {
        "config": "N",
        "redundant_modules": 0,
        "concurrent_maintainable": False,
        "fault_tolerant": False,
        "description": "Basic site infrastructure. No redundancy.",
    },
    "II": {
        "config": "N+1",
        "redundant_modules": 1,
        "concurrent_maintainable": False,
        "fault_tolerant": False,
        "description": "Redundant capacity components. Single distribution path.",
    },
    "III": {
        "config": "N+1",
        "redundant_modules": 1,
        "concurrent_maintainable": True,
        "fault_tolerant": False,
        "description": "Concurrently maintainable. Multiple distribution paths (one active).",
    },
    "IV": {
        "config": "2N",
        "redundant_modules": None,  # calculated as N
        "concurrent_maintainable": True,
        "fault_tolerant": True,
        "description": "Fault tolerant. Multiple active distribution paths.",
    },
}


@dataclass
class RedundancyResult:
    """Result of a redundancy analysis."""
    tier: str
    config: str
    total_load_kw: float
    module_size_kw: float
    active_modules: int
    redundant_modules: int
    total_modules: int
    total_installed_capacity_kw: float
    capacity_with_redundancy_loss_kw: float
    utilization_pct: float
    concurrent_maintainable: bool
    fault_tolerant: bool
    single_point_of_failure: bool
    description: str


def model_redundancy(
    tier: str,
    total_load_kw: float,
    module_size_kw: float,
) -> RedundancyResult:
    """Model power redundancy for a given Uptime Tier.

    Args:
        tier: Uptime Tier classification (I, II, III, or IV).
        total_load_kw: Total IT load in kW to be supported.
        module_size_kw: Size of each redundancy module in kW (UPS, generator, etc.).

    Returns:
        RedundancyResult with module counts and redundancy analysis.

    Raises:
        ValueError: If tier is invalid or load/module_size are non-positive.
    """
    tier = tier.upper().strip()
    if tier not in TIER_MAP:
        raise ValueError(
            f"Invalid tier '{tier}'. Must be one of: {', '.join(TIER_MAP.keys())}"
        )
    if total_load_kw <= 0:
        raise ValueError(f"Total load must be positive, got {total_load_kw} kW")
    if module_size_kw <= 0:
        raise ValueError(f"Module size must be positive, got {module_size_kw} kW")

    tier_info = TIER_MAP[tier]
    active_modules = math.ceil(total_load_kw / module_size_kw)

    if tier == "IV":
        # 2N: duplicate the entire active set
        redundant_modules = active_modules
        config = "2N"
    else:
        redundant_modules = tier_info["redundant_modules"]
        config = tier_info["config"]

    total_modules = active_modules + redundant_modules
    total_installed_capacity_kw = total_modules * module_size_kw

    # Capacity available after losing one module (worst-case maintenance scenario)
    capacity_after_loss = (total_modules - 1) * module_size_kw

    # Utilization at the active module level
    utilization_pct = round((total_load_kw / (active_modules * module_size_kw)) * 100, 1)

    # Single point of failure analysis
    # Tier I has SPOF; Tier II has SPOF in distribution; Tier III/IV have no SPOF
    spof = tier in ("I", "II")

    return RedundancyResult(
        tier=tier,
        config=config,
        total_load_kw=total_load_kw,
        module_size_kw=module_size_kw,
        active_modules=active_modules,
        redundant_modules=redundant_modules,
        total_modules=total_modules,
        total_installed_capacity_kw=total_installed_capacity_kw,
        capacity_with_redundancy_loss_kw=capacity_after_loss,
        utilization_pct=utilization_pct,
        concurrent_maintainable=tier_info["concurrent_maintainable"],
        fault_tolerant=tier_info["fault_tolerant"],
        single_point_of_failure=spof,
        description=tier_info["description"],
    )


def main():
    parser = argparse.ArgumentParser(
        description="Model data center power redundancy configurations.",
        epilog="Part of eng-power-model skill (stellenium/dc-skills).",
    )
    parser.add_argument(
        "--tier",
        choices=["I", "II", "III", "IV"],
        help="Uptime Tier classification",
    )
    parser.add_argument(
        "--load", type=float, help="Total IT load in kW"
    )
    parser.add_argument(
        "--module-size", type=float, help="Size of each UPS/generator module in kW"
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
        result = model_redundancy(
            tier=data["tier"],
            total_load_kw=data["total_load_kw"],
            module_size_kw=data["module_size_kw"],
        )
    elif args.tier and args.load and args.module_size:
        result = model_redundancy(args.tier, args.load, args.module_size)
    else:
        parser.error(
            "Provide either --input FILE or all of --tier, --load, --module-size"
        )

    output = json.dumps(asdict(result), indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
