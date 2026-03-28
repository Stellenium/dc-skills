---
name: eng-brownfield-convert
description: "Assess building-to-data-center conversion feasibility with weighted scoring across structural, power, cooling, and compliance factors. Use when evaluating whether an existing building can become a data center, assessing warehouse or industrial conversion potential, or scoring brownfield sites for DC conversion. Trigger with \"brownfield conversion\", \"building conversion\", \"convert to data center\", \"warehouse to DC\", \"adaptive reuse\", or \"can this building become a data center?\"."
argument-hint: "<building-type>"
---

# Brownfield Conversion Feasibility Assessment

Evaluate existing building suitability for data center conversion using weighted
multi-factor scoring across 8 criteria. Produces a GO, CONDITIONAL, or NO-GO
recommendation with remediation cost estimates per item. Consumes construction
cost benchmarks for regional cost calibration.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire assessment approach.

**Building Context:**

1. What type of building is being evaluated?
   - Industrial warehouse / distribution center
   - Office building (Class A, B, or C)
   - Big-box retail / commercial
   - Manufacturing / factory
   - Mixed-use or other (describe)

2. What is the building age (year built)?
   - Pre-1980 (asbestos/lead paint risk -- triggers contamination assessment)
   - 1980-2000 (moderate -- some legacy materials possible)
   - Post-2000 (low contamination risk)

3. What is the total floor area (sqft) and number of floors?
   - Ground floor only vs multi-story
   - Usable area for whitespace vs support space

4. What is the current use and occupancy status?
   - Vacant (simplifies conversion timeline)
   - Occupied (requires phased transition plan)
   - Partially occupied (identify available sections)

5. What is the building location?
   - City, state/province, country
   - Specific address if available (for seismic zone and zoning lookup)

6. What is the target IT capacity (MW) and rack density (kW/rack)?
   - Total target IT load for the conversion
   - Per-rack density target (affects structural and cooling requirements)

7. What are the budget constraints?
   - Total conversion budget or budget range
   - Hard ceiling vs flexible based on feasibility
   - Timeline constraints (months to operational)

8. What is the primary workload type?
   - AI training (high density, likely liquid cooling)
   - AI inference (moderate density, mixed cooling)
   - Enterprise / general compute (standard density)
   - Colocation (multi-tenant, variable density)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather building-specific detail.

### Structural Assessment

1. What is the floor loading capacity (psf)?
   - Ground floor slab thickness and reinforcement type
   - Upper floor loading if multi-story
   - Known structural reports or engineering assessments

2. What is the column spacing (ft x ft)?
   - Standard rack rows need minimum 10ft clear between columns
   - Wide bays (40ft+) preferred for flexible layout

3. What is the clear ceiling height (ft)?
   - Minimum 14ft for overhead cable trays and cooling
   - 18ft+ preferred for containment and overhead piping
   - Warehouse/industrial typically 20-30ft (excellent)
   - Office typically 9-12ft (challenging)

### Power Infrastructure

1. What is the existing electrical service?
   - Utility voltage and amperage at the building entrance
   - Existing transformer capacity (kVA/MVA)
   - Switchgear age and condition
   - Distance to nearest utility substation

2. What is the upgrade path?
   - Utility capacity available for expansion
   - Right-of-way for new utility feed
   - Estimated timeline for utility upgrade (typically 12-24 months)

### Fiber and Connectivity

1. What is the existing telecom infrastructure?
   - Number of fiber providers currently serving the building
   - Conduit routes to property boundary
   - Distance to nearest carrier hotel or meet-me room

2. What is the carrier proximity?
   - Fiber-lit buildings within 1 mile
   - Dark fiber availability
   - Diverse physical route options

### Environmental Assessment

1. Has a Phase I ESA been conducted?
   - Known contamination issues (asbestos, lead, PCBs, USTs)
   - Soil contamination from prior industrial use
   - Remediation estimates if available

2. Building material concerns?
   - Asbestos in insulation, tiles, or roofing (pre-1980 buildings)
   - Lead paint
   - PCB-containing transformers or ballasts

## Scoring Framework

### 8-Factor Weighted Scoring (1-5 Scale)

