#!/usr/bin/env python3
"""Brownfield Conversion Scorer -- eng-brownfield-convert bundled script.

Weighted multi-factor scoring calculator for building-to-data-center conversion
feasibility. Scores 8 criteria on a 1-5 scale, applies configurable weights,
computes weighted average, checks override rules, aggregates remediation costs,
and produces GO/CONDITIONAL/NO-GO recommendation.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 brownfield-scorer.py --help
    python3 brownfield-scorer.py --input assessment.json --output results.json
    python3 brownfield-scorer.py --structural 4 --power 3 --fiber 4 --contamination 2 --seismic 5 --zoning 3 --logistics 4 --hvac 3
"""
import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from typing import List, Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Default weights (must sum to 1.0)
DEFAULT_WEIGHTS = {
    "structural_capacity": 0.20,
    "power_infrastructure": 0.20,
    "fiber_access": 0.10,
    "contamination_risk": 0.15,
    "seismic_zone": 0.10,
    "zoning_compatibility": 0.15,
    "logistics_dock_access": 0.05,
    "hvac_compatibility": 0.05,
}

# Decision thresholds
THRESHOLD_GO = 3.5
THRESHOLD_CONDITIONAL = 2.5

# Criterion display names
CRITERION_NAMES = {
    "structural_capacity": "Structural Capacity",
    "power_infrastructure": "Power Infrastructure",
    "fiber_access": "Fiber Access",
    "contamination_risk": "Contamination Risk",
    "seismic_zone": "Seismic Zone",
    "zoning_compatibility": "Zoning Compatibility",
    "logistics_dock_access": "Logistics/Dock Access",
    "hvac_compatibility": "HVAC Compatibility",
}

