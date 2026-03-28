---
name: fin-project-tco
description: "Calculate Total Cost of Ownership for data center projects over 10/20 year horizons with CapEx/OpEx breakdown, tax incentive modeling, and NPV calculation. Use when estimating DC project costs, calculating TCO, modeling tax incentives (ITC, bonus depreciation, Opportunity Zones), comparing site economics, or preparing cost projections for investors. Trigger with \"TCO\", \"total cost of ownership\", \"DC project cost\", \"CapEx OpEx\", \"cost model\", \"how much will this data center cost?\", or \"NPV analysis\"."
---

# Total Cost of Ownership Model

Calculate 10/20-year Total Cost of Ownership with detailed CapEx/OpEx breakdown,
US federal and state tax incentive modeling, sensitivity analysis, and NPV calculation.
The most reference-data-intensive skill in the library, consuming 4 reference files.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire financial model.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction from bare site
   - **Brownfield:** Conversion of existing building or facility upgrade

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the total IT capacity (MW) and build-out phasing?
   - Total target capacity and number of phases
   - Phase 1 capacity and target completion date

4. What is the project location (state or country)?
   - Drives tax incentive eligibility and power cost assumptions
   - If US: state determines sales tax, property tax, and incentive programs
   - If multi-site comparison: list all candidate locations

5. What analysis horizon?
   - 10-year (standard investment analysis)
   - 20-year (asset lifecycle analysis)
   - Both (recommended for investment materials)

6. What discount rate for NPV?
   - Specify WACC or target IRR if known
   - Default: 8-10% WACC if unknown

7. What is the ownership structure?
   - **Owner-occupied:** Full CapEx, depreciation benefits, operating expense deductions
   - **Leased:** Lower CapEx, lease payments as OpEx, limited depreciation
   - **Colocation:** Tenant pays per-kW/month; build-out CapEx only for tenant improvements

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. What is the land acquisition cost (or is land already owned)?
2. What is the construction timeline (months from groundbreaking to COD)?
3. What is the financing structure? (all equity, project finance, construction loan)
4. Are there any unusual site development costs? (rock blasting, environmental remediation, utility relocation)

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. What is the acquisition cost for the existing facility?
2. What is the estimated renovation budget?
3. What existing equipment has salvage or reuse value?
4. What is the expected construction timeline for conversion?

### Tax Incentive Path

Based on project location:

1. Is the site in a designated Opportunity Zone? (from FEDERAL-TAX-GUIDE.md)
2. Does the project qualify for state sales tax exemption? (from US-STATE-INCENTIVES.md -- check investment threshold)
3. Is property tax abatement available? (from US-STATE-INCENTIVES.md -- check job creation requirements)
4. Is behind-the-meter renewable energy planned? (determines ITC/PTC eligibility from FEDERAL-TAX-GUIDE.md)

### Multi-Site Comparison Path

If comparing multiple locations:

1. List candidate sites with state/region
2. Specify which variables to hold constant vs vary by site
3. Rank sites by NPV, IRR, and payback period

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Total IT load (kW)
- Total facility load (kW) including cooling and overhead
- PUE (calculated)
- Redundancy tier (affects CapEx for electrical infrastructure)
- Phased build-out schedule with capacity per phase
- Power infrastructure CapEx estimate (if available)

**From cooling-design-report (eng-cooling-design):**
- Cooling technology selected
- Cooling infrastructure CapEx estimate
- Annual water consumption estimate
- PUE contribution from cooling systems

If upstream data is not available, I will ask you for key values or use
COST-BENCHMARKS.md regional defaults.

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| CapEx $/MW typical | $8-12M | $7-10M | $12-18M | $8-14M | $6-9M | $10-15M |
| OpEx % of CapEx/yr | 8-12% | 6-8% | 10-15% | 8-12% | 8-10% | 12-18% |
| Staff per MW | 3-5 | 1-2 | 5-8 | 3-5 | 1-3 | 0.5-1 |
| Typical lease term | N/A | N/A | 15-20yr | 5-10yr | 3-5yr | 3-5yr |

## TCO Model Components

### CapEx Categories

- **Land acquisition:** Purchase price, closing costs, survey, environmental assessment
- **Site development:** Grading, utilities, roads, stormwater, fencing
- **Building shell:** Structure, envelope, core and shell
- **Mechanical systems:** Cooling infrastructure (from upstream cooling-design-report)
- **Electrical systems:** Power chain (from upstream power-capacity-model)
- **IT infrastructure:** Racks, cabling, network backbone, structured cabling
- **Fire protection and security:** Clean agent suppression, VESDA, access control, CCTV
- **Professional fees:** Architecture, engineering, project management, legal (8-15% of hard costs)
- **Contingency:** 5-15% of hard costs depending on design completeness

### OpEx Categories (Annual)

- **Power cost:** Total facility kW x $/kWh x 8,760 hours (from POWER-TARIFFS.md regional rate)
- **Cooling-specific OpEx:** Water cost, refrigerant, cooling maintenance
- **Staffing:** Headcount x loaded cost per employee (from COST-BENCHMARKS.md labor index)
- **Maintenance:** Preventive + corrective, typically 2-4% of M&E CapEx annually
- **Insurance:** Property + liability + business interruption, typically 0.5-1% of replacement value
- **Property tax:** Assessed value x local mill rate (before abatement)
- **SaaS/software:** DCIM, BMS, security software, licensing fees

### Tax Incentive Line Items

