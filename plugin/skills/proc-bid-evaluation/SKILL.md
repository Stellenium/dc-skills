---
name: proc-bid-evaluation
description: "Evaluate vendor bids for data center projects with weighted scoring, TCO normalization, risk assessment, and recommendation matrix. Use when comparing vendor proposals, scoring bids, evaluating DC procurement responses, or making a recommendation on which vendor to select. Trigger with \"bid evaluation\", \"vendor comparison\", \"score bids\", \"evaluate proposals\", \"vendor selection\", or \"which vendor should I pick?\"."
---

# Bid Evaluation & Vendor Selection

Evaluate vendor bids with weighted scoring methodology producing a recommendation
memo with comparison matrix, scoring rationale, and risk assessment. Produces a
defensible evaluation document suitable for procurement committee review and audit trail.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the evaluation approach.

**Evaluation Context:**

1. How many bids were received?
   - If fewer than 3: consider whether re-solicitation is warranted
   - List bidders (anonymized as Bidder A, B, C... if preferred)

2. What is the evaluation methodology?
   - **Best Value:** Weighted scoring across technical, price, schedule, and qualifications
   - **LPTA (Lowest Price Technically Acceptable):** Technical pass/fail, then lowest price wins
   - **Qualifications-Based Selection (QBS):** Used for professional services (A/E firms)

3. What are the evaluation criteria categories and weights?
   - Technical approach and methodology: [weight %]
   - Price / commercial terms: [weight %]
   - Schedule / delivery timeline: [weight %]
   - Qualifications and experience: [weight %]
   - Safety record: [weight %]
   - Sustainability / ESG: [weight %]
   - (Weights must sum to 100%)

4. What are the deal-breaker (must-have) requirements?
   - Minimum bond capacity
   - Required licenses and certifications
   - Minimum project experience ($ value, facility type)
   - Insurance minimums
   - Safety record thresholds (EMR, OSHA recordable rate)

5. What is the procurement type?
   - Full data center construction
   - M&E (mechanical & electrical) package
   - IT equipment procurement
   - Managed services
   - Specific trade package

6. Is there an incumbent bidder?
   - Yes (identify which bidder)
   - No
   - If yes: what is the incumbent advantage/disadvantage policy?

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Best-Value Path

If evaluation methodology is Best Value:

1. What sub-criteria exist within each major category?
2. Are there scoring rubrics (1-5 scale, 1-10 scale, adjectival)?
3. Who is on the evaluation committee? (roles, not names)
4. Will oral presentations or interviews be conducted?

### LPTA Path

If evaluation methodology is LPTA:

1. What are the specific pass/fail technical criteria?
2. How is price evaluated? (total price, unit rates, lifecycle cost)
3. Are there any technical preference factors despite LPTA?

### Price Normalization

For all methodologies:

1. Are bid prices on identical scope? If not, what scope differences exist?
2. What cost elements need normalization? (mobilization, overhead, profit, escalation)
3. Should lifecycle cost (TCO) be considered or just initial price?

## What I Need from Upstream

**From rfp-document (proc-rfp-generator):**
- Original evaluation criteria and weights
- Technical requirements (for compliance checking)
- Submission requirements (for responsiveness check)
- Commercial terms (for price comparison baseline)
- Scoring methodology defined in the RFP

If upstream RFP artifact is not available, I will ask you to provide
the evaluation criteria and technical requirements directly.

## Evaluation Process

### Step 1: Responsiveness Check
- Verify all required documents submitted
- Confirm bid bond (if required) is present and valid
- Check submission deadline compliance
- Verify all mandatory forms completed
- Result: Responsive or Non-Responsive (non-responsive bids eliminated)

### Step 2: Compliance Matrix
- Evaluate each must-have requirement as Pass/Fail
- Document specific evidence for each pass/fail determination
- Any single Fail on a must-have requirement eliminates the bidder
- Result: Compliant or Non-Compliant

### Step 3: Technical Scoring
- Score each technical sub-criterion using defined rubric
- Document specific strengths and weaknesses per bidder
- Apply technical category weight
- For LPTA: technical scoring is pass/fail only

### Step 4: Price Analysis
- Normalize bid prices to identical scope
- Calculate total evaluated price including lifecycle costs (if applicable)
- Check for unbalanced pricing (abnormally high/low line items)
- Compare against independent cost estimate (ICE) or should-cost
- Apply price category weight

### Step 5: Schedule and Qualifications Scoring
- Evaluate proposed schedules against required milestones
- Score qualifications: relevant experience, team resumes, references
- Apply respective category weights

### Step 6: Risk Assessment
- Financial stability (bonding capacity, credit, annual revenue vs project size)
- Capacity (current backlog vs available workforce)
- Technical risk (approach feasibility, innovation risk)
- Schedule risk (aggressive timeline, weather/seasonal factors)
- Reference check results (independently verified)

