#!/usr/bin/env python3
"""CPM Scheduler -- proc-schedule bundled script.

Critical Path Method (CPM) scheduler for data center construction projects.
Generates a task graph with forward/backward pass, float analysis, critical
path identification, resource loading by trade, and Gantt-ready JSON output.

**CPM Algorithm:**
1. Forward pass: Calculate Early Start (ES) and Early Finish (EF) for each task.
   ES = max(EF of all predecessors). EF = ES + duration.
2. Backward pass: Calculate Late Finish (LF) and Late Start (LS) from project end.
   LF = min(LS of all successors). LS = LF - duration.
3. Float = LS - ES (equivalently LF - EF).
4. Critical path = sequence of tasks where float == 0.

**Task Graph Assumptions:**
- Standard DC construction sequence: site prep -> foundations -> steel -> envelope
  -> MEP rough-in -> electrical + mechanical (parallel) -> fire protection ->
  commissioning -> IST -> fit-out.
- Long-lead items (transformers, generators) start at project kickoff and must
  arrive before electrical infrastructure begins.
- Multi-phase projects generate parallel task sets per data hall with shared
  infrastructure tasks as predecessors.

**Duration Scaling Rules:**
- Base durations calibrated for 50MW hyperscale data hall.
- Enterprise: 0.6x duration (simpler systems, less redundancy).
- Colo: 0.8x duration (standard but multi-tenant adds fit-out complexity).
- Modular: 0.4x duration (factory-built, minimal site work).
- Edge: 0.25x duration (pre-integrated, rapid deployment).
- Capacity scaling: durations increase logarithmically with capacity above 50MW.

Requires: Python 3.11+ (stdlib only, no external dependencies).

Usage:
    python3 cpm-scheduler.py --help
    python3 cpm-scheduler.py --facility-type hyperscale --capacity-mw 50 --phases 1 --start-date 2026-06-01 --brownfield false
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, timedelta
from typing import Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Base durations in weeks for a 50MW hyperscale data hall
BASE_TASKS = [
    {"id": "site_prep", "name": "Site Preparation", "duration": 6,
     "deps": [], "resources": {"general_labor": 25, "equipment_operators": 8}},
    {"id": "foundations", "name": "Foundations", "duration": 8,
     "deps": ["site_prep"], "resources": {"general_labor": 30, "concrete_workers": 15}},
    {"id": "structural_steel", "name": "Structural Steel", "duration": 10,
     "deps": ["foundations"], "resources": {"ironworkers": 20, "general_labor": 10}},
    {"id": "building_envelope", "name": "Building Envelope", "duration": 10,
     "deps": ["structural_steel"], "resources": {"cladding_crew": 15, "roofing_crew": 10}},
    {"id": "mep_roughin", "name": "MEP Rough-In", "duration": 14,
     "deps": ["building_envelope"], "resources": {"electricians": 20, "pipefitters": 15, "general_labor": 10}},
    {"id": "electrical_infra", "name": "Electrical Infrastructure", "duration": 12,
     "deps": ["mep_roughin"], "resources": {"electricians": 35, "controls_techs": 8}},
    {"id": "mechanical_infra", "name": "Mechanical Infrastructure", "duration": 12,
     "deps": ["mep_roughin"], "resources": {"pipefitters": 25, "hvac_techs": 15}},
    {"id": "fire_protection", "name": "Fire Protection", "duration": 7,
     "deps": ["electrical_infra", "mechanical_infra"], "resources": {"fire_protection_techs": 10}},
    {"id": "commissioning", "name": "Commissioning (Level 2-3)", "duration": 6,
     "deps": ["fire_protection"], "resources": {"commissioning_agents": 8, "controls_techs": 6}},
    {"id": "ist", "name": "Integrated Systems Testing (Level 4)", "duration": 3,
     "deps": ["commissioning"], "resources": {"commissioning_agents": 6, "controls_techs": 4}},
    {"id": "fitout", "name": "White Space Fit-Out", "duration": 10,
     "deps": ["ist"], "resources": {"electricians": 15, "general_labor": 12, "cabling_techs": 10}},
]

# Brownfield-specific tasks prepended to the schedule
BROWNFIELD_TASKS = [
    {"id": "demolition", "name": "Demolition", "duration": 4,
     "deps": [], "resources": {"general_labor": 20, "equipment_operators": 6}},
    {"id": "abatement", "name": "Hazmat Abatement", "duration": 3,
     "deps": ["demolition"], "resources": {"abatement_crew": 12}},
]

# Long-lead procurement tasks (run in parallel with construction)
LONGLEAD_TASKS = [
    {"id": "longlead_transformer", "name": "Transformer Procurement", "duration": 60,
     "deps": [], "resources": {}},
    {"id": "longlead_generator", "name": "Generator Procurement", "duration": 40,
     "deps": [], "resources": {}},
    {"id": "longlead_switchgear", "name": "Switchgear Procurement", "duration": 33,
     "deps": [], "resources": {}},
]

# Facility type duration multipliers
FACILITY_MULTIPLIERS = {
    "hyperscale": 1.0,
    "enterprise": 0.6,
    "colo": 0.8,
    "modular": 0.4,
    "edge": 0.25,
}

# Shared infrastructure tasks for multi-phase campuses
SHARED_INFRA_TASKS = [
    {"id": "shared_site_work", "name": "Campus Site Work & Utilities", "duration": 10,
     "deps": [], "resources": {"general_labor": 30, "equipment_operators": 12}},
    {"id": "shared_utility_feeds", "name": "Utility Feed Installation", "duration": 8,
     "deps": ["shared_site_work"], "resources": {"electricians": 15, "general_labor": 10}},
]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Task:
    """A single CPM task."""
    id: str
    name: str
    duration_weeks: int
    dependencies: list
    resources: dict
    early_start: int = 0       # week number
    early_finish: int = 0
    late_start: int = 0
    late_finish: int = 0
    float_weeks: int = 0
    phase: int = 0             # 0 = shared/single, 1+ = per-hall


@dataclass
class ScheduleResult:
    """Complete CPM schedule result."""
    tasks: list
    critical_path: list
    total_duration_weeks: int
    milestones: list
    resource_histogram: dict


# ---------------------------------------------------------------------------
# Core CPM functions
# ---------------------------------------------------------------------------

def scale_duration(base_duration: int, facility_type: str, capacity_mw: float) -> int:
    """Scale task duration by facility type and capacity.

    Base durations are calibrated for 50MW hyperscale. Capacity scaling
    uses logarithmic growth above 50MW to avoid linear blowup.
    """
    multiplier = FACILITY_MULTIPLIERS.get(facility_type, 1.0)

    # Capacity scaling: log2(capacity/50) * 0.15 additional factor above 50MW
    capacity_factor = 1.0
    if capacity_mw > 50:
        capacity_factor = 1.0 + math.log2(capacity_mw / 50) * 0.15
    elif capacity_mw < 50 and capacity_mw > 0:
        capacity_factor = max(0.5, capacity_mw / 50)

    scaled = base_duration * multiplier * capacity_factor
    return max(1, round(scaled))


def build_task_graph(
    facility_type: str,
    capacity_mw: float,
    phases: int,
    brownfield: bool,
    long_lead_weeks: int,
) -> list[Task]:
    """Build the complete task graph for the project."""
    tasks = []

    # Override transformer lead time if specified
    longlead = []
    for lt in LONGLEAD_TASKS:
        t = dict(lt)
        if t["id"] == "longlead_transformer":
            t["duration"] = long_lead_weeks
        longlead.append(t)

    # Long-lead procurement tasks (always included, no scaling)
    for lt in longlead:
        tasks.append(Task(
            id=lt["id"],
            name=lt["name"],
            duration_weeks=lt["duration"],
            dependencies=list(lt["deps"]),
            resources=dict(lt.get("resources", {})),
            phase=0,
        ))

    if phases > 1:
        # Multi-phase: add shared infrastructure first
        for st in SHARED_INFRA_TASKS:
            dur = scale_duration(st["duration"], facility_type, capacity_mw)
            tasks.append(Task(
                id=st["id"],
                name=st["name"],
                duration_weeks=dur,
                dependencies=list(st["deps"]),
                resources=dict(st["resources"]),
                phase=0,
            ))

        # Generate per-hall task sets
        for phase_num in range(1, phases + 1):
            prefix = f"hall{phase_num}_"
            first_dep = "shared_utility_feeds"

            if brownfield and phase_num == 1:
                # Only first hall gets brownfield tasks
                for bt in BROWNFIELD_TASKS:
                    dur = scale_duration(bt["duration"], facility_type, capacity_mw)
                    task_id = prefix + bt["id"]
                    deps = [prefix + d if d else first_dep for d in bt["deps"]]
                    if not bt["deps"]:
                        deps = [first_dep]
                    tasks.append(Task(
                        id=task_id,
                        name=f"Hall {phase_num}: {bt['name']}",
                        duration_weeks=dur,
                        dependencies=deps,
                        resources=dict(bt["resources"]),
                        phase=phase_num,
                    ))
                first_dep = prefix + "abatement"

            for bt in BASE_TASKS:
                dur = scale_duration(bt["duration"], facility_type, capacity_mw)
                task_id = prefix + bt["id"]
                deps = []
                for d in bt["deps"]:
                    deps.append(prefix + d)
                if not bt["deps"]:
                    deps = [first_dep]

                # Electrical infra also depends on long-lead deliveries
                if bt["id"] == "electrical_infra":
                    deps.extend(["longlead_transformer", "longlead_generator", "longlead_switchgear"])

                tasks.append(Task(
                    id=task_id,
                    name=f"Hall {phase_num}: {bt['name']}",
                    duration_weeks=dur,
                    dependencies=deps,
                    resources=dict(bt["resources"]),
                    phase=phase_num,
                ))
    else:
        # Single hall
        first_task_deps: list[str] = []

        if brownfield:
            for bt in BROWNFIELD_TASKS:
                dur = scale_duration(bt["duration"], facility_type, capacity_mw)
                tasks.append(Task(
                    id=bt["id"],
                    name=bt["name"],
                    duration_weeks=dur,
                    dependencies=list(bt["deps"]),
                    resources=dict(bt["resources"]),
                    phase=0,
                ))
            first_task_deps = ["abatement"]

        for bt in BASE_TASKS:
            dur = scale_duration(bt["duration"], facility_type, capacity_mw)
            deps = list(bt["deps"]) if bt["deps"] else first_task_deps

            # Electrical infra depends on long-lead deliveries
            if bt["id"] == "electrical_infra":
                deps = list(bt["deps"])
                deps.extend(["longlead_transformer", "longlead_generator", "longlead_switchgear"])

            tasks.append(Task(
                id=bt["id"],
                name=bt["name"],
                duration_weeks=dur,
                dependencies=deps,
                resources=dict(bt["resources"]),
                phase=0,
            ))

    return tasks


def forward_pass(tasks: list[Task]) -> None:
    """CPM forward pass: calculate ES and EF for each task."""
    task_map = {t.id: t for t in tasks}

    # Topological order processing
    resolved = set()
    iterations = 0
    max_iter = len(tasks) * len(tasks)  # safety limit

    while len(resolved) < len(tasks) and iterations < max_iter:
        iterations += 1
        for task in tasks:
            if task.id in resolved:
                continue
            # Check if all dependencies are resolved
            if all(d in resolved for d in task.dependencies):
                if task.dependencies:
                    task.early_start = max(
                        task_map[d].early_finish for d in task.dependencies
                    )
                else:
                    task.early_start = 0
                task.early_finish = task.early_start + task.duration_weeks
                resolved.add(task.id)


def backward_pass(tasks: list[Task]) -> None:
    """CPM backward pass: calculate LS, LF, and float for each task."""
    task_map = {t.id: t for t in tasks}

    # Find project end (max EF)
    project_end = max(t.early_finish for t in tasks)

    # Build successor map
    successors: dict[str, list[str]] = {t.id: [] for t in tasks}
    for task in tasks:
        for dep in task.dependencies:
            if dep in successors:
                successors[dep].append(task.id)

    # Initialize all LF to project end
    for task in tasks:
        task.late_finish = project_end
        task.late_start = project_end - task.duration_weeks

    # Process in reverse topological order
    resolved = set()
    iterations = 0
    max_iter = len(tasks) * len(tasks)

    # Start from tasks with no successors
    while len(resolved) < len(tasks) and iterations < max_iter:
        iterations += 1
        for task in reversed(tasks):
            if task.id in resolved:
                continue
            # Check if all successors are resolved
            if all(s in resolved for s in successors[task.id]):
                if successors[task.id]:
                    task.late_finish = min(
                        task_map[s].late_start for s in successors[task.id]
                    )
                else:
                    task.late_finish = project_end
                task.late_start = task.late_finish - task.duration_weeks
                task.float_weeks = task.late_start - task.early_start
                resolved.add(task.id)


def find_critical_path(tasks: list[Task]) -> list[dict]:
    """Identify the critical path (tasks with zero float)."""
    critical = [t for t in tasks if t.float_weeks == 0]
    # Sort by early start to get the path in sequence
    critical.sort(key=lambda t: t.early_start)
    return [{"task_id": t.id, "task_name": t.name} for t in critical]


def generate_milestones(tasks: list[Task], start_date: date) -> list[dict]:
    """Generate milestone dates from key tasks."""
    task_map = {t.id: t for t in tasks}
    milestone_keys = [
        ("foundations", "Foundations Complete"),
        ("structural_steel", "Steel Complete"),
        ("building_envelope", "Building Watertight"),
        ("mep_roughin", "MEP Rough-In Complete"),
        ("electrical_infra", "Electrical Energization"),
        ("commissioning", "Commissioning Complete"),
        ("ist", "IST Complete"),
        ("fitout", "Substantial Completion"),
    ]

    milestones = []

    # Check for single-phase vs multi-phase
    for key, label in milestone_keys:
        if key in task_map:
            ms_date = start_date + timedelta(weeks=task_map[key].early_finish)
            milestones.append({"name": label, "date": ms_date.isoformat()})
        else:
            # Check for hall1_ prefix (multi-phase)
            hall_key = f"hall1_{key}"
            if hall_key in task_map:
                ms_date = start_date + timedelta(weeks=task_map[hall_key].early_finish)
                milestones.append({"name": f"Hall 1: {label}", "date": ms_date.isoformat()})

    return milestones


def generate_resource_histogram(tasks: list[Task], total_weeks: int) -> dict:
    """Generate resource histogram: headcount by trade by week."""
    trades: dict[str, list[int]] = {}

    for task in tasks:
        if not task.resources:
            continue
        for trade, headcount in task.resources.items():
            if trade not in trades:
                trades[trade] = [0] * total_weeks
            for week in range(task.early_start, min(task.early_finish, total_weeks)):
                trades[trade][week] += headcount

    weeks = list(range(1, total_weeks + 1))
    return {"weeks": weeks, "trades": trades}


def run_cpm(
    facility_type: str,
    capacity_mw: float,
    phases: int,
    start_date: date,
    brownfield: bool,
    long_lead_weeks: int,
) -> ScheduleResult:
    """Run the complete CPM analysis."""
    # Build task graph
    tasks = build_task_graph(facility_type, capacity_mw, phases, brownfield, long_lead_weeks)

    # Forward pass
    forward_pass(tasks)

    # Backward pass
    backward_pass(tasks)

    # Critical path
    critical_path = find_critical_path(tasks)

    # Total duration
    total_duration = max(t.early_finish for t in tasks)

    # Milestones
    milestones = generate_milestones(tasks, start_date)

    # Resource histogram
    histogram = generate_resource_histogram(tasks, total_duration)

    # Convert tasks to serializable format with dates
    task_list = []
    for t in tasks:
        es_date = start_date + timedelta(weeks=t.early_start)
        ef_date = start_date + timedelta(weeks=t.early_finish)
        ls_date = start_date + timedelta(weeks=t.late_start)
        lf_date = start_date + timedelta(weeks=t.late_finish)
        task_list.append({
            "id": t.id,
            "name": t.name,
            "duration_weeks": t.duration_weeks,
            "early_start": es_date.isoformat(),
            "early_finish": ef_date.isoformat(),
            "late_start": ls_date.isoformat(),
            "late_finish": lf_date.isoformat(),
            "float_weeks": t.float_weeks,
            "dependencies": t.dependencies,
            "resources": [
                {"trade": trade, "headcount": count}
                for trade, count in t.resources.items()
            ],
            "phase": t.phase,
        })

    return ScheduleResult(
        tasks=task_list,
        critical_path=critical_path,
        total_duration_weeks=total_duration,
        milestones=milestones,
        resource_histogram=histogram,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "CPM scheduler for data center construction projects. "
            "Generates task graph with critical path analysis, float "
            "calculation, resource loading, and Gantt-ready JSON output."
        ),
        epilog=(
            "Examples:\n"
            "  python3 cpm-scheduler.py --facility-type hyperscale --capacity-mw 50 --phases 1 --start-date 2026-06-01 --brownfield false\n"
            "  python3 cpm-scheduler.py --facility-type enterprise --capacity-mw 10 --phases 1 --start-date 2026-09-01 --brownfield true\n"
            "  python3 cpm-scheduler.py --facility-type hyperscale --capacity-mw 200 --phases 4 --start-date 2026-06-01 --brownfield false\n"
            "\nPart of proc-schedule skill (stellenium/dc-skills)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--facility-type",
        choices=["hyperscale", "enterprise", "colo", "modular", "edge"],
        default="hyperscale",
        help="Facility type (default: hyperscale)",
    )
    parser.add_argument(
        "--capacity-mw", type=float, default=50.0,
        help="IT capacity in MW (default: 50)",
    )
    parser.add_argument(
        "--phases", type=int, default=1,
        help="Number of data halls / phases (default: 1)",
    )
    parser.add_argument(
        "--start-date", default="2026-06-01",
        help="Construction start date YYYY-MM-DD (default: 2026-06-01)",
    )
    parser.add_argument(
        "--brownfield", default="false",
        help="Brownfield conversion: true/false (default: false)",
    )
    parser.add_argument(
        "--long-lead-weeks", type=int, default=60,
        help="Transformer lead time override in weeks (default: 60)",
    )
    parser.add_argument(
        "--output", metavar="FILE",
        help="JSON output file (default: stdout)",
    )

    return parser.parse_args()


def main():
    """Entry point."""
    args = parse_args()

    # Parse start date
    try:
        start = date.fromisoformat(args.start_date)
    except ValueError:
        print(f"Error: Invalid date format '{args.start_date}'. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    brownfield = args.brownfield.lower() in ("true", "1", "yes")

    # Run CPM
    result = run_cpm(
        facility_type=args.facility_type,
        capacity_mw=args.capacity_mw,
        phases=args.phases,
        start_date=start,
        brownfield=brownfield,
        long_lead_weeks=args.long_lead_weeks,
    )

    # Serialize
    output = {
        "artifact_type": "construction-schedule",
        "skill_version": "1.0",
        "facility_type": args.facility_type,
        "capacity_mw": args.capacity_mw,
        "phases": args.phases,
        "start_date": args.start_date,
        "brownfield": brownfield,
        "tasks": result.tasks,
        "critical_path": result.critical_path,
        "total_duration_weeks": result.total_duration_weeks,
        "milestones": result.milestones,
        "resource_histogram": result.resource_histogram,
    }

    output_json = json.dumps(output, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json + "\n")
        print(f"Schedule written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
