---
name: proc-rfp-generator
description: "Generate RFP documents for data center equipment and services with technical specifications, evaluation criteria, and scoring methodology. Use when creating an RFP for DC equipment, writing procurement documents, defining evaluation criteria for vendor selection, or building scoring rubrics for bids. Trigger with \"RFP\", \"request for proposal\", \"procurement RFP\", \"vendor RFP\", \"equipment RFP\", \"generate an RFP\", or \"write a data center RFP\"."
argument-hint: "<equipment-or-service-type>"
---

# RFP Generator

Generate complete, issuable Request for Proposal documents for data center construction,
equipment procurement, or managed services. Synthesizes upstream engineering artifacts
into a procurement-ready document with technical specifications, evaluation criteria,
weighted scoring, commercial terms, and contract form selection.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire RFP structure.

**Project Context:**

1. What is the RFP scope?
   - Full data center construction (shell, core, M&E, IT)
   - Mechanical & Electrical (M&E) package only
   - IT equipment procurement (servers, storage, networking)
   - Managed services (operations, maintenance, staffing)
   - Specific trade package (electrical, mechanical, fire protection, security)

2. What procurement delivery method?
   - **Design-Build:** Single entity for design and construction
   - **Design-Bid-Build:** Separate design (architect/engineer) and construction contracts
   - **EPC (Engineering, Procurement, Construction):** Turnkey with commissioning and performance guarantees
   - **EPCM (Engineering, Procurement, Construction Management):** Owner retains more control; CM manages trades
   - **CM at-Risk:** Construction Manager provides GMP; subcontracts trade packages

3. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

4. What is the target budget range?
   - Used for evaluation threshold setting and should-cost analysis
   - Specify total project budget or per-MW budget

5. How many respondents are expected?
   - 3-5 (targeted shortlist)
   - 5-10 (competitive field)
   - 10+ (open solicitation)

6. What contract form is preferred?
   - AIA (American Institute of Architects)
   - EJCDC (Engineers Joint Contract Documents Committee)
   - FIDIC (International Federation of Consulting Engineers)
   - Custom / owner-developed
   - No preference (recommend based on scope)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Construction RFP Path

If scope is full construction or M&E package:

1. What are the site conditions? (grading status, geotechnical data available, environmental constraints)
2. What is the permit status? (zoning approved, building permit submitted, entitlements complete)
3. What are the schedule constraints? (target completion, phased occupancy, liquidated damages triggers)
4. What labor requirements apply? (prevailing wage, Project Labor Agreement, local hire targets)

### Equipment RFP Path

If scope is IT equipment procurement:

1. What equipment categories? (servers, storage, networking, racks, cabling)
2. What vendor qualification requirements? (OEM direct, authorized reseller, refurbished acceptable)
3. What is the delivery schedule? (single delivery, phased, just-in-time)
4. Does installation scope accompany procurement? (deliver-only, deliver and install, install and commission)

### Managed Services Path

If scope is managed services:

1. What SLA requirements? (uptime guarantee, response time, MTTR targets)
2. What transition plan is needed? (incumbent provider, in-house to outsourced, timeline)
3. What staffing model? (dedicated on-site, shared services, hybrid)
4. What KPIs will govern performance? (availability, PUE maintenance, incident response, customer satisfaction)

### Multi-Package Path

If scope spans multiple packages:

1. How should scope be divided among packages? (by trade, by building, by phase)
2. What interface coordination requirements exist between packages?
3. Who manages coordination? (owner, lead contractor, separate CM)

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Project location and site description
- Site constraints and environmental factors
- Zoning status and entitlements
- Utility availability (power, water, fiber)

**From power-capacity-model (eng-power-model):**
- Electrical specifications: utility feed voltage, capacity (MW), redundancy tier
- UPS configuration and capacity
- PDU/RPP distribution architecture
- Phased build-out schedule with power per phase

**From cooling-design-report (eng-cooling-design):**
- Mechanical specifications: cooling technology, total cooling capacity (kW)
- Equipment list (chillers, CRAHs, CDUs, cooling towers)
- Water requirements (consumption, supply pressure)
- PUE contribution from cooling systems

If upstream artifacts are not available, I will ask you for the technical requirements
or generate placeholder specifications marked [TO BE CONFIRMED].

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical scope | Full DC | Shell & core + fit-out | Full DC + security | Multi-tenant fit-out | Factory + field | Prefab deploy |
| Eval weight: price | 30% | 25% | 20% | 30% | 35% | 35% |
| Eval weight: technical | 40% | 45% | 40% | 35% | 30% | 30% |
| Eval weight: schedule | 15% | 20% | 15% | 15% | 25% | 25% |
| Eval weight: qualifications | 15% | 10% | 25% | 20% | 10% | 10% |

## RFP Assembly Process

The generated RFP document contains seven sections assembled from discovery and upstream data:

