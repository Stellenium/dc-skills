---
name: fin-deal-structure
description: "Structure data center investment deals with SPV design, tax optimization stacking (Opportunity Zones, ITC, bonus depreciation), and waterfall modeling. Use when structuring a DC investment, designing SPV/holding entities, modeling promote and waterfall structures, or stacking tax incentives for a data center deal. Trigger with \"deal structure\", \"SPV\", \"tax optimization\", \"waterfall\", \"promote structure\", \"Opportunity Zone\", or \"how to structure a DC deal\"."
---

# Deal Structure & Tax Optimization

Structure data center investment deals with SPV/holding entity design,
tax optimization stacking (OZ, ITC, cost segregation, MACRS, 179D),
multi-entity waterfall distribution, and exit scenario modeling.
Consumes the upstream financial model for revenue and cost projections.

**This skill produces estimates for planning purposes only. Not investment advice.**
See Disclaimer section for full terms.

## What I Need from Upstream

**From financial-model (fin-project-model):**
- Revenue projections with occupancy ramp
- Cost structure and EBITDA waterfall
- Total CapEx breakdown (land, building, M&E, IT)
- Annual NOI and free cash flow projections
- Tax jurisdiction and incentive eligibility

If upstream data is not available, I will ask you for key values or generate
simplified assumptions based on facility type and capacity.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire deal structure.

**Project Context:**

1. What is the project type and scale?
   - Greenfield development (new construction)
   - Acquisition of operating facility
   - Recapitalization of existing investment
   - Portfolio aggregation (multiple assets)

2. What are the target investor returns?
   - IRR target (levered equity): [8-25% range typical]
   - MOIC target: [1.5-3.5x range typical]
   - Cash-on-cash yield preference: [6-12%]

3. Who are the investor types?
   - LP/GP structure (institutional PE/infra fund)
   - Co-investment (GP + direct LP co-invest)
   - Joint venture (developer + capital partner)
   - DFI/sovereign (development finance institution)
   - Single-entity (corporate balance sheet)

4. Is the site Opportunity Zone eligible?
   - Yes (designated OZ census tract)
   - No / Unknown
   - If yes: new construction or substantial improvement?

5. What state incentives apply?
   - Sales tax exemptions on equipment
   - Property tax abatement or PILOT
   - Job creation credits
   - Utility rate incentives
   - None identified

6. What is the investor tax appetite?
   - High (can absorb all tax benefits directly)
   - Moderate (some tax capacity, may need tax equity)
   - Low (requires tax credit transfer or tax equity partner)
   - Tax-exempt (pension, endowment -- no direct tax benefit)

7. What is the exit timeline?
   - 3-5 years (value-add/development)
   - 5-7 years (core-plus)
   - 7-10 years (core infrastructure)
   - 10+ years (long-hold / perpetual)

8. Entity jurisdiction preference?
   - Delaware LLC (most common US)
   - Cayman/BVI (international investors)
   - Luxembourg (European investors)
   - No preference / advise

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Tax Position Refinements

1. Has a cost segregation study been completed or budgeted?
2. Are there specific ITC-eligible assets (on-site solar, BESS, fuel cells)?
3. What is the estimated ITC qualifying cost?
4. Is the project located in an energy community (ITC bonus)?
5. Does the project meet prevailing wage + apprenticeship requirements?
6. Any existing tax loss carryforwards from prior investments?

### Investor Structure Refinements

**LP/GP structure:**
1. Number of LPs and minimum commitment size?
2. Preferred return rate? (typically 8-10% for DC)
3. GP catch-up provision? (50/50 until GP at carried interest share)
4. Carried interest percentage? (typically 20-30%)
5. Clawback provision required?

**JV structure:**
1. Developer contribution (cash, land, entitlements)?
2. Capital partner contribution and governance rights?
3. Decision-making thresholds (major decisions list)?
4. Buy-sell provisions?

