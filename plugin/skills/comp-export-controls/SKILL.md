---
name: comp-export-controls
description: "Assess GPU import/export compliance for data center projects covering EAR, ITAR, dual-use regulations, and country-specific restrictions. Use when importing GPUs internationally, evaluating export control risk for AI hardware, navigating chip export restrictions, or assessing dual-use technology compliance. Trigger with \"export controls\", \"GPU import\", \"EAR compliance\", \"chip export restrictions\", \"ITAR\", \"dual-use\", or \"can I export these GPUs?\"."
argument-hint: "<destination-country>"
---

# Export Controls Compliance Assessment

Assess GPU import/export compliance and technology transfer controls for data center
projects. Covers EAR classification, ITAR screening, Wassenaar dual-use analysis,
OFAC/EU sanctions screening, deemed export analysis for foreign national access, and
end-use monitoring program design. Consumes REGULATORY-MATRIX.md for country data.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** Export control planning can be integrated from procurement phase
   - **Brownfield:** Assess existing equipment classification and compliance posture

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What equipment types require export control assessment?
   - GPU accelerators (specify models and quantities)
   - High-performance networking (InfiniBand, high-speed switches)
   - Security/encryption hardware
   - Full server systems
   - Custom ASICs or FPGAs

4. What is the origin country of the equipment?
   - United States (EAR applies)
   - EU member state (EU Dual-Use Regulation applies)
   - Other (specify)

5. What is the destination country/countries?
   - Specify all deployment locations

6. What is the end-user type?
   - Commercial enterprise
   - Government (civilian)
   - Defense / military
   - Academic / research

7. Will foreign nationals have physical or logical access to the facility?
   - No foreign national access
   - Foreign national employees on-site
   - Foreign national visitors/contractors
   - Multi-national tenant access (colo)

8. What GPU models and quantities are planned?
   - NVIDIA H100/H200/B100/B200 (specify)
   - AMD MI300X/MI400 (specify)
   - Other accelerators
   - Total TOPS (Tera Operations Per Second) if known

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### US-Origin Equipment Path

If equipment origin is United States:

1. Has an ECCN (Export Control Classification Number) been determined?
2. Are any end-users on the Entity List (BIS)?
3. Has a license determination been made by BIS?
4. Existing Technology Control Plan (TCP) for deemed exports?

### Multi-National Access Path

If foreign nationals will access the facility:

1. Nationalities of all foreign national personnel
2. Type of access (physical tour, logical access, hands-on equipment)
3. Information to be shared (specifications, configurations, source code)
4. Duration and frequency of access

### Sanctions Screening Path

If destination includes countries in Groups D:1-D:5 or E:1-E:2:

1. Has OFAC SDN list screening been completed?
2. Are sectoral sanctions applicable?
3. EU consolidated sanctions list checked?
4. Any pending or prior voluntary self-disclosures?

## What I Need from Upstream

This skill can be invoked independently.

**If sovereignty-assessment is available (from comp-sovereignty):**
- Jurisdiction analysis and applicable regulatory frameworks
- Foreign ownership structure assessment
- Data classification level
- Cross-border transfer requirements

## Analysis & Output

### Process

1. **Classify equipment** by ECCN using BIS Commerce Control List
2. **Determine license requirements** by destination country group
3. **Screen end-users** against OFAC SDN, Entity List, EU consolidated list
4. **Analyze deemed exports** for all foreign national access scenarios
5. **Assess technology transfer controls** for technical data and software
6. **Design compliance program** with training, record-keeping, and audit
7. **Document risk rating** and produce compliance assessment

### Classification Thresholds

**GPU Accelerators (as of Jan 2025 BIS rules):**
- Advanced Computing Chips: >4,800 TOPS triggers license requirement for Group D:5 countries
- Covered Items: >300 TOPS for certain items with additional parameters
- Chip performance density thresholds apply to datacenter-class accelerators
- These thresholds have changed 3 times since October 2022 -- verify current BIS rules

**Country Group Classifications:**
- A:1-A:6: Wassenaar, MTCR, NSG, Australia Group, CWC participants
- B: Broad set of trading partners with fewer restrictions
- D:1-D:5: National security, chemical/biological, nuclear, missile, US arms embargo concerns
- E:1-E:2: Terrorism-supporting countries (most restricted)

### Deemed Export Analysis

"Deemed export" = release of controlled technology to a foreign national within the
United States (or other origin country). Key rules:

