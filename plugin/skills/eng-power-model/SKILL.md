---
name: eng-power-model
description: "Model data center power capacity from utility feed to rack-level distribution with Tier I-IV redundancy and PUE calculations. Use when designing electrical distribution for a DC, sizing power infrastructure, calculating PUE, modeling N+1/2N redundancy configurations, or evaluating power capacity for new or expanded facilities. Trigger with \"power model\", \"electrical design\", \"PUE calculation\", \"power capacity\", \"redundancy design\", \"DC power distribution\", or \"how much power do I need?\"."
argument-hint: "<IT-load-MW>"
---

# Power Capacity Model

Model data center power capacity from utility feed to rack-level distribution.
Produces a complete power chain analysis with redundancy modeling, PUE calculation,
and phased capacity planning. Consumes the upstream site feasibility report.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Available utility capacity (MW) at the site boundary
- Grid interconnection status (signed, pending, not started)
- Number and diversity of utility feeds
- Climate zone (affects cooling load, which impacts total facility power)
- Site constraint flags (seismic, flood, environmental)

If upstream data is not available, I will ask you for these values or use
industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction from bare site -- proceed to Greenfield Path below
   - **Brownfield:** Conversion of existing building or facility upgrade -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the total planned IT load (MW)?
   - Specify per phase if multi-phase deployment

4. What redundancy tier is required?
   - Tier I (basic, no redundancy)
   - Tier II (redundant components, N+1)
   - Tier III (concurrently maintainable, N+1 minimum)
   - Tier IV (fault tolerant, 2N or 2N+1)

5. What is the utility voltage and service configuration?
   - Single utility feed
   - Dual utility feed (diverse paths)
   - Specify voltage if known (e.g., 13.8kV, 34.5kV)

6. Is behind-the-meter generation planned?
   - Grid-only
   - Solar/wind + grid
   - Gas turbine + grid
   - Full microgrid capability

7. What is the target PUE?
   - < 1.2 (aggressive, likely requires liquid cooling)
   - 1.2 - 1.4 (standard modern facility)
   - 1.4 - 1.6 (traditional air-cooled)
   - No target specified

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. Has the utility interconnection agreement been signed?
2. What is the available utility capacity at the site boundary?
3. Are there any utility feed routing constraints (easements, rights-of-way)?
4. What is the planned build-out timeline (phases and target dates)?

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. What is the existing electrical infrastructure?
   - Utility service entrance capacity (voltage/amperage)
   - Existing switchgear and distribution
   - UPS systems (make, model, capacity, age)
   - Generator systems (fuel type, capacity, runtime)
2. What is the current IT load vs. available capacity?
3. Are there known electrical code compliance gaps?
4. What is the maximum allowable downtime for electrical upgrades?

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Scale range (MW) | 2-20 | 20-500+ | 5-50 | 1-50 | 0.5-10 | 0.1-5 |
| Default redundancy | Tier III | Tier III | Tier IV | Tier III | Tier II | Tier I-II |
| UPS topology | Double-conversion | Modular/scalable | Double-conversion 2N | Double-conversion | Integrated | Line-interactive |
| Generator config | N+1 diesel | N+1 diesel/gas | 2N diesel | N+1 diesel | Packaged | Optional |
| Typical PUE range | 1.3-1.5 | 1.1-1.3 | 1.3-1.5 | 1.4-1.6 | 1.2-1.4 | 1.4-1.8 |

### Facility Type Refinements

**Hyperscale additions:**
- Campus-level power distribution strategy?
- Standardized power module size (e.g., 4MW blocks)?
- Custom vs. vendor-standard UPS platforms?

**Sovereign additions:**
- Dual utility feed from separate substations required?
- On-site fuel storage requirements (days of autonomy)?
- SCIF or classified space power isolation requirements?

**Edge additions:**
- Single-phase or three-phase utility service?
- Containerized/pre-integrated power solution preferred?
- Remote monitoring requirements (unmanned site)?

## Analysis & Output

### Process

1. **Map the power chain:** Utility service entrance -> ATS/STS -> main switchgear -> UPS input -> UPS -> PDU/RPP -> rack-level distribution
2. **Size each component** based on IT load, redundancy tier, and growth plan
3. **Calculate losses** at each conversion stage (transformer: 1-2%, UPS: 3-8%, PDU: 2-3%)
4. **Compute PUE** from component-level efficiency data using `scripts/pue-calculator.py`
5. **Model redundancy** scenarios (N, N+1, 2N, 2N+1) using `scripts/redundancy-model.py`
6. **Phase the build-out** if multi-phase deployment
7. **Estimate capital cost ranges** using COST-BENCHMARKS.md regional data

### Reference Data

Load these files on demand -- do not read upfront:

- [GPU specifications](../../references/GPU-REFERENCE.md) -- Section: "Cooling Requirements by GPU" for per-rack power sizing by accelerator type
- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Section: "North America Construction Costs" for regional $/MW capital estimates

### Validation Loop