| Factor | Default Weight | Score 5 (Excellent) | Score 3 (Adequate) | Score 1 (Critical Risk) |
|--------|---------------|--------------------|--------------------|------------------------|
| Structural Capacity | 20% | >150 psf floor load, 30ft+ ceiling, wide bays | 100-150 psf, 14-18ft ceiling | <75 psf, <12ft ceiling, narrow bays |
| Power Infrastructure | 20% | Existing 13.8kV+ service, >5MW available, substation adjacent | 480V service, 1-5MW, upgrade possible | 208V only, <1MW, major utility work needed |
| Fiber Access | 10% | 3+ carriers on-net, diverse routes | 1-2 carriers, single route, upgrade feasible | No fiber, >2 miles to nearest POP |
| Contamination Risk | 15% | Post-2000, no ESA findings, clean history | Minor issues, manageable abatement ($5-15/sqft) | Asbestos throughout, UST, major soil contamination |
| Seismic Zone | 10% | Zone 0-1, no special requirements | Zone 2, moderate seismic bracing needed | Zone 3-4, major structural retrofit required |
| Zoning Compatibility | 15% | Industrial/data center zoned, no change needed | Commercial, change-of-use feasible (6-12 months) | Residential/protected, zoning change unlikely |
| Logistics/Dock Access | 5% | Loading dock, truck court, generator pad space | Street-level access, limited staging | No dock, constrained access, no generator space |
| HVAC Compatibility | 5% | Large mechanical room, roof capacity for cooling | Moderate space, some equipment fits | No mechanical space, weak roof structure |

**Weights must sum to 100%.** Users may adjust weights based on project priorities.

### Decision Thresholds

| Weighted Average | Recommendation | Action |
|-----------------|----------------|--------|
| >= 3.5 | **GO** | Proceed with detailed engineering and due diligence |
| 2.5 - 3.49 | **CONDITIONAL** | Proceed only with specific remediations for low-scoring factors |
| < 2.5 | **NO-GO** | Building is not feasible for DC conversion at acceptable cost |

**Override rule:** Any single factor scoring 1 triggers automatic CONDITIONAL
regardless of weighted average. Document the blocking factor and required remediation.

### Remediation Cost Estimates

Each factor scoring below 3 includes a remediation cost estimate:

| Remediation Item | Typical Cost Range | Timeline | Source |
|------------------|-------------------|----------|--------|
| Structural reinforcement (floor loading) | $15-40/sqft | 3-6 months | COST-BENCHMARKS.md |
| Electrical upgrade (utility feed) | $500K-15M depending on capacity | 12-24 months | COST-BENCHMARKS.md |
| Fiber build (new route) | $50K-500K per route mile | 3-9 months | Industry standard |
| Asbestos abatement | $5-25/sqft | 2-6 months | EPA contractor rates |
| Lead paint removal | $3-10/sqft | 1-3 months | EPA contractor rates |
| UST removal and soil remediation | $50K-500K per tank | 3-12 months | State environmental agency |
| Seismic retrofit | 15-30% of structural cost | 6-12 months | COST-BENCHMARKS.md |
| Zoning change application | $10K-100K (legal/filing) | 6-18 months | Municipal fee schedules |
| Loading dock construction | $150K-500K | 2-4 months | Construction estimates |
| Mechanical space expansion | $200-400/sqft | 3-6 months | Construction estimates |

### Reference Data

Load these files on demand -- do not read upfront:

- [Construction cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional construction costs, labor indices, and power cost benchmarks for remediation cost calibration
- [Power tariffs](../../references/POWER-TARIFFS.md) -- Regional power costs for operational cost assessment

## Analysis & Output

### Process

1. **Collect building data** from Phase 1 and Phase 2 discovery
2. **Score each factor 1-5** using defined thresholds
3. **Apply weights** (default or user-adjusted, must sum to 100%)
4. **Calculate weighted average** across all 8 factors
5. **Check override rule** (any factor scoring 1 triggers CONDITIONAL)
6. **Estimate remediation costs** for factors scoring below 3
7. **Sum total remediation range** (low and high estimates)
8. **Generate recommendation** with cost-benefit context
9. **Run bundled script** for deterministic scoring: `scripts/brownfield-scorer.py`

### Quality Check

1. Verify all 8 factors are scored (no gaps)
2. Confirm weights sum to 100%
3. Cross-check remediation costs against COST-BENCHMARKS.md regional data
4. Validate that override rule is applied when any factor scores 1
5. Ensure pre-1980 buildings have contamination risk specifically assessed
6. Confirm structural floor loading assessment accounts for rack + cooling equipment weight

## Output

This skill produces two files:
1. `<project-name>-brownfield-conversion-assessment.md` -- Full report
2. `<project-name>-brownfield-conversion-assessment.json` -- Structured data

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-brownfield-convert v1.0]

