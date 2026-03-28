---
name: fin-project-model
description: "Build a complete data center financial model with revenue projections, cost structure, EBITDA waterfall, IRR/NPV/MOIC calculations, and sensitivity analysis. Use when building a financial model for a DC, calculating returns, projecting revenue and EBITDA, or performing sensitivity analysis on key assumptions. Trigger with \"financial model\", \"DC pro forma\", \"IRR calculation\", \"EBITDA waterfall\", \"project economics\", \"returns analysis\", or \"build a financial model\"."
---

# Data Center Financial Model

Build a complete project finance model with revenue projections, cost structure,
EBITDA waterfall, IRR/NPV/MOIC calculations, and multi-tranche equity waterfall
distribution. Supports senior debt, mezzanine, and equity tranches with
configurable hurdle rates, catch-up, and carried interest provisions.
Consumes the upstream TCO model for cost inputs.

**This skill produces estimates for planning purposes only. Not investment advice.**
See Disclaimer section for full terms.

## What I Need from Upstream

**From tco-model (fin-project-tco):**
- Total CapEx breakdown (land, building, M&E, IT infrastructure, professional fees)
- Annual OpEx projections with escalation
- PUE and power cost assumptions
- Tax incentive estimates (ITC, MACRS, 179D, OZ)
- Regional cost benchmarks used

If upstream data is not available, I will ask you for key values or use
COST-BENCHMARKS.md regional defaults.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire financial model.

**Project Context:**

1. What is the project capacity (MW)?
   - Total IT load at full build-out
   - Phased deployment schedule if applicable

2. What is the revenue model?
   - Colocation: $/kW/month pricing with occupancy ramp
   - Hyperscale: Contracted (fixed-term, take-or-pay)
   - Enterprise: Internal cost allocation (no external revenue)
   - Hybrid: Mixed colo + hyperscale tenants

3. What is the capital structure?
   - Percentage debt vs equity
   - Mezzanine layer included? (yes/no, amount)
   - Construction financing separate from permanent financing?

4. What are the debt terms?
   - Senior debt interest rate
   - Debt tenor (years) and amortization schedule
   - Target DSCR (Debt Service Coverage Ratio)

5. What is the equity return target?
   - IRR hurdle rate for preferred return
   - MOIC target (if applicable)
   - GP/LP split structure

6. What is the projection period?
   - 10 years (standard investment analysis)
   - 15 years (mid-term, common for colo)
   - 20 years (asset lifecycle, common for hyperscale)

7. What is the tax jurisdiction?
   - US state (for MACRS/ITC/179D modeling)
   - International (for local depreciation schedules)

8. What are the occupancy ramp assumptions?
   - Year 1 occupancy percentage
   - Annual ramp rate
   - Stabilized occupancy target and year achieved

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Revenue Model Refinements

**Colocation:**
1. What is the tenant mix? (retail, wholesale, hyperscale anchor)
2. Average contract term by tenant type?
3. Renewal probability and pricing escalation at renewal?
4. Power markup model? (pass-through, blended, metered)

**Hyperscale:**
1. Contract structure? (take-or-pay MW, revenue per MW/month)
2. Contract term and extension options?
3. Build-to-suit vs speculative capacity?
4. Customer credit quality? (investment grade, sub-IG)

**Enterprise:**
1. Cost allocation methodology? (per-rack, per-kW, per-sqft)
2. Chargeback to business units or centralized IT budget?
3. Comparison benchmark? (internal vs external colo pricing)

### Capital Structure Refinements

**Senior debt:**
1. Fixed or floating rate? (if floating, reference rate + spread)
2. Amortization schedule? (level payments, bullet, interest-only period)
3. Cash sweep provisions? (excess cash flow applied to principal)

**Mezzanine (if applicable):**
1. Coupon rate? (typically 12-15% for DC deals)
2. Equity kicker or warrant coverage? (%)
3. Subordination terms and intercreditor agreement?

