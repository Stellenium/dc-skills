---
name: eng-btm-power
description: "Evaluate behind-the-meter power generation for data centers including gas turbines, solar PV, wind, BESS, and fuel cells with LCOE comparison. Use when evaluating on-site power generation, sizing BTM generation, comparing grid vs self-generation economics, or designing microgrid solutions for a DC. Trigger with \"behind the meter\", \"BTM power\", \"on-site generation\", \"microgrid\", \"self-generation\", \"solar for data center\", or \"gas turbine for DC\"."
---

# Behind-the-Meter Power Assessment

Evaluate behind-the-meter (BTM) power generation options for data center facilities.
Models multiple energy sources individually and in hybrid combinations, computes
levelized cost of energy (LCOE), applies federal tax credits (ITC/PTC), and compares
BTM economics against grid power. Consumes the upstream power capacity model.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load (MW) and facility load (MW including PUE overhead)
- Redundancy tier and configuration (affects BTM reliability requirements)
- Grid interconnection status and utility feed configuration
- Behind-the-meter generation flag from Phase 1 discovery

If upstream data is not available, I will ask you for these values or use
industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire BTM evaluation approach.

**Project Context:**

1. What is the facility power requirement (MW)?
   - Total IT load and PUE-adjusted facility load
   - Specify per phase if multi-phase deployment

2. What is the site location?
   - Country and region (for solar GHI and wind capacity factor lookup)
   - Latitude/longitude if available (for precise resource assessment)

3. What is the current grid power situation?
   - Grid power availability (MW at point of interconnection)
   - Current or expected grid tariff ($/kWh)
   - Grid reliability history (outages/year, average duration)

4. Which energy sources should be evaluated? (select all that apply)
   - Natural gas turbine/reciprocating engine
   - Solar PV (ground-mount or rooftop)
   - Wind (onshore)
   - Battery Energy Storage System (BESS)
   - Fuel cells (hydrogen or natural gas)
   - Small Modular Reactor (SMR) -- emerging technology

5. What land is available for on-site generation?
   - Available acreage for solar arrays, wind turbines, or other generation
   - Roof area available for rooftop solar (sqft)
   - Setback and zoning constraints

6. What is the natural gas availability?
   - Pipeline access (yes/no, distance to interconnect)
   - Pipeline pressure and capacity
   - Contracted gas price ($/MMBtu) if known

7. What are the sustainability and carbon goals?
   - Carbon-neutral target date
   - Renewable energy percentage target
   - PPA or REC strategy preferences

8. What is the project timeline?
   - Construction start date (for ITC/PTC safe harbor analysis)
   - Commercial operation date target

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather source-specific detail.

### Solar Path

If solar PV is selected:

1. What is the site GHI (kWh/m2/day)? (Load from SOLAR-WIND-RESOURCE.md for region)
2. Preferred array configuration? (fixed tilt, single-axis tracking, dual-axis)
3. DC:AC ratio target? (typical 1.2-1.4)
4. Panel degradation assumption? (default 0.5%/year)

### Wind Path

If wind is selected:

1. What is the average wind speed at hub height? (Load from SOLAR-WIND-RESOURCE.md)
2. Hub height and turbine class? (IEC Class I/II/III)
3. Terrain complexity? (flat, moderate, complex -- affects wake losses)

### Gas Path

If natural gas is selected:

1. Turbine type preference? (simple cycle, combined cycle, reciprocating engine)
2. Heat recovery potential? (CHP for campus heating/cooling absorption chillers)
3. Emissions permitting constraints? (NOx/SOx limits, carbon pricing jurisdiction)

### BESS Path

If BESS is selected:

1. Primary use case? (peak shaving, backup/UPS replacement, renewable firming, arbitrage)
2. Duration requirement? (2-hour, 4-hour, 8-hour)
3. Cycle life requirement? (daily cycling vs occasional backup)

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| BTM scale range (MW) | 1-10 | 10-200+ | 5-50 | 1-20 | 0.5-5 | 0.1-2 |
| Typical BTM strategy | Gas CHP | Solar+BESS portfolio | Gas+solar (independence) | Shared BTM, tenant allocation | Packaged BESS | BESS-primary |
| Reliability requirement | 99.9% | 99.99% | 99.999% | Per-tenant SLA | 99.9% | 99% |
| Carbon driver | ESG reporting | PPA/REC strategy | Government mandate | Tenant requirements | Corporate policy | Minimal |

