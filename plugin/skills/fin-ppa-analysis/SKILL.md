---
name: fin-ppa-analysis
description: "Evaluate power purchase agreements for data center operators with buyer-side LCOE comparison, contract term analysis, and risk assessment. Use when evaluating a PPA for a DC, comparing PPA vs spot/utility pricing, analyzing renewable energy contracts, or assessing PPA risk and pricing terms. Trigger with \"PPA\", \"power purchase agreement\", \"PPA analysis\", \"renewable PPA\", \"LCOE comparison\", \"energy procurement\", or \"should I sign this PPA?\"."
---

# PPA & Energy Procurement Analysis

Evaluate power purchase agreements for data center operators with buyer-side
levelized cost comparison of PPA vs self-generation vs grid. Models basis risk,
curtailment exposure, escalation, and additionality requirements.

**This skill produces estimates for planning purposes only. Not investment advice.**
See Disclaimer section for full terms.

## What I Need from Upstream

**From power-capacity-model (eng-power-model):**
- Facility load profile (MW, utilization, ramp schedule)
- PUE and total facility power demand
- Behind-the-meter generation if applicable
- Grid connection capacity

If upstream data is not available, I will ask you for key values or generate
simplified assumptions based on facility type and capacity.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the procurement evaluation.

**Project Context:**

1. What is the facility location and grid market?
   - ISO/RTO: ERCOT, PJM, MISO, CAISO, ISO-NE, NYISO, SPP
   - International: EU market, Nordic, APAC
   - Specific utility territory if known

2. What is the facility load?
   - Total IT load (MW)
   - Total facility load including cooling (MW)
   - Load factor / utilization percentage
   - Ramp schedule if new facility

3. What PPA offers have been received?
   - Price per MWh
   - Annual escalation rate
   - Term (years)
   - Technology (solar, wind, hybrid)
   - Settlement structure (physical vs virtual/financial)
   - Volume commitment (firm vs as-generated)

4. Is self-generation feasible?
   - On-site solar potential (available area, orientation)
   - On-site wind potential (zoning, wind resource)
   - Behind-the-meter BESS considered?
   - ITC eligibility for self-gen assets

5. What is the current grid tariff?
   - Rate per kWh or MWh
   - Tariff structure (flat, TOU, demand charges)
   - Historical trend (escalation over past 5 years)

6. Are there ESG/additionality requirements?
   - Corporate renewable energy target (RE100, SBTi)
   - CSRD reporting requirements (EU)
   - Additionality requirement (new-build only?)
   - Scope 2 accounting method (market-based vs location-based)

7. What is the preferred contract structure?
   - Physical PPA (delivered power)
   - Virtual/financial PPA (contract for differences)
   - Sleeved PPA (through utility intermediary)
   - Direct equity investment in generation asset

8. What is the analysis term?
   - 10 years (typical minimum PPA term)
   - 15 years (most common PPA term)
   - 20 years (long-term, matches asset life)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### PPA Term Refinements

1. What is the PPA settlement node?
   - Node name or zone in ISO market
   - Historical congestion data available?
   - Distance from facility delivery point?

2. What are the curtailment provisions?
   - Does buyer pay during curtailment?
   - Curtailment cap or sharing mechanism?
   - Historical curtailment rates in the market?

3. What are the contract exit provisions?
   - Termination fee structure?
   - Buyout option?
   - Change of control provisions?

### Self-Generation Refinements

1. Available roof or ground area for solar (sqft or acres)?
2. Local permitting requirements for on-site generation?
3. Net metering or export tariff available?
4. Interconnection queue status?

### Grid Tariff Refinements

1. Demand charge structure ($/kW)?
2. Time-of-use periods and rate differentials?
3. Any special economic development rate available?
4. Utility franchise area restrictions?

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical PPA size | 5-20MW | 50-500MW | 10-100MW | 5-30MW | 1-10MW | 0.5-5MW |
| PPA structure | Physical | Virtual | Physical | Physical | Physical | Grid only |
| Self-gen viability | Moderate | High | Moderate | Low (land) | Low | Very low |
| Additionality req | Low | High (ESG) | Varies | Moderate | Low | Low |
| Basis risk tolerance | Low | Higher | Low | Low | N/A | N/A |
| Typical term | 10-15yr | 12-20yr | 10-20yr | 10-15yr | 5-10yr | N/A |

## Analysis & Output

### Process

1. **Establish grid baseline:** Current tariff from POWER-TARIFFS.md, projected escalation (typically 2-3% annual), total grid cost over analysis term
2. **Evaluate PPA offer:** Contract price with escalator, settlement structure (physical delivery vs financial/virtual CFD), volume commitment, curtailment provisions, basis risk assessment
3. **Calculate self-gen LCOE:** Solar/wind capacity factors from SOLAR-WIND-RESOURCE.md, installed cost per kW, O&M cost, degradation (0.5% annual for solar), ITC benefit (30% per FEDERAL-TAX-GUIDE.md for eligible assets)
4. **Quantify basis risk:** PPA settlement node vs facility delivery node price spread, historical congestion patterns, typical DC basis risk $2-8/MWh depending on market (per Pitfall 3)
5. **Model curtailment exposure:** Renewable curtailment rates (1-8% by market), buyer payment obligation during curtailment events, impact on effective PPA cost
6. **Assess additionality:** New-build vs existing facility, ESG reporting implications per CSRD/SBTi frameworks, Scope 2 market-based accounting
7. **Build levelized comparison:** PPA all-in cost (price + escalation + basis risk + curtailment) vs grid all-in (tariff + demand charges + escalation) vs self-gen LCOE over 10/15/20 year terms
8. **Run sensitivity analysis:** Vary grid escalation +/-1%, curtailment +/-2%, basis risk +/-$2/MWh

