---
name: predev-environmental
description: "Produce an Environmental Impact Assessment scoping document for data center development with water rights analysis and permitting requirements. Use when assessing environmental impact of a DC build, evaluating water usage rights, preparing EIA documents, or understanding environmental permitting for data centers. Trigger with \"environmental impact\", \"EIA for data center\", \"water rights\", \"environmental assessment\", or \"DC environmental permitting\"."
---

# Environmental Assessment

Produce an EIA (Environmental Impact Assessment) scoping document for data center
development with a water rights deep-dive and LEED/BREEAM certification path
analysis. Covers all environmental categories relevant to DC development with
jurisdiction-specific regulatory mapping.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location and climate zone
- Facility type, scale (MW), and cooling type
- Water source and estimated consumption
- Site acreage, topography, and existing conditions
- Environmental flags (wetlands, floodplain, endangered species)
- Sustainability certification target (if any)

If upstream artifact is not available, I will gather project details
directly through discovery questions or generate placeholders marked [DATA NEEDED].

## Phase 1: Critical Discovery

> Answer these questions first. They determine the environmental scope.

**Project Context:**

1. What is the project location?
   - Country, state/province, municipality
   - Climate zone (ASHRAE climate zone 1-8)
   - Water stress level (WRI Aqueduct classification)

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the cooling type?
   - Air-cooled (dry coolers, no water for heat rejection)
   - Evaporative (cooling towers, adiabatic systems)
   - Liquid cooling (direct-to-chip, immersion)
   - Hybrid (air + evaporative or air + liquid)

4. What is the water source?
   - Municipal supply
   - On-site well (groundwater)
   - Reclaimed/recycled water
   - Surface water (river, lake)
   - No water for cooling (air-cooled only)

5. What is the planned MW capacity?
   - Phase 1 IT load and total build-out
   - Total facility load including PUE overhead

6. What sustainability certification is targeted?
   - LEED (specify level: Certified, Silver, Gold, Platinum)
   - BREEAM (specify level: Pass, Good, Very Good, Excellent, Outstanding)
   - No certification target
   - Other (specify)

7. Is this a water-stressed region?
   - Yes -- high or extremely high water stress (WRI classification)
   - Moderate water stress
   - Low water stress
   - Unknown

8. What generators are planned?
   - Diesel generators (number and MW)
   - Natural gas generators
   - None (grid + battery only)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather category-specific detail.

### Water-Stressed Region Path

If Phase 1 Q7 = high or extremely high water stress:

1. What is the current water allocation for the site? (existing water rights)
2. Has a water rights transfer or new appropriation been filed?
3. What is the drought contingency plan? (mandatory in many western US states)
4. Has zero-liquid-discharge (ZLD) been evaluated?
5. What Water Use Effectiveness (WUE) target is achievable?

### Greenfield Environmental Path

1. Has a Phase 1 Environmental Site Assessment (ESA) been completed?
2. Are there known wetlands, waterways, or floodplain on site?
3. Has a biological survey been conducted? (endangered species, migratory birds)
4. Is the site within a designated air quality non-attainment area?
5. What is the stormwater discharge destination?

### LEED/BREEAM Path

If certification is targeted:

1. Has a LEED/BREEAM pre-assessment been completed?
2. What credit categories are priorities? (energy, water, materials, indoor, site)
3. Is commissioning by a third-party CxA planned? (prerequisite for LEED)
4. What renewable energy commitment exists? (on-site, PPA, RECs)

## Environmental Categories

### Water Rights Deep-Dive

**Prior Appropriation Doctrine (Western US states: AZ, CO, NV, NM, UT, WY, MT, ID, OR, WA):**
- "First in time, first in right" -- senior water rights take priority during shortage
- Water rights are property rights, transferable independently from land
- New appropriations require proof of beneficial use and available unappropriated water
- During drought, junior rights holders are curtailed first -- a DC with junior rights may lose water allocation
- New DC projects in fully appropriated basins must acquire existing water rights (purchase or lease from agricultural users)
- Colorado River Compact states (AZ, CA, CO, NV, NM, UT, WY) face increasingly strict allocations

