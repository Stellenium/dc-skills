---
name: bd-rfp-response
description: "Prepare a comprehensive RFP response for data center procurement with compliance matrix, technical narrative, pricing tables, and win themes. Use when responding to a data center RFP, preparing a bid response, mapping compliance to requirements, or writing a competitive proposal for DC services. Trigger with \"RFP response\", \"bid response\", \"respond to RFP\", \"compliance matrix\", \"proposal response\", or \"help me win this RFP\"."
---

# RFP Response Generator

Prepare a comprehensive RFP response with compliance matrix, technical and management
approach narratives, win theme development, relevant experience case studies, and
pricing structure. The response document IS the deliverable -- a polished, submission-ready
package for light editing and final review.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire response strategy.

**RFP Context:**

1. What is the RFP document?
   - Provide the RFP text, or describe its key sections and requirements
   - Identify the issuing entity (government agency, enterprise, hyperscale provider)
   - Note the RFP number/reference and submission deadline

2. What is your company profile?
   - Company name, headquarters, years in operation
   - Core capabilities relevant to this RFP
   - Annual revenue and financial stability indicators
   - Relevant certifications (SOC 2, ISO 27001, Uptime Tier certifications)

3. What are your key differentiators?
   - What makes your response stronger than competitors?
   - Unique capabilities, proprietary technology, or geographic advantage
   - Financial strength or backing (parent company, investor grade)
   - Operational track record (uptime history, number of facilities)

4. What relevant experience do you have?
   - 2-3 similar projects completed (type, scale, customer segment)
   - Customer references available for citation
   - Any prior work with this specific issuer

5. What is your pricing strategy?
   - Aggressive (win on price), premium (win on quality), or balanced
   - Pricing model: per-kW, per-cabinet, per-sqft, or custom
   - Are there pricing constraints or floor margins?

6. What is the team composition?
   - Key personnel for the project (project manager, technical lead, operations)
   - Resumes or qualifications available for submission
   - Local presence or planned local office

7. What is the submission deadline?
   - Hard deadline (date and time with timezone)
   - Pre-submission conference date (if any)
   - Questions/clarifications deadline

8. Are there known compliance gaps?
   - Requirements you cannot fully meet
   - Areas where you plan to offer alternatives
   - Subcontracting or partnering strategy for gap coverage

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather RFP-specific detail.

### Requirement Analysis

1. How many discrete requirements does the RFP contain?
   - Count all SHALL/MUST/REQUIRED items
   - Identify optional/desired items separately
   - Flag ambiguous requirements needing clarification

2. What are the evaluation criteria and weights?
   - Technical approach: [weight %]
   - Management approach: [weight %]
   - Past performance / experience: [weight %]
   - Price: [weight %]
   - Small business / diversity participation: [weight %]

3. What format and page constraints does the RFP specify?
   - Volume structure (technical, management, past performance, price as separate volumes)
   - Page limits per volume
   - Font, margin, and formatting requirements
   - Required forms and certifications

### Competitive Intelligence

1. Who are the likely competing bidders?
   - Known incumbents or pre-qualified vendors
   - Competitor strengths and weaknesses
   - Is this a re-compete of an existing contract?

2. What is the customer's hot button?
   - Speed to delivery / schedule
   - Price sensitivity
   - Technical innovation
   - Reliability / risk aversion
   - Local economic impact

## Win Theme Development

Identify 2-3 win themes from discovery -- differentiators that distinguish your
response from competitors. Every narrative section must reference at least one
win theme. Win themes are the thread that ties the entire response together.

**Common win theme categories:**
- **Speed to market:** Faster delivery through modular construction, pre-approved designs, or existing inventory
- **Financial strength:** Parent company backing, investment-grade credit, bonding capacity
- **Local expertise:** Existing facilities in the region, local workforce, community relationships
- **Operational track record:** Uptime history, number of facilities managed, customer retention rate
- **Technical innovation:** Proprietary cooling technology, sustainability leadership, AI-ready infrastructure
- **Risk reduction:** Proven delivery methodology, phased approach, performance guarantees

## Output Template

This skill produces two files:

### Response Document: `<project-name>-rfp-response.md`

**RFP Reference:** [RFP Number]
**Respondent:** [Company Name]
**Date:** [Submission Date]
**Prepared by:** [Skill: bd-rfp-response v1.0]

#### 1. Compliance Matrix

Map every RFP requirement to a compliance status. Missing requirements are automatic
disqualifiers -- the matrix must cover 100% of stated requirements.