### Reference Data

Load these files on demand -- do not read upfront:

- [Power tariffs](../../references/POWER-TARIFFS.md) -- Industrial grid tariffs by market for baseline comparison
- [Solar & wind resource](../../references/SOLAR-WIND-RESOURCE.md) -- Capacity factors by location for self-gen LCOE
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC rates for self-generation cost reduction
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required financial and tax disclaimer language

### Validation Loop

1. Compute levelized costs for all three options (grid, PPA, self-gen)
2. Verify grid tariff is consistent with POWER-TARIFFS.md for the specified market
3. Check solar/wind capacity factors against SOLAR-WIND-RESOURCE.md for the location
4. Validate basis risk estimate is within typical range for the ISO market ($2-8/MWh)
5. Confirm curtailment rate is consistent with market data (1-8% range)
6. Verify PPA escalation rate is market-reasonable (1-3% typical)
7. Check that ITC is only applied to qualifying self-gen assets per FEDERAL-TAX-GUIDE.md
8. If any input outside expected range: flag and explain deviation
9. Recompute with adjusted assumptions if flags triggered

## Output

This skill produces two files:
1. `<project-name>-ppa-analysis.md` -- Full report
2. `<project-name>-ppa-analysis.json` -- Structured data for downstream skills

### PPA Analysis Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: fin-ppa-analysis v1.0]

#### 1. Levelized Cost Comparison
| Option | Year 1 $/MWh | Levelized $/MWh | NPV ($M) | Savings vs Grid |
|--------|-------------|----------------|---------|----------------|
| Grid (baseline) | [$X] | [$X] | [$X] | -- |
| PPA (all-in) | [$X] | [$X] | [$X] | [$X M / X%] |
| Self-gen (LCOE) | [$X] | [$X] | [$X] | [$X M / X%] |

#### 2. Basis Risk Assessment
| Factor | Value | Impact |
|--------|-------|--------|
| PPA settlement node | [node] | |
| Facility delivery node | [node] | |
| Historical spread ($/MWh) | [$X-Y] | [$X M/yr] |
| Congestion frequency | [X%] | |
| Net basis risk adder | [$X/MWh] | [$X M over term] |

#### 3. Curtailment Analysis
| Market | Curtailment Rate | Annual Cost | Term Cost |
|--------|-----------------|-------------|-----------|
| [market] | [X%] | [$X M] | [$X M] |

#### 4. Recommendation Matrix
| Scenario | Recommended | Rationale |
|----------|-------------|-----------|
| Cost-optimized | [PPA/Grid/Self-gen] | [lowest levelized cost] |
| ESG-optimized | [PPA/Self-gen] | [additionality + cost] |
| Risk-minimized | [Grid/Physical PPA] | [no basis risk] |

#### 5. Sensitivity Analysis
| Variable | Base | Low | High | Impact on Recommendation |
|----------|------|-----|------|------------------------|
| Grid escalation | [X%] | [X-1%] | [X+1%] | [changes at...] |
| Curtailment | [X%] | [X-2%] | [X+2%] | [changes at...] |
| Basis risk | [$X] | [$X-2] | [$X+2] | [changes at...] |

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
  "artifact_type": "ppa-analysis",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "grid_levelized_cost": 0,
  "ppa_levelized_cost": 0,
  "selfgen_levelized_cost": 0,
  "recommendation": "",
  "savings_vs_grid": 0,
  "basis_risk_annual": 0,
  "curtailment_cost_annual": 0,
  "sensitivity": {},
  "additionality_assessment": ""
}
```

## Gotchas

- **Basis risk can negate apparent PPA savings** -- a PPA priced $10/MWh below grid is not $10/MWh savings if there is $5-8/MWh of basis risk between the PPA settlement node and the facility delivery node. Always model the all-in cost including basis risk adder.
- **Virtual PPAs provide no physical power delivery** -- a financial/virtual PPA is a contract for differences settled against a market index. The buyer still pays full grid tariff for physical power and receives (or pays) the difference between PPA price and index. Accounting treatment (ASC 815) can affect balance sheet.
- **Curtailment risk is asymmetric** -- in many PPA structures, the buyer pays the PPA price even during curtailment events (when the generator is ordered offline by the grid operator). The buyer pays but gets no power or RECs during these periods. Curtailment rates of 5-8% are common in congested markets.
- **Additionality claims require new-build verification** -- under CSRD, SBTi, and RE100 frameworks, additionality increasingly means the renewable facility would not have been built "but for" the PPA commitment. Buying RECs from existing facilities may not satisfy additionality requirements.
- **PPA accounting treatment matters** -- ASC 815 (derivatives) applies to most virtual PPAs, requiring mark-to-market on the balance sheet. Physical PPAs may qualify for the "normal purchases and normal sales" exception. The accounting treatment can materially affect reported earnings volatility.

## Calculation Scripts

For deterministic PPA cost calculations, use the bundled script:

- `scripts/ppa-calculator.py` -- Levelized cost comparison with basis risk, curtailment, and sensitivity

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering PPA analysis across
different markets, contract structures, and facility types.
