---
name: comp-sovereignty
description: "Assess data sovereignty and regulatory compliance for data center projects including residency requirements, cross-border transfer, and AI regulation. Use when evaluating data sovereignty requirements, assessing GDPR/regulatory compliance for a DC location, planning sovereign cloud infrastructure, or understanding cross-border data transfer rules. Trigger with \"data sovereignty\", \"regulatory compliance\", \"GDPR\", \"data residency\", \"sovereign cloud\", \"cross-border data\", or \"sovereign data center\"."
argument-hint: "<jurisdiction>"
---

# Sovereignty & Regulatory Assessment

Assess data sovereignty, regulatory compliance, and jurisdictional requirements for data
center projects. Evaluates data residency obligations, cross-border transfer mechanisms,
AI regulation applicability, ownership restrictions, and defense classification requirements.
Produces a sovereignty assessment with COMPLIANT, CONDITIONALLY COMPLIANT, or NON-COMPLIANT
determination per applicable framework.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction -- regulatory requirements inform site selection
   - **Brownfield:** Existing facility -- assess current compliance posture and gap remediation

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the target jurisdiction(s)?
   - Country and region/state where the facility will be located
   - If multi-jurisdiction: list all locations under evaluation

4. What is the data classification level?
   - Public / unclassified
   - Confidential / business sensitive
   - Secret / classified (government)
   - Mixed classification levels

5. Who are the primary data subjects?
   - EU/EEA citizens (GDPR applies)
   - US persons (sectoral laws -- HIPAA, GLBA, CCPA/CPRA, state privacy laws)
   - Government / defense personnel (security classification applies)
   - Mixed international (multiple jurisdictions)

6. What is the primary workload type?
   - AI model training (EU AI Act compute thresholds may apply)
   - AI inference / deployment (AI Act use-case classification applies)
   - Government / defense computing (FISMA, FedRAMP, CMMC, NATO)
   - Commercial cloud services (standard data protection)
   - Mixed workloads

7. What is the ownership structure?
   - Domestic private entity
   - Foreign-owned (specify country of parent entity)
   - Joint venture (specify partner nationalities)
   - Government entity / state-owned enterprise

8. Are cross-border data flows required?
   - Single jurisdiction (all data stays in-country)
   - Multi-jurisdiction within a region (e.g., EU-only)
   - Global data flows across multiple regions

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Sovereign / Government Path

If data classification is **Secret/Classified** or facility type is **Sovereign**:

1. What security clearance level is required for facility personnel?
2. Air-gapped network segments required?
3. ITAR/EAR controlled technology present in workloads?
4. Physical security tier? (SCIF, SAP, standard secure facility)
5. Supply chain restrictions? (domestic-only vendors, NDAA Section 889 compliance)

### EU / GDPR Path

If data subjects include **EU/EEA citizens**:

1. Is the facility operator the data controller or processor (Art. 28)?
2. Existing GDPR compliance framework? (DPO appointed, DPIA completed)
3. Schrems II supplementary measures in place for any US transfers?
4. EU AI Act system classification for AI workloads? (prohibited, high-risk, limited-risk, minimal-risk)

### US Compliance Path

If jurisdiction is **United States** with government/regulated workloads:

1. FedRAMP authorization level required? (Low, Moderate, High, Li-SaaS)
2. CMMC level required? (Level 1, Level 2, Level 3)
3. FISMA categorization? (Low, Moderate, High)
4. State-level privacy laws applicable? (CCPA/CPRA, state-specific)

### Multi-Jurisdiction Path

If cross-border flows are **Multi-jurisdiction** or **Global**:

1. Which jurisdictions have conflicting data localization requirements?
2. Transfer mechanisms currently in use? (SCCs, BCRs, adequacy decisions, consent)
3. Any pending regulatory changes in target jurisdictions affecting data flows?

### AI Workload Path

If workload type includes **AI training** or **AI inference**:

1. Training data volume and source jurisdictions?
2. Model deployment jurisdictions? (where inference occurs)
3. Is the AI system customer-facing? (affects EU AI Act classification)
4. China market exposure? (algorithm filing requirements)

