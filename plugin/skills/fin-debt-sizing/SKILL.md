---
name: fin-debt-sizing
description: "Size debt capacity for data center projects using DSCR-based methodology with construction facility modeling, term loan sizing, and covenant structuring. Use when sizing debt for a DC, modeling construction financing, calculating debt service coverage, or structuring loan covenants for data center projects. Trigger with \"debt sizing\", \"DSCR\", \"construction financing\", \"term loan\", \"debt capacity\", \"loan sizing\", or \"how much debt can this DC support?\"."
---

# Debt Sizing & Covenant Analysis

Size debt capacity for data center projects using DSCR-based methodology.
Models construction facility draw, term loan amortization, covenant testing,
and cash trap provisions. Calculates CFADS (Cash Flow Available for Debt
Service) from EBITDA with proper deductions -- not raw EBITDA.

**This skill produces estimates for planning purposes only. Not investment advice.**
See Disclaimer section for full terms.

## What I Need from Upstream

**From financial-model (fin-project-model):**
- Annual EBITDA projections with occupancy ramp
- Maintenance CapEx schedule
- Tax rate and effective tax payments
- Working capital requirements
- Revenue concentration and contract terms

If upstream data is not available, I will ask you for key values or generate
simplified assumptions based on facility type and capacity.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the debt sizing approach.

**Project Context:**

1. What is the total project cost?
   - CapEx breakdown if available (land, building, M&E, IT)
   - Construction timeline (months to COD)

2. What is the expected stabilized EBITDA?
   - Annual EBITDA at stabilized occupancy
   - Occupancy ramp timeline (years to stabilization)

3. What is the construction timeline?
   - Months from ground-breaking to COD (Certificate of Occupancy)
   - Phased construction? (if so, phase schedule)

4. What is the target leverage?
   - Target LTV (loan-to-value): typically 65-75% for DC
   - Or target DSCR: typically 1.25-1.40x minimum

5. What type of lender?
   - Bank (relationship lender, typically conservative)
   - Life insurance company (long-term, fixed rate)
   - CMBS (conduit, higher leverage, less flexible)
   - Debt fund (flexible, higher rate)
   - Agency (Fannie/Freddie -- limited DC applicability)

6. What is the current interest rate environment?
   - Base rate (SOFR, Treasury) and spread expectation
   - Fixed vs floating preference
   - Rate lock or hedge strategy

7. Is there existing debt to refinance?
   - Existing balance, rate, maturity
   - Prepayment penalty or defeasance cost

8. Is this new financing or refinancing?
   - New construction facility + term loan
   - Refinancing of existing facility
   - Acquisition financing

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Cash Flow Profile

1. What is the monthly/quarterly cash flow pattern?
   - Seasonal variation in power costs?
   - Revenue concentration risk (top tenant %)?
   - Contract expiration schedule?

2. What maintenance CapEx is required?
   - Annual maintenance as % of revenue (typically 2-5%)
   - Major equipment replacement schedule?

3. What are the working capital requirements?
   - Accounts receivable terms?
   - Security deposit levels?

### Lender Requirements

**Bank/Life Co:**
1. Minimum DSCR requirement? (typically 1.30-1.40x)
2. Maximum LTV? (typically 65-70%)
3. Cash management requirements? (lockbox, sweep)
4. Reporting requirements?

**CMBS:**
1. Minimum debt yield? (typically 8-10%)
2. Defeasance vs yield maintenance?
3. Carve-out guarantees required?

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical DSCR min | 1.35x | 1.25x | N/A | 1.30x | 1.35x | 1.40x |
| Typical LTV max | 65% | 75% | N/A | 70% | 65% | 60% |
| Construction term | 24-36mo | 18-30mo | 24-48mo | 18-24mo | 6-12mo | 3-6mo |
| Term loan | 7-10yr | 10-15yr | 15-20yr | 7-10yr | 5-7yr | 3-5yr |
| Amortization | 15-25yr | 20-30yr | 25-30yr | 15-25yr | 10-15yr | 7-10yr |
| Debt yield min | 8-10% | 7-9% | N/A | 8-10% | 9-11% | 10-12% |

## Analysis & Output

### Process

1. **Calculate CFADS:** EBITDA - taxes - maintenance CapEx - working capital changes (CFADS is the correct denominator for DSCR, not EBITDA per Pitfall 2)
2. **Determine minimum DSCR:** Based on lender type and facility risk profile (1.25-1.40x)
3. **Size debt capacity:** Maximum annual debt service = CFADS / minimum DSCR; solve for loan amount given rate and amortization
4. **Model construction facility:** Interest-only on drawn balance, floating rate, 18-36 month draw period, converts to term at COD
5. **Build amortization schedule:** Constant payment (mortgage-style), annual DSCR recalculation
6. **Test covenants annually:** Minimum DSCR (1.25-1.30x), debt yield (>8%), LTV (<75%), identify cash trap trigger (DSCR <1.15x) and default trigger (DSCR <1.05x)
7. **Run sensitivity analysis:** DSCR at NOI +/-10%, interest rate +/-100bps, occupancy variation

