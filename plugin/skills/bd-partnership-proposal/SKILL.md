---
name: bd-partnership-proposal
description: "Generate a partnership or joint venture proposal with strategic rationale, contribution framework, governance structure, and exit mechanisms. Use when proposing a DC joint venture, structuring a partnership agreement, defining contribution frameworks, or writing a partnership pitch for a data center project. Trigger with \"partnership proposal\", \"joint venture\", \"JV proposal\", \"DC partnership\", \"contribution framework\", or \"propose a joint venture\"."
---

# Partnership & JV Proposal Generator

Generate a polished partnership or joint venture proposal with strategic
rationale, contribution framework, governance structure, and term sheet.
The document adapts to partner type and proposed structure to produce a
submission-ready proposal.

This skill produces a polished narrative document, not a data table.
The proposal IS the deliverable.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the proposal framing.

**Partnership Context:**

1. What is the partner type?
   - **Technology:** Cloud hyperscaler, compute provider, AI platform (contributes compute/technology/customers)
   - **Infrastructure:** Utility, landowner, power company (contributes land/power/permits)
   - **Financial:** PE fund, infrastructure fund, pension, sovereign wealth fund (contributes equity/debt capital)
   - **Government/Sovereign:** Government entity, DFI, sovereign wealth fund with policy objectives (contributes land/incentives/regulatory support)

2. What is the proposed structure?
   - **Joint venture (JV):** New entity co-owned by partners
   - **Strategic partnership:** Contractual arrangement without equity JV
   - **Development agreement:** One party develops, other provides resources
   - **Concession:** Government grants operating rights for defined period

3. What is the proposed equity split range?
   - 50/50
   - Majority/minority (specify range)
   - To be negotiated (what factors determine split?)

4. What does each partner contribute?
   - **Capital:** Cash equity, debt financing, guarantees
   - **Land:** Owned, leased, option on land
   - **Power:** Utility interconnection, PPAs, BTM generation
   - **Technology:** Compute platforms, networking, IP
   - **Customers:** Anchor tenant commitment, pre-lease pipeline
   - **Permits:** Entitlements, environmental approvals, government relationships

5. What is the project stage?
   - Concept / pre-feasibility
   - Feasibility complete, seeking development partner
   - Permitted, seeking financial partner
   - Under construction, seeking operational partner
   - Operating, seeking expansion partner

6. What is the total project scope?
   - IT capacity (MW)
   - Number of phases
   - Estimated total investment
   - Target markets / geography

7. Is exclusivity being offered or requested?
   - Geographic exclusivity (radius)
   - Technology exclusivity (platform)
   - Customer exclusivity (tenant restrictions)
   - No exclusivity

## Phase 2: Context Refinement

> Based on partner type, gather additional detail.

### Technology Partner Path

If partner type is **Technology:**

1. What is the compute commitment? (MW reserved, minimum term)
2. What pricing framework applies? (market rate, discounted, cost-plus)
3. What SLA guarantees are required by the technology partner?
4. What is the technology refresh cycle expectation? (3-5 year GPU replacement)
5. What IP rights apply to custom infrastructure? (proprietary cooling, power designs)

### Infrastructure Partner Path

If partner type is **Infrastructure:**

1. What is the land/power contribution valuation methodology? (appraisal, market comp, income approach)
2. Is the structure a lease or equity contribution?
3. What development milestone obligations does the infrastructure partner have?
4. Who is responsible for ongoing operations and maintenance?

### Financial Partner Path

If partner type is **Financial:**

1. What is the equity contribution schedule? (upfront, milestone-based, capital calls)
2. What preferred return is expected? (8-12% for infrastructure funds)
3. What is the waterfall distribution structure? (return of capital, preferred return, GP catch-up, carried interest)
4. What governance rights does the financial partner require? (board seats, protective provisions, ROFO/ROFR)
5. What is the target hold period and exit mechanism? (IPO, secondary sale, buy-sell)