## What I Need from Upstream

This skill can be invoked independently -- no upstream artifacts required.

**If site-feasibility-report is available (from predev-site-feasibility):**
- Target jurisdiction and geographic location
- Facility type classification
- Regulatory constraint flags identified during site evaluation
- Sovereignty factor score and notes

If upstream data is not available, the skill will gather jurisdiction and facility
details directly from discovery questions.

## Analysis & Output

### Process

1. **Map applicable frameworks** by jurisdiction using REGULATORY-MATRIX.md
2. **Classify data handling requirements:** residency, sovereignty, localization levels
3. **Assess AI regulation applicability** by workload type and deployment jurisdiction
4. **Evaluate ownership restrictions** and foreign investment screening requirements
5. **Identify cross-border transfer mechanisms** and assess their viability
6. **Build risk matrix:** compliance risk per requirement (low / medium / high / blocking)
7. **Determine overall compliance status** per framework with gap identification

### Compliance Status Levels

| Status | Definition | Action |
|--------|------------|--------|
| **COMPLIANT** | All applicable frameworks satisfied | Proceed with current design |
| **CONDITIONALLY COMPLIANT** | Compliance achievable with specific mitigations | Proceed with remediation roadmap |
| **NON-COMPLIANT** | Blocking regulatory gaps exist | Redesign required or jurisdiction change |

**Framework-level assessment:** Each applicable framework receives its own status.
Overall status is the worst-case across all frameworks (any NON-COMPLIANT = overall NON-COMPLIANT).

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical data classification | Confidential | Mixed | Secret+ | Mixed | Varies | Public-Confidential |
| Ownership scrutiny | Low | Medium | High | Medium | Low | Low |
| Foreign investment screening | Unlikely | Possible | Likely | Possible | Unlikely | Unlikely |
| AI regulation exposure | Low | High | High | Medium | Low | Medium |
| Cross-border complexity | Low | High | Restricted | High | Low | Medium |

### Reference Data

Load these files on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-specific data protection, AI regulation, data residency, and foreign ownership requirements
- [Sovereignty frameworks](references/sovereignty-frameworks.md) -- Detailed framework comparison: EU AI Act tiers, GDPR adequacy, defense classifications, sovereign AI initiatives

## Output Template

This skill produces two files:
1. `<project-name>-sovereignty-assessment.md` -- Full report
2. `<project-name>-sovereignty-assessment.json` -- Structured data for downstream skills

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: comp-sovereignty v1.0]

#### 1. Executive Summary
- **Overall Status:** COMPLIANT / CONDITIONALLY COMPLIANT / NON-COMPLIANT
- **Jurisdiction:** [primary jurisdiction]
- **Applicable Frameworks:** [count] frameworks assessed
- **Blocking Gaps:** [count] (if any)
- **Key Finding:** [1-2 sentence summary]

#### 2. Applicable Frameworks

| Framework | Jurisdiction | Status | Key Requirement | Gap | Remediation |
|-----------|-------------|--------|-----------------|-----|-------------|
| [GDPR] | [EU] | [status] | [requirement] | [gap or none] | [action] |

#### 3. Data Residency Requirements
- Data residency level: None / Residency / Sovereignty / Localization
- In-country storage required: Yes / No / Conditional
- Cross-border transfer mechanism: [SCCs / BCRs / Adequacy / Consent / Blocked]

#### 4. AI Regulation Classification
- EU AI Act: [Not applicable / Minimal risk / Limited risk / High risk / Prohibited]
- Compute threshold (10^25 FLOP): [Above / Below / Not applicable]
- Other jurisdictions: [summary per applicable jurisdiction]

#### 5. Cross-Border Transfer Analysis
- Transfer mechanisms available and their viability
- Conflicting jurisdiction analysis
- Recommended transfer architecture

#### 6. Ownership Compliance
- Foreign investment screening: [Required / Not required / Cleared]
- Ownership restrictions: [None / Partial / Blocking]
- Recommended entity structure

