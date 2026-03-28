---
name: predev-mou-framework
description: "Generate MOU and LOI documents for data center development projects adaptive to government, landowner, utility, and anchor tenant counterparties. Use when drafting an MOU or LOI for a DC deal, structuring early-stage agreements, or formalizing preliminary terms with a counterparty for a data center project. Trigger with \"MOU\", \"LOI\", \"memorandum of understanding\", \"letter of intent\", \"DC preliminary agreement\", or \"early-stage deal terms\"."
argument-hint: "<counterparty-type>"
---

# MOU/LOI Framework

Generate MOU (Memorandum of Understanding) and LOI (Letter of Intent) documents
adaptive to counterparty type for data center development projects. The document
IS the deliverable -- ready for legal review and counterparty submission. Adapts
term structure, language, and provisions by counterparty type.

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Site location and jurisdiction
- Utility availability and capacity assessment
- Land ownership and lease structure findings
- Tax incentive eligibility
- GO/CONDITIONAL/NO-GO recommendation

If upstream artifact is not available, I will gather project details
directly through discovery questions or generate placeholders marked [DATA NEEDED].

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire document structure.

**Agreement Context:**

1. What type of counterparty?
   - **Government:** Federal, state, or municipal agency (tax incentives, land, permitting)
   - **Landowner:** Private or institutional land/building owner (lease, purchase option)
   - **Utility:** Electric utility or power provider (capacity commitment, interconnection)
   - **Technology partner:** OEM, cloud provider, or anchor tenant (capacity reservation, SLA)

2. What document type?
   - MOU (broader framework, multiple areas of cooperation)
   - LOI (specific transaction, precursor to definitive agreement)

3. Binding or non-binding?
   - Fully non-binding (statement of intent only)
   - Non-binding with binding provisions (confidentiality, exclusivity, cost allocation)
   - Fully binding (enforceable obligations -- rare for MOUs)

4. Is exclusivity required?
   - No exclusivity (either party free to negotiate with others)
   - Mutual exclusivity (both parties commit to negotiate only with each other)
   - One-way exclusivity (specify which party is bound)
   - Exclusivity with breakup fee

5. What jurisdiction governs?
   - US state (specify state)
   - International (specify country)
   - Multiple jurisdictions (specify primary)

6. What is the project stage?
   - Early exploration (no site selected, seeking options)
   - Site identified (specific site, seeking commitment)
   - Pre-development (site secured, seeking supporting agreements)

7. What is the target timeline for definitive agreement?
   - 30-60 days (fast track)
   - 60-120 days (standard)
   - 120+ days (complex negotiation expected)

8. What is the project scale?
   - Total capacity (MW)
   - Total estimated investment ($)
   - Number of phases

## Phase 2: Context Refinement

> Based on counterparty type, gather specific detail.

### Government Path

If counterparty is **Government:**

1. What government level? (federal, state, municipal)
2. What commitments are sought? (tax incentives, land, permitting fast-track, infrastructure)
3. What commitments are offered? (jobs, investment, tax revenue, community benefits)
4. Is a clawback provision acceptable? (standard for government incentive agreements)
5. What approval process does the government require? (council vote, commission approval, executive authority)

### Landowner Path

If counterparty is **Landowner:**

1. Is this a lease or purchase?
   - Ground lease (long-term, 20-30 years with options)
   - Purchase option (right to buy at predetermined price)
   - Lease with purchase option (hybrid)
2. What is the site acreage and current use?
3. Are there environmental conditions? (contamination, wetlands, endangered species)
4. Who bears environmental liability? (critical for brownfield sites)
5. What access rights are needed during due diligence? (surveys, soil testing, environmental)

### Utility Path

If counterparty is **Utility:**

1. What is the power commitment sought? (MW at point of interconnection)
2. What is the interconnection timeline expectation?
3. Is a dedicated feed or substation required?
4. What rate structure is expected? (tariff, economic development rate, negotiated)
5. Is dual-feed / diverse path required?
6. Is there an existing interconnection agreement or queue position?

### Technology Partner Path

If counterparty is **Technology partner:**

1. What type of partner? (cloud provider, GPU/server OEM, network carrier, anchor tenant)
2. What capacity reservation? (MW, cabinets, or sqft)
3. What SLA commitments apply? (availability, latency, power density)
4. What exclusivity provisions? (sole provider, preferred provider, ROFR)
5. What IP and data rights apply? (data sovereignty, processing restrictions)
6. What is the minimum commitment period?

## Analysis

### Counterparty-Specific Term Structures

**Government MOU terms:**
- Sovereignty commitments and data residency assurances
- Tax incentive package (property tax abatement/PILOT, sales tax exemption, income tax credits)
- Timeline obligations and milestone commitments
- Clawback provisions tied to job creation and investment thresholds
- Infrastructure commitments (road, water, power upgrades)
- Community benefit commitments
- Confidentiality of commercial terms

