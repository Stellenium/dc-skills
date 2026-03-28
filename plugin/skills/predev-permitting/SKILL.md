---
name: predev-permitting
description: "Generate a jurisdiction-specific permitting roadmap for data center development with dependency tracking, critical path analysis, and timeline estimation. Use when planning permits for a DC build, navigating zoning approvals, understanding what permits a data center needs, or tracking permitting dependencies and timelines. Trigger with \"permitting roadmap\", \"DC permits\", \"zoning approval\", \"what permits do I need?\", \"building permits for data center\", or \"permitting timeline\"."
argument-hint: "<jurisdiction>"
---

# Permitting Roadmap

Generate a jurisdiction-specific permitting roadmap for data center development.
Maps all required permits with dependency tracking, identifies the critical path,
and estimates timelines by jurisdiction type. Consumes REGULATORY-MATRIX.md for
international regulatory overlays.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location (jurisdiction, zoning classification)
- Facility type and scale (MW, sqft, building height)
- Greenfield/brownfield status
- Generator type and count (for air quality permits)
- Water source and cooling type
- Utility interconnection status

If upstream artifact is not available, I will gather project details
directly through discovery questions or generate placeholders marked [DATA NEEDED].

## Phase 1: Critical Discovery

> Answer these questions first. They determine the permitting universe.

**Project Context:**

1. What is the jurisdiction?
   - Country, state/province, municipality
   - If US: state, county, city (permits may be required at all levels)
   - If international: specify country and region

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. Greenfield or brownfield?
   - **Greenfield:** New construction -- full permitting sequence required
   - **Brownfield:** Conversion -- change of use permits, possible code compliance gaps

4. What is the generator configuration?
   - Number of generators and fuel type (diesel, natural gas, dual-fuel)
   - Total generator capacity (MW)
   - None (grid-only with UPS battery backup)

5. What is the current zoning classification?
   - Already zoned industrial/data center
   - Requires rezoning (from agricultural, residential, commercial)
   - Special/conditional use permit required
   - Unknown

6. What is the planned MW capacity?
   - Phase 1 IT load
   - Total campus build-out

7. What is the building height?
   - Single story (< 40 ft)
   - Multi-story (specify floors and height)
   - Proximity to airports (FAA notification threshold: 200 ft AGL or within approach zones)

8. What is the cooling type and water source?
   - Air-cooled (no water permits for cooling)
   - Evaporative/hybrid (water consumption permits required)
   - Liquid cooling with cooling towers (water rights and discharge permits)

## Phase 2: Context Refinement

> Based on jurisdiction, gather permit-specific detail.

### US Jurisdiction Path

If jurisdiction is US:

1. Is the project in an Opportunity Zone or enterprise zone? (may qualify for fast-track)
2. Is there a data center-specific incentive program with expedited permitting? (Virginia, Texas, Georgia, Ohio)
3. Are there state-level environmental requirements beyond federal? (CEQA in California, SEPA in Washington)
4. Is the site in a floodplain (FEMA zones A or V)?
5. Are there wetlands on or adjacent to the site? (Army Corps Section 404 permit)

### International Jurisdiction Path

If jurisdiction is outside US:

1. What is the national permitting framework? (centralized vs decentralized)
2. Are there data sovereignty requirements affecting facility design? (load REGULATORY-MATRIX.md)
3. Is there an environmental impact assessment (EIA) requirement? (EU EIA Directive, national equivalents)
4. Are there foreign investment approvals needed? (load REGULATORY-MATRIX.md Foreign Ownership section)
5. What is the typical permitting timeline for industrial projects in this jurisdiction?

## Permit Categories and Dependencies

### Complete Permit Universe

| Permit | Authority | Typical Duration | Dependencies | Critical Path? |
|--------|-----------|-----------------|-------------|----------------|
| Zoning/land use approval | Municipal planning | 4-26 weeks | None (first permit) | Yes -- gates everything |
| Conditional use permit (CUP) | Municipal planning/council | 8-26 weeks | Public hearings required | Yes if required |
| Environmental review (NEPA/CEQA/EIA) | Federal/state environmental | 12-52 weeks | Project description complete | Yes for greenfield |
| Building permit | Municipal building dept | 4-12 weeks | Approved plans, zoning approval | Yes |
| Electrical permit | Municipal/state electrical | 2-8 weeks | Building permit (often concurrent) | Sometimes |
| Mechanical permit | Municipal building dept | 2-8 weeks | Building permit (often concurrent) | Rarely |
| Fire/life safety review | Fire marshal/AHJ | 4-12 weeks | Building plans, suppression design | Sometimes |
| Water rights/water supply | State water board/utility | 8-52 weeks | Water source identification | Yes in stressed regions |
| Air quality (generator) | State/regional air quality | 8-26 weeks | Generator specs, emissions modeling | Yes if >1MW gen |
| Noise variance | Municipal code enforcement | 4-12 weeks | Acoustic study | If near residential |
| Transportation/traffic | Municipal/state DOT | 4-16 weeks | Traffic impact study | If road improvements needed |
| Utility interconnection | Utility/ISO/RTO | 26-260 weeks | Interconnection application | Yes -- longest lead time |
| FAA determination | FAA | 4-12 weeks | Structure height and coordinates | If >200ft or near airport |
| Stormwater/SWPPP | State/EPA | 4-8 weeks | Site grading plan | Rarely critical |
| Wetlands (Section 404) | Army Corps of Engineers | 12-52 weeks | Wetland delineation study | Yes if wetlands present |
| Hazardous materials | Fire marshal/environmental | 4-8 weeks | Chemical inventory (diesel, battery) | Rarely critical |

