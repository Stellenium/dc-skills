---
name: predev-market-study
description: "Analyze data center market supply and demand for a target geography with inventory, absorption rates, pricing, and competitive landscape. Use when evaluating DC market conditions, sizing demand in a region, preparing market justification for investors, or answering \"is there demand for a data center here?\". Trigger with \"data center market study\", \"DC market analysis\", \"demand for data centers in [region]\", \"market supply and demand\", or \"competitive landscape\"."
argument-hint: "<target-geography>"
---

# Data Center Market Study

Analyze data center market supply, demand, absorption, pricing, and anchor tenant
opportunities for a target geography. Consumes upstream site feasibility report for
location context and cost benchmarks. Produces a market study consumed by project
narrative and financial modeling skills.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New market entry or expansion -- proceed to Greenfield Path below
   - **Brownfield:** Conversion of existing facility in established market -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the target geography?
   - Country, state/region, and specific metro area
   - For multi-market analysis, list all candidate metros

4. What is the planned capacity range (MW)?
   - Phase 1 capacity and ultimate build-out capacity

5. What is the primary workload type?
   - Cloud compute (general purpose)
   - AI training / HPC (high density)
   - AI inference (moderate density)
   - Enterprise IT (standard density)
   - Mixed / colocation (multiple tenant workloads)

6. Do you have awareness of existing supply in the target market?
   - Yes -- provide known inventory, operators, or vacancy data
   - No -- full market inventory needed

7. What is the anchor tenant status?
   - Pre-committed anchor tenant (specify capacity)
   - Active discussions with potential anchors
   - No anchor tenant identified yet
   - Self-use (hyperscale / enterprise campus)

8. What is the competitive landscape awareness?
   - Known competitors and their pipeline
   - General awareness only
   - No knowledge of competition

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. Is this a primary, secondary, or emerging market?
2. What is driving demand growth in this geography? (cloud expansion, AI buildout, enterprise migration, sovereignty mandates)
3. Are there known land or power constraints limiting new supply?
4. What is the target delivery timeline (months from decision to COD)?

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. What is the current market occupancy rate?
2. Are there competing brownfield conversion projects in the pipeline?
3. What power capacity is available at the existing site vs. market demand?
4. Is there existing tenant demand for the converted facility?

### Facility Type Refinements

**Colocation additions:**
- Retail vs wholesale colo target mix?
- Target number of tenants and average deal size?
- Carrier-neutral or carrier-specific strategy?

**Hyperscale additions:**
- Single cloud tenant or multi-hyperscale campus?
- Land pipeline for future phases beyond initial capacity?
- Custom build-to-suit or speculative shell?

**Sovereign additions:**
- Government procurement vehicle (direct contract, GSA, state contract)?
- Security clearance requirements impacting market size?
- Mandatory in-country data residency driving demand?

## What I Need from Upstream

**site-feasibility-report** (from predev-site-feasibility):
- Location and geographic context
- Power availability and cost (for supply constraint analysis)
- Tax incentive data (affects competitive positioning)
- Connectivity assessment (affects market attractiveness)

**Fallback:** If no upstream artifact is available, gather location, power, and cost
context directly from the user during Phase 1 discovery.

## Analysis & Output

### Process

1. **Market Inventory:** Identify existing data center supply (total MW operational, under construction, planned) from public filings, broker reports, and operator announcements
2. **Absorption Analysis:** Calculate quarterly take-up rates (MW leased per quarter), trailing 12-month absorption, and vacancy trends
3. **Demand Driver Assessment:** Evaluate demand drivers -- cloud growth, AI training pipeline, enterprise migration, sovereignty mandates, content delivery, financial services
4. **Gap Analysis:** Compare supply pipeline (existing + under construction + planned) vs demand forecast (absorption rate x growth multiplier) over 3-5 year horizon
5. **Pricing Analysis:** Document current pricing by product type ($/kW/month for wholesale, $/kW/month for retail, $/sqft for cage/cabinet) with trends
6. **Anchor Tenant Identification:** Profile potential anchor tenants based on market presence, expansion patterns, and publicly announced capacity needs
7. **Risk Assessment:** Identify market risks -- overbuilding, utility constraints, regulatory changes, competitive entry, economic cycle sensitivity

### Reference Data

Load these files on demand -- do not read upfront:

