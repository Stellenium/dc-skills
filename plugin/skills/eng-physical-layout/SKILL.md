---
name: eng-physical-layout
description: "Design data center hall layout including whitespace planning, hot/cold aisle containment, cable management, and rack placement. Use when laying out a data center floor, planning aisle containment, optimizing rack placement, or designing cable pathways and whitespace allocation. Trigger with \"floor layout\", \"hall design\", \"aisle containment\", \"rack placement\", \"whitespace planning\", \"cable management\", or \"DC physical layout\"."
---

# Physical Layout Planning

Design data center hall layout with whitespace planning, containment strategy,
cable management, power distribution routing, and BICSI 002-2024 compliance.
Produces a physical layout plan with rack arrangement, aisle dimensions,
pathway sizing, and compliance checklist.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load per hall (MW)
- Per-rack power budget (kW/rack)
- Power distribution approach (busway vs whip, RPP placement)
- Redundancy tier and configuration

**From cooling-design-report (eng-cooling-design):**
- Cooling distribution type (overhead, underfloor, in-row, rear-door, direct-to-chip)
- Containment strategy recommendation (hot aisle, cold aisle, chimney cabinet)
- Airflow requirements per rack (CFM)
- Cooling infrastructure footprint (CRAHs, CDUs, piping)

If upstream data is not available, I will ask you for IT capacity, rack density,
and cooling approach, or use standard defaults for the facility type.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire layout approach.

**Project Context:**

1. Is this a greenfield hall or renovation of existing space?
   - **Greenfield:** New construction -- full design freedom
   - **Renovation:** Existing structure -- proceed to Renovation Path below

2. What facility type?
   - Traditional enterprise (single-tenant, mixed density, 2-20MW)
   - Hyperscale (standardized halls, uniform density, 20-500MW+)
   - AI/HPC training facility (ultra-high density, liquid cooling)
   - Colocation (multi-tenant, partitioned halls)
   - Edge (single room, compact layout)

3. What is the available floor area?
   - Total square footage or square meters per hall
   - Number of halls or rooms
   - Floor-to-floor height and usable ceiling height

4. What is the target IT capacity per hall (MW)?
   - Total IT load to be supported
   - Target rack count

5. What is the rack density range?
   - Standard density: 5-15 kW/rack
   - Medium density: 15-30 kW/rack
   - High density: 30-60 kW/rack
   - Ultra-high density: 60-120+ kW/rack (AI/HPC)

6. What is the floor construction?
   - Raised floor (specify height: 18", 24", 30", 36")
   - Slab-on-grade (no raised floor)
   - Hybrid (raised floor in data halls, slab in support areas)

7. What is the cooling distribution type?
   - Underfloor (raised floor with perforated tiles)
   - Overhead (ceiling-mounted supply, hot aisle return)
   - In-row (between-rack cooling units)
   - Rear-door heat exchangers
   - Direct-to-chip liquid cooling with manifolds
   - Mixed (different zones with different cooling)

8. What is the structural floor loading capacity?
   - Standard: 150-250 lbs/sqft
   - Heavy: 250-500 lbs/sqft
   - Reinforced: 500+ lbs/sqft
   - Unknown (will need structural assessment)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Renovation Path

If Phase 1 answer is **Renovation**:

1. What is the existing column grid spacing?
2. Are there structural obstructions (columns, beams, utilities)?
3. What is the existing floor loading capacity?
4. Are there fixed points (electrical rooms, HVAC locations) constraining layout?

### Density-Based Refinements

**Ultra-high density (>60 kW/rack) -- AI/HPC path:**
1. What GPU/accelerator type? (Load GPU-REFERENCE.md for rack density data)
2. Is liquid cooling infrastructure already designed?
3. What interconnect fabric? (InfiniBand, RoCEv2 -- affects cable pathway sizing)
4. Cluster topology constraints? (fat-tree, rail-optimized -- affects rack adjacency)

**Multi-tenant (colo) path:**
1. How many tenant zones per hall?
2. Cage vs suite vs open-floor partitioning?
3. Per-tenant metering requirements?
4. Shared vs dedicated cooling per tenant zone?

### Facility Type Parameters

| Parameter | Enterprise | Hyperscale | AI/HPC | Colo | Edge |
|-----------|------------|------------|--------|------|------|
| Rack density (kW) | 5-15 | 15-40 | 40-120+ | 5-30 | 5-15 |
| Cold aisle width | 48" | 48" | 48-60" | 48" | 36-42" |
| Hot aisle width | 36-42" | 36-42" | 42-48" | 36" | 36" |
| Row length (racks) | 10-20 | 20-40 | 8-16 | 10-20 | 4-10 |
| Containment | Hot or cold | Cold aisle | Chimney/cold | Hot aisle | Optional |
| Cable pathway | Overhead | Overhead | Overhead | Overhead/underfloor | Underfloor |

## Analysis & Output

### Process

