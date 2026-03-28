---
name: eng-cooling-design
description: "Design data center cooling systems covering all 14 cooling technologies with climate analysis, ASHRAE TC 9.9 compliance, and technology selection. Use when selecting cooling technology for a DC, designing liquid cooling systems, evaluating free cooling potential, sizing cooling infrastructure, or comparing air vs liquid cooling for GPU workloads. Trigger with \"cooling design\", \"liquid cooling\", \"ASHRAE compliance\", \"cooling technology\", \"free cooling\", \"heat rejection\", or \"how to cool a data center\"."
---

# Cooling System Design

Design data center cooling systems by evaluating all 14 cooling technologies against
climate, rack density, water availability, and cost constraints. Produces ranked
technology recommendations with PUE/WUE projections and ASHRAE TC 9.9 compliance
analysis. Consumes the upstream power capacity model.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load (kW)
- Target PUE
- Per-rack power density (kW/rack)
- Redundancy tier (Tier I-IV)
- Phased deployment schedule (if multi-phase)

If upstream data is not available, I will ask you for these values or use
industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction -- proceed to Greenfield Path below
   - **Brownfield:** Existing building conversion or upgrade -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the total IT load (MW) and per-rack density target (kW/rack)?
   - Density determines which cooling technologies are viable
   - < 15 kW/rack: air-cooled feasible
   - 15-40 kW/rack: hybrid air/liquid recommended
   - 40-80 kW/rack: direct liquid cooling required
   - > 80 kW/rack: immersion or rack-scale liquid mandatory

4. What is the facility location and climate zone?
   - Hot-humid (Miami, Singapore, Jakarta)
   - Hot-dry (Phoenix, Riyadh, Las Vegas)
   - Temperate (Northern Virginia, Amsterdam, London)
   - Cold (Stockholm, Montreal, Helsinki)
   - Provide city/region for ASHRAE climate analysis

5. What is the water availability?
   - Abundant (municipal supply, no restrictions)
   - Limited (seasonal restrictions or metering)
   - Scarce/restricted (drought-prone, regulatory limits)
   - Unknown

6. What are the target PUE and WUE?
   - Aggressive: PUE < 1.2, WUE < 0.5 L/kWh
   - Standard: PUE 1.2-1.4, WUE 0.5-1.8 L/kWh
   - No target specified

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

1. Are cooling tower or evaporative system permits obtainable?
2. Site water rights and supply capacity (gallons/day)?
3. Building orientation and prevailing wind direction?
4. District cooling or heat reuse agreements available?

### Brownfield Path

1. Existing HVAC infrastructure assessment:
   - Chiller plant capacity (tons)
   - Air handler type and airflow (CFM)
   - Chilled water loop temperature and flow rate
   - Cooling tower condition and capacity
2. Structural load capacity for rooftop equipment?
3. Available mechanical room space for expansion?
4. Maximum allowable downtime for cooling upgrades?

### High-Density Path (>40 kW/rack)

If rack density exceeds 40 kW:
- Direct liquid cooling (DLC) or immersion cooling is required
- Evaluate: cold plate DLC, single-phase immersion, or two-phase immersion
- Plan CDU (Coolant Distribution Unit) placement and piping manifold
- Secondary loop design: facility water loop temperature and flow rate

### Water-Scarce Path

If water is scarce or restricted:
- Prioritize dry coolers, closed-loop glycol systems, or adiabatic with reclamation
- Cooling towers are high-risk (7-10M gallons/year per MW IT load)
- Calculate WUE impact of each technology option

### Sovereign Path

If facility type is sovereign:
- Prioritize water-independent cooling (operational security)
- Evaluate supply chain security for refrigerants and coolants
- Consider closed-loop systems to avoid external water dependency

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Density range (kW/rack) | 5-15 | 15-80+ | 10-50 | 5-30 | 10-50 | 5-20 |
| Default technology | Air (raised floor) | Hybrid air/liquid | Air/liquid | Air (containment) | Packaged DX | Packaged DX |
| Cooling redundancy | N+1 | N+1 | 2N | N+1 | N | N |
| Water tolerance | Standard | Standard | Restricted | Standard | Limited | None |
| Typical PUE contribution | 0.3-0.5 | 0.1-0.3 | 0.2-0.4 | 0.3-0.5 | 0.2-0.4 | 0.3-0.7 |

## Technology Ranking Framework

All 14 cooling technologies ranked by density tier. Detailed specifications for each
technology are in [cooling-technologies.md](references/cooling-technologies.md) -- load on demand.

| Technology | <15 kW | 15-40 kW | 40-80 kW | >80 kW | Water Use | Relative Cost |
|------------|--------|----------|----------|--------|-----------|---------------|
| Raised-floor air | Primary | Limited | No | No | None | Low |
| In-row cooling | Primary | Primary | No | No | None | Low-Med |
| Hot/cold containment | Primary | Primary | Limited | No | None | Med |
| Rear-door HEX (RDHx) | Viable | Primary | Limited | No | Low | Med |
| Direct-to-chip liquid (DLC) | No | Viable | Primary | Primary | None | Med-High |
| Single-phase immersion | No | Viable | Primary | Primary | None | High |
| Two-phase immersion | No | No | Viable | Primary | None | Very High |
| Adiabatic/evaporative | Support | Support | Support | Support | Medium | Low-Med |
| Dry coolers | Support | Support | Support | Support | None | Med |
| Cooling towers | Support | Support | Support | Support | High | Low |
| Free cooling/economizer | Support | Support | Support | Support | None-Low | Low |
| Geothermal | Support | Support | Support | Support | None | High |
| Absorption cooling | Support | Support | Support | Support | Medium | High |
| Heat reuse | Support | Support | Support | Support | None | Med-High |

