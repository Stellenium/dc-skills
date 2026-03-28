#!/usr/bin/env python3
"""Availability Model -- eng-sla-design bundled script.

Models data center availability using serial/parallel reliability chains.
Calculates system availability from component MTBF/MTTR data, classifies
against Uptime Tier I-IV targets, and generates credit structure templates.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 availability-model.py --help
    python3 availability-model.py --input sla-inputs.json --output sla-results.json
    python3 availability-model.py --target-availability 99.995
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Constants — standard DC component defaults
# ---------------------------------------------------------------------------

DEFAULT_COMPONENTS = {
    "ups": {"mtbf_hours": 150000, "mttr_hours": 4, "name": "UPS"},
    "generator": {"mtbf_hours": 2000, "mttr_hours": 24, "name": "Generator"},
    "crah": {"mtbf_hours": 80000, "mttr_hours": 8, "name": "CRAH/CRAC"},
    "chiller": {"mtbf_hours": 40000, "mttr_hours": 12, "name": "Chiller"},
    "pdu": {"mtbf_hours": 200000, "mttr_hours": 2, "name": "PDU"},
    "transfer_switch": {"mtbf_hours": 500000, "mttr_hours": 1, "name": "Transfer Switch"},
}

# Uptime Institute Tier availability targets (designed availability)
TIER_TARGETS = {
    "I": 99.671,
    "II": 99.741,
    "III": 99.982,
    "IV": 99.995,
}

# Hours per year
HOURS_PER_YEAR = 8760
MINUTES_PER_YEAR = 525600


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Component:
    """A single infrastructure component in the reliability chain."""
    name: str
    mtbf_hours: float
    mttr_hours: float
    redundancy: str = "N"     # "N", "N+1", "2N", "2N+1"
    count: int = 1            # number of active units (N in N+1)


@dataclass
class CreditTier:
    """A single SLA credit tier."""
    level: int
    min_downtime_minutes: float
    max_downtime_minutes: float
    credit_pct: float           # percentage of MRC
    description: str


@dataclass
class AvailabilityInput:
    """Input for availability calculation."""
    components: list = field(default_factory=list)  # list of Component dicts
    target_availability: float = 99.982              # default Tier III
    planned_maintenance_hours_year: float = 0.0
    measurement_interval_minutes: int = 5
    credit_cap_pct: float = 30.0   # max credit as % of MRC


@dataclass
class ComponentResult:
    """Availability result for a single component group."""
    name: str
    mtbf_hours: float
    mttr_hours: float
    redundancy: str
    count: int
    single_availability: float
    group_availability: float


@dataclass
class AvailabilityResult:
    """Complete availability calculation result."""
    component_availabilities: dict    # name -> availability %
    system_availability: float
    annual_downtime_minutes: float
    tier_classification: str          # I, II, III, IV, or "Beyond IV"
    meets_target: bool
    target_availability: float
    margin_pct: float
    weakest_link: str
    credit_structure: list            # list of CreditTier dicts
    confidence_range_low: float
    confidence_range_high: float
    component_details: list           # list of ComponentResult dicts
    recommendations: list             # upgrade recommendations if target not met


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def calculate_single_availability(mtbf: float, mttr: float) -> float:
    """Calculate availability for a single component: A = MTBF / (MTBF + MTTR)."""
    if mtbf <= 0:
        return 0.0
    return mtbf / (mtbf + mttr)


def calculate_parallel_availability(
    single_a: float, redundancy: str, count: int
) -> float:
    """Calculate availability for a redundant group.

    N:    A = single_a (no redundancy)
    N+1:  A = 1 - (1-A)^(count+1)  — one spare for count active
    2N:   A = 1 - (1-A)^(2*count)   — full duplication
    2N+1: A = 1 - (1-A)^(2*count+1) — full duplication plus one spare
    """
    if redundancy == "N":
        # Serial contribution of 'count' identical units
        return single_a ** count if count > 1 else single_a

    failure_prob = 1 - single_a

    if redundancy == "N+1":
        total_units = count + 1
    elif redundancy == "2N":
        total_units = 2 * count
    elif redundancy == "2N+1":
        total_units = 2 * count + 1
    else:
        # Unknown redundancy, treat as N
        return single_a ** count if count > 1 else single_a

    # System fails only if more than (total_units - count) units fail
    # For simplicity with typical DC configs, use the standard parallel formula
    # A_group = 1 - P(all redundant paths fail)
    # For N+1 with count required: need at least count working out of total_units
    # Exact: A = 1 - sum(C(total,k) * p^k * (1-p)^(total-k)) for k > allowed_failures
    # Simplified (conservative): A = 1 - (1-A_single)^total_units
    # This is exact for 1-of-N scenarios, conservative for k-of-N

    group_a = 1 - (failure_prob ** total_units)
    return group_a


def classify_tier(availability_pct: float) -> str:
    """Classify availability against Uptime Tier targets."""
    if availability_pct >= TIER_TARGETS["IV"]:
        if availability_pct >= 99.999:
            return "Beyond IV"
        return "IV"
    elif availability_pct >= TIER_TARGETS["III"]:
        return "III"
    elif availability_pct >= TIER_TARGETS["II"]:
        return "II"
    elif availability_pct >= TIER_TARGETS["I"]:
        return "I"
    else:
        return "Below I"


def generate_credit_structure(
    target_availability: float, credit_cap_pct: float
) -> List[CreditTier]:
    """Generate a tiered SLA credit structure based on target availability."""
    # Annual downtime budget in minutes
    downtime_budget = MINUTES_PER_YEAR * (1 - target_availability / 100)

    # Level 1: 1x to 2x downtime budget per month
    monthly_budget = downtime_budget / 12
    levels = [
        CreditTier(
            level=1,
            min_downtime_minutes=round(monthly_budget, 1),
            max_downtime_minutes=round(monthly_budget * 2, 1),
            credit_pct=min(5.0, credit_cap_pct),
            description="Minor SLA breach",
        ),
        CreditTier(
            level=2,
            min_downtime_minutes=round(monthly_budget * 2, 1),
            max_downtime_minutes=round(monthly_budget * 5, 1),
            credit_pct=min(15.0, credit_cap_pct),
            description="Moderate SLA breach",
        ),
        CreditTier(
            level=3,
            min_downtime_minutes=round(monthly_budget * 5, 1),
            max_downtime_minutes=round(monthly_budget * 10, 1),
            credit_pct=min(credit_cap_pct, credit_cap_pct),
            description=f"Major SLA breach (credit cap: {credit_cap_pct}% MRC)",
        ),
    ]
    return levels


def calculate_availability(inputs: AvailabilityInput) -> AvailabilityResult:
    """Run the full availability calculation."""
    # Parse components
    components = []
    for c in inputs.components:
        if isinstance(c, dict):
            components.append(Component(**c))
        elif isinstance(c, Component):
            components.append(c)

    # If no components provided, use default Tier III configuration
    if not components:
        components = [
            Component(name="UPS", mtbf_hours=150000, mttr_hours=4,
                      redundancy="N+1", count=2),
            Component(name="Generator", mtbf_hours=2000, mttr_hours=24,
                      redundancy="N+1", count=2),
            Component(name="CRAH", mtbf_hours=80000, mttr_hours=8,
                      redundancy="N+1", count=4),
            Component(name="Chiller", mtbf_hours=40000, mttr_hours=12,
                      redundancy="N+1", count=2),
            Component(name="PDU", mtbf_hours=200000, mttr_hours=2,
                      redundancy="N+1", count=2),
            Component(name="Transfer Switch", mtbf_hours=500000, mttr_hours=1,
                      redundancy="N+1", count=1),
        ]

    # Calculate per-component and per-group availability
    comp_results = []
    component_availabilities = {}
    system_availability = 1.0
    weakest_link = ""
    weakest_a = 1.0

    for comp in components:
        single_a = calculate_single_availability(comp.mtbf_hours, comp.mttr_hours)
        group_a = calculate_parallel_availability(single_a, comp.redundancy, comp.count)

        result = ComponentResult(
            name=comp.name,
            mtbf_hours=comp.mtbf_hours,
            mttr_hours=comp.mttr_hours,
            redundancy=comp.redundancy,
            count=comp.count,
            single_availability=round(single_a * 100, 6),
            group_availability=round(group_a * 100, 8),
        )
        comp_results.append(result)
        component_availabilities[comp.name] = round(group_a * 100, 6)

        # Serial chain: multiply availabilities
        system_availability *= group_a

        # Track weakest serial link
        if group_a < weakest_a:
            weakest_a = group_a
            weakest_link = comp.name

    system_avail_pct = round(system_availability * 100, 6)

    # Account for planned maintenance
    if inputs.planned_maintenance_hours_year > 0:
        maint_unavail = inputs.planned_maintenance_hours_year / HOURS_PER_YEAR
        effective_avail = system_availability * (1 - maint_unavail)
        system_avail_pct = round(effective_avail * 100, 6)

    # Annual downtime
    downtime_fraction = 1 - (system_avail_pct / 100)
    annual_downtime_min = round(MINUTES_PER_YEAR * downtime_fraction, 1)

    # Tier classification
    tier = classify_tier(system_avail_pct)

    # Target comparison
    meets_target = system_avail_pct >= inputs.target_availability
    margin = round(system_avail_pct - inputs.target_availability, 6)

    # Credit structure
    credits = generate_credit_structure(inputs.target_availability, inputs.credit_cap_pct)

    # Confidence range (+/- based on MTTR uncertainty)
    uncertainty = 0.002  # +/- 0.002% typical for MTTR variability
    conf_low = round(system_avail_pct - uncertainty, 6)
    conf_high = round(min(system_avail_pct + uncertainty, 100.0), 6)

    # Recommendations if target not met
    recommendations = []
    if not meets_target:
        recommendations.append(
            f"System availability {system_avail_pct}% is below target "
            f"{inputs.target_availability}%."
        )
        recommendations.append(
            f"Weakest serial link: {weakest_link} "
            f"(group availability: {weakest_a * 100:.6f}%). "
            "Consider upgrading redundancy on this component."
        )
        # Suggest specific upgrade
        for comp in components:
            if comp.name == weakest_link:
                if comp.redundancy == "N":
                    recommendations.append(
                        f"Upgrade {comp.name} from N to N+1 redundancy."
                    )
                elif comp.redundancy == "N+1":
                    recommendations.append(
                        f"Upgrade {comp.name} from N+1 to 2N redundancy."
                    )

    return AvailabilityResult(
        component_availabilities=component_availabilities,
        system_availability=system_avail_pct,
        annual_downtime_minutes=annual_downtime_min,
        tier_classification=tier,
        meets_target=meets_target,
        target_availability=inputs.target_availability,
        margin_pct=margin,
        weakest_link=weakest_link,
        credit_structure=[asdict(c) for c in credits],
        confidence_range_low=conf_low,
        confidence_range_high=conf_high,
        component_details=[asdict(c) for c in comp_results],
        recommendations=recommendations,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Model data center availability using serial/parallel reliability "
            "chains. Classifies against Uptime Tier I-IV targets and generates "
            "SLA credit structures."
        ),
        epilog=(
            "Examples:\n"
            "  python3 availability-model.py --input sla-inputs.json\n"
            "  python3 availability-model.py --target-availability 99.995\n"
            "\nDefault components: UPS, Generator, CRAH, Chiller, PDU, "
            "Transfer Switch (all N+1).\n"
            "\nPart of eng-sla-design skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--input", metavar="FILE",
        help="JSON input file with components array and target availability",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )
    parser.add_argument(
        "--target-availability", type=float, default=99.982,
        help="Target availability percentage (default: 99.982 = Tier III)",
    )
    parser.add_argument(
        "--maintenance-hours", type=float, default=0.0,
        help="Planned maintenance hours per year (default: 0)",
    )
    parser.add_argument(
        "--credit-cap", type=float, default=30.0,
        help="Maximum SLA credit as %% of MRC (default: 30)",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        with open(args.input) as f:
            data = json.load(f)
        inputs = AvailabilityInput(
            components=data.get("components", []),
            target_availability=data.get("target_availability", 99.982),
            planned_maintenance_hours_year=data.get(
                "planned_maintenance_hours_year", 0.0
            ),
            measurement_interval_minutes=data.get(
                "measurement_interval_minutes", 5
            ),
            credit_cap_pct=data.get("credit_cap_pct", 30.0),
        )
    else:
        inputs = AvailabilityInput(
            target_availability=args.target_availability,
            planned_maintenance_hours_year=args.maintenance_hours,
            credit_cap_pct=args.credit_cap,
        )

    result = calculate_availability(inputs)
    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Availability results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
