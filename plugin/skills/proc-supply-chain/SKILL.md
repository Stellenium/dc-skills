---
name: proc-supply-chain
description: "Assess data center supply chain risks with lead time modeling, vendor diversification scoring, and mitigation strategies for critical equipment. Use when evaluating supply chain risk for DC equipment, planning procurement timelines, assessing vendor concentration, or building mitigation plans for long-lead items. Trigger with \"supply chain\", \"lead times\", \"vendor diversification\", \"procurement risk\", \"long-lead items\", \"supply chain risk\", or \"equipment delivery timeline\"."
---

# Supply Chain Risk Assessment

Assess supply chain risks for data center equipment procurement. Covers lead
time analysis, single-source dependency identification, geopolitical risk
factors, and alternative supplier strategies. Produces a risk matrix with
mitigation recommendations and a total procurement timeline estimate.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the supply chain assessment scope.

**Procurement Context:**

1. Which equipment categories need assessment? Select all that apply:
   - **Power:** Transformers, switchgear, UPS, generators, ATS, PDUs
   - **Cooling:** Chillers, CRAH/CRAC, CDUs (liquid cooling), cooling towers, dry coolers
   - **IT infrastructure:** Racks/cabinets, structured cabling, raised floor, fire suppression
   - **Structural:** Steel, concrete, building envelope components
   - **Controls:** BMS, DCIM, environmental sensors, power metering

2. What is the project location?
   - Country and state/region
   - Is this a single site or multi-site deployment?

3. What is the target delivery date?
   - Equipment needed on site by when?
   - What is the construction start date?

4. Are there preferred suppliers or existing contracts?
   - Named vendor preferences
   - Master purchase agreements in place
   - Incumbent vendor relationships

5. What is the budget flexibility for expediting?
   - Fixed budget, cannot expedite
   - 10-20% premium acceptable for critical items
   - Schedule is paramount, budget is flexible

6. Are there domestic content or sourcing requirements?
   - **Buy American** (US government-funded projects)
   - **EU content requirements** (European public procurement)
   - **Local content** (developing country requirements)
   - **No sourcing restrictions**

7. What is the total project capacity (MW)?
   - Determines equipment quantities and bulk purchasing leverage

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Power Equipment Path

If power equipment is selected:

1. What transformer voltage and configuration? (13.8kV, 34.5kV, 69kV; oil-filled, dry-type)
2. How many transformers? (single unit vs fleet purchase affects lead time negotiation)
3. UPS topology? (static double-conversion, rotary, lithium vs VRLA)
4. Generator fuel type and emissions requirements? (diesel, natural gas, bi-fuel; Tier 4 emissions)

### Cooling Equipment Path

If cooling equipment is selected:

1. Cooling technology? (air-cooled chillers, water-cooled, adiabatic, DLC, immersion)
2. Custom vs standard configurations? (custom = longer lead, higher single-source risk)
3. Refrigerant requirements? (R-134a, R-1234ze, R-290 propane -- regulatory driven)

### Multi-Site Path

If multi-site deployment:

1. How many sites? What is the deployment sequence?
2. Are all sites in the same country/region?
3. Can equipment be standardized across sites?
4. Is there a central staging/warehouse location?

## What I Need from Upstream

**From equipment-spec-package (proc-equipment-spec):**
- Equipment list with quantities and specifications
- Performance requirements per category
- Compliance requirements (UL, CE, seismic)
- Preferred vendor list (if any)

If upstream artifact is not available, I will develop the equipment list
from discovery questions and standard DC equipment configurations.

## Lead Time Database

Current lead time estimates for major DC equipment categories. Lead times
reflect order-to-delivery for standard configurations from Tier 1 manufacturers.