### Step 7: Recommendation
- Rank bidders by total weighted score
- Document recommendation rationale
- Identify conditions or clarifications needed before award
- Note minority/disadvantaged business participation (if tracked)

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical bid count | 3-5 | 5-8 | 3-5 | 3-5 | 3-5 | 2-3 |
| Price weight emphasis | Medium | Medium | Low | Medium | High | High |
| Technical weight emphasis | High | High | High | Medium | Medium | Low |
| Qualifications emphasis | Medium | Medium | Very High | Medium | Low | Low |
| Security screening | None | Limited | Extensive | Limited | None | None |

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-bid-evaluation-memo.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: proc-bid-evaluation v1.0]

#### 1. Executive Summary
- Recommended bidder and rationale (1 paragraph)
- Total number of bids received and evaluated
- Evaluation methodology used
- Key discriminators between top-ranked bidders

#### 2. Responsiveness and Compliance Matrix

| Requirement | Bidder A | Bidder B | Bidder C |
|-------------|----------|----------|----------|
| Bid bond submitted | Pass/Fail | Pass/Fail | Pass/Fail |
| [Must-have requirement 1] | Pass/Fail | Pass/Fail | Pass/Fail |
| [Must-have requirement 2] | Pass/Fail | Pass/Fail | Pass/Fail |
| **Compliance Result** | **Compliant/Non** | **Compliant/Non** | **Compliant/Non** |

#### 3. Scoring Summary

| Category | Weight | Bidder A | Bidder B | Bidder C |
|----------|--------|----------|----------|----------|
| Technical | [%] | [score] | [score] | [score] |
| Price | [%] | [score] | [score] | [score] |
| Schedule | [%] | [score] | [score] | [score] |
| Qualifications | [%] | [score] | [score] | [score] |
| **Weighted Total** | **100%** | **[total]** | **[total]** | **[total]** |
| **Rank** | | **[1/2/3]** | **[1/2/3]** | **[1/2/3]** |

#### 4. Detailed Bidder Analysis
- Per-bidder sections with strengths, weaknesses, and scoring rationale
- Price normalization details and scope adjustment notes

#### 5. Risk Assessment

| Risk Factor | Bidder A | Bidder B | Bidder C |
|-------------|----------|----------|----------|
| Financial stability | Low/Med/High | Low/Med/High | Low/Med/High |
| Capacity | Low/Med/High | Low/Med/High | Low/Med/High |
| Technical | Low/Med/High | Low/Med/High | Low/Med/High |
| Schedule | Low/Med/High | Low/Med/High | Low/Med/High |

#### 6. Recommendation
- Recommended bidder with award conditions
- Clarifications or negotiations needed before contract execution
- Minority/disadvantaged business participation summary (if applicable)

### JSON Sidecar: `<project-name>-bid-evaluation-memo.json`

```json
{
  "artifact_type": "bid-evaluation-memo",
  "skill_version": "1.0",
  "project_name": "...",
  "evaluation_methodology": "best-value | lpta | qbs",
  "procurement_type": "construction | equipment | managed-services | trade-package",
  "bidder_count": 0,
  "compliant_bidder_count": 0,
  "evaluation_criteria": [
    {"name": "Technical", "weight": 40},
    {"name": "Price", "weight": 30},
    {"name": "Schedule", "weight": 15},
    {"name": "Qualifications", "weight": 15}
  ],
  "bidder_rankings": [
    {
      "bidder": "Bidder A",
      "rank": 1,
      "total_weighted_score": 0.00,
      "compliant": true,
      "recommended": true
    }
  ],
  "recommended_bidder": "Bidder A",
  "award_conditions": ["..."]
}
```

## Gotchas

- **LPTA evaluations must still document technical scoring.** LPTA means price is the deciding factor among compliant bids, not that technical evaluation doesn't happen. Technical pass/fail criteria must be rigorously applied and documented -- cutting corners on technical review in LPTA is the leading cause of procurement protests.

- **Always check references independently.** 90% of vendor-provided references are curated successes. Request "any project over $X in the last 3 years" instead of "your best 3 projects." Call references directly and ask about schedule performance, change order frequency, and safety incidents -- not just overall satisfaction.

- **Price normalization across bids with different scope assumptions can swing rankings by 20-30%.** Before comparing prices, normalize all bids to identical scope: same mobilization assumptions, same general conditions, same allowance amounts, same escalation basis year. Without normalization, you are comparing different projects, not different bidders.

- **Unbalanced bids are a red flag, not just a pricing strategy.** A bidder who front-loads early line items (mobilization, excavation) and underprices later items (commissioning, testing) may plan to submit change orders or cut corners on completion. Flag bids where any line item deviates more than 30% from the independent cost estimate.

- **Two bids may warrant re-solicitation rather than evaluation.** With only two bidders, there is insufficient competition to ensure market pricing. Document the decision to proceed or re-solicit, including market conditions and timeline constraints that justify proceeding with two bids.

## Evaluations

See `evals/evals.json` for test scenarios covering best-value construction, LPTA equipment, and incumbent bias evaluation.