- [Construction cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional $/MW for development cost context
- [Industrial power tariffs](../../references/POWER-TARIFFS.md) -- Regional power costs affecting market attractiveness

### Quality Check

1. Verify inventory figures reconcile (total = existing + under construction + planned)
2. Confirm absorption rate calculation methodology is consistent
3. Cross-check pricing against COST-BENCHMARKS.md regional data for plausibility
4. Validate demand projections against at least 2 independent growth estimates
5. Ensure anchor tenant analysis reflects actual publicly announced capacity needs, not speculation

## Output Template

This skill produces two files:
1. `<project-name>-market-study.md` -- Full market study report
2. `<project-name>-market-study.json` -- Structured data for downstream skills

### Markdown Report Structure

**Project:** [Project Name]
**Market:** [Target Metro / Region]
**Date:** [Date]
**Prepared by:** [Skill: predev-market-study v1.0]

#### 1. Executive Summary
- **Market Rating:** Strong / Moderate / Weak / Emerging
- **Supply-Demand Balance:** Undersupplied / Balanced / Oversupplied
- **Recommended Entry Strategy:** [brief recommendation]
- **Key Opportunity:** [primary market opportunity]
- **Key Risk:** [primary market risk]

#### 2. Market Inventory

| Category | Capacity (MW) | Facilities | Key Operators |
|----------|--------------|-----------|---------------|
| Operational | [MW] | [count] | [operators] |
| Under Construction | [MW] | [count] | [operators] |
| Planned/Announced | [MW] | [count] | [operators] |
| **Total Pipeline** | **[MW]** | **[count]** | |

#### 3. Demand Analysis
- **Trailing 12-Month Absorption:** [MW]
- **Quarterly Absorption Rate:** [MW/quarter]
- **Primary Demand Drivers:** [ranked list]
- **Demand Forecast (3-year):** [MW with confidence range]

#### 4. Gap Analysis
- **Current Vacancy:** [%]
- **Projected Supply Gap/Surplus:** [MW over 3-5 years]
- **Market Entry Window:** [timing recommendation]

#### 5. Pricing Analysis

| Product Type | Current Rate | 12-Month Trend | Market Comparison |
|-------------|-------------|---------------|-------------------|
| Wholesale ($/kW/mo) | [rate] | [trend] | [vs. comparable markets] |
| Retail ($/kW/mo) | [rate] | [trend] | [vs. comparable markets] |
| Powered Shell ($/sqft/yr) | [rate] | [trend] | [vs. comparable markets] |

#### 6. Anchor Tenant Opportunities

| Potential Anchor | Estimated Need (MW) | Likelihood | Evidence |
|-----------------|--------------------|-----------:|----------|
| [tenant] | [MW] | High/Med/Low | [public data] |

#### 7. Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [risk] | High/Med/Low | High/Med/Low | [strategy] |

### JSON Sidecar Schema

```json
{
  "artifact_type": "market-study",
  "skill_version": "1.0",
  "project_name": "...",
  "target_market": "...",
  "market_rating": "strong | moderate | weak | emerging",
  "supply_demand_balance": "undersupplied | balanced | oversupplied",
  "inventory": {
    "operational_mw": 0,
    "under_construction_mw": 0,
    "planned_mw": 0,
    "total_pipeline_mw": 0
  },
  "absorption": {
    "trailing_12mo_mw": 0,
    "quarterly_rate_mw": 0,
    "vacancy_pct": 0
  },
  "pricing": {
    "wholesale_per_kw_month": 0,
    "retail_per_kw_month": 0,
    "trend": "rising | stable | declining"
  },
  "gap_analysis": {
    "projected_gap_mw": 0,
    "forecast_horizon_years": 3,
    "confidence_range": { "low": 0, "high": 0 }
  },
  "demand_drivers": [],
  "anchor_tenants": [],
  "risk_factors": []
}
```

## Gotchas

- **Pre-leasing absorbs 60-80% of planned supply before COD.** A market showing 500MW "planned" may already have 300-400MW pre-leased. Always check absorption velocity and pre-lease rates, not just total pipeline -- the "available" pipeline is far smaller than announced pipeline.

- **Hyperscale land banking distorts market signals.** Cloud providers acquire land and power positions 3-5 years ahead of buildout. A market with 500MW of "planned" hyperscale may not see that capacity come online for years. Distinguish between land-banked positions and active construction.

- **Wholesale pricing floors exist.** Below ~$120/kW/month in most US primary markets, development economics turn negative. If market pricing is below the development cost floor, new supply will stall regardless of demand -- an opportunity signal for contrarian entry with locked-in tenants.

- **AI demand is geographically concentrated.** Unlike cloud compute (follows population), AI training demand follows cheap power and fiber connectivity. A market with expensive power will not attract AI training regardless of other factors. Northern Virginia, Texas, and the Nordics dominate for a reason.

- **Municipal utility markets have hidden capacity.** Some of the best supply-demand dynamics exist in secondary markets with municipal utilities offering favorable rates and streamlined interconnection -- but these markets are invisible in broker reports that focus on primary markets.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale primary market,
emerging African market, and enterprise colo in secondary US market.
