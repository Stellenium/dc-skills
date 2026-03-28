---
name: predev-project-narrative
description: "Generate a polished 2-3 page concept paper synthesizing feasibility and market data into a compelling project narrative. Use when preparing a data center project summary for stakeholders, writing a concept paper for investors, or creating a project narrative that tells the story of why this DC should be built. Trigger with \"project narrative\", \"concept paper\", \"DC project summary\", \"tell the story of this project\", or \"project pitch document\"."
---

# Project Narrative

Generate a polished 2-3 page concept paper synthesizing upstream site feasibility
and market study data into a compelling project narrative. The narrative IS the
deliverable -- it must persuade, not just inform. Adapts framing, metrics, and
tone by target audience.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- GO / CONDITIONAL / NO-GO recommendation and weighted score
- Factor scoring matrix (power, connectivity, cost, tax, climate, labor, sovereignty, seismic, water)
- Key strengths and key risks
- Tax incentive summary and Opportunity Zone eligibility
- Site location, facility type, and target capacity

**From market-study (predev-market-study):**
- Supply/demand gap analysis for the target geography
- Absorption rate and vacancy trends
- Pricing benchmarks (per kW, per cabinet, per sqft)
- Demand driver identification (enterprise, hyperscale, AI/HPC, government)
- Anchor tenant pipeline status

If upstream artifacts are not available, I will ask you for the key data points
needed to construct the narrative, or generate placeholders marked [DATA NEEDED].

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire narrative framing.

**Narrative Context:**

1. Who is the target audience?
   - Internal executive team (go/no-go decision framing)
   - Equity investors (IRR/MOIC language, risk-adjusted returns)
   - Debt lenders (DSCR, collateral, downside protection)
   - Government partners (jobs, economic impact, sovereignty, tax revenue)
   - JV / strategic partners (complementary capabilities, market access)

2. What project stage is this?
   - Concept (earliest stage, seeking initial alignment or seed investment)
   - Pre-development (site secured, seeking development capital)
   - Development (permits in hand, seeking construction financing)

3. What are the key selling points to emphasize? Select top 3:
   - Market opportunity (supply gap, demand growth)
   - Location advantage (power, connectivity, cost)
   - Technology differentiation (AI/HPC ready, liquid cooling, sustainability)
   - Financial returns (IRR, MOIC, cash yield)
   - Economic impact (jobs, tax revenue, community benefit)
   - Sovereignty / national security alignment
   - Speed to market (modular, fast-track, pre-permitted)

4. What is the project scale and timeline?
   - Total capacity (MW), number of phases
   - Total estimated investment ($)
   - Target operational date for Phase 1

5. What are the known risks, and do you have mitigants?
   - List the top 3 risks the audience will ask about
   - For each: the mitigant or response you want framed in the narrative

6. What tone is appropriate?
   - Conservative (understated claims, wide ranges, emphasis on downside protection)
   - Balanced (realistic optimism with clear risk acknowledgment)
   - Aggressive (emphasis on upside, market urgency, first-mover advantage)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather audience-specific detail.

### Investor Path

If Phase 1 Q1 = Equity investors or Debt lenders:

1. What is the target return profile? (IRR range, MOIC, cash-on-cash)
2. What comparable transactions should be referenced? (recent DC acquisitions, cap rates)
3. Is there anchor tenant pre-leasing or LOI activity?
4. What is the capital structure assumption? (debt/equity ratio, construction financing)

### Government Path

If Phase 1 Q1 = Government partners:

1. What level of government? (federal, state, municipal, foreign)
2. What economic impact metrics matter most? (permanent jobs, construction jobs, tax revenue, CAPEX)
3. Is there a specific government program or incentive being sought?
4. Are there competing jurisdictions the government should know about?

### Internal Path

If Phase 1 Q1 = Internal executive team:

1. What is the investment committee expecting? (full business case, preliminary screening, go/no-go)
2. Are there competing projects or opportunity costs to acknowledge?
3. What strategic objectives does this project advance?

## Narrative Assembly Process

The concept paper is assembled as a flowing prose document, not a structured data dump.
Each section is 2-4 paragraphs of polished narrative writing.

### Section Flow