### Government/Sovereign Partner Path

If partner type is **Government/Sovereign:**

1. What concession terms are proposed? (duration, renewal, transfer restrictions)
2. What incentive commitments is the government making? (tax holidays, subsidies, land)
3. What local content requirements apply? (workforce, procurement, manufacturing)
4. What sovereignty protections are required? (data residency, ownership restrictions, technology transfer)
5. What dispute resolution mechanism is acceptable? (local courts, international arbitration, treaty protection)

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location and site characteristics
- Utility availability and capacity
- Regulatory environment summary
- Market attractiveness scoring

**From project-financial-model (fin-project-model):**
- Total project cost and phasing
- Revenue projections and return metrics
- Capital structure assumptions
- Sensitivity analysis results

If upstream artifacts are not available, I will gather project details
directly through discovery questions.

## Partner Type Analysis

### Technology Partner Proposal

**Key sections:**
- Compute commitment and capacity reservation framework
- Pricing methodology (market rate, discount to market, cost-plus margin)
- SLA guarantees and performance measurement
- Technology refresh cycle and CapEx obligations (who funds GPU upgrades)
- IP rights for custom infrastructure designs
- Exclusivity radius and competitive restrictions

### Infrastructure Partner Proposal

**Key sections:**
- Land/power contribution valuation methodology and agreed value
- Lease vs equity structure comparison and recommendation
- Development milestone obligations and timeline
- Operating responsibility allocation (who runs day-to-day)
- Environmental and permitting responsibility

### Financial Partner Proposal

**Key sections:**
- Investment thesis and return profile
- Equity contribution schedule with capital call mechanics
- Preferred return structure (8-12% for infrastructure, higher for development risk)
- Waterfall distribution: return of capital -> preferred return -> GP catch-up -> carried interest
- Governance framework: board composition, protective provisions, major decision list
- Exit mechanisms: ROFO/ROFR, buy-sell, tag/drag, IPO path

### Government/Sovereign Partner Proposal

**Key sections:**
- Strategic alignment with national/regional development objectives
- Concession terms and duration
- Incentive package: tax holidays, land, infrastructure, utility commitments
- Local content: workforce hiring commitments, local procurement targets, technology transfer
- Sovereignty protections: data residency guarantees, ownership structure, dispute resolution
- DFI funding alignment (reference DFI-FUNDING.md if applicable)

## Term Sheet Section

Every proposal includes a structured term sheet with the following fields:

| Term | Description |
|------|-------------|
| **Parties** | Legal entities and roles |
| **Structure** | JV, partnership, concession, development agreement |
| **Contributions** | What each party contributes (capital, land, power, technology, customers) |
| **Equity Split** | Ownership percentages with adjustment mechanisms |
| **Governance** | Board composition, voting rights, protective provisions |
| **Economics** | Preferred return, distribution waterfall, management fees |
| **Exclusivity** | Geographic, technology, or customer exclusivity terms |
| **Term** | Duration, renewal options, extension mechanisms |
| **Exit** | ROFO, ROFR, buy-sell, tag-along, drag-along |
| **Dispute Resolution** | Governing law, arbitration, deadlock mechanism |
| **Conditions Precedent** | Regulatory approvals, financing, permits |

## Output Template

This skill produces two files:

### Narrative Document: `<project-name>-partnership-proposal.md`

A polished proposal document with persuasive narrative -- not a data table.
The document is the deliverable, ready for light editing and submission.

**Cover Page**
- Project name and partnership title
- Developer / sponsor name
- Partner name (or "Confidential -- Partner Selection")
- Date

**1. Executive Summary** (1 page)
- Partnership opportunity overview
- Strategic rationale (why this partnership, why now)
- Key commercial terms headline
- Value creation thesis

**2. Strategic Rationale**
- Market opportunity and timing
- Complementary capabilities analysis
- Competitive advantage of the partnership
- Alignment with partner's strategic priorities

