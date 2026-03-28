---
name: bd-government-proposal
description: "Generate a polished government proposal with strategy alignment, economic impact quantification, and ask/offer matrix for DC incentive negotiations. Use when pitching a data center to a government, requesting incentives, writing a government proposal, or structuring an ask/offer for tax breaks and infrastructure support. Trigger with \"government proposal\", \"incentive request\", \"DC government pitch\", \"tax incentive negotiation\", \"ask/offer matrix\", or \"pitch to the government\"."
---

# Government Proposal Generator

Generate a polished government proposal with strategic alignment, economic impact
quantification, and ask/offer matrix. The document adapts tone and framing by
counterparty level -- federal, state, municipal, or foreign government -- to match
the priorities and language of each audience.

This skill produces a submission-ready narrative document, not a data table.
The proposal IS the deliverable.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the proposal's entire framing.

**Proposal Context:**

1. What is the government counterparty level?
   - **Federal:** National government agency (e.g., DoD, DOE, GSA, DFC)
   - **State:** State-level government or economic development authority
   - **Municipal:** City, county, or regional authority
   - **Foreign government:** National or regional government outside the US

2. Who is the specific agency, office, or counterparty?
   - Name the entity and decision-maker level (if known)

3. What is the project capacity and scope?
   - Total IT capacity (MW)
   - Number of phases and timeline
   - Facility type (hyperscale, enterprise, sovereign, colo)

4. What is the project location?
   - Specific site or candidate sites
   - State/country for incentive and regulatory framing

5. What is your ask? (What you need from the government)
   - Land lease or land sale at below-market rate
   - Tax incentives (sales tax, property tax, income tax)
   - Permitting fast-track or streamlined approval
   - Utility commitment (dedicated feed, rate agreement)
   - Grant funding or low-interest financing
   - Infrastructure improvements (road, water, power upgrades)

6. What is your offer? (What you provide to the government/community)
   - Direct permanent jobs (operations, security, maintenance)
   - Construction employment (temporary, with local hiring commitments)
   - Capital investment (total project cost)
   - Tax revenue (property tax, sales tax, income tax)
   - Infrastructure investment (utility upgrades, road improvements)
   - Technology transfer or workforce training programs
   - Community benefits (education partnerships, digital inclusion)

7. What is the project timeline?
   - Construction start and completion targets
   - Phased deployment schedule

8. What is the competitive landscape?
   - Are other developers pitching the same government?
   - What differentiates your project?

## Phase 2: Context Refinement

> Based on counterparty level, gather jurisdiction-specific detail.

### Federal Path

If counterparty is **Federal:**

1. What national priority does this project support?
   - National security / defense compute
   - Compute sovereignty / domestic AI capability
   - CHIPS and Science Act alignment
   - Critical infrastructure resilience
   - Federal cloud / FedRAMP requirements

2. What security classification level is relevant?
   - Unclassified
   - CUI (Controlled Unclassified Information)
   - Secret / Top Secret
   - SCIF requirements

3. What federal funding mechanisms are targeted?
   - DFC (Development Finance Corporation) -- for international projects with US interest
   - DOE grants (clean energy, grid modernization)
   - DoD contracts (defense compute)
   - CHIPS Act incentives

Load reference: REGULATORY-MATRIX.md for sovereignty framing if the project involves allied nations or compute sovereignty positioning.

### State Path

If counterparty is **State:**

1. What state-level incentives are you targeting?
   - Sales and use tax exemption on equipment
   - Property tax abatement or PILOT (Payment in Lieu of Taxes)
   - Income tax credits for job creation
   - Utility rate discount or economic development tariff
   - Infrastructure grants (road, water, power)

2. What economic impact data do you have?
   - Jobs per MW: 30-50 permanent for traditional, 10-20 for hyperscale
   - Construction jobs (peak employment during build)
   - Capital investment multiplier (typically 1.5-2.0x for indirect economic activity)
   - Property tax revenue estimate

3. What is the state's current data center policy stance?
   - Pro-DC with active incentive programs
   - Neutral / no specific DC policy
   - Under review / moratorium concerns

Load reference: US-STATE-INCENTIVES.md for state-specific incentive program details, thresholds, and clawback provisions.

### Municipal Path

If counterparty is **Municipal:**

1. What community concerns need to be addressed proactively?
   - Noise (generator testing, cooling equipment)
   - Water consumption (in water-stressed areas)
   - Grid strain (utility capacity impact on other ratepayers)
   - Visual impact (facility size, lighting, fencing)
   - Traffic (construction phase and ongoing)

2. What community benefits are you offering?
   - Local hiring commitments (% of construction and permanent workforce)
   - Community benefits agreement (CBA)
   - Education partnerships (STEM programs, workforce training)
   - Infrastructure upgrades (roads, utilities, broadband)
   - Tax revenue to local school district and services

3. What is the zoning and permitting situation?
   - Already zoned for industrial / data center use
   - Requires rezoning or special use permit
   - Conditional use permit with public hearing

### Foreign Government Path

If counterparty is **Foreign government:**

1. What is the country's national AI or digital strategy?
   - Name the specific strategy document or initiative
   - How does this project align with stated national goals?