#### 1. Executive Summary
- **Building:** [type, age, location, sqft]
- **Recommendation:** GO / CONDITIONAL / NO-GO
- **Weighted Score:** [X.XX] / 5.00
- **Override Triggered:** Yes / No (if yes, which factor)
- **Total Remediation Cost Estimate:** $[low] - $[high]
- **Key Strengths:** [top 2-3 factors]
- **Key Risks:** [bottom 2-3 factors with remediation summary]

#### 2. Scoring Matrix

| Factor | Score (1-5) | Weight | Weighted Score | Remediation Needed | Cost Estimate | Notes |
|--------|-------------|--------|----------------|-------------------|---------------|-------|
| Structural Capacity | [X] | 20% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Power Infrastructure | [X] | 20% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Fiber Access | [X] | 10% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Contamination Risk | [X] | 15% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Seismic Zone | [X] | 10% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Zoning Compatibility | [X] | 15% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| Logistics/Dock Access | [X] | 5% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| HVAC Compatibility | [X] | 5% | [X.XX] | [Yes/No] | [$X-Y] | [detail] |
| **Total** | | **100%** | **[X.XX]** | | **$[low]-$[high]** | |

#### 3. Remediation Plan

| Item | Priority | Cost Range | Timeline | Dependencies |
|------|----------|-----------|----------|--------------|
| [remediation] | Critical/High/Medium | [$X-Y] | [months] | [blockers] |

#### 4. Recommended Next Steps
- GO: proceed with detailed structural engineering, Phase I ESA if not done, utility application
- CONDITIONAL: address specific remediations before proceeding, get detailed quotes
- NO-GO: alternative building recommendations, greenfield comparison

### JSON Sidecar Schema

```json
{
  "artifact_type": "brownfield-conversion-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "building_type": "...",
  "building_age": 0,
  "floor_area_sqft": 0,
  "recommendation": "GO | CONDITIONAL | NO-GO",
  "weighted_score": 0.00,
  "override_triggered": false,
  "override_factor": null,
  "criteria": [
    {
      "name": "structural_capacity",
      "score": 0,
      "weight": 0.20,
      "weighted_score": 0.00,
      "cost_low": 0,
      "cost_high": 0,
      "notes": "..."
    }
  ],
  "total_cost_low": 0,
  "total_cost_high": 0,
  "remediation_items": []
}
```

## Gotchas

- **Floor loading is the #1 killer for brownfield conversions.** Most office buildings are designed for 50-80 psf live load. A standard server rack with equipment weighs 2,000-3,000 lbs on a 2x4 ft footprint -- that is 250-375 psf concentrated load. Even warehouses at 150 psf may need reinforcement for high-density deployments. Always get a structural engineer's assessment before committing.

- **Utility upgrade timelines are typically the critical path.** Getting 5-20MW of new utility power to a building that currently has 480V/2000A service (roughly 1.5MW) takes 12-24 months in most markets and can cost $5-15M depending on distance to substation and required infrastructure. Start the utility application before finalizing the building purchase.

- **Pre-1980 buildings almost always have asbestos.** It is not just in obvious places like pipe insulation -- it is in floor tiles, ceiling tiles, mastic adhesives, roofing materials, and even drywall joint compound. Full abatement of a 100,000 sqft building can cost $1-2.5M and take 3-6 months. Budget for this even if a Phase I ESA has not been done yet.

- **Zoning change-of-use is not just a paperwork exercise.** Converting commercial or retail to industrial/data center use triggers parking requirement changes, noise ordinance reviews (generators), environmental impact assessments, and sometimes community hearings. Budget 6-18 months and $50-100K in legal and application fees. Some municipalities have imposed DC moratoriums.

- **Ceiling height constrains everything.** Below 14ft clear height, overhead cable trays, containment systems, and cooling infrastructure compete for vertical space. Below 12ft, most modern cooling technologies cannot be deployed effectively. Office buildings with 9-10ft ceilings often require drop-ceiling removal and may still be too constrained.

## Calculation Scripts

For deterministic scoring calculations, use the bundled script:

- `scripts/brownfield-scorer.py` -- Weighted multi-factor scoring calculator with GO/CONDITIONAL/NO-GO recommendation, override rule, and cost aggregation

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering industrial warehouse,
Class A office, and big-box retail conversion assessments.