### Section 1: Introduction and Project Overview
- Project name, owner, and location (from site-feasibility-report)
- Facility type and target capacity
- Project objectives and success criteria
- Procurement timeline and key dates

### Section 2: Scope of Work
- Detailed scope definition from Phase 1 scope selection
- Work included and work explicitly excluded
- Owner-furnished equipment and services
- Interface boundaries with other contractors or packages

### Section 3: Technical Requirements
- Electrical requirements (from power-capacity-model): utility feed, UPS, PDU, redundancy
- Mechanical requirements (from cooling-design-report): cooling technology, capacity, water
- Structural requirements: floor loading, seismic design criteria
- Fire protection, security, and monitoring requirements
- Reference standards: ASHRAE, NFPA 75/76, BICSI 002, TIA-942, Uptime Tier
- Items not sourced from upstream are marked [TO BE CONFIRMED]

### Section 4: Evaluation Criteria and Scoring
- Weighted evaluation matrix using facility-type defaults (adjustable)
- Technical evaluation: approach, methodology, design innovation, sustainability
- Price evaluation: total cost, unit rates, allowances, value engineering
- Schedule evaluation: construction timeline, milestones, acceleration capability
- Qualifications: relevant experience, team resumes, financial capacity, safety record
- Criteria weights must sum to 100%

### Section 5: Submission Requirements
- Proposal format (page limits, required sections, file format)
- Submission deadline and delivery method
- Pre-bid conference date and site visit schedule
- Questions and clarifications process (RFI deadline, addenda distribution)
- Mandatory vs optional requirements matrix

### Section 6: Commercial Terms
- Contract form (from Phase 1 selection) with key provisions
- Payment milestones and schedule of values
- Retention percentage (typically 5-10%)
- Warranty requirements (1-year standard, extended for critical systems)
- Liquidated damages formula (genuine pre-estimate of loss, not penalty)
- Insurance requirements (GL, professional liability, builder's risk, pollution)
- Bonding requirements (bid bond, performance bond, payment bond)
- Change order process and dispute resolution

### Section 7: Appendices
- Drawings list and specifications table of contents
- Site plans, surveys, and geotechnical data references
- Existing conditions documentation (brownfield)
- Reference standards list with edition/year
- Sample forms (bid form, qualification questionnaire, safety questionnaire)

## Reference Data

Load on demand -- do not read upfront:

- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional $/MW for should-cost estimates and evaluation threshold setting

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-rfp-document.md`

A complete, issuable RFP with all 7 sections above. Each section contains boilerplate
language suitable for direct use or owner customization. Technical specifications
are populated from upstream artifacts where available, with [TO BE CONFIRMED] placeholders
where upstream data is missing.

### JSON Sidecar: `<project-name>-rfp-document.json`

```json
{
  "artifact_type": "rfp-document",
  "skill_version": "1.0",
  "project_name": "...",
  "rfp_type": "construction | equipment | managed-services | trade-package",
  "procurement_method": "design-build | design-bid-build | epc | epcm | cm-at-risk",
  "facility_type": "traditional | hyperscale | sovereign | colo | modular | edge",
  "scope": "Description of RFP scope",
  "budget_range": {"low": 0, "high": 0, "unit": "USD"},
  "evaluation_criteria": [
    {"name": "Technical", "weight": 40},
    {"name": "Price", "weight": 30},
    {"name": "Schedule", "weight": 15},
    {"name": "Qualifications", "weight": 15}
  ],
  "contract_form": "AIA | EJCDC | FIDIC | custom",
  "submission_deadline_placeholder": "[DATE]",
  "technical_specs_source": {
    "power": "power-capacity-model | manual | placeholder",
    "cooling": "cooling-design-report | manual | placeholder",
    "site": "site-feasibility-report | manual | placeholder"
  },
  "respondent_count": 5
}
```

## Gotchas

- **Evaluation criteria weights must sum to 100%.** Adding custom criteria without rebalancing existing weights is the most common RFP error and can invalidate the entire evaluation.
- **"Design-Build" and "EPC" are NOT the same.** EPC includes commissioning and performance guarantees; design-build typically does not. Misusing these terms creates contractual ambiguity and disputes.
- **Liquidated damages must be a genuine pre-estimate of loss, not a penalty.** Courts can void penalty clauses, leaving the owner with no schedule protection. Document the basis for LD calculations.
- **Prevailing wage requirements (Davis-Bacon Act for federal, state equivalents) can add 15-30% to labor costs.** Failing to include prevailing wage in scope/budget causes bid prices to far exceed estimates.
- **Technical specifications should reference standards by number (ASHRAE 90.4, NFPA 75, BICSI 002-2024), not describe requirements from scratch.** Standards references reduce ambiguity and strengthen the owner's legal position in disputes.

## Evaluations

See `evals/evals.json` for test scenarios covering construction, equipment, and managed services RFPs.
