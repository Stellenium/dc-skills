---
name: predev-stakeholder-map
description: "Map stakeholders for a data center development project with influence/interest scoring, engagement strategy, and risk assessment. Use when identifying who matters for a DC project, planning community engagement, mapping political stakeholders, or assessing opposition risk for a data center build. Trigger with \"stakeholder map\", \"stakeholder analysis\", \"community engagement\", \"who are the stakeholders?\", or \"DC political landscape\"."
---

# Stakeholder Map

Identify and map stakeholders for data center development projects with
influence/interest scoring, community opposition risk assessment, and
targeted engagement strategies. Produces a comprehensive stakeholder map
that enables proactive risk management of political, community, and
regulatory dynamics.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location (city, county, state/country)
- Facility type and scale (MW)
- Greenfield/brownfield status
- Water source and consumption estimates
- Grid interconnection impact assessment
- Zoning and land use classification

If upstream artifact is not available, I will gather project details
directly through discovery questions or generate placeholders marked [DATA NEEDED].

## Phase 1: Critical Discovery

> Answer these questions first. They determine the stakeholder universe.

**Project Context:**

1. What is the project location?
   - City/county, state or country
   - Urban, suburban, or rural setting
   - Distance to nearest residential areas

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the planned scale (MW)?
   - Phase 1 IT load and total build-out
   - Number of buildings/phases

4. Greenfield or brownfield?
   - **Greenfield:** New construction on undeveloped or agricultural land
   - **Brownfield:** Conversion of existing commercial/industrial building

5. Are there known opposition issues?
   - Active community opposition (describe)
   - Prior project rejections in the area
   - Media coverage of DC concerns in the region
   - None known

6. What existing community relationships exist?
   - Prior developer presence in the community
   - Existing employer relationships
   - Political connections or prior engagement

7. What is the government support status?
   - Government actively recruiting DC development
   - Government neutral
   - Government or community moratorium on DC development
   - Unknown

8. What is the water source and estimated consumption?
   - Municipal water, well, reclaimed, surface water
   - Estimated annual consumption (gallons)
   - Water-stressed region flag

## Phase 2: Context Refinement

> Based on Phase 1 answers, refine stakeholder assessment.

### Rural/Greenfield Path

If location is rural and/or greenfield:

1. Is the land currently agricultural? (farmland conversion concerns)
2. Are there adjacent residential properties within 1 mile?
3. Is there a local planning commission or zoning board that must approve?
4. Are there tribal/indigenous lands within 5 miles?
5. What is the local water district capacity?

### Urban/Brownfield Path

If location is urban and/or brownfield:

1. What is the current building use and neighborhood character?
2. Is the site in a residential, commercial, or industrial zone?
3. Are there neighborhood associations or community development organizations?
4. What environmental remediation history exists?
5. Are there gentrification or displacement concerns?

### Sovereign/Government Path

If facility type is sovereign:

1. What national security stakeholders are involved?
2. Is there a classified component requiring restricted engagement?
3. What government agency is the primary sponsor?
4. Are there interagency coordination requirements?

## Stakeholder Analysis

### Stakeholder Categories

| Category | Typical Stakeholders | Primary Concerns | Influence Level |
|----------|---------------------|-----------------|-----------------|
| Government -- Elected | Mayor, city council, county commissioners, state legislators | Jobs, tax revenue, re-election, constituent concerns | High |
| Government -- Staff | Planning department, economic development, building officials | Code compliance, process adherence, workload | Medium-High |
| Utility | Electric utility, water utility, telecom providers | Load growth, infrastructure investment, rate impact | High |
| Community groups | Neighborhood associations, HOAs, civic organizations | Quality of life, property values, traffic, noise | Medium-High |
| Environmental orgs | Conservation groups, watershed councils, climate advocates | Water use, emissions, habitat impact, sustainability | Medium |
| Labor unions | Building trades, electricians, operating engineers | Local hiring, prevailing wage, apprenticeship programs | Medium |
| Adjacent property | Neighboring landowners, businesses, residential | Noise, visual impact, property values, traffic | Medium |
| Media | Local newspapers, TV, trade press, social media influencers | Story angle (jobs vs environmental impact), public interest | Medium-High |
| Tribal/indigenous | Tribal councils, cultural preservation offices | Sacred sites, water rights, cultural resources, sovereignty | High (if applicable) |
| Education | Universities, community colleges, K-12 districts | Workforce pipeline, STEM programs, tax revenue to schools | Low-Medium |
| Business community | Chamber of commerce, economic development council | Economic growth, supply chain opportunities, workforce | Low-Medium |

### Influence/Interest Scoring Matrix

Score each stakeholder 1-5 on two dimensions:

- **Influence:** Ability to approve, block, or delay the project (5 = veto power, 1 = no formal authority)
- **Interest:** Level of active engagement or concern about the project (5 = highly engaged, 1 = indifferent)

