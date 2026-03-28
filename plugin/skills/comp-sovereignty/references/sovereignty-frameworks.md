# Sovereignty Frameworks Reference

> Detailed framework comparison for the comp-sovereignty skill.
> Covers EU AI Act risk tiers, GDPR adequacy, defense classifications,
> cross-border transfer mechanisms, and sovereign AI national initiatives.
> Loaded on demand by comp-sovereignty SKILL.md -- do not load upfront.

**As-of:** 2026-03-27
**Next review:** 2026-06-27
**Staleness warning:** 90 days

---

## EU AI Act Risk Classification

The EU AI Act (Regulation 2024/1689) classifies AI systems by risk tier based on use case,
not underlying technology. Full application begins August 2, 2026.

### Prohibited Practices (Art. 5) -- Effective February 2, 2025

| Practice | Description | DC Impact |
|----------|-------------|-----------|
| Social scoring | Government social credit systems | Cannot host for EU deployment |
| Subliminal manipulation | AI exploiting vulnerabilities to distort behavior | Cannot host for EU deployment |
| Real-time remote biometric ID | Public space facial recognition by law enforcement (limited exceptions) | Cannot host for EU deployment |
| Emotion recognition | Workplace and educational institution emotion inference | Cannot host for EU deployment |
| Untargeted facial scraping | Building facial recognition databases from internet/CCTV | Cannot host training workloads |

### High-Risk Systems (Annex III)

| Domain | Examples | DC Operator Obligation |
|--------|----------|----------------------|
| Biometric identification | 1:N facial matching, gait recognition | Compute tracking if hosted |
| Critical infrastructure | Energy grid management, water treatment, transport | May require EU-located compute |
| Education | Automated grading, admission screening | Tenant compliance documentation |
| Employment | CV screening, interview analysis, performance monitoring | Tenant compliance documentation |
| Essential services | Credit scoring, insurance pricing, social benefit eligibility | Tenant compliance documentation |
| Law enforcement | Predictive policing, evidence analysis | Enhanced security requirements |
| Migration | Border control, visa processing, risk assessment | Government facility requirements |
| Democratic processes | Voter influence assessment, political micro-targeting | Enhanced transparency |

### General-Purpose AI Models (Art. 51-56)

| Category | Threshold | Obligations | DC Impact |
|----------|-----------|-------------|-----------|
| Standard GPAI | No threshold | Technical documentation, training data summary, copyright compliance | Minimal -- provider obligation |
| Systemic risk GPAI | Training compute > 10^25 FLOP | Model evaluation, adversarial testing, incident reporting, energy consumption reporting | DC must track and report compute usage; energy metering infrastructure required |

---

## GDPR Adequacy Decisions

Countries receiving EU adequacy decisions enabling free data flow from EU/EEA without
additional safeguards (SCCs, BCRs).

### Adequate Countries (as of March 2026)

| Country | Decision Date | Scope | Notes |
|---------|--------------|-------|-------|
| Andorra | Oct 2010 | Full | Stable |
| Argentina | Jun 2003 | Full | Stable |
| Canada | Dec 2001 | Commercial (PIPEDA) only | Does not cover government or provincial processing |
| Faroe Islands | Mar 2010 | Full | Stable |
| Guernsey | Nov 2003 | Full | Stable |
| Israel | Jan 2011 | Full | Under periodic review |
| Isle of Man | Apr 2004 | Full | Stable |
| Japan | Jan 2019 | Mutual adequacy (APPI) | Supplementary rules apply |
| Jersey | May 2008 | Full | Stable |
| New Zealand | Dec 2012 | Full | Stable |
| Republic of Korea | Dec 2022 | Full (PIPA) | Supplementary rules apply |
| Switzerland | Ongoing | Full | Pre-GDPR decision; updated assessment expected |
| United Kingdom | Jun 2021 | Full | Extended; sunset review pending |
| United States | Jul 2023 | EU-US Data Privacy Framework | Schrems III challenge possible; requires DPF certification |

### Transfer Mechanisms When No Adequacy Decision

| Mechanism | Complexity | Cost | Timeline | Best For |
|-----------|-----------|------|----------|----------|
| Standard Contractual Clauses (SCCs) | Medium | Low-Medium | 2-4 weeks | Most commercial transfers |
| Binding Corporate Rules (BCRs) | High | High | 12-18 months | Intra-group transfers for multinational corporations |
| Consent (Art. 49) | Low | Low | Immediate | Occasional, non-systematic transfers |
| Contractual necessity (Art. 49) | Low | Low | Immediate | B2B contract performance |
| Certification mechanisms | Medium | Medium | 3-6 months | Emerging; limited adoption |

---

## Defense Classification Systems

### NATO Classification Levels

| Level | Marking | Description | DC Requirements |
|-------|---------|-------------|-----------------|
| COSMIC TOP SECRET | CTS | Exceptionally grave damage to NATO | Dedicated facility; TEMPEST; national accreditation |
| NATO SECRET | NS | Serious damage to NATO | Accredited facility; personnel clearance; physical security |
| NATO CONFIDENTIAL | NC | Damage to NATO interests | Controlled access; cleared personnel |
| NATO RESTRICTED | NR | Disadvantage to NATO | Basic security measures; access control |
| NATO UNCLASSIFIED | NU | No security implications | Standard commercial DC acceptable |

### Five Eyes (FVEY) Classification

| Level | US | UK | Canada | Australia | New Zealand |
|-------|----|----|--------|-----------|-------------|
| Top Secret | TS | UK TOP SECRET | TOP SECRET | TOP SECRET | TOP SECRET |
| Secret | S | UK SECRET | SECRET | SECRET | SECRET |
| Confidential | C | UK OFFICIAL-SENSITIVE | CONFIDENTIAL | -- | CONFIDENTIAL |
| Restricted/Protected | CUI | UK OFFICIAL | PROTECTED A/B/C | PROTECTED | IN-CONFIDENCE |