**Landowner LOI/MOU terms:**
- Lease term, rent structure, and escalation formula
- Purchase option price, exercise period, and conditions
- Access rights during due diligence period
- Environmental liability allocation and indemnification
- Zoning and entitlement cooperation obligations
- Exclusivity period and breakup fee (if applicable)
- Assignment and subletting rights
- Right of first refusal for adjacent parcels

**Utility MOU terms:**
- Power commitment level (MW) and delivery timeline
- Interconnection scope of work and cost allocation
- Rate structure or rate negotiation framework
- Redundancy and feed configuration requirements
- Demand response and curtailment provisions
- Renewable energy supply options
- Term length and termination provisions
- Service level commitments (outage limits, notification)

**Technology partner MOU terms:**
- Capacity reservation (MW, cabinets, sqft) and ramp schedule
- SLA framework (availability, latency, power density, cooling)
- Exclusivity and right of first refusal provisions
- Pricing framework (rate card, volume discounts, most-favored-nation)
- IP rights and data processing restrictions
- Co-investment or revenue sharing structure
- Term, renewal, and early termination provisions
- Technology refresh and upgrade obligations

## Output

This skill produces two files:
1. `<project-name>-mou-framework.md` -- MOU/LOI document ready for legal review
2. `<project-name>-mou-framework.json` -- Structured metadata

### MOU/LOI Document

**[MOU/LOI] Between [Party A] and [Party B]**
**Date:** [Date]
**Re:** [Project Name] Data Center Development

**1. Purpose and Background**
- Recitals describing the parties and the contemplated transaction

**2. Key Terms**
- Counterparty-specific terms per analysis above
- Milestones and timeline
- Financial commitments

**3. Exclusivity and Confidentiality**
- Exclusivity provisions (if applicable)
- Confidentiality obligations (typically binding even in non-binding MOU)
- Non-disclosure period and scope

**4. Due Diligence / Conditions Precedent**
- Access rights and cooperation obligations
- Information sharing requirements
- Conditions that must be satisfied before definitive agreement

**5. Timeline to Definitive Agreement**
- Target date for definitive agreement execution
- Extension provisions
- Milestones between MOU and definitive agreement

**6. Binding and Non-Binding Provisions**
- Clear statement of which provisions are binding and which are non-binding
- Governing law and dispute resolution (typically binding)
- Cost allocation (each party bears own costs unless specified)

**7. Termination**
- Circumstances under which MOU/LOI terminates
- Effect of termination on binding provisions (confidentiality survives)
- Breakup fee provisions (if applicable)

### JSON Sidecar

```json
{
  "artifact_type": "mou-framework",
  "skill_version": "1.0",
  "project_name": "...",
  "counterparty_type": "government | landowner | utility | tech-partner",
  "document_type": "mou | loi",
  "binding_status": "non-binding | mixed | fully-binding",
  "key_terms": ["..."],
  "exclusivity_provisions": "none | mutual | one-way | with-breakup-fee",
  "jurisdiction": "...",
  "expiration_date": "...",
  "timeline_to_definitive_days": 0,
  "financial_commitments": {},
  "conditions_precedent": ["..."]
}
```

## Gotchas

- **LOI exclusivity clauses can create binding obligations even in otherwise non-binding documents.** Courts have enforced exclusivity and confidentiality provisions in LOIs that explicitly state they are "non-binding." Always clearly identify which specific provisions are binding and which are not. A blanket "non-binding" statement at the top does not override specific binding language in individual clauses.

- **Government MOUs in many US jurisdictions require legislative or commission approval to be enforceable** -- an MOU signed by an economic development director may not bind the city council to deliver tax incentives. Verify the signatory's authority to commit the government entity. Include a condition precedent for any required legislative approval.

- **Utility MOUs are NOT interconnection agreements.** A utility MOU expressing intent to provide 100MW does not reserve capacity in the interconnection queue. The formal interconnection application must be filed separately, and queue position is determined by application date, not MOU date. A 12-month gap between MOU and interconnection application can result in years of additional queue delay.

- **Technology partner exclusivity with minimum commitments can trigger antitrust scrutiny** in markets with limited data center supply. If the partner is a dominant cloud provider and the exclusivity covers a significant portion of regional capacity, seek antitrust counsel before executing.

- **Breakup fees in data center LOIs typically range from 1-3% of total project cost** for the party that walks away. Below 1% provides insufficient incentive to negotiate in good faith; above 3% can be challenged as a penalty clause rather than liquidated damages.

## Evaluations

See `evals/evals.json` for test scenarios covering government, landowner, and utility MOUs.
