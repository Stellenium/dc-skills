---
name: proc-schedule
description: "Generate a data center project schedule with phase sequencing, critical path analysis, milestone tracking, and resource loading. Use when building a DC construction schedule, identifying the critical path, planning project phases and milestones, or estimating project duration and resource needs. Trigger with \"project schedule\", \"construction timeline\", \"critical path\", \"milestone schedule\", \"Gantt chart\", \"DC project timeline\", or \"how long will this take?\"."
---

# Construction Schedule & CPM Analysis

Generate a construction schedule with Critical Path Method analysis, long-lead
item integration, resource loading by trade, and float analysis. The bundled
CPM scheduler script produces deterministic critical path identification and
Gantt-ready JSON output for data center construction projects.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the schedule framework.

**Project Context:**

1. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

2. What is the total IT capacity (MW)?
   - Per data hall if multi-hall campus

3. How many phases or data halls?
   - Single data hall
   - Multi-hall campus (specify number)
   - Phased deployment with timeline targets

4. Is this greenfield or brownfield?
   - **Greenfield:** New construction from bare site
   - **Brownfield:** Conversion of existing building (adds demolition/abatement tasks)

5. What is the construction start date?
   - Planned notice-to-proceed (NTP) date

6. What is the target substantial completion date?
   - Contractual milestone or business requirement

7. What are the site conditions?
   - Clear site, ready for construction
   - Demolition required
   - Environmental remediation needed
   - Grading and earthwork significant (hilly terrain, poor soils)

8. What climate zone affects construction?
   - Arid (minimal weather delays)
   - Temperate (moderate weather buffer needed)
   - Cold/wet (significant weather buffer: 10-15% on outdoor tasks)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Hyperscale Path

If facility type is **Hyperscale:**

1. Is the campus infrastructure (utility feeds, roads, central plant) already built?
2. What is the standardized data hall module size?
3. Are halls being delivered in parallel or sequence?
4. What is the long-lead equipment procurement status? (ordered/not ordered)

### Brownfield Path

If project is **Brownfield:**

1. What demolition scope is required?
2. Is asbestos or hazardous material abatement needed?
3. What existing infrastructure can be reused?
4. What is the maximum allowable downtime for adjacent operations?

### Modular/Prefab Path

If facility type is **Modular/prefab:**

1. Where is the factory manufacturing location?
2. What is the factory-to-site transport method and distance?
3. How many modules per shipment?
4. What site preparation is needed for module placement?

## What I Need from Upstream

**From contract-structure (proc-contract-structure):**
- Milestone payment schedule (triggers define schedule milestones)
- Liquidated damages trigger dates
- Defects liability period start date

**From supply-chain-assessment (proc-supply-chain):**
- Long-lead item delivery dates (especially transformers and generators)
- Equipment delivery sequence by category
- Procurement timeline constraints

If upstream artifacts are not available, I will use standard DC construction
durations and industry-standard long-lead assumptions.

## Calculation Scripts

For deterministic CPM calculations, use the bundled script:

- `scripts/cpm-scheduler.py` -- CPM algorithm with forward/backward pass, float analysis, resource loading, and multi-phase support

**Usage:**
```bash
python3 scripts/cpm-scheduler.py \
  --facility-type hyperscale \
  --capacity-mw 50 \
  --phases 1 \
  --start-date 2026-06-01 \
  --brownfield false
```

**Arguments:**
- `--facility-type`: hyperscale, enterprise, colo, modular, edge
- `--capacity-mw`: IT capacity in MW
- `--phases`: Number of data halls (multi-phase generates parallel task sets)
- `--start-date`: Construction start date (YYYY-MM-DD)
- `--brownfield`: true/false (adds demolition/abatement if true)
- `--long-lead-weeks`: Override transformer lead time (default: 60)

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Schedule Analysis Process

### Step 1: Define Task Graph

Standard DC construction task graph for a single data hall:

| Task | Duration (weeks) | Dependencies | Key Trades |
|------|-------------------|--------------|------------|
| Site preparation | 4-8 | None | General labor, earthwork |
| Foundations | 6-10 | Site prep | Concrete, rebar |
| Structural steel | 8-12 | Foundations | Ironworkers |
| Building envelope | 8-12 | Structural steel | Cladding, roofing |
| MEP rough-in | 12-16 | Building envelope | Electricians, pipefitters |
| Electrical infrastructure | 10-14 | MEP rough-in | Electricians, controls |
| Mechanical infrastructure | 10-14 | MEP rough-in (parallel with electrical) | Pipefitters, HVAC techs |
| Fire protection | 6-8 | Electrical + mechanical | Fire protection techs |
| Commissioning (Level 2-3) | 4-8 | Fire protection | Commissioning agents |
| IST (Level 4) | 2-4 | Commissioning | Controls techs, commissioning |
| Fit-out (white space) | 8-12 | IST complete | All trades |

**Long-lead procurement** (starts at project kickoff, not in construction sequence):
- Transformers: 52-78 weeks from order
- Generators: 26-52 weeks from order
- Switchgear: 26-40 weeks from order

### Step 2: Run CPM Algorithm