1. Compute initial power model from Phase 1 and Phase 2 inputs
2. Cross-check per-rack power against GPU-REFERENCE.md TDP data
3. Validate PUE is physically possible (PUE < 1.0 is impossible; PUE < 1.1 requires liquid cooling)
4. Verify total load does not exceed utility feed capacity (including redundancy overhead)
5. Check that redundancy tier matches component configuration (e.g., Tier III requires N+1 minimum, not just N)
6. Verify generator sizing includes motor starting current for cooling systems (+15-20% over running load)
7. If any constraint violated: flag the error, adjust assumptions, recompute from step 1
8. Repeat until all constraints satisfied

## Output

This skill produces two files:
1. `<project-name>-power-capacity-model.md` -- Full report
2. `<project-name>-power-capacity-model.json` -- Structured data for downstream skills

### Power Capacity Model Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-power-model v1.0]

#### 1. Executive Summary
- Facility type: [type]
- Total IT load: [X-Y MW] (range reflecting design uncertainty)
- Total facility load: [X-Y MW]
- PUE: [X.XX - X.XX] (range with methodology)
- Redundancy: [Tier] / [N configuration]
- Estimated CapEx: [$X-Y M/MW] (from COST-BENCHMARKS.md regional data)

#### 2. Utility Service
- Utility feed: [voltage] / [amperage]
- Service configuration: [single/dual feed]
- Contracted capacity: [MW]
- Redundancy: [N / N+1 / 2N / 2N+1]

#### 3. Power Chain
| Stage | Equipment | Capacity | Redundancy | Efficiency | Loss (kW) |
|-------|-----------|----------|------------|------------|-----------|
| Utility entrance | [Transformer] | [MVA] | [config] | [97-99%] | [X] |
| Transfer switch | [ATS/STS] | [A] | [config] | [99.5%+] | [X] |
| Main switchgear | [Type] | [A] | [config] | [99.5%+] | [X] |
| UPS | [Type] | [kVA] | [config] | [92-97%] | [X] |
| PDU/RPP | [Type] | [kVA] | [config] | [97-98%] | [X] |

#### 4. Capacity Summary
- Total IT load: [MW] (with +/- uncertainty margin)
- Total facility load: [MW]
- PUE: [calculated range]
- Available capacity margin: [%]

#### 5. Phased Build-out
| Phase | IT Load (MW) | Facility Load (MW) | Timeline | Capital Estimate |
|-------|-------------|-------------------|----------|-----------------|
| Phase 1 | [X-Y] | [X-Y] | [date] | [$X-YM] |
| Phase 2 | [X-Y] | [X-Y] | [date] | [$X-YM] |

#### 6. Redundancy Analysis
- Configuration: [N / N+1 / 2N / 2N+1]
- Single point of failure: [identified / none]
- Concurrent maintainability: [yes / no]
- Fault tolerance: [yes / no]
- Sensitivity: [impact of losing one UPS module / one generator on available capacity]

#### 7. Sensitivity Analysis
| Variable | Base Case | Low Case | High Case | Impact on PUE |
|----------|-----------|----------|-----------|---------------|
| IT load utilization | [%] | [%] | [%] | [range] |
| UPS efficiency | [%] | [%] | [%] | [range] |
| Cooling overhead | [%] | [%] | [%] | [range] |

### JSON Sidecar

```json
{
  "artifact_type": "power-capacity-model",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "total_it_load_kw": 10000,
  "total_facility_load_kw": 13500,
  "pue": 1.35,
  "pue_range_low": 1.30,
  "pue_range_high": 1.40,
  "redundancy_tier": "III",
  "redundancy_config": "N+1",
  "utility_feed": {
    "voltage_kv": 13.8,
    "configuration": "dual",
    "contracted_capacity_mw": 15
  },
  "power_chain": [
    {"stage": "transformer", "capacity_mva": 20, "efficiency_pct": 98.5},
    {"stage": "ups", "capacity_kva": 12000, "efficiency_pct": 96},
    {"stage": "pdu", "capacity_kva": 11000, "efficiency_pct": 97.5}
  ],
  "phases": [
    {"phase": 1, "it_load_kw": 5000, "facility_load_kw": 6750, "timeline": "2025-Q4"},
    {"phase": 2, "it_load_kw": 10000, "facility_load_kw": 13500, "timeline": "2027-Q2"}
  ]
}
```

## Gotchas

- Tier III does NOT mean 2N redundancy -- it means Concurrently Maintainable (N+1 minimum). Tier IV is fault tolerant (2N or 2N+1).
- PUE below 1.1 requires liquid cooling; claiming sub-1.1 PUE with air cooling only is a red flag in any feasibility study.
- Utility feed sizing must account for ALL planned phases even if only Phase 1 is being built -- utility upgrades have 2-5 year lead times.
- UPS efficiency varies dramatically with load percentage: a 2N UPS system at 25% load per unit has significantly worse efficiency than N+1 at 60% load per unit. Always model efficiency at expected operating point, not rated capacity.
- Generator sizing must include motor starting current for cooling systems -- a common oversight that causes undersizing by 15-20%.

## Calculation Scripts

For deterministic calculations, use bundled scripts:

- `scripts/pue-calculator.py` -- PUE calculation with component-level losses and uncertainty ranges
- `scripts/redundancy-model.py` -- Redundancy analysis for N through 2N+1 configurations with module sizing

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios.