1. **Whitespace planning:** Calculate gross-to-net ratio (typically 55-65% usable for IT), determine aisle widths per BICSI 002-2024 minimums, allocate space for cooling infrastructure, electrical rooms, and egress paths
2. **Rack layout:** Design row length, row spacing, end-of-row clearance (minimum 48" per BICSI), rack orientation (front-to-back airflow alignment)
3. **Containment strategy:** Select hot aisle containment, cold aisle containment, or chimney cabinet based on density and cooling type. Design containment panels, doors, and blanking strategy
4. **Cable management:** Size cable pathways per TIA-569 (40% fill horizontal, 25% fill vertical), plan fiber vs copper distribution, design structured cabling from MDA to HDA to rack
5. **Power distribution routing:** Place RPPs, busway runs or whip routing, coordinate with rack rows, maintain separation from data cables per NEC requirements
6. **BICSI 002-2024 compliance checklist:** Verify minimum aisle widths (48" cold, 36" hot), clearances around equipment, egress path widths and distances, ADA accessibility requirements, equipment access clearances

### Reference Data

Load these files on demand -- do not read upfront:

- [GPU specifications](../../references/GPU-REFERENCE.md) -- Section matching accelerator type for per-rack power density and cooling requirements (H100 racks ~40-70kW, GB200 NVL72 racks ~120kW)

### Quality Check

1. Verify all aisle widths meet BICSI 002-2024 minimums (48" cold aisle, 36" hot aisle)
2. Confirm egress paths comply with NFPA 75 and local fire code
3. Cross-check rack density assumptions against GPU-REFERENCE.md for AI/HPC facilities
4. Validate floor loading does not exceed structural capacity for high-density rows
5. Verify cable pathway fill does not exceed TIA-569 limits (40% horizontal)
6. Confirm power and data cable separation meets NEC requirements

## Output

This skill produces two files:
1. `<project-name>-physical-layout-plan.md` -- Full report
2. `<project-name>-physical-layout-plan.json` -- Structured data for downstream skills

### Physical Layout Plan Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-physical-layout v1.0]

#### 1. Executive Summary
- Hall area: [sqft/sqm] gross, [sqft/sqm] net usable
- Gross-to-net ratio: [%]
- Rack count: [N] racks in [N] rows
- IT capacity: [MW] at [kW/rack] average density
- Containment: [hot aisle / cold aisle / chimney]

#### 2. Hall Layout
- Dimensions: [L x W x H]
- Column grid: [spacing if applicable]
- Row configuration: [N] rows of [N] racks each
- Row orientation: [direction, aligned with cooling airflow]
- Aisle dimensions: cold aisle [inches], hot aisle [inches]
- End-of-row clearance: [inches]

#### 3. Containment Design
- Strategy: [hot aisle / cold aisle / chimney cabinet]
- Panel type: [rigid / curtain / hybrid]
- Door configuration: [sliding / swing / bi-fold]
- Blanking strategy: [standard blanking panels in all unused U-spaces]
- Bypass airflow target: [<5% for well-contained system]

#### 4. Cable Management
| Pathway | Type | Size | Fill Ratio | Route |
|---------|------|------|------------|-------|
| Horizontal main | Ladder tray | [width x depth] | [%] | [overhead/underfloor] |
| Horizontal branch | Cable tray | [width x depth] | [%] | [overhead/underfloor] |
| Vertical | Cabinet vertical manager | [width] | [%] | [per-rack] |
| Fiber distribution | Innerduct | [diameter] | [%] | [route] |

#### 5. Power Distribution Layout
- Distribution type: [busway / whip / combination]
- RPP locations: [per-row / end-of-row / overhead]
- Busway routing: [overhead / underfloor]
- Cable separation: [distance from data cables per NEC]

#### 6. BICSI 002-2024 Compliance
| Requirement | Standard | Design | Compliant |
|-------------|----------|--------|-----------|
| Cold aisle width | >= 48" | [value] | [Y/N] |
| Hot aisle width | >= 36" | [value] | [Y/N] |
| End-of-row clearance | >= 48" | [value] | [Y/N] |
| Egress distance | per NFPA 75 | [value] | [Y/N] |
| ADA accessibility | per ADA | [value] | [Y/N] |
| Equipment front clearance | >= 36" | [value] | [Y/N] |

### JSON Sidecar

```json
{
  "artifact_type": "physical-layout-plan",
  "skill_version": "1.0",
  "project_name": "...",
  "hall_area_sqft": {"gross": 0, "net": 0},
  "gross_to_net_ratio": 0.00,
  "rack_count": 0,
  "row_count": 0,
  "racks_per_row": 0,
  "it_capacity_kw": 0,
  "avg_density_kw_per_rack": 0,
  "containment_type": "hot-aisle | cold-aisle | chimney",
  "floor_type": "raised | slab | hybrid",
  "aisle_widths_inches": {"cold": 0, "hot": 0},
  "cable_pathway_fill_pct": {"horizontal": 0, "vertical": 0},
  "bicsi_002_compliant": true,
  "power_distribution": "busway | whip | combination"
}
```

## Gotchas

- **BICSI 002-2024 requires minimum 48-inch cold aisle and 36-inch hot aisle -- many legacy designs use 42/36 which is now non-compliant.** The 2024 revision increased cold aisle minimums from 42" to 48". Any new design citing BICSI 002 compliance must meet the 48" minimum. Renovation projects may need to remove rack positions to achieve compliance.

- **Floor loading for high-density AI racks can exceed 3,000 lbs/sqft -- verify structural capacity before placing >60kW racks on raised floor.** A fully loaded GB200 NVL72 rack at 120kW weighs approximately 3,000-3,500 lbs on a 2x4ft footprint. Raised floor panels rated for 250 lbs/sqft (standard) cannot support this. Slab-on-grade or reinforced raised floor is required.

- **Cable pathway fill should not exceed 40% for horizontal runs (TIA-569) -- plan for 3x current cable count to allow growth.** Day-one cable fill at 40% means the pathway is already at capacity with no room for adds/moves/changes. Design initial fill at 20-25% to accommodate cable growth over the facility lifecycle without pathway expansion.

- **Hot aisle containment is preferred over cold aisle containment in high-density facilities.** Cold aisle containment traps heat if cooling fails, creating a thermal runaway risk. Hot aisle containment allows heat to dissipate into the room if containment fails, providing a safer failure mode. Most Tier III+ facilities use hot aisle containment for this reason.

## Evaluations

See `evals/evals.json` for test scenarios covering enterprise, AI training, and multi-tenant colo layouts.