#### 7. Risk Matrix

| Requirement | Risk Level | Impact | Likelihood | Mitigation |
|-------------|-----------|--------|------------|------------|
| [requirement] | High/Med/Low/Blocking | [impact] | [likelihood] | [action] |

#### 8. Gap Remediation Roadmap
- Prioritized list of compliance gaps with remediation steps
- Estimated timeline and cost for each remediation
- Dependencies between remediation actions

#### 9. Disclaimer
[See Disclaimer section below]

### JSON Sidecar Schema

```json
{
  "artifact_type": "sovereignty-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "compliance_status": "COMPLIANT | CONDITIONALLY COMPLIANT | NON-COMPLIANT",
  "jurisdiction": "...",
  "frameworks": [
    {
      "name": "...",
      "status": "COMPLIANT | CONDITIONALLY COMPLIANT | NON-COMPLIANT",
      "key_requirement": "...",
      "gap": "..."
    }
  ],
  "data_residency_level": "none | residency | sovereignty | localization",
  "ai_classification": {
    "eu_ai_act": "not_applicable | minimal | limited | high_risk | prohibited",
    "compute_threshold_exceeded": false
  },
  "cross_border": {
    "transfer_mechanism": "...",
    "conflicting_jurisdictions": []
  },
  "ownership": {
    "foreign_screening_required": false,
    "restrictions": "none | partial | blocking"
  },
  "risks": [
    {
      "requirement": "...",
      "level": "low | medium | high | blocking",
      "mitigation": "..."
    }
  ],
  "gaps": [
    {
      "framework": "...",
      "gap": "...",
      "remediation": "...",
      "priority": "critical | high | medium | low"
    }
  ]
}
```

## Gotchas

- **Data residency is not data sovereignty.** Residency means data is stored in-country; sovereignty means data is subject ONLY to that country's laws. The US CLOUD Act can compel disclosure of data stored in any country if held by a US-headquartered provider -- residency alone does not prevent this. True sovereignty requires non-US entity ownership of the infrastructure and data.

- **EU AI Act classifies by USE CASE, not technology.** The same GPU cluster running the same model is unregulated for weather forecasting but classified as high-risk when used for hiring decisions or creditworthiness assessment. The DC operator's regulatory exposure depends on what tenants do with the compute, not the hardware itself.

- **Schrems II did not ban EU-US data transfers.** It invalidated Privacy Shield, but Standard Contractual Clauses (SCCs) remain valid with supplementary technical measures (encryption where the EU entity holds keys, pseudonymization). Many organizations overcorrect by refusing all EU-US transfers when compliant transfer architectures exist.

- **China requires algorithm filing for recommendation systems.** Any "recommendation algorithm" deployed to Chinese users must be filed with the Cyberspace Administration of China (CAC), even if the inference server is physically outside China. This catches many global AI deployments by surprise.

- **Sovereign AI initiatives require domestic ownership, not just data residency.** EU Sovereign Cloud requirements, India's National AI Mission, Saudi Vision 2030, and UAE's National AI Strategy often require majority domestic ownership of the facility operating entity -- not just storing data in-country. A foreign-owned DC with in-country data storage may not qualify for sovereign AI programs.

## Disclaimer

---

REGULATORY DISCLAIMER: The regulatory analysis, compliance guidance, and
jurisdiction-specific information produced by this skill reflect the regulatory
landscape as of the skill's publication date. Regulations change frequently --
new legislation, executive orders, court decisions, and regulatory guidance can
alter requirements without notice.

This output does not constitute legal advice. Users must verify with local counsel
in each relevant jurisdiction all regulatory requirements before relying on this
analysis for compliance decisions, permit applications, or contractual obligations.

Where jurisdiction-specific caveats are noted, they highlight known areas of
regulatory complexity or recent change. Absence of a caveat does not imply
regulatory simplicity or stability.

---

## Evaluations

See `evals/evals.json` for test scenarios covering EU commercial, Gulf state sovereign,
and US government/defense assessments.