# Score descriptions for reference
SCORE_DESCRIPTIONS = {
    "structural_capacity": {
        5: ">150 psf floor load, 30ft+ ceiling, wide column bays",
        3: "100-150 psf, 14-18ft ceiling, adequate spacing",
        1: "<75 psf, <12ft ceiling, narrow bays",
    },
    "power_infrastructure": {
        5: "13.8kV+ service, >5MW available, substation adjacent",
        3: "480V service, 1-5MW, upgrade path exists",
        1: "208V only, <1MW, major utility work required",
    },
    "fiber_access": {
        5: "3+ carriers on-net, diverse physical routes",
        3: "1-2 carriers, single route, expansion feasible",
        1: "No fiber, >2 miles to nearest POP",
    },
    "contamination_risk": {
        5: "Post-2000, clean ESA, no legacy materials",
        3: "Minor issues, manageable abatement ($5-15/sqft)",
        1: "Asbestos throughout, UST, major soil contamination",
    },
    "seismic_zone": {
        5: "Zone 0-1, no special requirements",
        3: "Zone 2, moderate seismic bracing required",
        1: "Zone 3-4, major structural retrofit needed",
    },
    "zoning_compatibility": {
        5: "Industrial/data center zoned, no change needed",
        3: "Commercial, change-of-use feasible (6-12 months)",
        1: "Residential/protected, zoning change unlikely",
    },
    "logistics_dock_access": {
        5: "Loading dock, truck court, generator pad space",
        3: "Street-level access, limited staging area",
        1: "No dock, constrained access, no generator space",
    },
    "hvac_compatibility": {
        5: "Large mechanical room, strong roof for equipment",
        3: "Moderate space, some rooftop equipment feasible",
        1: "No mechanical space, weak roof structure",
    },
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class CriterionScore:
    """A single criterion's assessment."""
    name: str
    score: int              # 1-5
    weight: float           # 0.0-1.0
    cost_low: float = 0.0   # remediation cost low estimate ($)
    cost_high: float = 0.0  # remediation cost high estimate ($)
    notes: str = ""


@dataclass
class BrownfieldAssessment:
    """Complete brownfield conversion assessment result."""
    criteria: list                  # list of CriterionScore dicts
    weighted_score: float
    recommendation: str             # GO, CONDITIONAL, NO-GO
    override_triggered: bool
    override_factor: Optional[str]
    total_cost_low: float
    total_cost_high: float
    building_type: str = ""
    building_age: int = 0
    floor_area_sqft: float = 0.0
    target_it_load_mw: float = 0.0


# ---------------------------------------------------------------------------
# Core calculation functions
# ---------------------------------------------------------------------------

def validate_score(score: int, criterion_name: str) -> int:
    """Validate that a score is between 1 and 5."""
    if not isinstance(score, (int, float)):
        raise ValueError(
            f"Score for '{criterion_name}' must be a number, got {type(score).__name__}"
        )
    score = int(score)
    if score < 1 or score > 5:
        raise ValueError(
            f"Score for '{criterion_name}' must be between 1 and 5, got {score}"
        )
    return score


def validate_weights(weights: dict) -> dict:
    """Validate that weights sum to approximately 1.0."""
    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        raise ValueError(
            f"Weights must sum to 1.0 (100%), got {total:.4f}. "
            f"Difference: {abs(total - 1.0):.4f}"
        )
    return weights


def calculate(
    scores: dict,
    weights: Optional[dict] = None,
    costs: Optional[dict] = None,
    building_type: str = "",
    building_age: int = 0,
    floor_area_sqft: float = 0.0,
    target_it_load_mw: float = 0.0,
) -> BrownfieldAssessment:
    """Calculate brownfield conversion feasibility assessment.

    Args:
        scores: Dict mapping criterion name to score (1-5).
                Keys must be from DEFAULT_WEIGHTS.keys().
        weights: Optional dict mapping criterion name to weight (0.0-1.0).
                 Defaults to DEFAULT_WEIGHTS. Must sum to 1.0.
        costs: Optional dict mapping criterion name to (cost_low, cost_high) tuple.
               Only needed for criteria scoring below 3.
        building_type: Type of building (warehouse, office, retail, etc.).
        building_age: Year the building was constructed.
        floor_area_sqft: Total floor area in square feet.
        target_it_load_mw: Target IT load in megawatts.

    Returns:
        BrownfieldAssessment with scored criteria, recommendation, and costs.
    """
    if weights is None:
        weights = DEFAULT_WEIGHTS.copy()
    if costs is None:
        costs = {}

    # Validate inputs
    validate_weights(weights)

    # Build criterion scores
    criteria = []
    weighted_sum = 0.0
    override_triggered = False
    override_factor = None
    total_cost_low = 0.0
    total_cost_high = 0.0

    for criterion_key, default_weight in DEFAULT_WEIGHTS.items():
        score_val = scores.get(criterion_key, 3)  # default to 3 if missing
        score_val = validate_score(score_val, criterion_key)
        weight = weights.get(criterion_key, default_weight)

        # Get remediation costs if provided
        cost_pair = costs.get(criterion_key, (0.0, 0.0))
        if isinstance(cost_pair, (list, tuple)) and len(cost_pair) >= 2:
            cost_low, cost_high = float(cost_pair[0]), float(cost_pair[1])
        else:
            cost_low, cost_high = 0.0, 0.0

        # Accumulate costs for factors scoring below 3
        if score_val < 3:
            total_cost_low += cost_low
            total_cost_high += cost_high

        # Check override rule: any factor scoring 1 triggers CONDITIONAL
        if score_val == 1:
            override_triggered = True
            if override_factor is None:
                override_factor = criterion_key

        weighted_score = score_val * weight
        weighted_sum += weighted_score

        criterion = CriterionScore(
            name=criterion_key,
            score=score_val,
            weight=weight,
            cost_low=cost_low,
            cost_high=cost_high,
            notes=SCORE_DESCRIPTIONS.get(criterion_key, {}).get(
                score_val,
                SCORE_DESCRIPTIONS.get(criterion_key, {}).get(3, "")
            ),
        )
        criteria.append(criterion)

    # Round weighted score
    weighted_sum = round(weighted_sum, 2)

    # Determine recommendation
    if override_triggered and weighted_sum >= THRESHOLD_GO:
        recommendation = "CONDITIONAL"
    elif weighted_sum >= THRESHOLD_GO:
        recommendation = "GO"
    elif weighted_sum >= THRESHOLD_CONDITIONAL:
        recommendation = "CONDITIONAL"
    else:
        recommendation = "NO-GO"

    return BrownfieldAssessment(
        criteria=[asdict(c) for c in criteria],
        weighted_score=weighted_sum,
        recommendation=recommendation,
        override_triggered=override_triggered,
        override_factor=override_factor,
        total_cost_low=round(total_cost_low, 2),
        total_cost_high=round(total_cost_high, 2),
        building_type=building_type,
        building_age=building_age,
        floor_area_sqft=floor_area_sqft,
        target_it_load_mw=target_it_load_mw,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Brownfield conversion feasibility scorer. Evaluates building "
            "suitability for data center conversion across 8 weighted criteria "
            "with GO/CONDITIONAL/NO-GO recommendation."
        ),
        epilog=(
            "Examples:\n"
            "  python3 brownfield-scorer.py --input assessment.json --output results.json\n"
            "  python3 brownfield-scorer.py --structural 4 --power 3 --fiber 4 "
            "--contamination 2 --seismic 5 --zoning 3 --logistics 4 --hvac 3\n"
            "  python3 brownfield-scorer.py --structural 5 --power 4 --fiber 5 "
            "--contamination 1 --seismic 5 --zoning 5 --logistics 5 --hvac 4\n"
            "\nScoring scale: 1 (critical risk) to 5 (excellent)\n"
            "Decision thresholds: >=3.5 GO, 2.5-3.49 CONDITIONAL, <2.5 NO-GO\n"
            "Override: any factor scoring 1 triggers automatic CONDITIONAL\n"
            "\nPart of eng-brownfield-convert skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--input", metavar="FILE",
        help="JSON input file with scores, weights, costs, and building metadata",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )

    # Individual criterion scores (quick-run CLI)
    parser.add_argument(
        "--structural", type=int, default=3, metavar="1-5",
        help="Structural capacity score (default: 3)",
    )
    parser.add_argument(
        "--power", type=int, default=3, metavar="1-5",
        help="Power infrastructure score (default: 3)",
    )
    parser.add_argument(
        "--fiber", type=int, default=3, metavar="1-5",
        help="Fiber access score (default: 3)",
    )
    parser.add_argument(
        "--contamination", type=int, default=3, metavar="1-5",
        help="Contamination risk score (default: 3)",
    )
    parser.add_argument(
        "--seismic", type=int, default=3, metavar="1-5",
        help="Seismic zone score (default: 3)",
    )
    parser.add_argument(
        "--zoning", type=int, default=3, metavar="1-5",
        help="Zoning compatibility score (default: 3)",
    )
    parser.add_argument(
        "--logistics", type=int, default=3, metavar="1-5",
        help="Logistics/dock access score (default: 3)",
    )
    parser.add_argument(
        "--hvac", type=int, default=3, metavar="1-5",
        help="HVAC compatibility score (default: 3)",
    )

    # Weight overrides
    parser.add_argument(
        "--weight-structural", type=float, default=None,
        help="Override structural capacity weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-power", type=float, default=None,
        help="Override power infrastructure weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-fiber", type=float, default=None,
        help="Override fiber access weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-contamination", type=float, default=None,
        help="Override contamination risk weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-seismic", type=float, default=None,
        help="Override seismic zone weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-zoning", type=float, default=None,
        help="Override zoning compatibility weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-logistics", type=float, default=None,
        help="Override logistics/dock access weight (0.0-1.0)",
    )
    parser.add_argument(
        "--weight-hvac", type=float, default=None,
        help="Override HVAC compatibility weight (0.0-1.0)",
    )

    # Building metadata
    parser.add_argument(
        "--building-type", type=str, default="",
        help="Building type (warehouse, office, retail, etc.)",
    )
    parser.add_argument(
        "--building-age", type=int, default=0,
        help="Year the building was constructed",
    )
    parser.add_argument(
        "--floor-area", type=float, default=0.0,
        help="Total floor area in square feet",
    )
    parser.add_argument(
        "--target-mw", type=float, default=0.0,
        help="Target IT load in megawatts",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    if args.input:
        # JSON file input mode
        with open(args.input) as f:
            data = json.load(f)

        scores = data.get("scores", {})
        weights = data.get("weights", None)
        costs = data.get("costs", {})
        building_type = data.get("building_type", "")
        building_age = data.get("building_age", 0)
        floor_area_sqft = data.get("floor_area_sqft", 0.0)
        target_it_load_mw = data.get("target_it_load_mw", 0.0)
    else:
        # CLI argument mode
        scores = {
            "structural_capacity": args.structural,
            "power_infrastructure": args.power,
            "fiber_access": args.fiber,
            "contamination_risk": args.contamination,
            "seismic_zone": args.seismic,
            "zoning_compatibility": args.zoning,
            "logistics_dock_access": args.logistics,
            "hvac_compatibility": args.hvac,
        }

        # Build weights from CLI overrides
        weights = DEFAULT_WEIGHTS.copy()
        weight_overrides = {
            "structural_capacity": args.weight_structural,
            "power_infrastructure": args.weight_power,
            "fiber_access": args.weight_fiber,
            "contamination_risk": args.weight_contamination,
            "seismic_zone": args.weight_seismic,
            "zoning_compatibility": args.weight_zoning,
            "logistics_dock_access": args.weight_logistics,
            "hvac_compatibility": args.weight_hvac,
        }
        for key, val in weight_overrides.items():
            if val is not None:
                weights[key] = val

        costs = {}
        building_type = args.building_type
        building_age = args.building_age
        floor_area_sqft = args.floor_area
        target_it_load_mw = args.target_mw

    result = calculate(
        scores=scores,
        weights=weights,
        costs=costs,
        building_type=building_type,
        building_age=building_age,
        floor_area_sqft=floor_area_sqft,
        target_it_load_mw=target_it_load_mw,
    )

    output_json = json.dumps(asdict(result), indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Assessment written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
