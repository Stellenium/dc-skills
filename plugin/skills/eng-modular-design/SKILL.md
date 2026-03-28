---
name: eng-modular-design
description: "Design modular and prefab data center facilities including pod sizing, factory vs field construction analysis, and transport logistics. Use when evaluating modular DC solutions, designing prefab data centers, comparing modular vs stick-built approaches, or planning containerized or pod-based deployments. Trigger with \"modular data center\", \"prefab DC\", \"containerized data center\", \"pod design\", \"factory-built\", or \"modular vs stick-built\"."
---

# Modular Data Center Design

Design modular and prefab data center facilities with pod sizing, factory vs field
analysis, transport logistics, and phased rollout planning. Produces a complete
modular design report with module specifications, deployment sequence, and cost
comparison against traditional stick-built construction.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Per-module power allocation (kW per module)
- Total facility power budget (MW)
- Redundancy scheme (N, N+1, 2N) and its impact on module utility connections
- Phased deployment schedule if multi-phase

If upstream data is not available, I will ask you for total power requirements
and redundancy level, or use industry-standard defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield standalone or brownfield expansion?
   - **Greenfield:** New modular facility from bare site
   - **Brownfield:** Adding modular capacity to existing facility

2. What facility type?
   - Hyperscale (fleet deployment, standardized pods, 20-500MW+)
   - Colocation (multi-tenant module isolation, 1-50MW)
   - Edge (micro-modular, 50kW-5MW per location)
   - Sovereign (hardened enclosures, enhanced security)
   - Enterprise (single-tenant, 2-20MW)

3. What is the total target capacity (MW)?
   - Specify per-phase if phased deployment

4. What phase size (MW per phase)?
   - How much capacity to deploy per deployment wave
   - Typical: 1-5MW per module, 5-20MW per phase

5. What is the preferred module type?
   - Containerized (ISO shipping container form factor, 20ft or 40ft)
   - Pod-based (custom-sized modular pods, 40-60ft)
   - Purpose-built modular (factory-assembled building sections)
   - No preference (recommend based on requirements)

6. What are the site constraints?
   - Access road width and weight limits
   - Crane availability and height restrictions
   - Utility connection points (number and location)
   - Available staging area for module placement

7. What is the deployment timeline urgency?
   - Critical: first module operational within 6 months
   - Standard: 9-18 months to first module
   - Long-range: phased deployment over 2-5 years

8. What is the operating environment?
   - Climate zone (ASHRAE classification)
   - Altitude (affects air density and cooling capacity)
   - Seismic zone (affects structural requirements)
   - Extreme conditions (flood plain, hurricane zone, extreme cold/heat)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Module Type Refinements

**Containerized path:**
1. Standard 20ft or 40ft ISO container?
2. Single-walled or double-walled (insulated) enclosure?
3. Pre-integrated power and cooling, or external utilities?
4. Stacked deployment (2-high) or single level?

**Pod-based path:**
1. Target dimensions (width x length x height)?
2. Internal row count and rack capacity per pod?
3. Cooling integration level (self-contained vs central plant connection)?
4. Pod-to-pod interconnect requirements (fiber, power bus)?

**Purpose-built modular path:**
1. Building section dimensions and transport constraints?
2. On-site assembly requirements (crane, welding, concrete)?
3. MEP integration level (factory-completed vs field-finished)?
4. Architectural requirements (exterior finish, code compliance)?

### Facility Type Parameters

| Parameter | Hyperscale | Colo | Edge | Sovereign | Enterprise |
|-----------|------------|------|------|-----------|------------|
| Module size (MW) | 1-5 | 0.5-2 | 0.05-0.5 | 0.5-2 | 0.5-3 |
| Standardization | Fleet-identical | Configurable | Fixed catalog | Custom-hardened | Semi-custom |
| Cooling | Central plant | Per-module | Self-contained | Per-module | Central/hybrid |
| Deployment rate | 1-4 per month | 1-2 per quarter | 5-20 per month | 1 per quarter | 1-2 per year |
| Typical lead time | 16-24 weeks | 12-20 weeks | 8-16 weeks | 20-32 weeks | 16-24 weeks |

## Analysis & Output

### Process

1. **Module sizing:** Determine IT load per unit, power and cooling per unit, dimensions, weight, and rack count based on capacity targets and module type
2. **Factory vs field analysis:** Compare lead time, cost, quality control, and customization trade-offs between factory assembly and site-built construction
3. **Transport logistics:** Assess road weight limits (80,000 lbs US highway standard), dimensional limits (12ft width for permit-free, 14ft with oversize permit), crane requirements, and site staging area
4. **Phased rollout plan:** Design deployment sequence, utility connection phasing, commissioning per phase, and ramp schedule
5. **Cost comparison:** Calculate modular vs traditional $/MW with timeline advantage quantified as financial benefit (earlier revenue, reduced interest carry)

