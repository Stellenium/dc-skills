---
name: fin-investor-memo
description: "Generate an investment memorandum adapted to investor type (VC, PE/infrastructure, sovereign wealth, DFI) with tailored metrics and narrative. Use when preparing materials for DC investors, writing an investment memo, pitching a data center project, or tailoring the story for different investor profiles. Trigger with \"investor memo\", \"investment memorandum\", \"pitch to investors\", \"DC investment case\", \"fundraising materials\", or \"investor presentation\"."
argument-hint: "<investor-type>"
---

# Investor Memorandum

Generate a polished, submission-ready investment memorandum adapted to investor type.
Each investor type receives a structurally different memo emphasizing the metrics,
tone, and framing that align with their investment thesis. Consumes upstream financial
model for quantitative inputs and FEDERAL-TAX-GUIDE.md / DFI-FUNDING.md for
tax benefit and development finance positioning.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. What investor type is the target?
   - **VC (Venture Capital):** Growth-stage, equity, exit-oriented
   - **PE/Infrastructure:** Yield-focused, asset-quality, stabilized returns
   - **DFI (Development Finance Institution):** Impact-first, concessional, ESG-aligned
   - **Sovereign Wealth Fund:** Strategic allocation, long-horizon, national infrastructure

2. What is the target investment size range?
   - Under $50M
   - $50M - $250M
   - $250M - $1B
   - Over $1B

3. What is the project stage?
   - Development (pre-construction)
   - Construction (active build)
   - Operational (stabilized or ramping)

4. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

5. What is the MW capacity?
   - Current operational MW
   - Planned total capacity at full build-out

6. What is the facility location?
   - Primary site(s)
   - Regional market context

7. Is an existing financial model available?
   - Yes (provide model outputs: IRR, MOIC, DSCR, revenue projections)
   - No (this skill will produce estimates based on market benchmarks)

8. What is the competitive landscape?
   - Describe key competitors and differentiation

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### VC Path

If investor type is **VC**:

1. What round (Seed, Series A, B, C+)?
2. Prior rounds and investors (if any)?
3. Team credentials and track record?
4. Customer pipeline and LOIs?
5. Path to exit (trade sale, secondary, IPO)?
6. Key competitive moat (site control, power access, regulatory)?

### PE/Infrastructure Path

If investor type is **PE/Infrastructure**:

1. Current occupancy and lease terms?
2. Contracted vs. spot revenue percentage?
3. Debt capacity and current leverage?
4. Asset condition and remaining useful life?
5. Comparable transaction multiples?
6. Downside protection mechanisms (guarantees, LDs)?

### DFI Path

If investor type is **DFI**:

1. Target DFI institution(s) (IFC, AfDB, EBRD, DFC, etc.)?
2. Development impact thesis (jobs, digital inclusion, technology transfer)?
3. ESG framework compliance (IFC Performance Standards, E&S safeguards)?
4. Concessional vs. commercial terms sought?
5. Local content requirements?
6. Community benefit commitments?

### Sovereign Wealth Path

If investor type is **Sovereign Wealth Fund**:

1. Target fund(s) and existing relationship?
2. Strategic rationale beyond financial returns?
3. Co-investment structure preference?
4. Governance and board representation requirements?
5. Sovereign compute / national AI alignment?
6. Portfolio correlation considerations?

## What I Need from Upstream

This skill benefits from upstream artifacts but can operate independently.

**If project-financial-model is available (from fin-project-model):**
- Revenue projections, EBITDA waterfall, IRR/NPV/MOIC
- Capital structure and debt terms
- DSCR analysis and covenant compliance
- Sensitivity analysis outputs

**If site-feasibility-report is available (from predev-site-feasibility):**
- Location analysis and competitive positioning
- Power availability and infrastructure assessment
- Regulatory and zoning status
- Market demand indicators

## Analysis & Output

### Process

1. **Determine investor type** and load appropriate memo template
2. **Gather financial inputs** from upstream model or discovery questions
3. **Adapt tone and structure** to investor type expectations
4. **Build financial summary** with type-appropriate metrics
5. **Position risk factors** relevant to investor type
6. **Integrate reference data** (FEDERAL-TAX-GUIDE, DFI-FUNDING) as appropriate
7. **Produce polished memo** ready for light editing and submission

### Investor Type Branching

**VC Memo Structure:**
- Executive summary: TAM ($X00B DC market), growth trajectory, why now
- Competitive moat: site control, power access, regulatory relationships, first-mover
- Use of proceeds: allocation across development, construction, operations
- Team: founder/operator credentials, domain expertise, advisory board
- Financial highlights: revenue CAGR, $/MW development cost advantage, time-to-revenue
- Market analysis: supply-demand dynamics, customer pipeline, LOIs
- Path to exit: trade sale to REIT/infrastructure fund, secondary, IPO comps
- Key metrics: revenue CAGR, customer pipeline MW, $/MW cost advantage, months to revenue

