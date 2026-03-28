---
name: comp-certification
description: "Generate a certification roadmap for data center facilities covering ISO 27001, SOC 2, Uptime Institute Tier, PCI DSS, and HIPAA. Use when planning DC certifications, preparing for ISO 27001 audit, pursuing Uptime Institute tier certification, or building a compliance roadmap for a data center. Trigger with \"certification roadmap\", \"ISO 27001\", \"SOC 2\", \"Uptime Institute\", \"PCI DSS\", \"HIPAA\", or \"DC compliance certifications\"."
---

# Certification Roadmap

Generate a certification roadmap for data center facilities. Produces per-certification
gap analysis, implementation timeline, audit preparation, cost estimation, and an
overlapping-controls matrix showing shared and unique controls across all selected certifications.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction -- certifications can be designed in from day one
   - **Brownfield:** Existing facility -- assess current certification status and gap remediation

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. Which certifications are targeted? (select all that apply)
   - ISO 27001 (Information Security Management System)
   - SOC 2 Type I (point-in-time) / SOC 2 Type II (period-of-time)
   - Uptime Institute Tier Certification (TCDD / TCCF / TCOS)
   - EN 50600 (European data center standard)
   - PCI DSS (Payment Card Industry)
   - HIPAA (Health Insurance Portability and Accountability Act)

4. What certifications does the facility currently hold (if any)?
   - List existing certifications with dates and scope

5. What is the target timeline for achieving certifications?
   - Aggressive (minimum viable timeline)
   - Standard (industry-typical)
   - Phased over 2+ years

6. What tenant or customer requirements are driving certification?
   - Enterprise SLAs requiring specific certifications
   - Government contracts (ISO 27001 + specific frameworks)
   - Financial services (SOC 2 + PCI DSS)
   - Healthcare (HIPAA + SOC 2)
   - European public sector (EN 50600 + ISO 27001)

7. What is the existing management system maturity?
   - No formal ISMS or compliance framework
   - Partial implementation (some policies, incomplete controls)
   - Mature framework seeking formal certification

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### ISO 27001 Path

If ISO 27001 is selected:

1. Has a risk assessment methodology been defined?
2. Which Annex A control domains are most relevant?
3. Internal audit capability (in-house vs. outsourced)?
4. Target certification body preference?

### SOC 2 Path

If SOC 2 is selected:

1. Which Trust Service Criteria apply?
   - Security (required for all SOC 2)
   - Availability
   - Processing Integrity
   - Confidentiality
   - Privacy
2. Type I (design assessment) or Type II (operating effectiveness)?
3. If Type II: has the minimum 6-month observation period been planned?
4. Current state of control documentation?

### Uptime Tier Path

If Uptime Tier is selected:

1. Target Tier level (I, II, III, IV)?
2. Which certification stage?
   - TCDD (Tier Certification of Design Documents)
   - TCCF (Tier Certification of Constructed Facility)
   - TCOS (Tier Certification of Operational Sustainability)
3. Has Uptime Institute been engaged for pre-assessment?

### EN 50600 Path

If EN 50600 is selected:

1. Target classification levels?
   - Availability Class 1-4
   - Protection Class 1-4
   - Energy Efficiency Enabling 0-5
2. Primary market driver (EU public sector, insurance, internal governance)?

## What I Need from Upstream

This skill can be invoked independently.

**If sovereignty-assessment is available (from comp-sovereignty):**
- Applicable regulatory frameworks and compliance status
- Jurisdiction-specific certification requirements
- Data classification level driving certification scope

## Analysis & Output

### Process

1. **Map certification requirements** for each selected framework
2. **Assess current state** against each certification's control set
3. **Identify gaps** per certification with severity (critical, high, medium, low)
4. **Build overlap matrix** showing shared controls across certifications
5. **Sequence certifications** to maximize overlap and minimize rework
6. **Estimate timelines** per certification including audit preparation
7. **Estimate costs** for consulting, audit fees, remediation, and ongoing maintenance
8. **Produce implementation roadmap** with milestones and dependencies

### Certification Details

**ISO 27001 (9-18 months typical):**
- ISMS scope definition and context establishment
- Risk assessment methodology (ISO 27005 or equivalent)
- Statement of Applicability (114 Annex A controls, select applicable)
- Control implementation and documentation
- Internal audit program establishment
- Management review
- Stage 1 audit (documentation review)
- Stage 2 audit (implementation assessment)
- Surveillance audits (annual) and recertification (3-year cycle)

**SOC 2 (6-12 months typical):**
- Trust Service Criteria selection (Security always required)
- Control identification and mapping to criteria
- Type I: point-in-time design assessment
- Type II: minimum 6-month observation period (no exceptions)
- Readiness assessment (recommended before formal audit)
- CPA firm engagement and audit execution
- Annual renewal required

**Uptime Tier (3-6 months per level):**
- Design documents submission (mechanical, electrical, architectural)
- Tier Standard compliance checklist review
- TCDD: design-level certification
- TCCF: constructed facility site visit and testing
- TCOS: operational sustainability review (12+ months operation required)
- Certifications are per site, not per organization

**EN 50600 (3-6 months):**
- Classification against EN 50600-1 (general concepts)
- EN 50600-2-1 (building construction)
- EN 50600-2-2 (power distribution)
- EN 50600-2-3 (environmental control)
- EN 50600-2-4 (telecommunications cabling)
- EN 50600-2-5 (security systems)
- EN 50600-3-1 (management and operational information)
- European market increasingly requires EN 50600 for public sector contracts

### Overlap Matrix Guidance