**Equity waterfall:**
1. Preferred return (hurdle) rate? (typically 8-12% for DC)
2. Catch-up provision? (GP receives 100% until split achieved)
3. Carried interest split? (e.g., 80/20 LP/GP above hurdle)
4. Clawback provision? (GP returns excess carry if total returns underperform)

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Revenue model | Internal allocation | Contracted/PPA | Cost-plus | $/kW/month | $/kW/month | Edge-as-a-service |
| Target IRR (levered) | N/A | 8-12% | N/A (cost recovery) | 12-18% | 15-20% | 18-25% |
| Typical MOIC | N/A | 1.5-2.0x | N/A | 2.0-2.5x | 2.0-3.0x | 2.5-3.5x |
| Debt/Equity typical | 0/100 | 60-70/30-40 | 0-30/70-100 | 65-75/25-35 | 50-70/30-50 | 40-60/40-60 |
| Occupancy ramp | 100% (captive) | 100% (contracted) | 100% (gov) | 3-5yr to stabilize | 1-2yr | 1-3yr |

### Facility Type Refinements

**Hyperscale additions:**
- Campus-level vs single-building financial model?
- Phase funding (draw-down facility) vs full upfront financing?
- Customer credit facility backstop?

**Colocation additions:**
- Retail vs wholesale margin differential?
- Cross-connect and managed services revenue?
- Tenant improvement allowance budget?

**Sovereign additions:**
- Government appropriation cycle alignment?
- Cost-plus margin structure?
- Multi-year funding certainty?

## Analysis & Output

### Process

1. **Build revenue projection:** Capacity * pricing * occupancy ramp, escalated annually
2. **Build OpEx projection:** From TCO model or user input, escalated annually
3. **Calculate EBITDA:** Revenue - OpEx (before depreciation, interest, tax)
4. **Model debt service:** Amortization schedule, interest payments, DSCR check
5. **Calculate free cash flow to equity (FCFE):** EBITDA - debt service - taxes - maintenance CapEx
6. **Compute returns:** IRR (Newton-Raphson on cash flow stream), NPV (discounted FCFE), MOIC (total distributions / equity invested)
7. **Run equity waterfall:** Preferred return -> catch-up -> carried interest distribution
8. **Sensitivity analysis:** IRR sensitivity to occupancy, power cost, construction cost, interest rate
9. **Apply tax benefits:** MACRS depreciation, ITC (reduces basis), bonus depreciation, 179D

### Reference Data

Load these files on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional construction $/MW and labor indices for revenue/cost validation
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC, PTC, MACRS, Section 179D, bonus depreciation, Opportunity Zone modeling
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required financial and tax disclaimer language

### Validation Loop

1. Compute financial model from inputs and assumptions
2. Cross-check CapEx $/MW against COST-BENCHMARKS.md regional range
3. Validate revenue per kW/month against market data (typically $100-200/kW/month for wholesale colo)
4. Check DSCR remains above covenant minimum (typically 1.25-1.50x) in all years
5. Verify IRR calculation converges and is within reasonable range (5-30%)
6. Validate MOIC is consistent with IRR and projection period
7. Check tax incentive eligibility against FEDERAL-TAX-GUIDE.md
8. If any metric outside expected range: flag and explain deviation
9. Recompute with adjusted assumptions if flags triggered

## Output

This skill produces two files:
1. `<project-name>-financial-model.md` -- Full report
2. `<project-name>-financial-model.json` -- Structured data for downstream skills

### Financial Model Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: fin-project-model v1.0]

#### 1. Executive Summary
- Project: [capacity] MW data center in [location]
- Total CapEx: [$X-Y M] (range)
- Revenue model: [type], stabilized at [$X M/yr]
- Capital structure: [X% debt / Y% equity]
- Project IRR: [X-Y%] (unlevered)
- Equity IRR: [X-Y%] (levered)
- NPV at [X%] discount: [$X-Y M]
- MOIC: [X.X-X.Xx]

#### 2. Revenue Model
| Year | Occupancy | Revenue | Growth |
|------|-----------|---------|--------|
| 1 | [X%] | [$X M] | -- |
| 2 | [X%] | [$X M] | [X%] |
| ... | ... | ... | ... |