**Riparian Rights Doctrine (Eastern US states):**
- Water rights attached to land adjacent to waterbody
- "Reasonable use" standard -- no fixed allocation, balanced against other riparian users
- Less restrictive than prior appropriation but subject to drought-era restrictions
- Some eastern states (FL, GA) have moved to permit-based systems overlaying riparian rights

**Groundwater Permits:**
- Most western states require permits for groundwater extraction
- Sustainable yield assessment required (aquifer recharge rate vs extraction rate)
- Monitoring and reporting obligations (meter installation, annual reporting)
- Some states (TX) follow "rule of capture" -- no permit needed but subject to groundwater conservation district rules

**Drought Contingency:**
- Mandatory drought contingency plans in water-stressed regions
- Tiered water reduction targets (10%, 20%, 50% curtailment scenarios)
- Alternative supply activation triggers
- DC-specific: switch from evaporative to air-cooled operation, reduce non-critical water use

**Zero-Liquid-Discharge (ZLD) Evaluation:**
- Eliminates cooling tower blowdown discharge entirely
- Technologies: thermal ZLD (brine concentrator + crystallizer), membrane ZLD (RO + electrodialysis)
- CapEx: $5-15M for 10MW facility (varies by water chemistry)
- OpEx: $0.015-0.030/gallon (energy-intensive)
- Recommended when: municipal discharge permits are restricted, water cost >$10/kgal, public perception of water discharge is negative

### Air Quality

- Generator emissions: NOx, SOx, PM2.5, CO from diesel and natural gas combustion
- Air Quality Management District (AQMD) requirements by region
- Non-attainment area restrictions (stricter permitting in EPA-designated areas)
- Emission offsets may be required for new major sources
- Emergency vs continuous operation classification affects permit requirements

### Noise

- Source identification: cooling towers (60-80 dBA at 50ft), generators (85-105 dBA at 50ft), transformers (55-70 dBA at 50ft)
- Jurisdictional dB limits: residential boundaries typically 45-55 dBA nighttime, 55-65 dBA daytime
- Acoustic modeling required for permits in residential-adjacent sites
- Mitigation: sound walls, equipment selection, setback distance, operational restrictions

### Wildlife and Habitat

- Endangered Species Act (US) -- consultation with US Fish & Wildlife Service
- Migratory Bird Treaty Act -- timing restrictions on land clearing
- Wetland delineation and mitigation (Section 404, Army Corps of Engineers)
- Habitat conservation plans for listed species
- International: EU Habitats Directive, national equivalents

### Stormwater

- SWPPP (Stormwater Pollution Prevention Plan) required for construction >1 acre
- Impervious surface increase requires stormwater detention/retention design
- Post-construction stormwater management (bioretention, permeable surfaces)
- MS4 permit coordination with local stormwater authority

### Hazardous Materials

- Diesel fuel storage (generator day tanks and bulk storage): SPCC plan required above 1,320 gallons
- Battery chemistry (lithium-ion BESS): fire code and hazmat storage requirements
- Fire suppression chemicals (clean agent, halon alternatives)
- Transformer oil (PCB-free certification)

## LEED/BREEAM Certification Path

### LEED v4.1 Data Center Credits

| Category | Applicable Credits | DC Relevance | Low-Hanging Fruit? |
|----------|-------------------|-------------|-------------------|
| Energy & Atmosphere | Optimize Energy Performance (1-18 pts) | PUE optimization, efficient UPS, variable speed drives | Yes -- PUE < 1.4 typically earns significant points |
| Energy & Atmosphere | Renewable Energy (1-5 pts) | On-site solar, green power purchase, RECs | Yes if PPA exists |
| Water Efficiency | Outdoor Water Use Reduction (1-2 pts) | Xeriscaping, efficient irrigation | Yes -- easy points |
| Water Efficiency | Indoor Water Use Reduction (1-6 pts) | Low-flow fixtures in offices, cooling water efficiency | Moderate -- WUE metrics |
| Water Efficiency | Cooling Tower Water Use (1-2 pts) | Cycles of concentration optimization, alternative water sources | Yes for evaporative cooling |
| Materials & Resources | Building Life-Cycle Impact Reduction (1-5 pts) | Whole-building LCA, EPDs for materials | Moderate effort |
| Indoor Environmental Quality | Limited DC relevance | Offices/NOC only, not white space | Limited points available |
| Sustainable Sites | Site Assessment, Rainwater Management | Stormwater design, heat island reduction | Yes -- typically achievable |
| Innovation | DC-specific innovations | Waste heat reuse, WUE reporting | Case-by-case |