1. **Executive Summary** (1 paragraph)
   - The opportunity in one compelling paragraph: what, where, why now, and the ask

2. **The Opportunity** (2-3 paragraphs)
   - Market context from market-study: supply gap, demand drivers, growth trajectory
   - Frame around the audience's priorities (returns for investors, impact for government)
   - Quantify the opportunity with specific metrics

3. **The Site** (2-3 paragraphs)
   - Location strengths from site-feasibility-report: power, connectivity, cost advantage
   - Address any site weaknesses with mitigants (from CONDITIONAL factors)
   - Position the site competitively against alternatives

4. **Market Dynamics** (2-3 paragraphs)
   - Demand analysis: who needs capacity and why (AI/HPC growth, enterprise migration, sovereignty)
   - Supply analysis: current inventory, pipeline, absorption rate
   - Pricing environment and lease-up projections

5. **Financial Overview** (1-2 paragraphs, audience-adapted)
   - **Investors:** IRR/MOIC targets, capital structure, exit scenarios
   - **Government:** CAPEX investment, tax revenue, jobs created per MW
   - **Internal:** NPV, payback period, strategic value beyond financial returns

6. **Development Timeline** (1 paragraph + milestone table)
   - Key milestones from permitting through stabilization
   - Phase deployment schedule

7. **Risks and Mitigants** (2-3 paragraphs)
   - Proactively address known risks with specific mitigants
   - Frame risks as manageable, not dismissible
   - Reference comparable projects that navigated similar challenges

8. **The Ask / Next Steps** (1 paragraph)
   - **Investors:** Investment amount, terms summary, timeline for commitment
   - **Government:** Incentive request, partnership structure, decision timeline
   - **Internal:** Decision requested, resources needed, deadline

## Output

This skill produces two files:
1. `<project-name>-project-narrative.md` -- Polished 2-3 page concept paper
2. `<project-name>-project-narrative.json` -- Structured metadata for downstream skills

### Concept Paper

The markdown output IS the polished narrative -- ready for PDF conversion and distribution
with light editing. Sections flow as prose paragraphs with strategic use of metrics
and emphasis. Not a template with brackets -- a completed narrative.

**Project:** [Project Name]
**Prepared for:** [Audience]
**Date:** [Date]
**Prepared by:** [Organization]

[Flowing prose narrative following the Section Flow above]

### JSON Sidecar

```json
{
  "artifact_type": "project-narrative",
  "skill_version": "1.0",
  "project_name": "...",
  "target_audience": "internal | equity | debt | government | jv-partner",
  "project_stage": "concept | pre-development | development",
  "tone": "conservative | balanced | aggressive",
  "total_capacity_mw": 0,
  "total_investment": 0,
  "key_selling_points": ["..."],
  "site_recommendation": "GO | CONDITIONAL | NO-GO",
  "site_weighted_score": 0.00,
  "market_supply_gap_mw": 0,
  "financial_highlights": {
    "irr_target": "...",
    "jobs_created": 0,
    "tax_revenue_annual": 0
  },
  "key_risks": ["..."],
  "key_mitigants": ["..."]
}
```

## Gotchas

- **A project narrative is NOT a feasibility report summary -- it must persuade, not just inform.** Lead with the opportunity, not the analysis. The feasibility report provides data; the narrative tells a story. Reorganize data around the audience's decision framework, do not simply restate factor scores.

- **Government audiences care about jobs-per-MW -- typically 30-50 permanent jobs per 100MW, plus 500-2,000 construction jobs.** Always quantify economic impact with specific numbers. Tax revenue projections (property tax, sales tax, income tax) must be annualized and cumulative over the project life.

- **Investor narratives must acknowledge risks upfront -- burying them kills credibility.** Sophisticated investors read the risks section first. Weak risk disclosure signals either naivete or deception. Frame risks with specific mitigants and comparable precedents.

- **The "ask" must be specific.** "We are seeking investment" is not an ask. "$75M in equity for a 60% ownership stake with 18% target IRR and 2.0x MOIC over a 7-year hold" is an ask. Vague asks signal an unprepared developer.

## Evaluations

See `evals/evals.json` for test scenarios covering investor, government, and internal narratives.
