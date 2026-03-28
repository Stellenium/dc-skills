---
name: bd-economic-impact
description: "Quantified economic impact analysis using input-output multiplier methodology calculating direct, indirect, and induced effects of a DC project. Use when quantifying economic benefits of a DC, preparing impact studies for government stakeholders, calculating job creation and tax revenue impact, or justifying a data center project. Trigger with \"economic impact\", \"job creation\", \"tax revenue impact\", \"multiplier analysis\", \"economic benefits\", or \"how many jobs will this DC create?\"."
---

# Economic Impact Analysis

Quantified economic impact analysis using methodology-agnostic input-output (I-O)
multiplier approach. Calculates direct, indirect, and induced impacts across jobs,
procurement spend, tax revenue, and GDP contribution. IMPLAN-style default multipliers
are provided; users can override any multiplier with project-specific or regional values.

This skill produces a presentation-ready economic impact report suitable for
government proposals, community engagement, and incentive negotiations.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the economic impact model.

**Project Context:**

1. What is the project location?
   - State and county (for US tax modeling)
   - Country (for international projects)
   - Metro area or rural designation

2. What is the total capital expenditure (CapEx)?
   - Construction phase total investment ($)
   - Equipment and IT infrastructure ($) (if included)
   - Phase breakdown if multi-phase

3. What is the estimated annual operating expenditure (OpEx)?
   - Annual operating cost at full occupancy ($)
   - Energy cost component ($)
   - Staffing cost component ($)

4. How many direct construction jobs (peak)?
   - Peak construction employment headcount
   - Average construction employment over project duration
   - Construction duration in months

5. How many direct permanent jobs?
   - Operations staff headcount at full capacity
   - Average annual salary for operations roles
   - Job categories (operations, security, maintenance, management)

6. What is the average wage for permanent positions?
   - Average annual salary ($)
   - Wage range (entry-level to management)
   - Benefits value (% of salary)

7. What is the construction timeline?
   - Total construction months
   - Phased deployment schedule (if applicable)

8. Are there specific multiplier values to use?
   - Use defaults (IMPLAN-style regional averages)
   - Provide custom multipliers (from IMPLAN, RIMS II, or custom study)
   - Adjust defaults for regional supply chain depth

## Phase 2: Context Refinement

> Based on project location and scale, refine the analysis.

### US Project Path

If project is in the **United States:**

1. What state incentives are being requested or received?
   - Sales tax exemption on equipment
   - Property tax abatement or PILOT
   - Income tax credits
   - Utility rate discount
   - Load reference: US-STATE-INCENTIVES.md for state-specific programs

2. Is the project in an Opportunity Zone?
3. What is the local property tax rate (mills)?
4. What is the assessed value methodology? (full market value, % of cost, income approach)

### International Project Path

If project is **International:**

1. What tax incentives are available? (tax holidays, free trade zones, investment incentives)
2. What is the local employment multiplier? (lower in emerging markets with shallow supply chains)
3. Is this project seeking DFI funding? (different multiplier expectations)
4. What is the local currency and exchange rate assumptions?

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location and site details
- Tax incentive preliminary assessment
- Workforce availability scoring
- Opportunity Zone eligibility

**From project-financial-model (fin-project-model):**
- Total CapEx and phasing
- Annual OpEx breakdown
- Revenue projections for tax modeling
- Staffing plan and wage assumptions

If upstream artifacts are not available, I will develop the economic
impact model from discovery question inputs.

## Reference Data

Load on demand -- do not read upfront:

- [US state incentives](../../references/US-STATE-INCENTIVES.md) -- State-specific tax incentive programs, thresholds, exemption values, and clawback provisions for WITH/WITHOUT incentive scenarios

## Economic Impact Methodology

### Input-Output Multiplier Approach

This skill uses methodology-agnostic I-O multipliers consistent with IMPLAN,
RIMS II, and similar regional economic models. Default multipliers are provided;
users can override any value.

### Default Multipliers

