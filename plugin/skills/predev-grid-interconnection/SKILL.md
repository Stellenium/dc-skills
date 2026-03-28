---
name: predev-grid-interconnection
description: "Assess utility grid interconnection for data center development including queue position, application process, timeline, and cost modeling. Use when connecting a DC to the grid, evaluating utility power availability, navigating interconnection queues, or estimating grid connection costs and timelines. Trigger with \"grid interconnection\", \"utility connection\", \"power interconnection\", \"grid queue\", or \"utility power for data center\"."
argument-hint: "<utility-territory or site>"
---

# Grid Interconnection Assessment

Assess utility grid interconnection for data center development. Produces a queue
position assessment, interconnection timeline, cost allocation analysis, and
alternative strategies for constrained markets. Navigates ISO/RTO-specific
interconnection processes from application through energization.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location (state, county, utility territory)
- Power availability assessment and utility capacity at site boundary
- Nearest substation identification and available capacity
- Grid interconnection status flags from site scoring

If upstream data is not available, I will ask you for location, target capacity,
and utility territory, or use publicly available ISO queue data.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. What is the target utility / ISO / RTO?
   - PJM (Mid-Atlantic, Ohio Valley)
   - ERCOT (Texas)
   - CAISO (California)
   - MISO (Midwest, South)
   - SPP (Central plains)
   - ISO-NE (New England)
   - NYISO (New York)
   - Non-ISO utility (vertically integrated)
   - International (specify country and grid operator)

2. What is the requested interconnection capacity (MW)?
   - Under 10MW (distribution-level, may avoid transmission queue)
   - 10-50MW (transmission or large distribution)
   - 50-200MW (transmission-level study required)
   - 200MW+ (multi-phase energization likely required)

3. What is the site location?
   - Specific address or substation name if known
   - State/county at minimum
   - Proximity to existing high-voltage infrastructure

4. What existing electrical infrastructure is at the site?
   - None (greenfield, no service)
   - Distribution service only (below 69kV)
   - Transmission-adjacent (near 69kV+ lines)
   - Adjacent to or on substation property

5. What is the preferred interconnection voltage?
   - 13.8kV (distribution)
   - 34.5kV (sub-transmission)
   - 69kV (transmission)
   - 115kV / 138kV (high voltage transmission)
   - 230kV+ (extra high voltage)
   - No preference (recommend based on capacity)

6. What is the timeline urgency?
   - Critical: need power within 12 months
   - Standard: 18-36 month horizon
   - Long-range: 36-60 month planning window
   - Phased: initial capacity fast, full capacity over time

7. Are you willing to fund network upgrades?
   - Participant-funded (willing to pay for dedicated upgrades)
   - Shared funding (prefer cost allocation across benefiting parties)
   - Minimal investment (seeking locations with existing capacity)

8. Are you aware of your queue position or application status?
   - Not yet applied
   - Application submitted, awaiting feasibility study
   - Feasibility study complete, in system impact study
   - Facilities study complete, negotiating interconnection agreement
   - Interconnection agreement signed, awaiting construction

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### ISO/RTO-Specific Path

**ERCOT path** (if Phase 1 Q1 = ERCOT):
1. Are you applying under standard generation interconnection or load interconnection?
2. Is the site in a Competitive Renewable Energy Zone (CREZ) with existing transmission?
3. What is the nearest ERCOT point of interconnection (POI)?
4. Are you considering co-location with existing generation assets?

**PJM path** (if Phase 1 Q1 = PJM):
1. Which PJM transmission zone? (e.g., Dominion, PECO, APS, ComEd)
2. Are you aware of the current FERC Order 2023 cluster study window?
3. Has a pre-application study been completed?
4. Is the site in an area with known transmission congestion?

**CAISO path** (if Phase 1 Q1 = CAISO):
1. Which utility service territory? (PG&E, SCE, SDG&E)
2. Are you applying under the cluster study process or independent study?
3. Is behind-the-meter generation planned to reduce interconnection capacity?

### Capacity-Based Refinements

**Under 10MW:**
- Can the load be served from existing distribution without substation upgrade?
- Does the local utility offer expedited commercial service for loads under a threshold?
- Is behind-the-meter generation an option to reduce grid draw below queue thresholds?

**200MW+:**
- How many phases for energization? (MW per phase, timeline per phase)
- Is a dedicated substation or switching station required?
- Are multiple points of interconnection being considered for redundancy?

## Analysis & Output

### Process

1. **Queue position assessment:** Query current ISO queue depth for the target area, calculate average wait time by ISO, identify withdrawal rates and realistic completion timeline
2. **Application process mapping:** Map the specific ISO/RTO interconnection process -- feasibility study, system impact study, facilities study, interconnection agreement
3. **Cost allocation analysis:** Model participant-funded vs shared network upgrade costs per FERC Order 2023 cost allocation reforms, estimate upgrade costs based on capacity and location
4. **Timeline estimation:** Build realistic timeline from application to energization (18-60 months depending on ISO, capacity, and queue position)
5. **Alternative strategy identification:** Evaluate bypass strategies -- behind-the-meter generation, co-location with existing substations, phased energization, capacity contracts with existing generators, battery-bridge strategies
6. **Risk assessment:** Identify cluster study risks, cost escalation factors, regulatory change exposure