### Dependency Graph

```
Zoning/CUP ──────────────────────────┐
  │                                    │
  ├─> Building Permit ──────────┐     │
  │     ├─> Electrical Permit   │     │
  │     ├─> Mechanical Permit   │     │
  │     └─> Fire/Life Safety    │     │
  │                              │     │
  ├─> Environmental Review ──────┤     │
  │     ├─> Air Quality         │     │
  │     ├─> Water Rights        │     │
  │     └─> Stormwater          │     │
  │                              │     │
  └─> Traffic Study ────────────┘     │
                                       │
Utility Interconnection ──── (parallel, independent) ──> Construction
FAA Determination ────────── (parallel, independent)
```

### Critical Path Identification

The critical path depends on jurisdiction and project specifics:

- **Fast-track jurisdictions** (Virginia, Texas data center corridors): Zoning pre-approved in DC zones, building permit 4-6 weeks, utility interconnection is the bottleneck
- **Standard US jurisdictions**: Zoning/CUP (8-16 weeks) -> Building permit (4-8 weeks) -> Construction. Environmental and air quality permits run in parallel
- **Complex US jurisdictions** (California, Pacific Northwest): CEQA review (26-52 weeks) dominates critical path, followed by water rights in drought regions
- **International jurisdictions**: EIA (12-52 weeks) and foreign investment approval (if required) are typically longest lead items

## Reference Data

Load on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-level regulatory data for international permitting requirements, data sovereignty, and foreign ownership restrictions

## Output

This skill produces two files:
1. `<project-name>-permitting-roadmap.md` -- Permitting roadmap report
2. `<project-name>-permitting-roadmap.json` -- Structured data for downstream skills

### Permitting Roadmap Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: predev-permitting v1.0]

#### 1. Executive Summary
- Total permits required: [N]
- Critical path duration: [X weeks]
- Critical path permits: [list]
- Parallel permit tracks: [N]
- Key risk permits: [list]

#### 2. Permit Register
[Table of all required permits with authority, duration, dependencies, and status]

#### 3. Dependency Map
[Visual dependency graph showing permit sequencing]

#### 4. Critical Path Analysis
[Identification of the longest sequential path with timeline]

#### 5. Parallel Tracks
[Permits that can be pursued simultaneously to compress timeline]

#### 6. Risk Permits
[Permits with highest rejection/delay risk with mitigation strategies]

### JSON Sidecar

```json
{
  "artifact_type": "permitting-roadmap",
  "skill_version": "1.0",
  "project_name": "...",
  "jurisdiction": "...",
  "permits": [
    {
      "name": "...",
      "authority": "...",
      "estimated_duration_weeks": 0,
      "dependencies": ["..."],
      "status": "not-started | in-progress | approved | conditional",
      "critical_path": true
    }
  ],
  "total_timeline_weeks": 0,
  "critical_path_permits": ["..."],
  "parallel_tracks": [
    {
      "track_name": "...",
      "permits": ["..."],
      "duration_weeks": 0
    }
  ],
  "risk_permits": ["..."]
}
```

## Gotchas

- **Conditional use permits for data centers in residential-adjacent zones can require 3-5 public hearings.** Each hearing adds 4-8 weeks to the timeline. Applicants who attend the first hearing unprepared for community noise and water concerns often face hostile receptions at subsequent hearings. Bring acoustic modeling, water usage data, and community benefit commitments to the FIRST hearing.

- **Some jurisdictions require separate air quality permits for each generator above 1MW.** A facility with 20 x 2MW generators may need 20 individual permits or a comprehensive facility-wide operating permit. Check whether the jurisdiction allows a single "synthetic minor" permit that caps total facility emissions below major source thresholds.

- **Utility interconnection is typically the longest lead-time item (2-5 years in congested ISOs) but is not dependent on any other permit.** File the interconnection application on day one of the project -- do not wait for zoning approval. Queue position is determined by application date. In PJM, the interconnection queue backlog exceeds 2,500 GW (as of 2025).

- **Virginia and Texas "data center alley" jurisdictions have pre-zoned industrial parks with by-right DC development** -- no CUP required. This eliminates 8-26 weeks from the critical path. However, by-right does not eliminate building, electrical, fire, or environmental permits.

- **International EIA requirements can be triggered by project size thresholds** that are much lower than the US NEPA threshold. EU EIA Directive Annex I requires mandatory EIA for thermal power stations >300MW thermal. Some member states set lower thresholds for data centers specifically (Ireland, Netherlands).

## Disclaimer

REGULATORY DISCLAIMER: The regulatory analysis, compliance guidance, and
jurisdiction-specific information produced by this skill reflect the regulatory
landscape as of the skill's publication date. Regulations change frequently --
new legislation, executive orders, court decisions, and regulatory guidance can
alter requirements without notice.

This output does not constitute legal advice. Users must verify all regulatory
requirements with qualified local counsel in each relevant jurisdiction before
relying on this analysis for compliance decisions, permit applications, or
contractual obligations.

Where jurisdiction-specific caveats are noted, they highlight known areas of
regulatory complexity or recent change. Absence of a caveat does not imply
regulatory simplicity or stability.

## Evaluations

See `evals/evals.json` for test scenarios covering Virginia fast-track, EU sovereign, and Texas BTM permitting.