| Equipment | Lead Time (weeks) | Trend | Single-Source Risk | Key Manufacturers |
|-----------|--------------------|-------|--------------------|--------------------|
| Utility transformers (>10MVA) | 52-78 | Stable (post-2024 peak) | High (3-4 global) | ABB/Hitachi, Siemens, GE Vernova, Hyundai |
| Medium-voltage switchgear | 26-40 | Improving | Medium (5-6 global) | Eaton, Schneider, ABB, Siemens, LS Electric |
| Diesel generators (>2MW) | 26-52 | Stable | Medium (4-5 global) | Caterpillar, Cummins, MTU/Rolls-Royce, Kohler |
| UPS systems (>500kVA) | 16-26 | Improving | Low (6+ manufacturers) | Vertiv, Schneider, Eaton, ABB, Huawei, Toshiba |
| Chillers (>500 ton) | 20-36 | Stable | Medium (4-5 global) | Trane, Carrier, York/JCI, Daikin, Mitsubishi |
| CRAH/CRAC units | 12-20 | Improving | Low (5+ manufacturers) | Vertiv, Schneider, Stulz, Rittal, Munters |
| PDUs/RPPs | 12-16 | Stable | Low (many suppliers) | Vertiv, Schneider, Eaton, Raritan, ServerTech |
| Fire suppression (clean agent) | 8-16 | Stable | Medium (limited agents) | Kidde/Carrier, Fike, Tyco/JCI, Novec/3M |
| Racks/cabinets | 6-12 | Stable | Low (many suppliers) | Vertiv, Rittal, CPI, Panduit, APC/Schneider |
| Structured cabling | 4-8 | Stable | Low (many suppliers) | Corning, CommScope, Panduit, Belden, Leviton |
| Raised floor | 8-12 | Stable | Low (many suppliers) | Tate, Kingspan, ASM, Haworth |

**Note:** GPU/server lead times are excluded. IT procurement is tenant responsibility
in most DC development models. This assessment covers facility infrastructure only.

## Risk Assessment Framework

### Single-Source Risk Identification

**Critical single-source risks in DC procurement:**
- **Utility transformers:** 3-4 major manufacturers globally. Custom windings (non-standard voltage) reduce options further. Lead times exceeded 100 weeks in 2023-2024.
- **Medium-voltage switchgear (2N+1):** Limited manufacturers for specialized DC configurations with integrated ATS and monitoring.
- **DLC manifolds/CDUs:** Emerging technology with limited mature suppliers (CoolIT, Vertiv, ZutaCore). Custom manifold designs are effectively single-source.
- **Clean agent fire suppression:** Novec 1230 (3M) production discontinued; transitioning to alternatives. FM-200 supply constrained by HFC phase-down regulations.

### Geopolitical Risk Factors

| Factor | Affected Equipment | Probability | Impact | Mitigation |
|--------|-------------------|-------------|--------|------------|
| US Section 301 tariffs on China | Electrical equipment, transformers, steel | High | 25% cost increase | Qualify non-China alternatives; request USTR exclusion |
| Rare earth supply (China dominance) | Transformer cores, permanent magnets, generators | Medium | Supply disruption | Strategic stockpiling; monitor USGS critical minerals list |
| Semiconductor shortage (cyclical) | UPS controllers, BMS, DCIM sensors | Medium | 12-26 week delay | Design with multi-source chipsets; carry spare controller boards |
| HFC phase-down (Kigali Amendment) | Refrigerants (R-134a), fire suppression (FM-200) | High | Forced technology transition | Specify low-GWP refrigerants; use Novec alternatives or water mist |
| Steel/aluminum tariffs (Section 232) | Structural steel, racks, enclosures | Medium | 10-25% cost increase | Domestic sourcing; factor tariffs into project budget |
| Shipping disruptions (Red Sea, Panama) | All imported equipment | Medium | 2-6 week delay | Route alternatives; FOB vs CIF risk allocation in contracts |

### Alternative Supplier Strategy

1. **Qualification timeline:** Allow 8-16 weeks for second-source qualification (factory audit, sample testing, reference verification)
2. **Dual-award strategy:** Split large orders (e.g., transformers) between two manufacturers to reduce single-source risk
3. **Regional sourcing:** Maintain qualified suppliers in Americas, EMEA, and APAC to mitigate regional disruptions
4. **Government set-asides:** Buy American requirements may eliminate 60%+ of transformer options -- qualify domestic alternatives early