**DFI/sovereign:**
1. DFI concessionality requirements?
2. Local content or employment conditions?
3. Reporting and ESG requirements?
4. Currency and repatriation restrictions?

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical entity | LLC | LLC/LP | Gov entity | REIT/LLC | LLC | LLC |
| Tax optimization | Full stack | Full stack | Limited | Full + REIT | Moderate | Limited |
| OZ applicability | High | High | Low | High | Moderate | Low |
| Exit mechanism | Sale | Sale/IPO | N/A | REIT/Sale | Sale | Portfolio sale |
| Typical hold | 5-7yr | 7-10yr | Perpetual | 5-10yr | 3-5yr | 3-5yr |

## Analysis & Output

### Process

1. **Design SPV entity structure:** LLC vs LP vs C-corp, single vs multi-entity, tax-transparent vs opaque, jurisdiction selection
2. **Stack tax optimization:** Evaluate and combine OZ benefits (10% exclusion at 5yr, step-up at 10yr, post-OBBBA rolling deferral), ITC (30% with prevailing wage on solar/BESS), cost segregation (reclassify 40-60% of construction cost from 39yr to 5-15yr), MACRS with 100% bonus depreciation, Section 179D ($5.36/sqft max, sunset June 30 2026)
3. **Model exit scenarios:** Sale (apply capital gains rates), recapitalization (refinancing proceeds distribution), REIT conversion (tax-efficient for portfolio), IPO (public market valuation)
4. **Calculate waterfall distribution:** 4-tier structure -- return of capital, preferred return (8-10% IRR hurdle), GP catch-up (50/50 until GP at carried share), carried interest (20-30% GP carry above hurdle)
5. **Run sensitivity analysis:** IRR sensitivity to tax benefit reduction, exit cap rate, occupancy, hold period

### Reference Data

Load these files on demand -- do not read upfront:

- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC, OZ, MACRS, Section 179D, cost segregation, bonus depreciation, tax equity structures
- [US state incentives](../../references/US-STATE-INCENTIVES.md) -- State-level tax benefits, sales tax exemptions, PILOT programs
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required financial and tax disclaimer language

### Validation Loop

1. Compute deal structure from inputs and tax assumptions
2. Cross-check OZ eligibility against census tract designation
3. Validate ITC qualifying cost against actual solar/BESS/fuel cell CapEx
4. Verify cost segregation percentages against IRS Cost Segregation ATG benchmarks
5. Check Section 179D eligibility (construction begun before June 30 2026)
6. Validate waterfall math: LP + GP distributions = total distributable cash
7. Verify exit scenario tax treatment against entity structure
8. If any constraint violated: flag and adjust assumptions
9. Recompute until all validations pass

## Output

This skill produces two files:
1. `<project-name>-deal-structure.md` -- Full report
2. `<project-name>-deal-structure.json` -- Structured data for downstream skills

### Deal Structure Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: fin-deal-structure v1.0]

#### 1. Executive Summary
- Entity: [SPV type] in [jurisdiction]
- Total project cost: [$X M]
- Tax benefit stack: [summary of OZ + ITC + cost seg + MACRS + 179D]
- Waterfall: [pref return %] / [carry %] GP/LP
- Exit strategy: [primary exit] at Year [N]

#### 2. Entity Structure
```
[Text-based entity structure diagram]
Holding Co (Delaware LLC)
  |-- SPV 1 (Project LLC)
  |     |-- Data Center Asset
  |     |-- On-site Solar/BESS (ITC entity)
  |-- QOF Entity (if OZ-eligible)
```

#### 3. Tax Benefit Summary
| Benefit | Value | Eligible | Timing | Notes |
|---------|-------|----------|--------|-------|
| OZ deferral | [$X M] | [Y/N] | 5yr/10yr | [details] |
| ITC | [$X M] | [Y/N] | Year 1 | [qualifying assets] |
| Cost segregation | [$X M] | [Y/N] | Year 1 | [% reclassified] |
| MACRS + bonus | [$X M] | [Y/N] | Year 1 | [100% bonus] |
| Section 179D | [$X M] | [Y/N] | Year 1 | [$X/sqft] |
| State incentives | [$X M] | [Y/N] | Varies | [specific programs] |
| **Total tax savings** | **[$X M]** | | | |