### Facility Type Refinements

**Hyperscale additions:**
- Portfolio-level BTM strategy across campus (100MW+ aggregate)?
- PPA vs owned generation preference?
- Curtailment strategy for excess renewable generation?

**Sovereign additions:**
- Energy independence mandate (days of autonomous operation)?
- Fuel diversification requirements?
- Classified generation equipment restrictions?

**Edge additions:**
- Grid-independent operation capability required?
- Containerized generation solution preferred?
- Remote fuel delivery logistics?

## Analysis & Output

### Process

1. **Assess available resources:** Look up solar GHI and wind capacity factors from SOLAR-WIND-RESOURCE.md for the site region
2. **Size each source:** Based on facility load, land availability, and resource quality
3. **Calculate individual LCOE:** For each source using `scripts/lcoe-calculator.py` with formula: LCOE = (CapEx * CRF + Annual OpEx + Annual Fuel - Tax Credits) / Annual Generation
4. **Model hybrid scenarios:** Combine sources (e.g., solar+BESS, gas+solar) and compute blended LCOE weighted by generation share
5. **Apply tax credits:** ITC for solar and BESS (30% post-OBBBA with prevailing wage), PTC for wind ($28.60/MWh post-OBBBA with prevailing wage)
6. **Compare to grid:** Net savings = Grid LCOE - Blended BTM LCOE, accounting for demand charges and time-of-use rates
7. **Assess reliability:** Model BTM contribution to facility uptime (capacity factor, intermittency, storage duration)
8. **Recommend configuration:** Optimal mix based on economics, reliability, sustainability goals, and timeline

### Reference Data

Load these files on demand -- do not read upfront:

- [Solar and wind resource data](../../references/SOLAR-WIND-RESOURCE.md) -- GHI by region, wind capacity factors, seasonal variation
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC rates (6-50% depending on adders), PTC rates, safe harbor rules, post-OBBBA changes
- [Power tariffs](../../references/POWER-TARIFFS.md) -- Grid electricity tariffs by region for grid vs BTM cost comparison

### Validation Loop

1. Compute BTM model from Phase 1 and Phase 2 inputs
2. Cross-check solar capacity factors against SOLAR-WIND-RESOURCE.md regional data
3. Cross-check wind capacity factors against SOLAR-WIND-RESOURCE.md for site class
4. Verify ITC/PTC rates and safe harbor dates against FEDERAL-TAX-GUIDE.md
5. Validate grid tariff against POWER-TARIFFS.md for the region
6. Check that total BTM capacity meets facility load with required redundancy margin
7. Verify LCOE calculation: CRF formula, degradation applied, fuel cost escalated
8. If any constraint violated: flag the error, adjust assumptions, recompute from step 1
9. Repeat until all constraints satisfied

## Output

This skill produces two files:
1. `<project-name>-btm-power-assessment.md` -- Full report
2. `<project-name>-btm-power-assessment.json` -- Structured data for downstream skills

### BTM Power Assessment Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-btm-power v1.0]

#### 1. Executive Summary
- Facility load: [X MW] (IT) / [X MW] (total with PUE)
- BTM sources evaluated: [list]
- Recommended configuration: [description]
- Blended LCOE: [$X-Y/MWh] (range reflecting uncertainty)
- Grid LCOE: [$X/MWh]
- Savings vs grid: [X-Y%]
- Tax credit benefit: [$X-Y M]

#### 2. Source Comparison Matrix

