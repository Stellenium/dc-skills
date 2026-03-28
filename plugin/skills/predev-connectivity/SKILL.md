---
name: predev-connectivity
description: "Assess data center connectivity requirements including carrier strategy, fiber entrance design, meet-me room planning, and IX peering. Use when planning network infrastructure for a DC, evaluating fiber availability at a site, designing carrier-neutral connectivity, or assessing IX peering options. Trigger with \"DC connectivity\", \"fiber assessment\", \"meet-me room\", \"carrier strategy\", \"network design for data center\", or \"IX peering\"."
---

# Data Center Connectivity Assessment

Evaluate data center connectivity infrastructure including fiber access, carrier
diversity, meet-me room design, Internet exchange peering strategy, and subsea
cable assessment. This is an independent entry-point skill -- no upstream artifacts
are required. Produces a connectivity assessment for project planning.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction requiring new fiber entrance -- proceed to Greenfield Path below
   - **Brownfield:** Existing facility with some network infrastructure -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the site location?
   - Country, city, specific address or area
   - Urban, suburban, or rural setting

4. What are the target latency requirements?
   - Ultra-low latency (<1ms to major peering point)
   - Low latency (1-5ms to regional hub)
   - Standard latency (5-20ms acceptable)
   - Latency not critical (batch/storage workloads)

5. What is the expected aggregate bandwidth requirement?
   - Initial bandwidth (Gbps) at facility opening
   - 5-year projected bandwidth (Gbps)

6. What carrier diversity level is required?
   - Minimum 2 diverse carriers (standard enterprise)
   - Minimum 3 diverse carriers (colocation/wholesale)
   - 4+ carriers with fully diverse physical paths (hyperscale/mission-critical)

7. Is Internet exchange (IX) peering a requirement?
   - Direct IX peering (facility must host IX node or be within 1ms of IX)
   - Remote peering acceptable (connected via carrier to nearest IX)
   - IX peering not required (private connectivity only)

8. Is subsea cable proximity relevant?
   - Yes -- coastal or island site, international traffic critical
   - No -- terrestrial connectivity sufficient

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. What is the distance to the nearest lit fiber building or carrier PoP?
2. Are there existing conduit routes (utility, road, rail) between the site and fiber infrastructure?
3. Has the local municipality or utility mapped available dark fiber?
4. What is the right-of-way situation for new fiber construction to the site?

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. What existing fiber infrastructure serves the building?
   - Number of fiber entrance points
   - Carriers currently on-net
   - Fiber type (single-mode, multi-mode) and strand count
2. Is there an existing meet-me room or demarcation area?
3. What is the current bandwidth capacity and utilization?
4. Are there conduit paths available for additional fiber entrance construction?

### Facility Type Refinements

**Colocation additions:**
- Carrier-neutral or carrier-specific strategy?
- Target number of on-net carriers at facility opening?
- Cross-connect pricing model (monthly recurring, NRC, or bundled)?
- Will you operate a carrier hotel / meet-me room as a revenue center?

**Hyperscale additions:**
- Private dark fiber or lit service procurement strategy?
- Long-haul fiber route diversity for inter-region connectivity?
- Dedicated fiber pairs to cloud on-ramp or peering edge?
- Willingness to fund fiber construction to site?

**Sovereign additions:**
- Encrypted transport requirements (NSA Type 1, FIPS 140-3)?
- Physically isolated network infrastructure required?
- Domestic-only routing requirements (no international transit)?
- TEMPEST or emanations security for fiber entrance?

## What I Need from Upstream

This skill is an independent entry point -- no upstream artifacts are required.

**Optional:** If a site-feasibility-report is available (from predev-site-feasibility),
the connectivity assessment will use location data and connectivity factor scoring
to enrich the analysis. Otherwise, location context is gathered directly from the user.

## Analysis & Output

### Process

1. **Fiber Audit:** Identify lit buildings, carrier PoPs, and dark fiber routes within 1, 5, and 10 miles of the site. Map existing conduit infrastructure (utility, municipal, railroad) for potential fiber routes.
2. **Carrier Diversity Assessment:** Evaluate the number and quality of available carriers. Map physical path diversity (separate conduit routes, distinct utility corridors) to confirm true diversity vs. shared-path "diversity."
3. **Fiber Entrance Design:** Recommend entrance architecture -- number of entrance points, physical separation requirements, conduit sizing, fiber strand count, and vault/manhole placement.
4. **Meet-Me Room Planning:** Design the carrier interconnection space -- room sizing, cage/cabinet count, cross-connect density, power/cooling for active equipment, and carrier-neutral vs. carrier-specific architecture.
5. **IX Peering Evaluation:** Assess nearest Internet exchange points, latency to major IXPs, peering vs. transit cost comparison, and remote peering feasibility. Identify whether the facility could host an IX node.
6. **Subsea Cable Assessment:** For coastal or island sites, evaluate proximity to subsea cable landing stations, available capacity, landing party options, and route diversity for international traffic.
7. **Cost Estimation:** Estimate fiber construction costs (per linear foot for conduit + fiber), carrier circuit NRCs, meet-me room build-out, and ongoing transport operating costs.

### Reference Data

This skill does not require shared reference data files. Connectivity assessment
relies on location-specific carrier and fiber data gathered during discovery.

### Quality Check

1. Verify carrier diversity claims represent physically separate routes (not shared conduit)
2. Confirm fiber entrance design meets the redundancy level required by facility type
3. Cross-check latency claims against distance calculations (fiber latency ~5 microseconds/km)
4. Validate IX peering recommendations against actual IX participation requirements
5. Ensure cost estimates include both construction NRC and ongoing monthly recurring costs

## Output Template