| Multiplier | Construction Phase | Operations Phase | Notes |
|------------|-------------------|------------------|-------|
| Type I -- Jobs | 1.8x | 1.5x | Direct + indirect jobs |
| Type I -- Output | 1.6x | 1.4x | Direct + indirect economic output |
| Type II -- Jobs | 2.4x | 2.0x | Direct + indirect + induced jobs |
| Type II -- Output | 2.1x | 1.8x | Direct + indirect + induced output |

**Regional adjustment guidance:**
- Mature DC ecosystems (Northern Virginia, Dallas): Use default or slightly higher multipliers
- Rural locations with limited supply chain: Reduce multipliers by 20-30%
- International emerging markets: Reduce multipliers by 30-50% (shallow local supply chains)

### Impact Categories

**1. Direct Impacts**
- Construction jobs (temporary, duration of build)
- Permanent operations jobs (ongoing)
- Direct CapEx spend in the local economy
- Direct annual OpEx
- Direct tax payments: property tax, sales tax on equipment and materials, income tax from direct employees

**2. Indirect Impacts (Type I)**
- Supply chain jobs created by procurement spending
- Indirect economic output from supplier purchases
- Tax revenue from indirect employment
- Apply Type I multiplier: indirect = direct * (Type I multiplier - 1.0)

**3. Induced Impacts (Type II)**
- Consumer spending from wages of direct and indirect workers
- Additional jobs from consumer spending (retail, services, housing)
- Tax revenue from induced employment and spending
- Apply Type II multiplier: induced = direct * (Type II multiplier - Type I multiplier)

### Tax Revenue Modeling

**Property Tax:**
- Assessed value based on project CapEx (varies by jurisdiction: full market, % of cost, income approach)
- Annual property tax = assessed value * local mill rate
- Model WITH incentives (abated/PILOT rate) and WITHOUT incentives (full rate)
- Net incentive cost = WITHOUT - WITH (what the government foregoes)

**Sales Tax:**
- Equipment and material purchases subject to state/local sales tax
- Many states exempt DC equipment purchases (reference US-STATE-INCENTIVES.md)
- Model WITH exemption and WITHOUT exemption

**Income Tax:**
- State and local income tax from direct + indirect + induced wages
- Federal income tax contribution (for federal proposals)

**Utility Tax:**
- Gross receipts tax on electricity consumption (varies by jurisdiction)
- Typically 2-5% of electricity cost

### GDP Contribution

- **Total economic output** = direct + indirect + induced spending
- **GDP contribution** = total output * GDP-to-output ratio
  - Construction phase: 0.55 ratio (high material/equipment import content reduces local GDP capture)
  - Operations phase: 0.65 ratio (higher local service content in ongoing operations)

### Community Benefits

Beyond quantifiable economic metrics, document qualitative community benefits:
- Digital infrastructure access and broadband improvements
- Workforce training programs (STEM education, trade apprenticeships)
- Local hiring commitments (% of construction and permanent workforce)
- Infrastructure improvements funded by the developer (roads, utilities, water/sewer)
- Sustainability commitments (renewable energy, water recycling, heat reuse)

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-economic-impact-report.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: bd-economic-impact v1.0]

#### 1. Executive Summary
- Total economic impact headline figures (jobs, investment, tax revenue)
- Key finding: jobs per incentive dollar (most politically effective metric)
- Multiplier methodology summary

#### 2. Construction Phase Impacts

| Impact Category | Jobs | Economic Output | Tax Revenue |
|-----------------|------|-----------------|-------------|
| Direct | [count] | $[amount] | $[amount] |
| Indirect | [count] | $[amount] | $[amount] |
| Induced | [count] | $[amount] | $[amount] |
| **Total** | **[count]** | **$[amount]** | **$[amount]** |

#### 3. Operations Phase Impacts (Annual)

| Impact Category | Jobs | Economic Output | Tax Revenue |
|-----------------|------|-----------------|-------------|
| Direct | [count] | $[amount] | $[amount] |
| Indirect | [count] | $[amount] | $[amount] |
| Induced | [count] | $[amount] | $[amount] |
| **Total** | **[count]** | **$[amount]** | **$[amount]** |