**3. Project Overview**
- Facility description (capacity, technology, location, timeline)
- Development plan and phasing
- Market positioning and tenant pipeline
- Financial summary (top-line, not detailed model)

**4. Contribution Framework**
- What each partner brings (detailed)
- Contribution valuation methodology
- Milestone obligations per partner

**5. Governance Structure**
- Board composition and voting mechanics
- Protective provisions for each partner
- Major decisions requiring unanimous consent
- Deadlock resolution mechanism
- Management and operations oversight

**6. Economics**
- Equity split and adjustment mechanisms
- Preferred return and distribution waterfall
- Management fees and cost allocation
- Tax structuring considerations

**7. Term Sheet**
- Structured commercial terms per template above

**8. Next Steps**
- Proposed timeline: LOI -> due diligence -> definitive agreement -> closing
- Key workstreams and responsible parties
- Conditions precedent

### JSON Sidecar: `<project-name>-partnership-proposal.json`

```json
{
  "artifact_type": "partnership-proposal",
  "skill_version": "1.0",
  "project_name": "...",
  "partner_type": "technology | infrastructure | financial | government-sovereign",
  "structure": "jv | strategic-partnership | development-agreement | concession",
  "contributions": {
    "partner_a": {
      "entity": "Developer",
      "items": ["capital", "development expertise", "operations"]
    },
    "partner_b": {
      "entity": "Partner",
      "items": ["land", "power", "permits"]
    }
  },
  "governance": {
    "board_composition": "3 Developer + 2 Partner + 1 Independent",
    "protective_provisions": ["budget approval", "capital calls >$X", "asset disposition"],
    "major_decisions": ["expansion beyond Phase 1", "additional debt", "change of business"]
  },
  "economics": {
    "equity_split": "60/40",
    "preferred_return": "10%",
    "waterfall": [
      "Return of capital",
      "10% preferred return",
      "GP catch-up to 20%",
      "80/20 carried interest"
    ]
  },
  "term_years": 25,
  "exit_mechanisms": ["ROFO on partner interest", "Buy-sell after year 7", "IPO path after year 5"],
  "term_sheet_summary": {}
}
```

## Gotchas

- **JV operating agreements for DC projects must address technology refresh CapEx obligations explicitly.** Partner disputes over who funds GPU upgrades are the #1 DC JV failure mode. A 100MW AI compute JV will need $500M+ in GPU refresh CapEx every 3-5 years. If the operating agreement is silent on this, the JV will deadlock when the first refresh cycle arrives.

- **"50/50 JV" governance structures require deadlock resolution mechanisms.** Equal partnerships without deadlock provisions fail. Options: swing vote director (independent), buyout trigger (Russian roulette clause), or binding arbitration. The deadlock mechanism must be agreed upfront -- negotiating it during a dispute is impossible.

- **Land contribution valuation in DC JVs is almost always disputed.** The landowner values at retail/entitled price; the developer values at industrial/unentitled price. Resolution: independent appraisal by a firm agreed upon by both parties, or formula-based valuation (e.g., $/acre based on utility capacity available, not comparable land sales).

- **Waterfall structures with GP catch-up clauses are poorly understood by non-financial partners.** A "20% carried interest after 10% preferred return with GP catch-up" means the GP receives 100% of distributions between the preferred return threshold and the catch-up threshold. Infrastructure and government partners frequently object to catch-up clauses retroactively. Explain the waterfall with worked examples in the proposal.

- **Exclusivity clauses in DC partnerships must define the geographic radius precisely.** "Exclusivity in Northern Virginia" is ambiguous. Define by county (Loudoun, Prince William, Fairfax), by radius from site (25 miles), or by submarket (Ashburn campus). Vague exclusivity clauses trigger disputes when partners identify adjacent opportunities.

## Evaluations

See `evals/evals.json` for test scenarios covering technology, infrastructure, and financial partnership proposals.
