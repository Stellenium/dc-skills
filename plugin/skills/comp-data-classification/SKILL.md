---
name: comp-data-classification
description: "Generate a data classification framework for data center facilities covering classification levels, handling requirements, and access controls. Use when building a data classification scheme, defining handling requirements by sensitivity level, or mapping classification to access controls and storage requirements. Trigger with \"data classification\", \"classification framework\", \"data handling\", \"sensitivity levels\", \"information classification\", or \"data categories\"."
---

# Data Classification Framework

Generate a data classification framework for data center facilities. Defines classification
levels with per-level handling requirements, encryption standards, physical security mapping,
and mixed-sensitivity architecture guidance for facilities hosting multiple classification
levels simultaneously. Consumes REGULATORY-MATRIX.md for jurisdiction-specific requirements.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** Classification requirements inform facility design from the start
   - **Brownfield:** Assess existing infrastructure against classification requirements

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What regulatory framework(s) govern data classification?
   - NIST SP 800-53 / FIPS 199 (US federal)
   - ISO 27001 Annex A (international)
   - Government-specific (CNSS, NATO, national schemes)
   - Industry-specific (PCI DSS, HIPAA, GLBA)
   - Custom enterprise framework

4. What tenant types will the facility serve?
   - Commercial enterprise only
   - Government (civilian agencies)
   - Defense / intelligence
   - Mixed commercial and government
   - Multi-tenant with diverse requirements

5. What is the highest data classification level?
   - Public / Unclassified
   - Confidential / CUI (Controlled Unclassified Information)
   - Secret
   - Top Secret / TS/SCI
   - Mixed levels in same facility

6. Is this a multi-tenant facility with mixed classification levels?
   - Single classification level throughout
   - Multiple levels with physical separation
   - Multiple levels with logical separation only
   - Mixed-sensitivity requiring cross-domain solutions

7. What data residency requirements apply?
   - No data residency constraints
   - Country-level residency required
   - Region-level residency (e.g., EU-only)
   - Jurisdiction-specific sovereignty requirements

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Government / Classified Path

If classification includes Secret or Top Secret:

1. What accreditation authority governs the facility?
2. SCIF (Sensitive Compartmented Information Facility) requirements?
3. TEMPEST/EMSEC (Electromagnetic Security) requirements?
4. Personnel security clearance levels required for facility staff?
5. Supply chain restrictions for infrastructure components?

### Multi-Tenant Mixed Path

If facility serves mixed classification levels:

1. Maximum number of concurrent classification levels?
2. Are cross-domain solutions (CDS) required between levels?
3. Shared infrastructure permitted? (power, cooling, physical plant)
4. Tenant contractual requirements for isolation?
5. Right-to-audit provisions in tenant agreements?

### Healthcare / Financial Path

If HIPAA or PCI DSS applies:

1. PHI (Protected Health Information) volume and types?
2. Cardholder data environment (CDE) scope?
3. Existing BAA (Business Associate Agreement) framework?
4. Network segmentation architecture in place?

## What I Need from Upstream

This skill can be invoked independently.

**If sovereignty-assessment is available (from comp-sovereignty):**
- Applicable regulatory frameworks and jurisdiction analysis
- Data residency and sovereignty requirements
- Foreign ownership assessment affecting classification trust
- Cross-border transfer restrictions

## Analysis & Output

### Process

1. **Define classification levels** aligned to regulatory framework
2. **Map handling requirements** per level (access, encryption, audit, disposal)
3. **Specify encryption standards** for at-rest and in-transit per level
4. **Design physical security mapping** linking classification to facility zones
5. **Architect mixed-sensitivity approach** if multiple levels coexist
6. **Define tenant classification requirements** for multi-tenant facilities
7. **Produce compliance mapping** against applicable frameworks

### Classification Levels

| Level | Examples | Facility Impact | Encryption (at-rest) | Encryption (in-transit) |
|-------|---------|----------------|---------------------|----------------------|
| **Public** | Marketing, open data | Standard zones | Optional | TLS 1.2+ |
| **Internal** | Business operations | Controlled access | AES-128+ | TLS 1.2+ |
| **Confidential** | PII, financial, CUI | Restricted zones | AES-256 | TLS 1.3 |
| **Restricted/Secret** | Government classified | Dedicated infrastructure | AES-256 + HSM | Suite B / CNSA |
| **Top Secret/SCI** | Intelligence, defense | Air-gapped, SCIF | NSA Type 1 | NSA Type 1 |

### Handling Requirements Per Level

**Public:**
- Access: No restrictions beyond facility entry
- Encryption: Recommended but not required
- Audit: Standard logging (90-day retention)
- Disposal: Standard media sanitization (NIST SP 800-88 Clear)
- Transport: No special requirements

**Internal:**
- Access: Authenticated facility access, role-based logical access
- Encryption: AES-128+ at rest, TLS 1.2+ in transit
- Audit: Activity logging (1-year retention)
- Disposal: NIST SP 800-88 Clear or Purge
- Transport: Encrypted in transit

**Confidential:**
- Access: Need-to-know basis, MFA required, visitor escort
- Encryption: AES-256 at rest, TLS 1.3 in transit, key management via HSM
- Audit: Comprehensive audit trail (3-year retention minimum)
- Disposal: NIST SP 800-88 Purge, physical destruction for SSDs
- Transport: Encrypted, chain of custody documented

**Restricted/Secret:**
- Access: Security clearance required, biometric access control, two-person integrity
- Encryption: AES-256 with FIPS 140-3 Level 3 validated modules, HSM key management
- Audit: Real-time monitoring, 7-year retention, tamper-evident logs
- Disposal: NIST SP 800-88 Destroy (physical destruction mandatory)
- Transport: Encrypted, armed courier, chain of custody