| Source | Capacity (MW) | CapEx ($M) | LCOE ($/MWh) | Capacity Factor | Annual Gen (MWh) | Tax Credit |
|--------|--------------|-----------|--------------|-----------------|-----------------|------------|
| Solar PV | [X] | [X-Y] | [X-Y] | [X%] | [X] | ITC [X%] |
| Wind | [X] | [X-Y] | [X-Y] | [X%] | [X] | PTC $[X]/MWh |
| Gas turbine | [X] | [X-Y] | [X-Y] | [X%] | [X] | N/A |
| BESS | [X MWh] | [X-Y] | [X-Y] | N/A | N/A | ITC [X%] |
| Fuel cell | [X] | [X-Y] | [X-Y] | [X%] | [X] | ITC [X%] |
| SMR | [X] | [X-Y] | [X-Y] | [X%] | [X] | PTC $[X]/MWh |

#### 3. Hybrid Scenario Analysis

| Scenario | Sources | Blended LCOE | Grid Savings | Reliability | Carbon Reduction |
|----------|---------|-------------|-------------|-------------|-----------------|
| Scenario A | [sources] | [$X-Y/MWh] | [X-Y%] | [X%] | [X%] |
| Scenario B | [sources] | [$X-Y/MWh] | [X-Y%] | [X%] | [X%] |

#### 4. Tax Credit Impact Analysis
- ITC eligible assets: [$X M] at [X%] = [$X M] credit
- PTC eligible generation: [X MWh/yr] at $[X]/MWh = [$X M/yr]
- Safe harbor status: [begin construction by July 4, 2026 under post-OBBBA]
- Net tax benefit (10-year): [$X-Y M]

#### 5. Grid vs BTM Cost Comparison
- Grid-only 10-year cost: [$X-Y M]
- BTM blended 10-year cost: [$X-Y M]
- Net savings: [$X-Y M] ([X-Y%])
- Payback period: [X-Y years]

#### 6. Sensitivity Analysis
| Variable | Base Case | Low Case | High Case | Impact on LCOE |
|----------|-----------|----------|-----------|----------------|
| Solar capacity factor | [%] | [%] | [%] | [$/MWh range] |
| Gas price | [$/MMBtu] | [$/MMBtu] | [$/MMBtu] | [$/MWh range] |
| ITC rate | [%] | [%] | [%] | [$/MWh range] |
| Discount rate | [%] | [%] | [%] | [$/MWh range] |

#### 7. Recommended Configuration
- Configuration: [description]
- Total BTM capacity: [X MW]
- Total estimated CapEx: [$X-Y M]
- Blended LCOE: [$X-Y/MWh]
- Grid dependency remaining: [X%]

### JSON Sidecar

```json
{
  "artifact_type": "btm-power-assessment",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "facility_load_mw": 0,
  "sources_evaluated": [],
  "source_lcoes": {},
  "blended_lcoe_per_mwh": 0,
  "grid_lcoe_per_mwh": 0,
  "savings_vs_grid_pct": 0,
  "itc_benefit_total": 0,
  "ptc_benefit_annual": 0,
  "recommended_config": "",
  "confidence_range_low": 0,
  "confidence_range_high": 0,
  "hybrid_scenarios": [],
  "sensitivity": {}
}
```

## Gotchas

- **ITC/PTC safe harbor requires "begin construction" by July 4, 2026 under post-OBBBA rules** -- projects not started lose significant tax benefits. Physical work or 5% safe harbor must be documented.
- **Solar capacity factor in IRENA data is AC-basis** -- DC-basis is typically 15-20% higher due to inverter clipping. Always clarify AC vs DC in calculations and use AC-basis for LCOE to match grid comparison.
- **BESS degradation reduces usable capacity by 2-3% annually** -- a 10-year model must account for 20-30% capacity fade. Warranty typically guarantees 70-80% of nameplate at year 10.
- **Behind-the-meter generation under 10MW in most ISOs avoids the interconnection queue** -- a major timeline and cost advantage. Above 10MW, expect 3-5 year queue delays in congested regions (PJM, CAISO, ERCOT).

## Calculation Scripts

For deterministic LCOE calculations, use the bundled script:

- `scripts/lcoe-calculator.py` -- Unified LCOE calculator for all energy sources with ITC/PTC modeling, hybrid blending, and grid comparison

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering BTM power assessment across
different facility types, energy source combinations, and tax credit structures.