- **Sales tax exemption** on construction materials and equipment (from US-STATE-INCENTIVES.md)
- **Property tax abatement** -- partial or full, with duration and clawback provisions (from US-STATE-INCENTIVES.md)
- **Federal ITC** for on-site solar/storage (from FEDERAL-TAX-GUIDE.md -- 6-50% depending on adders)
- **Federal PTC** for wind generation (from FEDERAL-TAX-GUIDE.md -- ~2.9 cents/kWh with prevailing wage)
- **MACRS accelerated depreciation** (from FEDERAL-TAX-GUIDE.md -- 5-15 year recovery periods)
- **Bonus depreciation** (from FEDERAL-TAX-GUIDE.md -- 100% post-OBBBA for qualifying property)
- **Section 179D** energy-efficient commercial building deduction (from FEDERAL-TAX-GUIDE.md -- up to $5.36/sqft, sunset June 30, 2026)
- **Opportunity Zone** capital gains deferral and exclusion (from FEDERAL-TAX-GUIDE.md -- 10+ year hold for full exclusion)

## Validation Loop

1. Compute TCO from inputs and reference data
2. Cross-check CapEx $/MW against COST-BENCHMARKS.md regional range -- flag if outside range
3. Validate power cost against POWER-TARIFFS.md for the selected location
4. Verify tax incentive eligibility against US-STATE-INCENTIVES.md qualification thresholds (investment minimum, job creation)
5. Check that NPV calculation uses consistent discount rate and escalation assumptions
6. If any input is outside reference data ranges: flag as "exceeds benchmark" with explanation
7. Recompute with adjusted assumptions if flags are triggered

## Sensitivity Analysis

Vary each parameter independently to identify the largest drivers of TCO and NPV:

- **Power cost:** +/-20% (largest OpEx driver, typically 60-70% of 10-year OpEx)
- **PUE:** +/-0.1 (efficiency directly scales power cost)
- **Construction cost:** +/-15% (CapEx uncertainty)
- **Discount rate:** +/-2% (NPV sensitivity to WACC assumptions)
- **Utilization ramp:** 50%, 75%, 100% at Year 1 (phased occupancy impact)

Present as a tornado chart (text table) showing which variable has the largest
impact on 10-year NPV. All quantitative outputs are presented as ranges reflecting
the sensitivity bounds.

## Reference Data

Load these files on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional construction $/MW and labor indices
- [Power tariffs](../../references/POWER-TARIFFS.md) -- Industrial electricity tariffs by region
- [US state incentives](../../references/US-STATE-INCENTIVES.md) -- State matching for incentive modeling
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC, PTC, MACRS, 179D, bonus depreciation, OZ

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-tco-model.md`

1. **Executive Summary:** Total 10-year and 20-year TCO as ranges, key assumptions, location
2. **CapEx Breakdown Table:** Line-item capital expenditures with ranges
3. **Annual OpEx Projection Table:** Year-by-year with escalation applied
4. **Tax Incentive Summary Table:** Each incentive, estimated value, eligibility status
5. **NPV Analysis:** 10-year and 20-year NPV at specified discount rate, as ranges
6. **Sensitivity Analysis:** Tornado chart as text table showing impact of each variable on NPV
7. **Assumptions and Methodology:** Escalation rates, discount rate, tax rate, data sources
8. **Disclaimer:** Financial and Tax disclaimers (mandatory)

### JSON Sidecar: `<project-name>-tco-model.json`

```json
{
  "artifact_type": "tco-model",
  "skill_version": "1.0",
  "project_name": "...",
  "location": "...",
  "facility_type": "...",
  "it_load_mw": 0,
  "total_capex": {"low": 0, "high": 0, "unit": "USD"},
  "annual_opex_year1": {"low": 0, "high": 0, "unit": "USD"},
  "total_tco_10yr": {"low": 0, "high": 0, "unit": "USD"},
  "total_tco_20yr": {"low": 0, "high": 0, "unit": "USD"},
  "npv_10yr": {"low": 0, "high": 0, "unit": "USD"},
  "npv_20yr": {"low": 0, "high": 0, "unit": "USD"},
  "pue": 0,
  "power_cost_kwh": 0,
  "discount_rate": 0.08,
  "tax_incentives": [
    {"name": "...", "value": 0, "eligible": true}
  ],
  "sensitivity": {
    "power_cost_impact_pct": 0,
    "pue_impact_pct": 0,
    "construction_cost_impact_pct": 0,
    "discount_rate_impact_pct": 0,
    "utilization_ramp_impact_pct": 0
  }
}
```

## Gotchas

- **Power cost is typically 60-70% of 10-year OpEx.** A 2 cent/kWh difference in electricity rate changes 10-year TCO by millions on a 10MW+ facility. Always validate against POWER-TARIFFS.md.
- **Bonus depreciation is 100% post-OBBBA (July 4, 2025) for property placed in service on or after January 20, 2025.** This is permanent, replacing the prior phasedown schedule. Year of construction completion still matters for Section 179D (sunset June 30, 2026).
- **State sales tax exemptions often have minimum investment thresholds ($50M-$250M) and job creation requirements.** Verify qualification against US-STATE-INCENTIVES.md before modeling the savings.
- **Property tax abatements typically have clawback provisions** if you close the facility within 10-15 years. Model the clawback risk for short-hold scenarios.
- **OZ benefits require holding the investment for 10+ years for full exclusion of NEW capital gains.** Short holds get the 5-year deferral and 10% basis step-up only.

## Calculation Scripts

For deterministic TCO calculations, use the bundled script:

- `scripts/tco-model.py` -- TCO calculation with CapEx/OpEx breakdown, NPV, tax incentives, and sensitivity analysis

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Disclaimer

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

## Evaluations

See `evals/evals.json` for test scenarios covering TCO analysis across different
facility types, locations, and tax incentive structures.
