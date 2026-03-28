---
name: fin-due-diligence
description: "Conduct structured due diligence for data center acquisitions, refinancings, and JV entries with DD tracker, red flag identification, and risk scoring. Use when performing due diligence on a DC asset, evaluating an acquisition target, preparing a DD checklist, or identifying red flags in a data center transaction. Trigger with \"due diligence\", \"DD checklist\", \"acquisition diligence\", \"DC due diligence\", \"red flags\", or \"evaluate this data center deal\"."
---

# Due Diligence Tracker

Conduct structured due diligence for data center acquisitions, refinancings,
and JV entries. Produces a DD tracker checklist across four workstreams with
per-item status tracking, risk assessment, and summary dashboard.

**This skill produces a structured checklist for planning purposes only. Not investment advice.**
See Disclaimer section for full terms.

## What I Need from Upstream

This skill consumes all available upstream artifacts but generates its own
baseline if none are provided. Useful upstream artifacts include:

- **site-feasibility-report** (predev-site-feasibility) -- Site condition, zoning, environmental
- **financial-model** (fin-project-model) -- Revenue, cost, EBITDA projections
- **power-capacity-model** (eng-power-model) -- Electrical infrastructure assessment
- **cooling-design-report** (eng-cooling-design) -- Mechanical systems condition

If none are available, I will generate baseline assumptions from your answers
and flag items requiring further investigation.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the DD scope and approach.

**Transaction Context:**

1. What is the transaction type?
   - Acquisition (asset purchase or entity purchase)
   - Refinancing (existing debt maturity or recapitalization)
   - JV entry (developer joining with capital partner)
   - Portfolio transaction (multiple assets)

2. What is the asset type?
   - Single data center facility
   - Campus (multiple buildings, shared infrastructure)
   - Portfolio (geographically dispersed facilities)
   - Land + entitlements (pre-construction)

3. What is the asset stage?
   - Operating (revenue-generating, stabilized)
   - Operating (lease-up, not yet stabilized)
   - Development (under construction)
   - Pre-development (land + entitlements, not yet built)
   - Brownfield (conversion from non-DC use)

4. What documents are available?
   - Financial statements (how many years?)
   - Rent roll / customer contracts
   - Environmental reports (Phase I/II ESA)
   - Building condition reports
   - Equipment inventory and age data
   - Title commitment / survey
   - Permits and entitlements
   - Insurance certificates

5. What are the critical concerns?
   - Specific risks identified in preliminary review
   - Known issues flagged by seller or broker
   - Regulatory or environmental red flags
   - Customer concentration or contract expiration

6. What is the DD timeline?
   - Standard (45-60 days)
   - Expedited (21-30 days)
   - Extended (90+ days for complex transactions)
   - Post-closing (confirmatory DD after signing)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Operating Asset Refinements

1. What is the current occupancy and tenant mix?
2. What is the weighted average remaining lease term (WALT)?
3. Any deferred maintenance identified?
4. Have there been any significant outages in the past 3 years?
5. What is the staffing model (in-house vs outsourced operations)?

### Development-Stage Refinements

1. What permits and entitlements are in place?
2. What is the construction budget and timeline?
3. Are there pre-lease commitments or LOIs?
4. What is the utility interconnection status?
5. Has environmental remediation been completed (brownfield)?

### Portfolio Refinements

1. How many facilities and in which markets?
2. Are facilities on a common platform (equipment, operations)?
3. Any cross-default provisions in existing debt?
4. Shared services or corporate overhead allocation?

## Due Diligence Workstreams

### Technical Workstream

Assess physical condition, infrastructure capacity, and remaining useful life.

| # | Item | Status | Findings | Risk |
|---|------|--------|----------|------|
| T-01 | Site condition and environmental (Phase I/II ESA) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-02 | Building structural integrity | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-03 | Electrical distribution capacity and condition | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-04 | UPS systems (make, model, age, remaining life) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-05 | Generator systems (fuel type, capacity, runtime, age) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-06 | Cooling systems assessment (type, capacity, efficiency) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-07 | Redundancy level (Tier I-IV) and single points of failure | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-08 | Capacity utilization (current load vs design capacity) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-09 | Deferred maintenance backlog | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-10 | Code compliance (electrical, fire, building) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-11 | Fire suppression systems (type, condition, compliance) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-12 | Fiber/connectivity infrastructure | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-13 | Security systems (access control, CCTV, perimeter) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-14 | Environmental compliance (air permits, water discharge) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| T-15 | Equipment replacement schedule (5-year forecast) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |

### Commercial Workstream

Assess revenue quality, customer relationships, and market position.