#### 3. Cost Structure
| Category | Year 1 | Stabilized | % of Revenue |
|----------|--------|-----------|-------------|
| Power | [$X M] | [$X M] | [X%] |
| Staffing | [$X M] | [$X M] | [X%] |
| Maintenance | [$X M] | [$X M] | [X%] |
| Insurance | [$X M] | [$X M] | [X%] |
| Total OpEx | [$X M] | [$X M] | [X%] |
| EBITDA | [$X M] | [$X M] | [X%] margin |

#### 4. Capital Structure
| Tranche | Amount | Rate | Term |
|---------|--------|------|------|
| Senior debt | [$X M] | [X%] | [X yr] |
| Mezzanine | [$X M] | [X%] | [X yr] |
| Equity | [$X M] | [X% hurdle] | -- |

#### 5. Debt Service
| Year | Interest | Principal | Total DS | DSCR |
|------|----------|-----------|----------|------|
| 1 | [$X M] | [$X M] | [$X M] | [X.Xx] |
| ... | ... | ... | ... | ... |

#### 6. Equity Waterfall
| Distribution Tier | Cumulative | LP Share | GP Share |
|-------------------|-----------|----------|---------|
| Return of capital | [$X M] | 100% | 0% |
| Preferred return ([X%]) | [$X M] | 100% | 0% |
| GP catch-up | [$X M] | 0% | 100% |
| Carried interest | [$X M] | [X%] | [X%] |

#### 7. Returns Summary
| Metric | Project (Unlevered) | Equity (Levered) | Range |
|--------|--------------------|--------------------|-------|
| IRR | [X%] | [X%] | [low-high] |
| NPV | [$X M] | [$X M] | [low-high] |
| MOIC | [X.Xx] | [X.Xx] | [low-high] |
| Payback period | [X yr] | [X yr] | [low-high] |

#### 8. Sensitivity Analysis
| Variable | Base | Low (-20%) | High (+20%) | IRR Impact |
|----------|------|-----------|------------|-----------|
| Occupancy rate | [X%] | [X%] | [X%] | [+/-X%] |
| Power cost | [$X/kWh] | [$X] | [$X] | [+/-X%] |
| Construction cost | [$X/MW] | [$X] | [$X] | [+/-X%] |
| Interest rate | [X%] | [X%] | [X%] | [+/-X%] |

#### 9. Tax Benefits
| Incentive | Value | Eligible | Notes |
|-----------|-------|----------|-------|
| MACRS 5-year | [$X M] | [Y/N] | [schedule applied] |
| Bonus depreciation | [$X M] | [Y/N] | [100% post-OBBBA] |
| ITC | [$X M] | [Y/N] | [qualifying assets] |
| Section 179D | [$X M] | [Y/N] | [sqft * rate] |

#### 10. Disclaimers

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
  "artifact_type": "financial-model",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "capacity_mw": 0,
  "total_capex": 0,
  "revenue_stabilized": 0,
  "ebitda_stabilized": 0,
  "project_irr": 0,
  "equity_irr": 0,
  "npv": 0,
  "moic": 0,
  "dscr_min": 0,
  "dscr_avg": 0,
  "equity_waterfall": {},
  "sensitivity": {},
  "confidence_range_low": 0,
  "confidence_range_high": 0
}
```

## Gotchas

- **DC project finance IRR targets are typically 8-12% levered for core assets, 15-20%+ for development** -- using a single hurdle rate masks risk differences between stabilized assets and greenfield development. Always model both unlevered and levered returns.
- **Occupancy ramp is the #1 model killer** -- most models assume 80%+ by Year 2, but industry median for new colo builds is 50-60% by Year 2. Hyperscale contracted deals avoid this risk but trade IRR for certainty.
- **MACRS 5-year depreciation for certain DC equipment (not building shell) can reduce effective tax rate by 15-25% in early years** -- always model equipment separately from building via cost segregation. Building shell is 39-year straight-line.
- **Mezzanine debt in DC deals is typically 12-15% coupon with equity kickers** -- modeling it as simple debt understates the true cost of capital. The equity kicker (warrants or conversion rights) can add 3-5% to the effective cost.

## Calculation Scripts

For deterministic financial calculations, use the bundled script:

- `scripts/waterfall-model.py` -- IRR/NPV/MOIC calculation with multi-tranche equity waterfall distribution

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering financial modeling across
different facility types, capital structures, and return targets.