| Req ID | Requirement Text (summary) | Status | Response Section | Explanation |
|--------|---------------------------|--------|-----------------|-------------|
| [ID] | [Requirement summary] | Compliant | [Section ref] | -- |
| [ID] | [Requirement summary] | Partial | [Section ref] | [How gap is addressed] |
| [ID] | [Requirement summary] | Exception | [Section ref] | [Alternative proposal] |

**Status definitions:**
- **Compliant:** Fully meets the requirement as stated
- **Partial:** Meets the requirement with minor deviations or conditions; explanation provided
- **Exception:** Cannot meet the requirement as stated; alternative approach proposed

#### 2. Executive Summary (1-2 pages)

- Project understanding and approach overview
- Win themes woven throughout -- each theme stated explicitly
- Key value proposition in 2-3 sentences
- Compliance summary (e.g., "Compliant with 48 of 50 requirements; 2 Partial with alternative approaches")

#### 3. Technical Approach

- Solution architecture aligned to RFP technical requirements
- Phased delivery plan with milestones
- Risk mitigation strategy for technical risks
- **Win theme integration:** Reference applicable win themes (e.g., speed to market through modular approach, technical innovation through liquid cooling)
- Compliance cross-references to specific RFP requirement IDs

#### 4. Management Approach

- Project team organization chart and key personnel
- Governance structure and decision-making authority
- Communication plan (reporting cadence, escalation procedures)
- Quality assurance and quality control processes
- **Win theme integration:** Reference applicable win themes (e.g., operational track record, local expertise)

#### 5. Relevant Experience / Past Performance

- 2-3 case studies demonstrating capability for similar projects
- Each case study includes: project scope, challenges overcome, results delivered, customer reference
- Case studies selected to reinforce win themes
- Relevance mapping: how each case study addresses specific RFP requirements

#### 6. Win Themes Summary

| Theme | Evidence | Sections Referenced |
|-------|----------|-------------------|
| [Theme 1] | [Specific proof point] | Executive Summary, Technical Approach |
| [Theme 2] | [Specific proof point] | Management Approach, Past Performance |
| [Theme 3] | [Specific proof point] | Technical Approach, Past Performance |

#### 7. Pricing Section

- Pricing structure aligned to RFP-specified format
- Unit pricing (per-kW, per-cabinet, per-sqft as required)
- Term structure and escalation provisions
- Options pricing (expansion, additional services)
- Note: This section formats pricing for submission -- it is not a pricing calculator

#### 8. Required Forms and Certifications

- List of all required forms with completion status
- Certifications provided (SOC 2, ISO 27001, Uptime Tier, etc.)
- Representations and warranties

### JSON Sidecar: `<project-name>-rfp-response.json`

```json
{
  "artifact_type": "rfp-response",
  "skill_version": "1.0",
  "rfp_reference": "...",
  "respondent": "...",
  "submission_date": "...",
  "compliance_matrix": {
    "total_requirements": 0,
    "compliant": 0,
    "partial": 0,
    "exception": 0,
    "compliance_rate_pct": 0
  },
  "win_themes": ["..."],
  "case_studies": [
    {
      "project_name": "...",
      "relevance": "...",
      "scale_mw": 0
    }
  ],
  "pricing_model": "per-kw | per-cabinet | per-sqft | custom",
  "evaluation_criteria_addressed": ["..."]
}
```

## Gotchas

- **The compliance matrix must cover 100% of stated RFP requirements.** Missing a single requirement -- even a minor administrative one -- can result in a "non-responsive" determination that eliminates your bid before evaluation begins. Map every SHALL/MUST/REQUIRED item, no exceptions.

- **Exception responses need clear alternative proposals, not just "we don't do this."** An Exception status without a compelling alternative is a scored zero. Propose a specific alternative that achieves the issuer's underlying intent, explain why the alternative is equal or better, and provide evidence of success with the alternative approach.

- **Win themes must appear in every section, not just the executive summary.** Evaluators often score individual sections independently. If your win theme of "speed to market" only appears in the executive summary but not in the technical approach section, the technical evaluator never sees it. Repeat and reinforce themes throughout.

- **Page and format constraints from the RFP itself must be honored exactly.** Exceeding page limits, using wrong fonts, or missing required section headers are grounds for rejection in government procurements. In enterprise RFPs, they signal inattention to detail. Always verify formatting compliance before submission.

- **Pricing volumes are often evaluated separately from technical volumes.** Do not embed pricing details in the technical narrative. Price references in technical sections (e.g., "cost-effective approach") should be qualitative, not quantitative. Cross-contamination between technical and price volumes is a common disqualification reason in government RFPs.

## Evaluations

See `evals/evals.json` for test scenarios covering government, enterprise, and hyperscale RFP responses.