- A foreign national touring a data center with visible GPU configurations = potential deemed export
- Providing technical specifications or performance data to foreign nationals = deemed export
- Same EAR classification applies as physical export to the person's home country
- Exceptions: published information, fundamental research, educational
- Visual inspection of equipment CAN constitute a deemed export if controlled technology is observable

### Reference Data

Load these files on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-specific export control frameworks, sanctions status, and trade restrictions
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Export control exposure | Low | High | Very High | High | Medium | Low |
| Deemed export risk | Low | High | Very High | Very High | Low | Low |
| Sanctions screening complexity | Low | High | High | Very High | Low | Low |
| Technology transfer sensitivity | Low | High | Very High | Medium | Medium | Low |
| Typical ECCN items | None | GPUs, networking | GPUs, crypto | Mixed | GPUs | Limited |

## Output Template

This skill produces two files:
1. `<project-name>-export-control-assessment.md` -- Full report
2. `<project-name>-export-control-assessment.json` -- Structured data

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: comp-export-controls v1.0]

#### 1. Executive Summary
- **Risk Rating:** LOW / MEDIUM / HIGH / CRITICAL
- **Items Classified:** [count]
- **License Requirements:** [count requiring license]
- **Deemed Export Scenarios:** [count]
- **Key Finding:** [1-2 sentence summary]

#### 2. Item Classification Table

| Item | ECCN | Classification | License Required | License Exception | Notes |
|------|------|---------------|-----------------|-------------------|-------|
| [item] | [ECCN] | [class] | Yes/No | [exception] | [notes] |

#### 3. Destination Analysis

| Country | Group | Sanctions Status | Restrictions | License Requirement |
|---------|-------|-----------------|-------------|-------------------|
| [country] | [group] | [status] | [restrictions] | [requirement] |

#### 4. Deemed Export Analysis

| Nationality | Access Type | Classification Impact | License Required | Mitigation |
|------------|-----------|---------------------|-----------------|-----------|
| [nationality] | [type] | [impact] | Yes/No | [mitigation] |

#### 5. Compliance Program Requirements
- Export classification procedures
- Screening protocols (SDN, Entity List, DPL)
- Technology Control Plan for deemed exports
- Record retention (5 years minimum)
- Training requirements (annual for all export-related personnel)
- Voluntary self-disclosure procedures

### JSON Sidecar Schema

```json
{
  "artifact_type": "export-control-assessment",
  "skill_version": "1.0",
  "project_name": "...",
  "items": [
    {
      "description": "...",
      "eccn": "...",
      "classification": "...",
      "license_required": false,
      "license_exception": "..."
    }
  ],
  "destinations": [
    {
      "country": "...",
      "group": "...",
      "sanctions_status": "clear | sanctioned | restricted",
      "restrictions": []
    }
  ],
  "deemed_exports": [
    {
      "nationality": "...",
      "classification_impact": "...",
      "license_required": false
    }
  ],
  "compliance_program": {
    "elements": [],
    "training_required": true,
    "record_retention_years": 5
  },
  "risk_rating": "low | medium | high | critical"
}
```

## Gotchas

- **"Deemed export" rules mean a Chinese national touring your Virginia DC triggers the same EAR analysis as physically shipping a GPU to Beijing.** The release of controlled technology to a foreign national in the US is classified identically to an export to that person's home country. Many operators are unaware that facility tours with visible GPU configurations constitute potential deemed exports.

- **GPU TOPS thresholds for export controls have changed 3 times since October 2022 and will change again.** The October 2022 rule, October 2023 update, and January 2025 revision each moved the performance thresholds. Any compliance program must include a monitoring process for BIS rule changes, not just a point-in-time assessment.

- **NVIDIA A100/H100 were retroactively added to advanced computing restrictions mid-shipment for some orders.** BIS interim final rules can take effect immediately upon Federal Register publication. In-transit shipments have been affected by rule changes. Export compliance must account for regulatory change risk during procurement lead times.

- **Entity List screening is not a one-time check.** The Entity List is updated multiple times per year. End-user screening must be performed at each transaction stage: order, shipment, delivery, and post-shipment verification. Automated screening tools are essential for colo operators with hundreds of tenants.

- **Colo operators with multi-national tenants face compounding deemed export risk.** Every tenant with foreign national employees accessing the facility creates a deemed export scenario. Without a Technology Control Plan and physical/logical access controls segregated by nationality, a single colo facility can generate dozens of simultaneous EAR compliance obligations.

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

See `evals/evals.json` for test scenarios covering US hyperscale with foreign engineers,
EU-to-UAE GPU deployment, and multi-national colo deemed export compliance.