### Reference Data

Load these files on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Section matching region for modular vs stick-built cost comparison

### Quality Check

1. Verify module dimensions fit transport constraints (width, height, weight)
2. Confirm power per module does not exceed cooling capacity of selected cooling approach
3. Cross-check cost estimates against COST-BENCHMARKS.md regional data
4. Validate that phased deployment sequence accounts for utility connection lead times
5. Ensure structural design accounts for seismic zone and climate requirements

## Output

This skill produces two files:
1. `<project-name>-modular-design-report.md` -- Full report
2. `<project-name>-modular-design-report.json` -- Structured data for downstream skills

### Modular Design Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-modular-design v1.0]

#### 1. Executive Summary
- Module type: [containerized / pod / purpose-built]
- Total capacity: [MW] in [N] modules across [N] phases
- Factory lead time: [weeks]
- First module operational: [date]
- Cost comparison: [$/MW modular vs $/MW traditional]

#### 2. Module Specifications
| Specification | Value |
|---------------|-------|
| Dimensions (W x L x H) | [ft x ft x ft] |
| Weight (loaded) | [lbs] |
| IT capacity | [kW] |
| Rack count | [N] |
| Cooling capacity | [kW] |
| Cooling type | [air/liquid/hybrid] |
| Power feed | [voltage/amperage] |
| Redundancy | [N/N+1] per module |

#### 3. Factory vs Field Analysis
| Factor | Factory | Field | Advantage |
|--------|---------|-------|-----------|
| Lead time | [weeks] | [weeks] | [winner] |
| Cost per MW | [$] | [$] | [winner] |
| Quality control | [rating] | [rating] | [winner] |
| Customization | [rating] | [rating] | [winner] |
| Weather dependency | [rating] | [rating] | [winner] |

#### 4. Transport Logistics
- Transport method: [flatbed / lowboy / specialized]
- Route constraints: [width, height, weight limits]
- Permit requirements: [standard / oversize / super-load]
- Crane requirements: [type, capacity, duration]
- Staging area: [dimensions needed]

#### 5. Phased Rollout Plan
| Phase | Modules | IT Capacity (MW) | Utility Connection | Ship Date | Operational |
|-------|---------|-------------------|--------------------|-----------|-------------|
| 1 | [N] | [MW] | [description] | [date] | [date] |
| 2 | [N] | [MW] | [description] | [date] | [date] |

#### 6. Cost Summary
| Category | Modular | Traditional | Delta |
|----------|---------|-------------|-------|
| Construction $/MW | [$] | [$] | [%] |
| Time to revenue | [months] | [months] | [months] |
| Carrying cost savings | [$] | -- | [$] |
| Total lifecycle $/MW | [$] | [$] | [%] |

### JSON Sidecar

```json
{
  "artifact_type": "modular-design-report",
  "skill_version": "1.0",
  "project_name": "...",
  "module_type": "containerized | pod | purpose-built",
  "total_capacity_mw": 0,
  "module_count": 0,
  "module_specs": {
    "dimensions_ft": {"width": 0, "length": 0, "height": 0},
    "weight_lbs": 0,
    "it_capacity_kw": 0,
    "rack_count": 0,
    "cooling_type": "air | liquid | hybrid",
    "cooling_capacity_kw": 0
  },
  "phases": [
    {"phase": 1, "modules": 0, "capacity_mw": 0, "operational_date": "..."}
  ],
  "cost_comparison": {
    "modular_per_mw": 0,
    "traditional_per_mw": 0,
    "time_to_revenue_months": 0,
    "carrying_cost_savings": 0
  },
  "factory_lead_time_weeks": 0
}
```

## Gotchas

- **Standard shipping container (40ft) limits IT load to 200-250kW with air cooling -- liquid cooling can push to 500kW+ but requires external CDU infrastructure.** The container form factor constrains internal airflow and heat rejection. Exceeding these limits without external cooling support causes thermal throttling or shutdown.

- **Road transport in most US states limits module width to 14ft without oversize permits -- design modules at 12ft width for permit-free delivery.** Oversize permits add $5-15K per move, require escort vehicles, restrict travel to daylight hours, and may prohibit certain routes. A fleet deployment of 50+ modules at 14ft width adds $250K-750K in permitting alone.

- **Factory lead times for custom modular pods are 16-24 weeks, not the 4-6 weeks sales teams quote -- always verify with production schedule.** The 4-6 week number typically represents assembly time only. Add engineering/design (4-8 weeks), procurement (6-12 weeks), and testing (1-2 weeks). Standard catalog products can ship faster; custom designs cannot.

- **Module-to-module fiber interconnect is the most common failure point in modular deployments.** External cable runs between modules are exposed to weather, rodents, and maintenance traffic. Use armored fiber in buried conduit between modules, not aerial runs or surface-mounted trays.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale fleet, edge micro-modular, and brownfield expansion.