This skill produces two files:
1. `<project-name>-connectivity-assessment.md` -- Full connectivity report
2. `<project-name>-connectivity-assessment.json` -- Structured data for downstream skills

### Markdown Report Structure

**Project:** [Project Name]
**Site:** [Location]
**Date:** [Date]
**Prepared by:** [Skill: predev-connectivity v1.0]

#### 1. Executive Summary
- **Connectivity Rating:** Excellent / Good / Adequate / Challenging / Poor
- **Carrier Diversity:** [X] carriers available via [Y] diverse physical paths
- **Nearest IX:** [IX name] at [distance/latency]
- **Key Strength:** [primary connectivity advantage]
- **Key Risk:** [primary connectivity risk]

#### 2. Fiber Audit

| Radius | Lit Buildings | Carriers On-Net | Dark Fiber Routes | Conduit Available |
|--------|--------------|-----------------|-------------------|-------------------|
| 1 mile | [count] | [carriers] | [routes] | [yes/no] |
| 5 miles | [count] | [carriers] | [routes] | [yes/no] |
| 10 miles | [count] | [carriers] | [routes] | [yes/no] |

#### 3. Carrier Diversity Analysis

| Carrier | Service Type | Entrance Path | Physical Route | Latency to IX | Confidence |
|---------|-------------|---------------|----------------|---------------|------------|
| [carrier] | [lit/dark/wavelength] | [entrance A/B] | [route description] | [ms] | [confirmed/estimated] |

#### 4. Fiber Entrance Design
- **Number of entrances:** [X] (minimum [Y] for [facility type])
- **Physical separation:** [distance between entrances, route diversity]
- **Conduit sizing:** [inner duct count, strand capacity per duct]
- **Entrance vault:** [dimensions, location, access requirements]

#### 5. Meet-Me Room Design
- **Room size:** [sqft]
- **Cage/cabinet capacity:** [count]
- **Cross-connect density:** [per cabinet]
- **Power allocation:** [kW]
- **Cooling:** [type and capacity]
- **Architecture:** [carrier-neutral / carrier-specific]

#### 6. IX Peering Assessment

| IX Point | Location | Distance | Latency | Participants | Peering Type | Monthly Cost |
|----------|----------|----------|---------|-------------|-------------|-------------|
| [IX] | [city] | [km] | [ms] | [count] | [public/private/remote] | [estimate] |

#### 7. Subsea Cable Assessment (if applicable)

| Cable System | Landing Station | Distance | Capacity | Route | Status |
|-------------|----------------|----------|----------|-------|--------|
| [cable] | [station] | [km] | [Tbps] | [origin-destination] | [active/planned] |

#### 8. Cost Estimate

| Item | NRC (One-Time) | MRC (Monthly) | Notes |
|------|---------------|---------------|-------|
| Fiber construction to site | [$] | N/A | [distance x $/linear foot] |
| Carrier circuit installation | [$] | [$] | [per carrier] |
| Meet-me room build-out | [$] | N/A | [fit-out cost] |
| IX port fees | [$] | [$] | [per IX] |
| **Total** | **[$]** | **[$]** | |

#### 9. Recommended Next Steps
- Immediate actions for fiber procurement
- Carrier engagement timeline
- Meet-me room construction milestones

### JSON Sidecar Schema

```json
{
  "artifact_type": "connectivity-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "site_location": "...",
  "connectivity_rating": "excellent | good | adequate | challenging | poor",
  "carrier_diversity": {
    "total_carriers": 0,
    "diverse_physical_paths": 0,
    "entrance_points": 0
  },
  "fiber_audit": {
    "lit_buildings_1mi": 0,
    "lit_buildings_5mi": 0,
    "dark_fiber_routes": 0
  },
  "ix_peering": {
    "nearest_ix": "...",
    "latency_ms": 0,
    "peering_type": "direct | remote | none"
  },
  "subsea_cable": {
    "relevant": false,
    "nearest_landing_km": 0,
    "cable_systems": []
  },
  "cost_estimate": {
    "total_nrc": 0,
    "total_mrc": 0,
    "currency": "USD"
  },
  "latency_requirements_met": true
}
```

## Gotchas

- **Fiber "available" on a carrier map often means 3-12 months and $500K+ in construction.** Carrier "coverage maps" show areas where they *can* build, not where fiber is already lit. Always verify lit vs dark vs planned status -- the difference between "we can serve you" and "fiber is on-net today" is 6-12 months and significant capital.

- **Shared conduit kills diversity.** Two carriers entering a building through the same conduit path provide zero physical diversity. A single backhoe hit takes out both. True diversity requires physically separate conduit routes from separate directions, ideally entering through different building walls. Verify conduit routes, not just carrier names.

- **Meet-me rooms are profit centers for colo operators.** Cross-connect revenue can generate $50-100/month per connection with near-zero marginal cost. Design the meet-me room as a revenue center from day one -- carrier-neutral architecture, scalable cage count, and competitive cross-connect pricing attract carriers and tenants alike.

- **IX peering economics flip at scale.** Below ~10Gbps aggregate, transit is cheaper than IX peering port fees + transport. Above 40-100Gbps, peering saves 30-60% vs transit. Most DC tenants never reach the peering breakeven -- design for it, but don't over-invest in IX infrastructure for a facility targeting small enterprise tenants.

- **Subsea cable landing rights are controlled by consortia.** Proximity to a subsea cable landing station does not guarantee access. Landing parties are pre-negotiated among consortium members. Access for a new DC typically requires a commercial agreement with a consortium member, adding 6-12 months and significant cost to the connectivity timeline.

## Evaluations

See `evals/evals.json` for test scenarios covering high-density fiber market,
rural sovereign facility, and coastal facility near subsea cable landing.