### Reference Data

Load these files on demand -- do not read upfront:

- [Industrial power tariffs](../../references/POWER-TARIFFS.md) -- Section matching target region for grid tariff comparison and cost context

### Quality Check

1. Verify ISO/RTO process matches the specific grid operator (not generic)
2. Confirm cost estimates use current FERC Order 2023 methodology where applicable
3. Cross-check queue depth data against publicly available ISO queue reports
4. Validate that alternative strategies are feasible for the specific location and capacity
5. Ensure timeline accounts for all study phases plus construction

## Output

This skill produces two files:
1. `<project-name>-grid-interconnection-assessment.md` -- Full report
2. `<project-name>-grid-interconnection-assessment.json` -- Structured data for downstream skills

### Grid Interconnection Assessment Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: predev-grid-interconnection v1.0]

#### 1. Executive Summary
- **Target capacity:** [MW]
- **ISO/RTO:** [name]
- **Estimated timeline to energization:** [months range]
- **Estimated interconnection cost:** [$X-Y M range]
- **Recommended strategy:** [direct queue / alternative / phased]

#### 2. Queue Analysis
- Current queue depth: [GW pending in target ISO]
- Historical withdrawal rate: [%]
- Average time from application to energization: [months]
- Position assessment: [favorable / moderate / congested]

#### 3. Application Roadmap
| Phase | Description | Duration | Cost | Status |
|-------|-------------|----------|------|--------|
| Pre-application | Screening study, site control | 1-3 months | $5-25K | [status] |
| Feasibility study | Initial grid impact assessment | 3-6 months | $50-100K | [status] |
| System impact study | Detailed network modeling | 6-12 months | $100-250K | [status] |
| Facilities study | Engineering design for upgrades | 6-12 months | $100-500K | [status] |
| IA negotiation | Interconnection agreement terms | 3-6 months | Legal costs | [status] |
| Construction | Network upgrades and interconnection | 12-36 months | [project-specific] | [status] |

#### 4. Cost Allocation Estimate
- Network upgrade costs: [$X-Y M]
- Allocation method: [participant-funded / shared / hybrid]
- FERC Order 2023 applicability: [yes/no, impact]
- Cost risk factors: [escalation scenarios]

#### 5. Timeline
- Best case: [months] (no upgrades required, favorable queue)
- Expected case: [months] (standard study process, moderate upgrades)
- Worst case: [months] (major upgrades, cluster delays, restudy)

#### 6. Alternative Strategies

| Strategy | Feasibility | Timeline Impact | Cost Impact | Risk |
|----------|-------------|-----------------|-------------|------|
| Behind-the-meter generation | [H/M/L] | [months saved] | [$impact] | [description] |
| Substation co-location | [H/M/L] | [months saved] | [$impact] | [description] |
| Phased energization | [H/M/L] | [months saved] | [$impact] | [description] |
| Capacity contract | [H/M/L] | [months saved] | [$impact] | [description] |
| Battery bridge | [H/M/L] | [months saved] | [$impact] | [description] |

#### 7. Risk Factors
- Cluster study delay risk: [assessment]
- Cost escalation risk: [assessment]
- Regulatory change risk: [assessment]
- Queue withdrawal risk: [assessment]

### JSON Sidecar

```json
{
  "artifact_type": "grid-interconnection-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "target_capacity_mw": 0,
  "iso_rto": "...",
  "estimated_timeline_months": {"best": 0, "expected": 0, "worst": 0},
  "estimated_cost": {"low": 0, "high": 0, "currency": "USD"},
  "queue_depth_gw": 0,
  "queue_position": "favorable | moderate | congested",
  "recommended_strategy": "direct-queue | alternative | phased",
  "alternative_strategies": [
    {"name": "...", "feasibility": "high | medium | low", "timeline_impact_months": 0}
  ],
  "application_status": "not-applied | feasibility | impact | facilities | ia-negotiation | construction",
  "ferc_order_2023_applicable": true
}
```

## Gotchas

- **ERCOT queue has 300+ GW pending as of 2025 -- average withdrawal rate is 80%, but surviving projects still face 3-5 year timelines.** Do not assume ERCOT's deregulated market means faster interconnection. The sheer volume of applications, particularly solar and storage, has created multi-year backlogs even for load interconnection.

- **FERC Order 2023 cluster study process means your timeline depends on every other project in your cluster -- a single lagging project can delay the entire cohort.** This is fundamentally different from the serial first-come-first-served process. Plan for cluster-driven delays of 6-18 months beyond individual study timelines.

- **Behind-the-meter generation under 10MW often avoids the interconnection queue entirely -- check ISO threshold rules.** Each ISO has different thresholds: ERCOT exempts loads under 10MW from full interconnection study, PJM has expedited processes for small loads. This is the single most effective bypass strategy for smaller facilities.

- **Network upgrade cost estimates in feasibility studies routinely double by the facilities study -- budget 2x the initial estimate.** Feasibility studies use planning-level estimates; facilities studies use engineering-level design. The gap between these consistently surprises developers. A $5M feasibility estimate becoming $10-15M in facilities study is normal, not exceptional.

## Evaluations

See `evals/evals.json` for test scenarios covering PJM deep queue, ERCOT fast-track, and behind-the-meter bypass.