### Mitigation Recommendations

- **Advance purchase agreements:** Lock in transformer and generator slots 18-24 months before needed
- **Strategic stockpiling:** Pre-purchase standardized transformers and generators for campus deployments
- **Modular/standardized designs:** Maximize design standardization for supplier flexibility and bulk pricing
- **Buffer time:** Add 10-15% schedule buffer for long-lead items in construction schedule
- **Vendor-managed inventory:** Negotiate VMI for high-consumption items (cabling, racks, PDUs)

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-supply-chain-assessment.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: proc-supply-chain v1.0]

#### 1. Executive Summary
- Critical path items identified
- Total procurement timeline
- Top 3 supply chain risks with mitigation actions

#### 2. Equipment Lead Time Analysis
- Lead time table by category with current market conditions
- Long-lead items flagged with procurement milestones

#### 3. Single-Source Risk Assessment
- Risk matrix with probability and impact scoring
- Alternative supplier identification for high-risk items

#### 4. Geopolitical Risk Analysis
- Tariff and trade policy impact on equipment sourcing
- Country-of-origin analysis for key components
- Regulatory transition risks (refrigerants, emissions)

#### 5. Mitigation Strategy
- Advance purchase recommendations with timelines
- Dual-source qualification plan
- Strategic inventory recommendations
- Schedule buffer recommendations

#### 6. Procurement Timeline
- Gantt-style timeline from order placement to site delivery
- Critical path identification
- Milestone dates for procurement decisions

### JSON Sidecar: `<project-name>-supply-chain-assessment.json`

```json
{
  "artifact_type": "supply-chain-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "equipment_categories": [
    {
      "category": "Utility transformers",
      "lead_time_weeks_range": [52, 78],
      "single_source_risk": "high",
      "suppliers_count": 4,
      "geopolitical_risk_level": "medium"
    }
  ],
  "critical_path_items": [
    {
      "item": "Utility transformer 34.5kV/13.8kV 40MVA",
      "risk_score": 9,
      "mitigation": "Advance purchase agreement 18 months before NTP"
    }
  ],
  "geopolitical_risks": [
    {
      "factor": "Section 301 tariffs",
      "affected_items": ["switchgear", "steel components"],
      "probability": "high",
      "impact": "25% cost increase"
    }
  ],
  "alternative_strategies": [
    "Dual-award transformer procurement across two manufacturers",
    "Regional sourcing strategy with Americas and EMEA qualified suppliers"
  ],
  "total_procurement_timeline_weeks": 78
}
```

## Gotchas

- **Utility-grade transformer lead times exceeded 100 weeks in 2023-2024 and remain at 52-78 weeks.** This is the #1 DC supply chain constraint globally. Transformer procurement must begin at project inception, not after design completion. A 78-week lead time means ordering 18 months before the transformer is needed on site.

- **"Buy American" requirements for government-funded projects eliminate 60%+ of transformer options.** Only 2-3 domestic transformer manufacturers exist with capacity for utility-grade units. Government-funded projects (DOE grants, CHIPS Act, DFC financing) must plan for domestic sourcing constraints early.

- **Modular DC providers often pre-purchase transformer capacity 2-3 years ahead.** Their apparent lead time advantage over traditional procurement is not faster manufacturing -- it is earlier commitment. Traditional developers can achieve similar results by placing advance orders, but this requires capital commitment before design is finalized.

- **Clean agent fire suppression is in technology transition.** 3M discontinued Novec 1230 production. FM-200 faces HFC phase-down under the Kigali Amendment. New installations should specify Novec 1230 alternatives or water mist systems. Existing stockpiles of Novec 1230 remain available but pricing is volatile.

- **Semiconductor content in UPS and BMS systems creates hidden supply chain risk.** A UPS is not just a power system -- its controller board depends on semiconductor supply chains. During the 2021-2023 chip shortage, UPS lead times doubled to 52+ weeks. Carry spare controller boards for critical UPS units.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale procurement, sovereign domestic content, and multi-site fleet deployment.