**Top Secret/SCI:**
- Access: TS/SCI clearance, SCIF access protocols, continuous evaluation
- Encryption: NSA Type 1 encryption, CNSA 2.0 Suite for quantum resistance
- Audit: Continuous monitoring, indefinite retention, compartmented access logs
- Disposal: NSA/CSS EPL-listed destruction methods only
- Transport: NSA-approved containers, cleared courier with two-person integrity

### Mixed-Sensitivity Architecture

**Physical Separation Models:**

| Model | Description | Cost Impact | Use Case |
|-------|-----------|------------|---------|
| **Separate facilities** | Dedicated buildings per level | Very High (+100-200%) | TS/SCI + commercial |
| **Separate halls** | Dedicated data halls, shared plant | High (+40-80%) | Secret + confidential |
| **Separate zones** | Zoned areas within hall | Medium (+20-40%) | Confidential + internal |
| **Logical separation** | Network/access controls only | Low (+5-15%) | Internal + public |

**Infrastructure Sharing Constraints:**

- **Power feeds:** Government contracts often prohibit sharing power distribution between classification levels -- separate utility feeds from separate substations may be required for TS/SCI
- **Cooling loops:** Dedicated cooling for classified zones prevents potential acoustic/vibration side-channel attacks
- **Network infrastructure:** Air-gapped networks for classified; no shared switches, routers, or fiber paths
- **TEMPEST shielding:** Required for TS/SCI facilities to prevent electromagnetic emanation -- adds 40-60% to construction cost per square foot

### Quantum-Resistant Considerations

- CNSA 2.0 Suite mandates begin in 2025 for US government systems
- CRYSTALS-Kyber (ML-KEM) for key encapsulation, CRYSTALS-Dilithium (ML-DSA) for signatures
- Hybrid classical+PQC approach recommended during transition period
- Commercial facilities handling government data should plan for PQC migration

### Reference Data

Load these files on demand -- do not read upfront:

- [Regulatory matrix](../../references/REGULATORY-MATRIX.md) -- Country-specific data classification frameworks and requirements
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Typical max classification | Confidential | Confidential | TS/SCI | Confidential | Secret | Internal |
| Mixed-sensitivity likelihood | Low | Medium | High | Very High | Low | Low |
| TEMPEST requirement | Never | Rare | Common | Rare | Possible | Never |
| Physical separation cost | N/A | Medium | Very High | High | Low | N/A |

## Output Template

This skill produces two files:
1. `<project-name>-data-classification-framework.md` -- Full report
2. `<project-name>-data-classification-framework.json` -- Structured data

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: comp-data-classification v1.0]

#### 1. Executive Summary
- Classification levels defined: [count]
- Highest classification: [level]
- Mixed-sensitivity architecture: [type]
- Key requirement: [summary]

#### 2. Classification Levels

For each level: handling requirements, encryption, audit, disposal, transport.

#### 3. Physical Security Mapping

Zone-to-classification mapping with access control requirements.

#### 4. Mixed-Sensitivity Architecture

Architecture type, isolation mechanisms, cross-domain solutions.

#### 5. Encryption Standards

At-rest, in-transit, and key management per classification level.

#### 6. Compliance Mapping

| Framework | Requirement | Classification Level | Status |
|-----------|-----------|---------------------|--------|
| [framework] | [req] | [level] | Met/Gap |

### JSON Sidecar Schema

```json
{
  "artifact_type": "data-classification-framework",
  "skill_version": "1.0",
  "project_name": "...",
  "levels": [
    {
      "name": "...",
      "handling_requirements": {
        "access": "...",
        "encryption": "...",
        "audit": "...",
        "disposal": "..."
      },
      "physical_requirements": {
        "zone": "...",
        "separation": "..."
      }
    }
  ],
  "mixed_sensitivity": {
    "architecture_type": "...",
    "isolation_mechanisms": [],
    "cross_domain_solutions": []
  },
  "encryption": {
    "at_rest": "...",
    "in_transit": "...",
    "key_management": "..."
  },
  "compliance_mapping": {
    "frameworks": [],
    "gaps": []
  }
}
```

## Gotchas

- **TEMPEST shielding for TS/SCI facilities adds 40-60% to construction cost per square foot.** This is not optional for facilities handling Top Secret or SCI data. The shielding prevents electromagnetic emanations that could be intercepted. Budget estimates that omit TEMPEST will be dramatically wrong for government classified facilities.

- **"Mixed-sensitivity" architecture sounds efficient but most government contracts prohibit sharing ANY infrastructure between classification levels.** This includes power feeds, cooling systems, and even structural walls in some cases. A facility design claiming to host TS/SCI and commercial in the same building with shared mechanical plant will fail government accreditation review.

- **Quantum-resistant encryption mandates (CNSA 2.0 Suite) begin in 2025 for US government systems.** NIST finalized ML-KEM and ML-DSA standards in 2024. Government data centers built today must support PQC algorithms. Commercial facilities handling government data should plan hybrid classical+PQC deployment within 2-3 years.

- **SSD disposal requires physical destruction, not just cryptographic erasure.** NIST SP 800-88 "Purge" for SSDs requires vendor-specific secure erase commands that may not be reliable across all SSD controllers. For Confidential and above, physical destruction (shredding) is the only guaranteed sanitization method. Budget for on-site destruction equipment.

- **Cross-domain solutions (CDS) for transferring data between classification levels require NSA approval for government use.** There is no commercial off-the-shelf CDS that can be deployed without going through the NSA's Cross Domain Solution Management Office. Lead times for CDS approval are 12-18 months.

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

See `evals/evals.json` for test scenarios covering sovereign TS/SCI mixed-use,
HIPAA/PCI colo, and GDPR hyperscale classification.