1. **Forward pass:** Calculate early start (ES) and early finish (EF) for each task
2. **Backward pass:** Calculate late start (LS) and late finish (LF) from project end date
3. **Float calculation:** Float = LS - ES (tasks with zero float are on the critical path)
4. **Critical path identification:** Sequence of tasks with zero float from start to finish

### Step 3: Validate Against Industry Benchmarks

| Facility Type | Typical Duration (single hall) | Notes |
|---------------|-------------------------------|-------|
| Hyperscale (50MW) | 18-24 months | Driven by electrical infrastructure |
| Enterprise (5MW) | 12-18 months | Simpler redundancy, faster commissioning |
| Colo (10MW) | 14-20 months | Multi-tenant fit-out adds 2-4 months |
| Modular (1MW pod) | 6-9 months (factory + site) | Factory build parallel with site prep |
| Edge (<1MW) | 3-6 months | Pre-integrated, minimal site work |

### Step 4: Resource Loading

Assign trade headcounts to each task for resource histogram generation:
- Electricians (peak during electrical infrastructure)
- Pipefitters (peak during mechanical infrastructure)
- Ironworkers (peak during structural steel)
- General labor (peak during site prep and foundations)
- Controls technicians (peak during commissioning)
- Commissioning agents (peak during IST)

### Step 5: Multi-Phase Coordination

For campus deployments with parallel halls:
- Shared infrastructure (utility feeds, central plant, roads) are predecessors for all halls
- Parallel hall construction can compress total timeline by 30-40%
- Resource conflicts between parallel halls must be identified and resolved
- Staggered starts (4-8 week offsets) smooth resource loading peaks

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-construction-schedule.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: proc-schedule v1.0]

#### 1. Schedule Summary
- Total duration: [weeks/months]
- Critical path: [task sequence]
- Key milestones with dates
- Float analysis highlights

#### 2. Task Schedule
- Full task list with durations, ES/EF/LS/LF, float, and dependencies
- Critical path tasks highlighted

#### 3. Long-Lead Item Integration
- Procurement milestones for transformers, generators, switchgear
- Required order dates based on delivery lead times
- Risk items flagged

#### 4. Resource Loading
- Resource histogram by trade and week
- Peak headcount periods identified
- Trade stacking and coordination notes

#### 5. Risk and Float Analysis
- Tasks with least float (near-critical)
- Weather delay buffer recommendations
- Schedule acceleration opportunities

### JSON Sidecar: `<project-name>-construction-schedule.json`

```json
{
  "artifact_type": "construction-schedule",
  "skill_version": "1.0",
  "project_name": "...",
  "tasks": [
    {
      "id": "site_prep",
      "name": "Site Preparation",
      "duration_weeks": 6,
      "early_start": "2026-06-01",
      "early_finish": "2026-07-13",
      "late_start": "2026-06-15",
      "late_finish": "2026-07-27",
      "float_weeks": 2,
      "dependencies": [],
      "resources": [
        {"trade": "general_labor", "headcount": 25},
        {"trade": "equipment_operators", "headcount": 8}
      ]
    }
  ],
  "critical_path": [
    {"task_id": "foundations", "task_name": "Foundations"},
    {"task_id": "structural_steel", "task_name": "Structural Steel"}
  ],
  "total_duration_weeks": 96,
  "milestones": [
    {"name": "Foundations complete", "date": "2026-10-01"},
    {"name": "Substantial completion", "date": "2028-06-01"}
  ],
  "resource_histogram": {
    "weeks": [1, 2, 3],
    "trades": {
      "electricians": [0, 0, 10],
      "pipefitters": [0, 0, 8]
    }
  }
}
```

## Gotchas

- **The critical path for DC construction is almost always the electrical infrastructure, not the building structure.** Transformer delivery (52-78 weeks) plus switchgear (26-40 weeks) plus electrical commissioning (4-8 weeks) dominates the schedule. Accelerating structural steel by 2 weeks is meaningless if the transformer arrives 10 weeks late.

- **Phased campus delivery can compress total timeline by 30-40% through parallel hall construction.** But parallel construction requires careful coordination of shared infrastructure (utility feeds, central plant, site roads). Starting a second hall before the first hall's electrical infrastructure is energized creates resource conflicts and safety risks.

- **Weather delays in foundation and steel phases should be buffered at 10-15% in non-arid climates.** Rain days during concrete pours cause 1-3 day delays per occurrence. In northern climates, foundation work has a seasonal window (April-October). Missing the window can delay the project by 4-6 months.

- **Commissioning is sequential, not parallelizable.** Level 2 (pre-functional) must complete before Level 3 (functional), which must complete before Level 4 (IST). Each level requires the previous level's sign-off. Compressing commissioning below 8 weeks for a 50MW facility is unrealistic regardless of staffing.

- **Resource conflicts between parallel tasks are the hidden schedule risk.** The schedule may show electrical and mechanical infrastructure running in parallel, but if the same electricians are needed for both, the actual duration is sequential. Resource-loaded schedules expose these conflicts; unloaded CPM schedules hide them.

## Evaluations

See `evals/evals.json` for test scenarios covering single-hall greenfield, multi-phase campus, and brownfield conversion schedules.