**"Primary"** = recommended at this density. **"Support"** = heat rejection or supplemental.
**"Viable"** = works but not optimal. **"Limited"** = only with containment/optimization.

### Reference Data

Load these files on demand -- do not read upfront:

- [GPU specifications](../../references/GPU-REFERENCE.md) -- Section: "Cooling Requirements by GPU" for per-accelerator thermal matrix and mandatory liquid cooling thresholds
- [Cooling technologies](references/cooling-technologies.md) -- All 14 technologies with specifications, pros/cons, and best-for scenarios

## Analysis & Output

### Process

1. **Determine cooling load** from IT load and target PUE: cooling_kW = IT_load_kW * (PUE_cooling_contribution)
2. **Screen technologies** against density tier, climate, and water constraints using ranking framework above
3. **Rank viable options** by PUE contribution, WUE, capital cost, and operational complexity
4. **Select primary and backup** cooling technologies
5. **Size the cooling plant** with redundancy per facility type parameters
6. **Calculate PUE/WUE** using `scripts/cooling-calculator.py`
7. **Estimate free cooling hours** based on climate zone and economizer type
8. **Project water budget** (annual gallons/liters) for water-using technologies
9. **Estimate capital cost ranges** using COST-BENCHMARKS.md regional data

### Validation Loop

1. Compute initial cooling load from IT load and PUE target
2. Cross-check per-rack heat rejection against GPU-REFERENCE.md TDP data
3. Validate cooling technology is viable for the climate zone (ASHRAE TC 9.9: A1 class 15-32C recommended inlet)
4. Verify WUE is consistent with selected technology (DLC has near-zero WUE; cooling towers 1.8-2.5 L/kWh)
5. Check total cooling capacity exceeds peak IT load by at least 20% margin
6. Validate that mandatory liquid cooling thresholds are met (GB200 NVL72 at 120kW/rack requires liquid, max 25C inlet)
7. If any constraint violated: flag error, adjust technology selection, recompute from step 1
8. Repeat until all constraints satisfied

## Output

This skill produces two files:
1. `<project-name>-cooling-design-report.md` -- Full report
2. `<project-name>-cooling-design-report.json` -- Structured data for downstream skills

### Cooling Design Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-cooling-design v1.0]

#### 1. Executive Summary
- Facility type and IT load: [type], [X-Y MW]
- Primary cooling technology: [technology]
- Backup/heat rejection: [technology]
- PUE (cooling contribution): [X.XX - X.XX]
- WUE: [X.X - X.X L/kWh]
- Annual water usage: [X-Y million gallons/year] or zero for waterless

#### 2. Climate Analysis
- Location: [city/region]
- ASHRAE climate zone: [zone]
- Design day dry-bulb temperature: [X C]
- Design day wet-bulb temperature: [X C]
- Free cooling hours per year: [X-Y hours] (dry-bulb economizer) / [X-Y hours] (wet-bulb)

#### 3. Technology Ranking Matrix
| Rank | Technology | PUE Contribution | WUE | CapEx ($/kW) | Feasible | Notes |
|------|-----------|------------------|-----|--------------|----------|-------|
| 1 | [tech] | [range] | [range] | [range] | Yes/No | [constraints] |

#### 4. Recommended System Design
- Primary cooling: [technology with sizing]
- Heat rejection: [technology with sizing]
- Redundancy: [N/N+1/2N] configuration
- Design capacity: [X kW] cooling for [Y kW] IT load

#### 5. PUE/WUE Projections
- PUE (cooling contribution): [X.XX - X.XX] (methodology: component-level)
- WUE: [X.X - X.X L/kWh]
- Sensitivity: [impact of ambient temperature +/-5C on PUE]

#### 6. Water Budget
- Annual consumption: [X-Y million gallons/year]
- Peak daily consumption: [X gallons/day]
- Source: [municipal / reclaimed / none]

#### 7. Phased Implementation
| Phase | Cooling Capacity (kW) | Technology | Timeline | Cost Estimate |
|-------|----------------------|------------|----------|---------------|
| Phase 1 | [X-Y] | [tech] | [date] | [$X-YM] |

### JSON Sidecar

```json
{
  "artifact_type": "cooling-design-report",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "primary_technology": "direct-liquid-cooling",
  "backup_technology": "dry-coolers",
  "total_cooling_capacity_kw": 15000,
  "pue_contribution": 0.15,
  "pue_contribution_range_low": 0.12,
  "pue_contribution_range_high": 0.20,
  "wue_liters_per_kwh": 0.1,
  "wue_range_low": 0.0,
  "wue_range_high": 0.3,
  "annual_water_liters": 500000,
  "free_cooling_hours": 4500,
  "climate_zone": "temperate",
  "ashrae_class": "A1",
  "cost_estimate_per_kw_low": 800,
  "cost_estimate_per_kw_high": 1200
}
```

## Gotchas

- PUE < 1.1 requires liquid cooling; air-only claims of sub-1.1 PUE are physically implausible.
- GB200 NVL72 racks at 120kW MANDATE liquid cooling with max 25C inlet temperature -- no air-cooled option exists at this density.
- Free cooling hours vary 2x between sites at the same latitude due to humidity (dry bulb vs wet bulb economizer). Always specify economizer type.
- Cooling tower water consumption at 1 MW IT load is roughly 7-10 million gallons/year -- a material concern in water-scarce regions like Phoenix, Las Vegas, or the Middle East.
- ASHRAE A1 envelope (15-32C recommended inlet) covers 95%+ of applications; going to A3/A4 saves capital but voids most GPU vendor warranties.

## Calculation Scripts

For deterministic calculations, use bundled scripts:

- `scripts/cooling-calculator.py` -- Cooling load sizing, PUE/WUE estimation, free cooling hours, and water budget calculation

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios.