**PE/Infrastructure Memo Structure:**
- Asset overview: location, capacity, tenant mix, lease terms
- Stabilized yield: NOI, cap rate, EBITDA multiple context
- Capital structure: debt capacity, DSCR analysis (reference FEDERAL-TAX-GUIDE.md for tax benefits enhancing debt capacity)
- CapEx/OpEx breakdown: per-MW economics, operating leverage
- Downside protection: contracted revenue, long-term PPAs, take-or-pay structures
- Value creation: expansion potential, PUE improvement, density upgrades
- Comparable transactions: recent DC M&A multiples and pricing
- Key metrics: stabilized NOI, cap rate, levered IRR, MOIC, debt yield, DSCR

**DFI Memo Structure:**
- Development impact thesis: FIRST section (before financial returns)
- Job creation: construction and permanent, direct and indirect, skills development
- Digital inclusion: connectivity beneficiaries, digital economy contribution
- Technology transfer: local capacity building, university partnerships, training programs
- ESG alignment: Scope 1/2 emissions, water efficiency, community benefits
- Concessional financing structure: how DFI capital de-risks private co-investment
- Institution-specific alignment: reference DFI-FUNDING.md for IFC Performance Standards, AfDB strategic priorities, EBRD transition impact
- Financial summary: project economics supporting the impact thesis
- Key metrics: jobs created, GDP impact, digital connectivity beneficiaries, ESG scores

**Sovereign Wealth Memo Structure:**
- Strategic allocation rationale: infrastructure as real asset, inflation hedge
- Sovereign compute capacity: national AI infrastructure, data sovereignty
- Long-horizon returns: 20-30 year DCF, patient capital advantage
- Portfolio fit: correlation to existing holdings, infrastructure allocation target
- Co-investment structures: club deal, JV, direct, fund commitment
- Governance protections: board seats, information rights, consent rights
- National strategic value: digital infrastructure, workforce development, technology sovereignty
- Key metrics: long-term IRR, inflation-adjusted returns, strategic value index

### Reference Data

Load these files on demand -- do not read upfront:

- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- ITC/PTC, MACRS, Section 179D for tax benefit structuring (PE/infra memos)
- [DFI funding](../../references/DFI-FUNDING.md) -- Institution profiles, eligibility criteria, strategic priorities (DFI memos)
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Typical investor | PE/Infra | PE/Infra, SWF | DFI, SWF | VC, PE | VC | VC |
| Investment size | $50-500M | $500M-5B+ | $200M-2B | $50-500M | $10-100M | $5-50M |
| Key selling point | Yield | Scale, contracts | Strategic | Growth | Speed | Ubiquity |
| Exit mechanism | Trade sale | REIT/secondary | Government buyback | IPO/trade sale | Aggregation | Portfolio sale |

## Output Template

This skill produces a polished investor memo document and a JSON sidecar:
1. `<project-name>-investor-memo.md` -- Submission-ready memo
2. `<project-name>-investor-memo.json` -- Structured data for downstream skills

### JSON Sidecar Schema

```json
{
  "artifact_type": "investor-memo",
  "skill_version": "1.0",
  "project_name": "...",
  "investor_type": "vc | pe_infra | dfi | sovereign_wealth",
  "investment_size": "...",
  "key_metrics": {},
  "financial_summary": {
    "irr": 0,
    "moic": 0,
    "dscr": 0,
    "payback_years": 0
  },
  "risk_factors": [],
  "use_of_proceeds": {},
  "team_summary": "..."
}
```

## Gotchas

- **PE infrastructure funds price DCs on stabilized NOI, not development upside.** Showing construction risk metrics, high CAGR, and "hockey stick" revenue projections to infrastructure buyers signals inexperience. Infra funds want yield, contracted revenue, and downside protection. Save the growth narrative for VC.

- **DFI investment committees require development impact metrics BEFORE financial returns in the memo structure.** Leading with IRR to an IFC or AfDB committee will get the memo deprioritized. Development impact is the screening criterion; financial returns are the enabling mechanism. Structure accordingly.

- **Sovereign wealth funds typically require board seats or governance rights proportional to their allocation.** A sovereign fund investing 30%+ equity expects at minimum one board seat, key decision consent rights, and quarterly reporting. Memos that don't address governance will be returned for revision before financial analysis begins.

- **VC memos for DC projects must address the capital intensity paradox.** VCs expect capital-efficient growth; DCs are capital-intensive by nature. The memo must explain why VC capital (not project finance) is the right tool -- typically pre-development, site control, and platform buildout before transitioning to project finance for construction.

- **Tax benefits (ITC, MACRS, bonus depreciation) materially improve PE/infra returns but must be modeled correctly.** Reference FEDERAL-TAX-GUIDE.md for current rates. Post-OBBBA 30% ITC on qualifying equipment and 100% bonus depreciation significantly enhance levered equity returns and DSCR. Omitting tax benefits from PE memos understates returns by 200-400 bps IRR.

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

See [Disclaimer Framework](../../references/DISCLAIMER-FRAMEWORK.md) for full terms.

---

## Evaluations

See `evals/evals.json` for test scenarios covering VC Series B, PE/infra stabilized asset,
and DFI Sub-Saharan Africa with IFC co-investment.