2. What sovereign capability does this project enable?
   - Domestic AI training and inference capacity
   - Data residency and sovereignty compliance
   - Digital infrastructure for government services
   - Technology transfer and local workforce development

3. What DFI (Development Finance Institution) funding is applicable?
   - IFC, AfDB, ADB, EBRD, USTDA, Power Africa, GCF, MIGA

Load references: REGULATORY-MATRIX.md for data protection and ownership requirements, DFI-FUNDING.md for development finance institution alignment (when available).

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location and site scoring results
- Opportunity Zone eligibility (for US projects)
- Tax incentive preliminary assessment
- Utility availability and capacity
- Workforce availability scoring

If upstream artifact is not available, I will gather project details
directly through discovery questions.

## Reference Data

Load on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-level regulatory data for sovereign framing (foreign government path)
- [US state incentives](../../references/US-STATE-INCENTIVES.md) -- State-specific incentive programs, thresholds, and clawback provisions (state/municipal paths)
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- OZ eligibility and federal incentive programs (federal/state paths)

## Output Template

This skill produces two files:

### Narrative Document: `<project-name>-government-proposal.md`

A polished proposal document with persuasive narrative -- not a data table.
The document is the deliverable, ready for light editing and submission.

**Cover Page**
- Project name
- Developer / company name
- Counterparty name and title
- Date

**1. Executive Summary** (1 page)
- Project overview in 2-3 sentences
- Strategic alignment headline
- Key economic impact figures
- The ask, concisely stated

**2. Strategic Alignment**
- How this project supports the government's stated priorities
- Federal: national security, compute sovereignty, CHIPS Act goals
- State: economic development strategy, workforce development, innovation economy
- Municipal: community development plan, infrastructure modernization
- Foreign: national AI/digital strategy, sovereign capability goals

**3. Project Overview**
- Facility description (capacity, technology, timeline)
- Location rationale
- Development team qualifications
- Project milestones

**4. Economic Impact**
- Direct jobs (permanent operations + construction)
- Capital investment
- Tax revenue (property, sales, income -- with annual estimates)
- Indirect economic activity (multiplier effects)
- Workforce development commitments
- Note: jobs-per-MW varies by facility type -- use project-specific numbers

**5. Ask/Offer Matrix**
- Structured as narrative, not raw table
- What the developer asks: specific incentives, commitments, or support
- What the developer offers: jobs, investment, tax revenue, community benefits
- Value proposition: government gets more than it gives

**6. Implementation Timeline**
- Phased milestones with dates
- Government decision points and dependencies
- Construction and operational milestones

**7. Risk Mitigation**
- How community concerns are addressed
- Environmental commitments (water, noise, visual)
- Clawback willingness (demonstrates confidence in commitments)
- Track record of similar projects

**8. Appendices**
- Supporting economic data
- Site plans or renderings (reference)
- Developer qualifications and references
- Letters of intent (if applicable)

### JSON Sidecar: `<project-name>-government-proposal.json`

```json
{
  "artifact_type": "government-proposal",
  "skill_version": "1.0",
  "project_name": "...",
  "counterparty_level": "federal | state | municipal | foreign",
  "counterparty_entity": "...",
  "project_capacity_mw": 0,
  "location": "...",
  "ask_summary": ["..."],
  "offer_summary": ["..."],
  "economic_impact": {
    "permanent_jobs": 0,
    "construction_jobs": 0,
    "capital_investment_usd": 0,
    "annual_tax_revenue_usd": 0,
    "economic_multiplier": 0
  },
  "incentives_requested": ["..."],
  "reference_data_used": ["US-STATE-INCENTIVES.md", "REGULATORY-MATRIX.md"]
}
```

## Gotchas

- **Government proposals are NOT investor pitches.** Lead with public benefit, not private returns. The ask/offer matrix must show the government gets more than it gives. If the value proposition does not clearly favor the public side, the proposal will fail regardless of project quality.

- **Jobs-per-MW varies wildly by facility type.** Traditional facilities: 30-50 permanent per 100MW. Hyperscale (highly automated): 10-20 per 100MW. Never use industry averages -- always calculate from YOUR facility staffing plan. Overstating jobs is the fastest way to trigger clawback provisions and lose government credibility.

- **Municipal proposals must address community opposition risks upfront.** Noise, water consumption, grid strain, visual impact, and traffic are the top 5 community concerns. Ignoring them ensures city council rejection. Proactive community benefits agreements (CBAs) with specific commitments convert opposition into support.

- **Foreign government proposals must reference the country's national AI/digital strategy by name.** Generic language about "digital transformation" signals you have not done homework. Name the strategy (e.g., Kenya's "Digital Economy Blueprint," Saudi Arabia's "Vision 2030 NEOM"), cite specific goals, and map your project to those goals.

- **State incentive clawback provisions are real and enforced.** If you commit to 50 permanent jobs and only deliver 35, the state will claw back the tax exemption -- retroactively. Undercommit and overdeliver. Build a 20% buffer into all job and investment commitments.

## Evaluations

See `evals/evals.json` for test scenarios covering state, federal, and foreign government proposals.
