---
name: eng-density-upgrade
description: "Plan air-to-liquid cooling retrofits for live data center facilities upgrading from 5-15 kW/rack to 30-100+ kW/rack for AI/HPC workloads. Use when upgrading rack density, retrofitting cooling for GPU workloads, planning live facility upgrades, or transitioning from air to liquid cooling in an existing DC. Trigger with \"density upgrade\", \"cooling retrofit\", \"air to liquid\", \"rack density upgrade\", \"GPU retrofit\", or \"upgrade existing DC for AI\"."
---

# Density Upgrade Planning (Air-to-Liquid Retrofit)

Plan the retrofit of existing data center facilities from air cooling to liquid
cooling for higher rack densities. Covers technology selection, CDU placement,
piping routes, electrical upgrades, and phased migration while maintaining
live operations. Consumes the upstream cooling design report for technology
evaluation context.

## What I Need from Upstream

**From cooling-design-report (eng-cooling-design):**
- Recommended liquid cooling technology (RDHx, direct-to-chip, or immersion)
- Current cooling infrastructure assessment
- PUE/WUE projections for the target technology
- Climate zone and water availability constraints

If upstream data is not available, this skill guides technology selection
directly using the technology path framework below.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire retrofit approach.

**Current Facility:**

1. What is the current facility type?
   - Traditional raised-floor data center
   - Slab-on-grade (no raised floor)
   - Modular/prefab facility
   - Other (describe)

2. What is the current rack density and target density?
   - Current: [X] kW/rack (typical air-cooled: 5-15 kW)
   - Target: [Y] kW/rack
   - Number of racks to upgrade

3. What is the current cooling infrastructure?
   - CRAH/CRAC units (raised-floor perforated tiles)
   - In-row cooling units
   - Hot/cold aisle containment
   - Other (describe)

4. What liquid cooling technology is preferred?
   - Rear-door heat exchangers (RDHx) -- moderate density 15-40 kW/rack
   - Direct-to-chip (cold plate) -- high density 40-80 kW/rack
   - Immersion cooling -- extreme density 80-100+ kW/rack
   - No preference (evaluate options)

5. What is the available mechanical space?
   - Square footage available for CDU placement
   - Roof capacity for additional heat rejection equipment
   - Adjacent outdoor space for dry coolers or cooling towers

6. What are the operational constraints?
   - Zero downtime (fully live migration required)
   - Maintenance windows available (specify duration and frequency)
   - Acceptable risk tolerance for migration (conservative/moderate/aggressive)

7. What is the timeline and budget?
   - Target completion date
   - Budget range
   - Phased rollout preference (one zone at a time, one row at a time)

8. What is the primary workload driving the upgrade?
   - AI training (sustained high power, liquid cooling mandatory above 40kW)
   - AI inference (variable load, may support mixed air/liquid)
   - HPC / scientific computing (steady-state, high utilization)
   - General enterprise growth (incremental density increase)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather facility-specific detail.

### Facility Layout

1. Hall dimensions (length x width x height)?
2. Current rack row layout (number of rows, racks per row, aisle widths)?
3. Cable tray routing (overhead, underfloor, or side-of-rack)?
4. Raised floor height if applicable (typically 18-36 inches)?
5. Ceiling height above racks (for overhead piping clearance)?

### Existing Infrastructure

1. Current electrical capacity per rack (circuit type, voltage, amperage)?
2. PDU/RPP locations and available capacity?
3. Existing chilled water infrastructure (if any)?
4. BMS/DCIM monitoring capabilities?
5. Fire suppression system type (pre-action sprinkler, clean agent)?

### Facility Type Refinements

**Traditional raised-floor:**
- Raised floor tile capacity for CDU weight (CDUs weigh 2,000-4,000 lbs)
- Underfloor clearance for piping routes (18" minimum, 24"+ preferred)
- Existing underfloor cable density (may conflict with piping)