| # | Item | Status | Findings | Risk |
|---|------|--------|----------|------|
| C-01 | Customer contracts (terms, expiry, renewal rights) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-02 | Revenue concentration (top 5 tenant percentage) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-03 | Customer credit quality | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-04 | Churn history (last 3 years) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-05 | Contract escalation mechanisms | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-06 | Market positioning vs competitors | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-07 | Pricing vs market benchmarks ($/kW/month) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-08 | Interconnection and cross-connect revenue | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-09 | Pipeline and LOIs | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-10 | Power procurement agreements | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-11 | Service level agreements and penalty history | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| C-12 | Managed services contracts | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |

### Legal Workstream

Assess legal standing, encumbrances, and regulatory compliance.

| # | Item | Status | Findings | Risk |
|---|------|--------|----------|------|
| L-01 | Title/deed (fee simple, leasehold, ground lease) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-02 | Easements and encumbrances | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-03 | Building permits (certificate of occupancy, use permits) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-04 | Environmental permits and compliance history | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-05 | Conditional use permits and zoning compliance | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-06 | Pending or threatened litigation | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-07 | Liens and encumbrances | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-08 | Insurance adequacy and claims history | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-09 | Lease terms (if leasehold interest) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-10 | IP and technology rights | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-11 | Regulatory obligations (state/local compliance) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-12 | Tax incentive compliance (clawback risk) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| L-13 | Data privacy and security compliance | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |

### Financial Workstream

Assess financial performance, capital requirements, and risk factors.

| # | Item | Status | Findings | Risk |
|---|------|--------|----------|------|
| F-01 | 3-year historical financials (audited preferred) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-02 | Revenue quality analysis (recurring vs one-time) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-03 | Working capital analysis | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-04 | CapEx requirements (deferred maintenance) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-05 | CapEx requirements (planned expansion) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-06 | Insurance claims history (3 years) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-07 | Tax compliance and filing status | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-08 | Tax incentive status and clawback risk | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-09 | Debt covenants and compliance (if refinancing) | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-10 | Accounts receivable aging | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-11 | Power cost analysis and utility contract terms | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-12 | Staffing costs and employment agreements | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |
| F-13 | Property tax assessment and appeal status | [Complete/Flagged/Missing] | [findings] | [Low/Medium/High/Critical] |

## Output

This skill produces two files:
1. `<project-name>-due-diligence.md` -- Full DD tracker report
2. `<project-name>-due-diligence.json` -- Structured checklist data

### DD Summary Dashboard

**Project:** [Project Name]
**Transaction:** [Acquisition/Refinancing/JV Entry]
**Date:** [Date]
**Prepared by:** [Skill: fin-due-diligence v1.0]

| Workstream | Items | Complete | Flagged | Missing | Critical Flags |
|------------|-------|----------|---------|---------|----------------|
| Technical | 15 | [N] | [N] | [N] | [N] |
| Commercial | 12 | [N] | [N] | [N] | [N] |
| Legal | 13 | [N] | [N] | [N] | [N] |
| Financial | 13 | [N] | [N] | [N] | [N] |
| **Total** | **53** | **[N]** | **[N]** | **[N]** | **[N]** |

**Overall DD Risk Rating:** [Low / Medium / High / Critical]
**Completion:** [N%]

### JSON Sidecar

```json
{
  "artifact_type": "due-diligence-report",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "transaction_type": "",
  "workstreams": {},
  "summary": {
    "total_items": 53,
    "complete": 0,
    "flagged": 0,
    "missing": 0,
    "critical_flags": 0,
    "completion_pct": 0,
    "risk_rating": ""
  }
}
```

## References

Load these files on demand -- do not read upfront:

- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required financial disclaimer language

## Disclaimers

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

## Gotchas

- **Due diligence is not advisory** -- this skill identifies risks and structures the DD process but does not make investment recommendations. All findings should be reviewed by qualified advisors.
- **Deferred maintenance is the #1 hidden cost in DC acquisitions** -- sellers often defer UPS battery replacements, generator overhauls, and roof repairs to improve trailing financials. A 20MW facility can have $5-15M in deferred maintenance that is not reflected in financial statements.
- **Revenue concentration >30% in one tenant is a critical flag** -- single-tenant hyperscale facilities have binary risk. Multi-tenant colo requires granular contract analysis. The higher the concentration, the more the valuation depends on one renewal decision.
- **Environmental liabilities can survive asset sale (successor liability)** -- unlike most liabilities that stay with the selling entity, environmental contamination can follow the property under CERCLA. A Phase I ESA is the minimum; Phase II if any recognized environmental conditions are identified.
- **Ground lease structures have hidden value destruction** -- if the DC sits on leased land, the ground lease terms (term, escalation, renewal rights, purchase option) directly affect long-term value. A 30-year ground lease with no renewal option materially reduces terminal value.

## Evaluations

See `evals/evals.json` for test scenarios covering due diligence across
different transaction types, asset stages, and risk profiles.