**Estimated certification timeline:** 12-18 months from registration to certification
**Estimated cost:** $150K-500K for certification fees, consulting, and documentation (varies by project size)

**Key LEED interpretation note:** LEED v4.1 data center credit interpretations differ from standard commercial buildings. PUE-based energy optimization credits require ASHRAE 90.4 (energy standard for data centers) baseline, not ASHRAE 90.1.

### BREEAM Data Center Assessment

BREEAM offers a bespoke assessment for data center facilities with credits weighted toward energy and water efficiency. Outstanding rating requires >85% score with innovation credits.

## Output

This skill produces two files:
1. `<project-name>-environmental-assessment.md` -- Environmental assessment report
2. `<project-name>-environmental-assessment.json` -- Structured data

### Environmental Assessment Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: predev-environmental v1.0]

#### 1. Executive Summary
- Overall environmental risk rating: [low / moderate / high / critical]
- Key environmental concerns: [list]
- Water rights status: [appropriation / riparian / permit-based]
- Certification path: [LEED level / BREEAM level / none]

#### 2. Water Rights Assessment
[Deep-dive on water doctrine, allocation, drought contingency, ZLD evaluation]

#### 3. Environmental Impact Categories
[Category-by-category assessment: air, noise, wildlife, stormwater, hazmat]

#### 4. Certification Path
[LEED/BREEAM credit analysis with estimated points and timeline]

#### 5. Mitigation Recommendations
[Prioritized mitigation measures by category and cost]

### JSON Sidecar

```json
{
  "artifact_type": "environmental-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "water_rights": {
    "type": "prior-appropriation | riparian | permit-based | rule-of-capture",
    "source": "municipal | well | reclaimed | surface",
    "annual_allocation_gallons": 0,
    "drought_contingency": "required | recommended | not-required",
    "zld_recommended": false
  },
  "eia_categories": [
    {
      "category": "air-quality | noise | wildlife | stormwater | hazmat | water",
      "risk_level": "low | moderate | high | critical",
      "mitigation": "...",
      "permit_required": true
    }
  ],
  "certification_path": {
    "target": "LEED-Gold | BREEAM-Excellent | none",
    "estimated_credits": 0,
    "timeline_months": 0,
    "estimated_cost": 0
  },
  "overall_risk_rating": "low | moderate | high | critical"
}
```

## Gotchas

- **Colorado River Compact states face increasingly strict water allocations.** Arizona, Nevada, and parts of California have experienced mandatory water cuts since 2022. A DC project relying on Colorado River water rights may face involuntary curtailment within its first decade of operation. Model drought scenarios explicitly and secure senior water rights or alternative supplies.

- **Some municipalities now require WUE < 1.2 for new data center permits.** Mesa, AZ and Chandler, AZ have imposed water efficiency requirements on DC developments. WUE < 1.2 effectively mandates air-cooled or hybrid cooling in hot climates -- a significant design constraint that increases energy consumption and PUE. Evaluate the trade-off between WUE and PUE early in design.

- **LEED v4.1 data center credit interpretations differ from standard commercial buildings.** The energy baseline uses ASHRAE 90.4 (data centers), not ASHRAE 90.1 (commercial). Many LEED consultants unfamiliar with DCs apply 90.1 baselines, which inflates energy credit estimates. Verify the consultancy has DC-specific LEED experience before engaging.

- **Zero-liquid-discharge (ZLD) systems consume 15-25 kWh per 1,000 gallons of water treated** -- adding 3-8% to total facility energy consumption. ZLD improves water footprint metrics but worsens energy/carbon metrics. In regions where carbon emissions are scrutinized as heavily as water use (California, EU), this trade-off must be explicitly modeled.

- **Migratory bird nesting season (March-August in most US regions) can halt land clearing for 5-6 months** if active nests of protected species are discovered. Conduct biological surveys and begin site clearing before nesting season to avoid this critical path delay.

## Evaluations

See `evals/evals.json` for test scenarios covering water-stressed Phoenix, Virginia LEED, and Nordic environmental assessment.