**Slab-on-grade:**
- Overhead clearance for piping manifolds (minimum 12" below ceiling)
- Cable tray relocation requirements for piping routes
- Floor penetration feasibility for supply/return headers

**Modular/prefab:**
- Module interconnection points for CDU integration
- External mechanical pad dimensions
- Pre-engineered connection points (some modular vendors provide liquid-ready options)

## Technology Path Framework

### Path A: Rear-Door Heat Exchangers (RDHx)

**Best for:** Moderate density upgrades (15-40 kW/rack)

- Passive or active RDHx units replace standard rear doors
- Chilled water or refrigerant loop removes 50-70% of rack heat at the door
- Remaining heat handled by existing room-level air cooling
- CDU requirement: 1 CDU per 15-25 racks (passive) or integrated per door (active)
- Piping: chilled water supply/return to each rack position (overhead or underfloor)
- Electrical: existing circuits may suffice for moderate upgrades; verify per-rack power budget
- Advantages: least disruptive retrofit, compatible with standard servers, no IT hardware changes
- Limitations: maximum ~40 kW/rack; diminishing returns above 30 kW

### Path B: Direct-to-Chip (Cold Plate)

**Best for:** High density (40-80 kW/rack)

- Cold plates attached directly to CPU/GPU heat spreaders
- Removes 60-80% of heat via liquid; remaining via air
- CDU requirement: 1 CDU per 8-16 racks (40-60 sqft per CDU)
- Supply temperature: 35-45C (warm water, enables free cooling)
- Piping: manifold per row with quick-disconnect per rack
- Electrical: 30kW racks need 40A 208V circuits minimum; 60kW+ need multiple circuits or 415V
- Advantages: proven technology, server vendor support (Dell, HPE, Lenovo), warm-water capable
- Limitations: requires compatible server hardware with cold plate mounts

### Path C: Immersion Cooling

**Best for:** Extreme density (80-100+ kW/rack)

- Servers submerged in dielectric coolant (single-phase or two-phase)
- Removes ~100% of heat via liquid
- CDU requirement: 1 CDU per 4-8 tanks (~60 sqft per CDU)
- Immersion tank dimensions: typically 4x2x3 ft per tank, 3,000-5,000 lbs filled
- Piping: larger diameter supply/return (2-4" vs 1-2" for DLC)
- Electrical: high-amperage connections per tank; 415V recommended for extreme density
- Advantages: highest density achievable, eliminates fans, enables heat reuse
- Limitations: specialized IT hardware, complex maintenance, limited vendor ecosystem

## CDU Placement and Piping

### CDU Sizing and Placement

- **Footprint:** 40-60 sqft per CDU (including service clearance)
- **Weight:** 2,000-4,000 lbs per CDU (verify floor loading capacity)
- **Placement options:**
  - End of row (preferred for retrofit -- minimizes piping runs)
  - Adjacent mechanical room (if available space)
  - Outdoor CDU (weather-rated, eliminates indoor space constraint)
- **Capacity:** Each CDU serves 8-20 racks depending on density and technology
- **Redundancy:** N+1 CDU configuration recommended; 2N for mission-critical

### Piping Route Design

- **Overhead routing (preferred for retrofit):**
  - Suspended from ceiling structure or dedicated pipe rack
  - Minimum 12" clearance below ceiling for maintenance access
  - Conflict check against existing cable trays (relocate if necessary)
  - Support brackets rated for filled pipe weight plus safety factor

- **Underfloor routing (raised-floor facilities):**
  - Requires 24"+ raised floor height for adequate clearance
  - Cannot share space with high-voltage power cables (code separation)
  - Risk of condensation in humid environments -- insulate cold supply lines
  - May conflict with existing underfloor cable density

- **Piping specifications:**
  - DLC: 1-2" supply/return per row manifold; 3/4" quick-disconnect per rack
  - Immersion: 2-4" supply/return headers; 1-2" per tank connection
  - RDHx: 3/4-1" supply/return per rack; 2" row header
  - Material: copper or stainless steel (no PVC -- pressure and temperature ratings)

### Leak Detection (Mandatory)

- **Zone-based leak detection under all piping routes** -- not optional for liquid cooling
- Drip trays under every CDU and piping connection point
- Rope-style leak sensors along piping runs and under raised floor
- Automatic shutoff valves at zone boundaries
- DCIM/BMS integration for immediate alerting
- Insurance carriers may require leak detection as a coverage condition

## Electrical Upgrade Requirements

### Per-Rack Power Scaling

| Target Density | Circuit Requirements | PDU Type | Panel Capacity |
|---------------|---------------------|----------|----------------|
| 15-30 kW/rack | 1x 30A 208V or 1x 40A 208V | Metered intelligent | 225A panel per 8-10 racks |
| 30-60 kW/rack | 2x 40A 208V or 1x 60A 208V or 1x 30A 415V | Switched intelligent | 400A panel per 6-8 racks |
| 60-100+ kW/rack | Multiple 60A 208V or 60A 415V | High-density PDU | 600A+ panel per 4-6 racks |

### Upgrade Scope

- **RPP (Remote Power Panel) additions:** new RPPs closer to high-density zones
- **Busway vs whip:** busway preferred for flexibility in high-density zones (easy tap-off repositioning)
- **Transformer capacity:** verify existing transformer can handle increased load; add or upsize as needed
- **Generator capacity:** ensure backup generation covers the upgraded load profile

## Phased Migration Plan

### Migration Principles

1. **Convert one zone at a time** while remaining facility stays operational
2. **Maintain N+1 cooling redundancy** during transition -- both air and liquid systems must provide coverage
3. **Commission per zone** -- mechanical, electrical, and leak testing before IT load migration
4. **Rollback plan per zone** -- ability to revert to air cooling if issues arise

### Migration Sequence Template

| Phase | Scope | Duration | Prerequisites | Rollback Plan |
|-------|-------|----------|---------------|---------------|
| Phase 0 | Infrastructure prep (CDU pad, piping backbone, electrical rough-in) | 4-8 weeks | Design approval, permits | N/A (no IT disruption) |
| Phase 1 | Convert Zone A (first row or pod) | 2-4 weeks | Phase 0 complete, leak test passed | Revert to air cooling, reconnect CRAH |
| Phase 2 | Convert Zone B | 2-4 weeks | Phase 1 operational 2+ weeks | Same as Phase 1 |
| Phase N | Final zone + decommission air cooling | 2-4 weeks | All prior zones stable | Retain air cooling backup for 30 days |
| Closeout | Remove temporary air cooling, optimize CDU settings | 1-2 weeks | All zones at target density | N/A |

### Transition Cooling Considerations

During migration, the facility runs a hybrid air + liquid cooling configuration:
- Air cooling continues for non-converted zones at existing density
- Liquid cooling handles converted zones at new density
- Total cooling capacity must cover both regimes simultaneously
- BMS must monitor both air and liquid cooling loops
- Gradual air cooling decommissioning as zones convert (do not remove prematurely)

## Output

This skill produces two files:
1. `<project-name>-density-upgrade-plan.md` -- Full retrofit plan
2. `<project-name>-density-upgrade-plan.json` -- Structured data

### Density Upgrade Plan Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-density-upgrade v1.0]

#### 1. Executive Summary
- Current state: [X racks at Y kW/rack, Z MW total]
- Target state: [X racks at Y kW/rack, Z MW total]
- Technology: [RDHx / Direct-to-chip / Immersion]
- CDU count: [X CDUs in N+1 configuration]
- Estimated cost: [$X-Y M]
- Timeline: [X-Y months]

#### 2. Technology Selection Rationale
- Selected technology and why
- Alternatives considered with trade-offs
- Upstream cooling-design-report alignment (if available)

#### 3. CDU Layout and Piping Plan
- CDU placement map (zone-by-zone)
- Piping route description (overhead/underfloor)
- Leak detection layout

#### 4. Electrical Upgrade Scope
- Per-rack power changes
- RPP/PDU additions
- Transformer/generator impact

#### 5. Zone-by-Zone Migration Schedule
- Per-zone conversion plan with timeline
- Cooling transition management
- Rollback triggers and procedures

#### 6. Cost Estimate

| Category | Low Estimate | High Estimate | Notes |
|----------|-------------|---------------|-------|
| CDU equipment | [$X] | [$Y] | [count x unit cost] |
| Piping and manifolds | [$X] | [$Y] | [linear feet x rate] |
| Electrical upgrades | [$X] | [$Y] | [RPPs, PDUs, panels] |
| Leak detection | [$X] | [$Y] | [zones x system cost] |
| Labor and commissioning | [$X] | [$Y] | [regional labor rates] |
| **Total** | **[$X]** | **[$Y]** | |

### JSON Sidecar Schema

```json
{
  "artifact_type": "density-upgrade-plan",
  "skill_version": "1.0",
  "project_name": "...",
  "current_density_kw": 0,
  "target_density_kw": 0,
  "rack_count": 0,
  "technology": "rdhx | direct-to-chip | immersion",
  "cdu_count": 0,
  "cdu_redundancy": "N+1",
  "piping_route": "overhead | underfloor",
  "migration_phases": 0,
  "estimated_timeline_months": 0,
  "cost_estimate_low": 0,
  "cost_estimate_high": 0,
  "electrical_upgrade_required": true,
  "zones": []
}
```

## Gotchas

- **Water leak detection is mandatory for liquid cooling retrofits -- not optional.** Insurance carriers increasingly require zone-based leak detection as a coverage condition for facilities with liquid cooling. Failure to install leak detection can void property and business interruption coverage. Budget $15-30K per zone for rope sensors, drip trays, and shutoff valves.

- **Floor loading may limit CDU placement in raised-floor facilities.** CDUs weigh 2,000-4,000 lbs. Standard raised floor tiles are rated for 250 lbs concentrated load. CDUs require structural support directly to the slab (pour concrete pads through the raised floor or place on reinforced sections). This is frequently missed in initial planning.

- **Insurance implications of liquid near electronics are significant.** Many property insurance policies have exclusions or surcharges for facilities with water-based cooling in the IT space. Engage your insurance broker early in the design phase. Dielectric immersion coolant (non-conductive) may mitigate underwriting concerns but requires specialized policy endorsements.

- **N+1 cooling redundancy must be maintained during every migration phase.** If you decommission air cooling in Zone A before Zone B's liquid cooling is fully commissioned and stable, a CDU failure in Zone A has no backup. Keep air cooling operational in each zone until the liquid system has run stable for at least 2 weeks under production load.

- **Warm-water direct-to-chip (35-45C supply) enables dramatic free cooling savings but requires compatible CDUs.** Not all CDUs support warm-water operation. Warm-water DLC can use dry coolers year-round in most climates (eliminating cooling towers), but the CDU heat exchangers must be rated for the higher supply temperatures. Specify warm-water compatibility in procurement.

## Evaluations

See `evals/evals.json` for test scenarios covering traditional raised-floor,
slab-on-grade hyperscale, and modular facility density upgrades.