#### 4. Waterfall Distribution
| Tier | Description | LP Share | GP Share | Cumulative |
|------|-------------|----------|---------|-----------|
| 1 | Return of capital | 100% | 0% | [$X M] |
| 2 | Preferred return ([X%]) | 100% | 0% | [$X M] |
| 3 | GP catch-up | 0% | 100% | [$X M] |
| 4 | Carried interest | [X%] | [X%] | [$X M] |

#### 5. Exit Scenario Comparison
| Scenario | Gross Proceeds | Tax Treatment | Net to Equity | Equity IRR |
|----------|---------------|---------------|--------------|-----------|
| Sale at Year [N] | [$X M] | [cap gains] | [$X M] | [X%] |
| Recapitalization | [$X M] | [refi proceeds] | [$X M] | [X%] |
| REIT conversion | [$X M] | [REIT treatment] | [$X M] | [X%] |

#### 6. Disclaimers

---

FINANCIAL DISCLAIMER: The financial projections, cost estimates, and economic
analyses produced by this skill are for preliminary planning and evaluation
purposes only. This is not investment advice, financial advice, or
a recommendation to proceed with any transaction. Actual costs, revenues, and
returns will vary based on market conditions, vendor negotiations, site-specific
factors, and regulatory changes not modeled here.

All financial outputs are presented as ranges where possible. Point estimates
should be treated as order-of-magnitude guidance, not bankable figures. Users
must engage qualified financial advisors, tax professionals, and legal counsel
before making investment decisions based on these outputs.

Sensitivity analyses are provided to illustrate the impact of key variable
changes. They do not represent probabilistic forecasts or guarantee that
outcomes will fall within the stated ranges.

---

TAX DISCLAIMER: Tax incentive calculations (ITC, PTC, MACRS, Section 179D,
Opportunity Zones, cost segregation, bonus depreciation) are estimates based
on current tax law as of the reference data publication date. Tax law is
subject to legislative change, IRS guidance updates, and judicial
interpretation.

Tax benefits modeled here assume qualification criteria are met. Actual
qualification depends on project-specific facts reviewed by a qualified tax
advisor. Do not rely on these estimates for tax planning, tax filing, or
investment structuring without professional tax counsel.

---

### JSON Sidecar

```json
{
  "artifact_type": "deal-structure",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "entity_structure": {},
  "tax_benefits": {},
  "waterfall_distributions": [],
  "exit_scenarios": {},
  "total_tax_savings": 0,
  "investor_irr": 0,
  "confidence_range_low": 0,
  "confidence_range_high": 0
}
```

## Gotchas

- **Opportunity Zone regulations are complex and frequently updated** -- post-OBBBA "OZ 2.0" has rolling 5-year deferral and indefinite program extension, but QOF must hold 90%+ assets in OZ property and meet substantial improvement test within 30 months for acquisitions. Always verify current rules.
- **Cost segregation studies require qualified engineers** -- this skill estimates reclassification percentages (40-60% typical for DC), but actual percentages depend on an engineering-based study. IRS expects detailed asset-by-asset review, not estimates.
- **Section 179D sunsets June 30, 2026** -- projects must begin construction by this date. The $5.36/sqft deduction requires 25% improvement over ASHRAE 90.1-2007, which most modern DC cooling systems easily achieve. Time-sensitive.
- **State incentive clawback provisions can negate benefits** -- many states require minimum headcount, investment thresholds, or operational timelines. Missing a threshold by even 1 employee or $1 can trigger full clawback of multi-year benefits.
- **ITC basis reduction affects depreciation** -- claiming 30% ITC reduces the depreciable basis by 15% (half the credit amount). Failing to account for this overstates total tax benefits. Always model ITC and depreciation together.

## Calculation Scripts

For deterministic deal structure calculations, use the bundled script:

- `scripts/deal-structure.py` -- SPV structure, tax optimization stacking, waterfall distribution, and exit modeling

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering deal structuring across
different entity types, tax optimization strategies, and exit mechanisms.