### US Government / Defense

| Framework | Scope | DC Requirements | Confidence |
|-----------|-------|-----------------|------------|
| FISMA High | Federal systems with high-impact data | FedRAMP High authorization; dedicated infrastructure; continuous monitoring | confirmed |
| FISMA Moderate | Federal systems with moderate-impact data | FedRAMP Moderate; can be shared infrastructure with logical separation | confirmed |
| CMMC Level 3 | Defense contractors handling CUI | Expert-assessed; 110+ NIST SP 800-171 controls; 24 additional controls | confirmed |
| CMMC Level 2 | Defense contractors handling CUI (self-assessed or third-party) | 110 NIST SP 800-171 controls; C3PAO assessment for prioritized acquisitions | confirmed |
| CMMC Level 1 | Defense contractors handling FCI | 17 basic safeguarding controls; annual self-assessment | confirmed |
| IL4 | Controlled Unclassified Information (DoD) | DoD Cloud SRG IL4; US-based DC; US persons access only | confirmed |
| IL5 | Higher sensitivity CUI + national security systems | DoD Cloud SRG IL5; dedicated infrastructure; physically isolated | confirmed |
| IL6 | Classified (SECRET) | Air-gapped; SCIF-grade facility; cleared personnel only | confirmed |

---

## Sovereign AI National Initiatives

Countries with active sovereign AI programs that impose specific requirements on data center
infrastructure, ownership, and operations.

| Country/Region | Initiative | Ownership Requirement | Data Localization | Compute Requirement | Status |
|----------------|-----------|----------------------|-------------------|--------------------|---------|
| EU | European Sovereign Cloud (EUCS) | EU-headquartered, EU-controlled entity | EU data residency for sovereign tier | EU-located infrastructure | Active; EUCS certification scheme expected 2026-2027 |
| France | "Cloud de Confiance" (SecNumCloud) | French or EU entity; no extraterritorial law exposure | French data residency | French-located infrastructure | Active; ANSSI certification required |
| Germany | Sovereign Cloud Stack (SCS) | German/EU entity for government workloads | German data residency for government | German-located | Active; Gaia-X federation standards |
| India | National AI Mission (IndiaAI) | Indian entity preferred; 100% FDI allowed | Indian data center for government AI | India-located GPU clusters | Active; Rs 10,372 crore allocated |
| Saudi Arabia | Vision 2030 + SDAIA National AI Strategy | Saudi or GCC entity for government; CITC licensed | Saudi data residency for government and financial | In-Kingdom compute | Active; NEOM and Riyadh AI hubs |
| UAE | National AI Strategy 2031 | UAE entity for government contracts | UAE data residency for classified data | UAE-located infrastructure | Active; Abu Dhabi AI hub (Technology Innovation Institute) |
| Singapore | National AI Strategy 2.0 | No ownership restriction | Singapore data residency for financial/government | Singapore-located (green DC only) | Active; moratorium partially lifted with green criteria |
| Japan | AI Strategy 2025 | No ownership restriction | Japan-located for government workloads | Japan-located GPU clusters encouraged | Active; subsidies for domestic AI compute |
| South Korea | AI Basic Act + K-Cloud | Korean entity preferred for government | Korea-located for government/financial | Korea-located infrastructure | Active; effective Jan 2026 |

### Key Patterns in Sovereign AI Programs

1. **Ownership control:** EU, France, Saudi, UAE require domestic or regional entity control for sovereign-tier workloads. Foreign-owned DCs can serve commercial workloads but are excluded from government/sovereign AI programs.

2. **Data localization escalation:** Most programs have tiered requirements -- commercial data may flow freely while government/classified data must remain in-country with sovereignty guarantees.

3. **Compute sovereignty:** Emerging requirement for GPU/AI accelerator infrastructure to be physically located in-country, driven by national security concerns about compute supply chain dependence.

4. **Certification frameworks:** EUCS (EU), SecNumCloud (France), C5 (Germany), CSA STAR (Singapore) provide certification paths for cloud and DC operators to demonstrate sovereign compliance.

---

## Cross-Border Transfer Mechanism Comparison

| Mechanism | Speed | Cost | Scope | Durability | Risk |
|-----------|-------|------|-------|-----------|------|
| EU Adequacy Decision | Immediate | None | Country-wide | High (but revocable -- Schrems I/II) | Low while active |
| EU-US Data Privacy Framework | Immediate (with certification) | $50K-200K annual compliance | US orgs certified with DoC | Medium (Schrems III possible) | Medium |
| Standard Contractual Clauses (SCCs) | 2-4 weeks | $10K-50K legal review | Per-transfer or per-relationship | High (Commission-adopted) | Low-Medium |
| Binding Corporate Rules (BCRs) | 12-18 months | $200K-500K | Intra-group only | Very High (DPA-approved) | Low |
| APEC CBPR System | 3-6 months | $50K-150K certification | APEC member economies | Medium | Low-Medium |
| Consent (GDPR Art. 49) | Immediate | Low | Per-transfer, non-systematic | Low (narrow interpretation) | High (regulatory scrutiny) |

### Supplementary Measures (Post-Schrems II)

When transferring to countries without adequacy decisions, the following technical
supplementary measures strengthen SCC-based transfers:

1. **Encryption in transit and at rest** with EU-held encryption keys
2. **Pseudonymization** where the re-identification key remains in the EU
3. **Split processing** where sensitive elements are processed in the EU
4. **Contractual commitments** to challenge government access requests
5. **Transparency reporting** on government access requests received