#### 4. Tax Revenue Analysis

| Tax Type | Annual (No Incentives) | Annual (With Incentives) | Net Incentive Cost |
|----------|------------------------|--------------------------|---------------------|
| Property tax | $[amount] | $[amount] | $[amount] |
| Sales tax | $[amount] | $[amount] | $[amount] |
| Income tax | $[amount] | $[amount] | $[amount] |
| Utility tax | $[amount] | $[amount] | $[amount] |
| **Total** | **$[amount]** | **$[amount]** | **$[amount]** |

#### 5. GDP Contribution
- Construction phase total GDP contribution
- Annual operations GDP contribution

#### 6. Community Benefits
- Local hiring commitments and workforce development
- Infrastructure improvements
- Sustainability commitments

#### 7. Multiplier Assumptions
- Table of all multipliers used with source/justification
- Sensitivity analysis at +/- 20% multiplier variation

### JSON Sidecar: `<project-name>-economic-impact-report.json`

```json
{
  "artifact_type": "economic-impact-report",
  "skill_version": "1.0",
  "project_name": "...",
  "impacts": {
    "construction": {
      "direct": {"jobs": 0, "spend": 0, "tax": 0},
      "indirect": {"jobs": 0, "spend": 0, "tax": 0},
      "induced": {"jobs": 0, "spend": 0, "tax": 0},
      "total": {"jobs": 0, "spend": 0, "tax": 0}
    },
    "operations": {
      "direct": {"jobs": 0, "spend": 0, "tax": 0},
      "indirect": {"jobs": 0, "spend": 0, "tax": 0},
      "induced": {"jobs": 0, "spend": 0, "tax": 0},
      "total": {"jobs": 0, "spend": 0, "tax": 0}
    }
  },
  "multipliers_used": {
    "type_1_jobs": {"construction": 1.8, "operations": 1.5},
    "type_1_output": {"construction": 1.6, "operations": 1.4},
    "type_2_jobs": {"construction": 2.4, "operations": 2.0},
    "type_2_output": {"construction": 2.1, "operations": 1.8}
  },
  "tax_revenue": {
    "annual": {
      "property": 0,
      "sales": 0,
      "income": 0,
      "utility": 0,
      "total": 0
    },
    "with_incentives": 0,
    "without_incentives": 0,
    "net_incentive_cost": 0
  },
  "gdp_contribution": {
    "construction_total": 0,
    "annual_operations": 0
  },
  "community_benefits": []
}
```

## Gotchas

- **I-O multipliers vary dramatically by region.** A data center in rural Nevada has a ~1.3x employment multiplier (limited local supply chain) vs ~2.0x in Northern Virginia (deep DC supply chain ecosystem). Using a national average multiplier for a rural project will overstate impact by 40-50%. Always adjust multipliers for regional supply chain depth.

- **Governments routinely discount economic impact studies that show >3x total multipliers as unrealistic.** An induced multiplier above 3.0x signals that the analysis is inflated. If your model produces >3x total impact, reduce multipliers or provide detailed justification for the high values. Credibility matters more than headline numbers.

- **The most politically effective metric is "jobs per incentive dollar," not total jobs.** A project creating 50 jobs with $5M in incentives ($100K per job) is a stronger political argument than 200 jobs with $100M in incentives ($500K per job). Normalize all job metrics by incentive cost for government audiences.

- **Property tax revenue is often the most compelling metric for municipal governments.** Cities care about property tax base growth more than temporary construction jobs. Show annual property tax revenue WITH and WITHOUT incentives, and calculate the breakeven point where cumulative tax revenue exceeds the incentive cost.

- **Construction jobs are temporary and should be stated clearly.** Listing "2,000 construction jobs" without noting they are temporary (18-24 months) and then adding them to "total jobs created" is misleading and will undermine credibility with sophisticated government reviewers. Always separate temporary construction employment from permanent operations jobs.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale Virginia, rural Southeast, and international DFI-funded projects.