| Control Domain | ISO 27001 | SOC 2 | Uptime Tier | EN 50600 | PCI DSS |
|---------------|-----------|-------|-------------|----------|---------|
| Physical security | A.11 | CC6.4 | -- | Class 1-4 | Req 9 |
| Access control | A.9 | CC6.1-6.3 | -- | -- | Req 7-8 |
| Business continuity | A.17 | A1.2 | Core focus | Avail Class | -- |
| Change management | A.12.1.2 | CC8.1 | -- | -- | Req 6.4 |
| Risk assessment | A.8 | CC3.2 | -- | -- | Req 12.2 |
| Incident management | A.16 | CC7.3-7.5 | -- | -- | Req 12.10 |

Note: Uptime Tier and ISO 27001 have **zero control overlap** -- they assess completely
different domains (physical infrastructure vs. information security management). Do not
assume Tier certification provides ISO 27001 credit.

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Typical certifications | ISO 27001, SOC 2 | SOC 2, Uptime | ISO 27001, EN 50600 | SOC 2, PCI DSS, Uptime | SOC 2 | SOC 2 (Type I) |
| Certification complexity | Medium | High | Very High | High | Low | Low |
| Multi-tenant scope impact | N/A | N/A | N/A | Significant | N/A | N/A |
| Typical budget (% of OpEx) | 2-4% | 1-2% | 4-8% | 3-5% | 1-3% | 1-2% |

### Reference Data

Load these files on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-specific certification requirements and recognition
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

## Output Template

This skill produces two files:
1. `<project-name>-certification-roadmap.md` -- Full report
2. `<project-name>-certification-roadmap.json` -- Structured data for downstream skills

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: comp-certification v1.0]

#### 1. Executive Summary
- **Certifications Targeted:** [list]
- **Overall Timeline:** [X months]
- **Estimated Total Cost:** [$range]
- **Recommended Sequence:** [ordered list]

#### 2. Per-Certification Roadmap

For each certification:
- Current status and gap count
- Implementation timeline with milestones
- Key milestones and dependencies
- Estimated cost range (consulting + audit + remediation)
- Audit preparation checklist

#### 3. Overlap Matrix
- Shared controls count across all selected certifications
- Unique controls per certification
- Recommended implementation sequence to maximize reuse

#### 4. Gap Analysis Matrix
| Certification | Control Area | Current State | Required State | Gap Severity | Remediation |
|--------------|-------------|---------------|----------------|-------------|-------------|
| [cert] | [area] | [state] | [required] | Critical/High/Med/Low | [action] |

#### 5. Implementation Timeline (Gantt-style)
- Phased milestones across all certifications
- Dependencies between certification activities
- Critical path identification

#### 6. Cost Estimation
| Certification | Consulting | Audit Fees | Remediation | Annual Maintenance | Total |
|--------------|-----------|------------|-------------|-------------------|-------|
| [cert] | [$range] | [$range] | [$range] | [$range] | [$range] |

### JSON Sidecar Schema

```json
{
  "artifact_type": "certification-roadmap",
  "skill_version": "1.0",
  "project_name": "...",
  "certifications": [
    {
      "name": "...",
      "current_status": "none | partial | certified",
      "gap_count": 0,
      "timeline_months": 0,
      "estimated_cost_range": { "low": 0, "high": 0 },
      "key_milestones": []
    }
  ],
  "overlap_matrix": {
    "shared_controls_count": 0,
    "unique_per_cert": []
  },
  "recommended_sequence": [],
  "total_timeline_months": 0
}
```

## Gotchas

- **Uptime Tier and ISO 27001 have zero control overlap.** They assess completely different domains -- Uptime evaluates physical infrastructure redundancy and maintainability; ISO 27001 evaluates information security management systems. Holding one provides zero credit toward the other.

- **SOC 2 Type II requires a minimum 6-month observation period with no exceptions.** Organizations sometimes plan for a 3-month audit window and discover mid-process that 6 months of operating evidence is required. The observation period cannot be shortened, waived, or retroactively applied.

- **EN 50600 is increasingly required for EU public sector contracts but has limited recognition outside Europe.** A facility targeting US and EU customers needs both Uptime Tier (US market standard) and EN 50600 (EU market standard) -- they are not interchangeable.

- **PCI DSS v4.0 added 64 new requirements** effective March 2025. Organizations certified under v3.2.1 need a full gap assessment against v4.0 requirements, particularly around multi-factor authentication and targeted risk analysis.

- **Certification sequencing matters for cost optimization.** ISO 27001 first provides a management system framework that accelerates SOC 2 readiness. Starting with SOC 2 without an ISMS creates duplicate effort when ISO 27001 is later required.

## Disclaimer

---

REGULATORY DISCLAIMER: The regulatory analysis, compliance guidance, and
jurisdiction-specific information produced by this skill reflect the regulatory
landscape as of the skill's publication date. Regulations change frequently --
new legislation, executive orders, court decisions, and regulatory guidance can
alter requirements without notice.

This output does not constitute legal advice. Users must verify all regulatory
requirements with qualified local counsel in each relevant jurisdiction before
relying on this analysis for compliance decisions, permit applications, or
contractual obligations.

Where jurisdiction-specific caveats are noted, they highlight known areas of
regulatory complexity or recent change. Absence of a caveat does not imply
regulatory simplicity or stability.

See [Disclaimer Framework](../../references/DISCLAIMER-FRAMEWORK.md) for full terms.

---

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale multi-certification,
colo SOC 2 upgrade, and sovereign EU certification programs.