| Quadrant | Influence | Interest | Strategy |
|----------|-----------|----------|----------|
| Key players | High (4-5) | High (4-5) | Deep engagement, regular updates, address concerns proactively |
| Context setters | High (4-5) | Low (1-3) | Keep satisfied, monitor for interest changes, provide periodic updates |
| Active stakeholders | Low (1-3) | High (4-5) | Keep informed, provide forums for input, manage expectations |
| General public | Low (1-3) | Low (1-3) | Monitor, provide information on request, maintain transparency |

### Opposition Risk Assessment

| Risk Type | Trigger | Likelihood Factors | Severity | Typical Mitigation |
|-----------|---------|-------------------|----------|-------------------|
| Water consumption | DC water use in stressed region | Drought conditions, limited aquifer, competing agricultural use | High -- can kill project | WUE < 1.2 commitment, air cooling, ZLD, reclaimed water, water offset credits |
| Noise | Generator testing, cooling towers, transformers | Proximity to residential, nighttime operations, cumulative noise | Medium -- delays permitting | Noise walls, equipment selection, testing schedule restrictions, acoustic modeling |
| Traffic | Construction phase, ongoing deliveries | Rural roads, school zones, peak hour conflicts | Medium -- conditions on permits | Traffic management plan, road improvements, delivery scheduling |
| Visual impact | Large industrial facility in scenic/residential area | Building height, lighting, fencing, setback distance | Medium -- design modifications | Architectural screening, landscaping, lighting controls, setback buffers |
| Property values | Perceived industrial intrusion | Residential proximity, property type (single-family vs commercial) | Medium -- community opposition | Property value guarantee program, buffer zones, community benefits |
| Grid strain | Large load on local distribution system | Capacity-constrained grid, impact on reliability for other ratepayers | Medium-High -- utility opposition | Dedicated feed, BTM generation, demand response commitments |
| Environmental | Habitat disruption, emissions, stormwater | Wetlands, endangered species, floodplain, agricultural conversion | High -- regulatory block | Environmental assessment, habitat mitigation, stormwater management |

## Output

This skill produces two files:
1. `<project-name>-stakeholder-map.md` -- Stakeholder map report
2. `<project-name>-stakeholder-map.json` -- Structured data for downstream skills

### Stakeholder Map Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: predev-stakeholder-map v1.0]

#### 1. Executive Summary
- Total stakeholders identified: [N]
- Key players (high influence/high interest): [N]
- Opposition risk rating: [low / moderate / high / critical]
- Recommended engagement timeline

#### 2. Stakeholder Register
[Table of all identified stakeholders with influence/interest scores and strategies]

#### 3. Opposition Risk Assessment
[Risk-by-risk analysis with likelihood, severity, and mitigation per Opposition Risk Assessment above]

#### 4. Engagement Strategy
[Phased engagement plan: pre-announcement, announcement, permitting, construction, operations]

#### 5. Engagement Timeline
[Calendar-aligned engagement milestones tied to project development schedule]

### JSON Sidecar

```json
{
  "artifact_type": "stakeholder-map",
  "skill_version": "1.0",
  "project_name": "...",
  "stakeholders": [
    {
      "name": "...",
      "category": "...",
      "influence_score": 0,
      "interest_score": 0,
      "position": "supportive | neutral | opposed | unknown",
      "engagement_strategy": "..."
    }
  ],
  "opposition_risks": [
    {
      "type": "water | noise | traffic | visual | property-values | grid | environmental",
      "likelihood": "low | medium | high",
      "severity": "low | medium | high | critical",
      "mitigation": "..."
    }
  ],
  "engagement_timeline": {
    "pre_announcement": [],
    "announcement": [],
    "permitting": [],
    "construction": [],
    "operations": []
  },
  "overall_risk_rating": "low | moderate | high | critical"
}
```

## Gotchas

- **Community opposition to DC water use is the fastest-growing risk factor.** Between 2023-2026, water-related DC opposition campaigns have delayed or blocked projects in Arizona, Oregon, Chile, and the Netherlands. In water-stressed regions, lead with water efficiency commitments (WUE < 1.2, air-cooled, reclaimed water) BEFORE the community raises the issue. Reactive water messaging always fails.

- **Tribal consultation requirements can add 6-18 months to permitting.** Section 106 of the National Historic Preservation Act (US) requires consultation with tribes when federal permits or funding are involved. Even without federal nexus, many states have parallel requirements. Identify tribal interests early -- a late-discovered sacred site or cultural resource can halt construction.

- **Adjacent property owners within 1 mile have standing to challenge zoning decisions in most US jurisdictions.** A single homeowner can file an appeal that delays conditional use permit approval by 6-12 months. Proactive engagement with adjacent owners (noise modeling, visual renderings, property value data) reduces appeal risk.

- **Social media amplifies opposition faster than traditional channels.** A single viral post about DC water consumption or noise can mobilize community opposition within days. Monitor social media for project mentions and have a response plan ready before the first public hearing. Community benefits agreements (CBAs) announced simultaneously with the project are the most effective counter.

## Evaluations

See `evals/evals.json` for test scenarios covering rural, urban brownfield, and sovereign stakeholder mapping.