### Reference Data

Load these files on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional construction $/MW for project cost validation
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required financial disclaimer language

### Validation Loop

1. Compute debt capacity from CFADS and minimum DSCR
2. Verify LTV does not exceed lender maximum
3. Check debt yield (stabilized NOI / loan amount) meets minimum
4. Validate DSCR remains above covenant minimum in all projection years
5. Verify construction interest capitalization does not exceed facility size
6. Check balloon payment risk at term maturity
7. If any covenant breached: reduce loan amount and recompute
8. Repeat until all covenants satisfied in all years

## Output

This skill produces two files:
1. `<project-name>-debt-sizing.md` -- Full report
2. `<project-name>-debt-sizing.json` -- Structured data for downstream skills

### Debt Sizing Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: fin-debt-sizing v1.0]

#### 1. Debt Capacity Summary
- Maximum debt capacity: [$X M]
- LTV: [X%]
- Debt yield: [X%]
- Interest rate: [X%] ([fixed/floating])
- Amortization: [X years]
- Term: [X years]
- Minimum DSCR: [X.XXx]

#### 2. Construction Facility
- Facility size: [$X M]
- Draw period: [X months]
- Rate: [SOFR + X bps]
- Capitalized interest: [$X M]
- Conversion to term at COD: [date]

#### 3. Amortization Schedule
| Year | Beginning Balance | Payment | Principal | Interest | Ending Balance | DSCR |
|------|-------------------|---------|-----------|----------|---------------|------|
| 1 | [$X M] | [$X M] | [$X M] | [$X M] | [$X M] | [X.XXx] |
| 2 | [$X M] | [$X M] | [$X M] | [$X M] | [$X M] | [X.XXx] |
| ... | ... | ... | ... | ... | ... | ... |

#### 4. Covenant Compliance
| Year | DSCR | Min Req | Debt Yield | Min Req | LTV | Max | Status |
|------|------|---------|------------|---------|-----|-----|--------|
| 1 | [X.XXx] | [1.30x] | [X%] | [8%] | [X%] | [75%] | [Pass/Trap/Default] |

#### 5. Sensitivity Analysis
| Scenario | DSCR Year 1 | DSCR Min | Covenant Status |
|----------|-------------|----------|-----------------|
| Base case | [X.XXx] | [X.XXx] | [Pass] |
| NOI -10% | [X.XXx] | [X.XXx] | [Pass/Trap] |
| NOI +10% | [X.XXx] | [X.XXx] | [Pass] |
| Rate +100bps | [X.XXx] | [X.XXx] | [Pass/Trap] |
| Rate -100bps | [X.XXx] | [X.XXx] | [Pass] |

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

### JSON Sidecar

```json
{
  "artifact_type": "debt-sizing-model",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "max_debt_capacity": 0,
  "ltv": 0,
  "debt_yield": 0,
  "interest_rate": 0,
  "amortization_years": 0,
  "term_years": 0,
  "min_dscr": 0,
  "annual_schedule": [],
  "covenant_compliance": [],
  "sensitivity": {},
  "construction_interest": 0
}
```

## Gotchas

- **DSCR must be calculated on CFADS, not EBITDA** -- the most common mistake in DC project finance. CFADS = EBITDA - taxes - maintenance CapEx - working capital changes. Using raw EBITDA overstates debt capacity by 15-25%.
- **Construction interest is capitalized, not expensed** -- during the 18-36 month construction period, interest on drawn amounts is added to the loan balance, not paid currently. This means the term loan balance at COD is higher than the original draw.
- **Balloon payment risk at year 5-7** -- most DC term loans have 7-year terms with 15-20 year amortization, creating a balloon payment at maturity that requires refinancing. If interest rates have risen or NOI has declined, refinancing may not cover the balloon.
- **Cash trap provisions restrict distributions even when DSCR >1.0x** -- most DC loans include a cash trap at DSCR <1.15x that sweeps excess cash to a reserve account, preventing equity distributions even though the loan is not technically in default.
- **Revenue concentration affects DSCR volatility** -- a single-tenant hyperscale DC has binary DSCR risk (tenant stays = 2.0x+, tenant leaves = 0x). Multi-tenant colo has smoother DSCR but lower peak coverage. Lenders price this differently.

## Calculation Scripts

For deterministic debt sizing calculations, use the bundled script:

- `scripts/debt-sizing.py` -- DSCR-based debt capacity with amortization schedule and covenant testing

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering debt sizing across
different facility types, leverage levels, and covenant structures.
