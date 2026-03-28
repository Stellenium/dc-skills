---
name: eng-physical-security
description: "Design data center physical security including tiered zones, CCTV, access control, OT/IT network segmentation, and compliance mapping. Use when designing security for a DC, planning access control systems, designing CCTV coverage, or mapping security requirements to compliance frameworks. Trigger with \"physical security\", \"access control\", \"CCTV design\", \"security zones\", \"DC security\", or \"data center security design\"."
---

# Physical Security Design

Design data center physical security with tiered security zones, CCTV surveillance,
access control, OT/IT network segmentation, and zero-trust architecture alignment.
Produces a comprehensive security design covering perimeter through rack-level
protection with compliance mapping to SOC 2, ISO 27001, NIST 800-53, and FedRAMP.

## What I Need from Upstream

This skill is independent -- no upstream artifacts required.

Can optionally consume a **physical-layout-plan** (eng-physical-layout) for zone
boundary placement, door locations, and hall partitioning. If available, security
zone boundaries will align with the physical layout. If not, zone boundaries are
designed based on discovery answers.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire security posture.

**Project Context:**

1. What is the security classification level?
   - Commercial (standard business data, SOC 2 / ISO 27001)
   - Government unclassified (CUI, FedRAMP, NIST 800-171)
   - Government classified (Secret, SCIF, ICD 705)
   - Sovereign (national critical infrastructure, national operator requirements)

2. What facility type?
   - Colocation (multi-tenant, tenant-managed spaces)
   - Hyperscale (single-tenant, large campus)
   - Enterprise (single-tenant, single building)
   - Edge (unmanned, remote locations)
   - Sovereign (government-aligned, enhanced physical protection)

3. How many security perimeters are required?
   - Standard (3 layers: site, building, data hall)
   - Enhanced (5 layers: perimeter, campus, building, hall, cage/vault)
   - Custom (specify requirements)

4. What is the visitor policy?
   - Escorted at all times (no unescorted visitor access)
   - Limited unescorted (pre-vetted, scheduled visits to common areas only)
   - Tenant self-managed (tenants control access within their cages/suites)

5. What compliance requirements apply? Select all:
   - SOC 2 Type II
   - ISO 27001
   - NIST 800-53 (specify revision: Rev 5)
   - FedRAMP (specify level: Low, Moderate, High)
   - PCI DSS 4.0
   - HIPAA
   - ICD 705 / SCIF
   - None specified (design to SOC 2 baseline)

6. Is this a new facility or security upgrade to existing?
   - New facility (full design freedom)
   - Existing facility upgrade (specify current security baseline)

7. What OT network isolation level is required?
   - Shared network (BMS/EPMS on same network as corporate IT)
   - Logically segmented (VLANs, firewall separation)
   - Physically segmented (separate switches, cabling, NOC)
   - Air-gapped (no IP connectivity between OT and IT networks)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Classification-Specific Path

**SCIF / Classified path** (if Phase 1 Q1 = Government classified):
1. What classification level? (Secret, Top Secret, TS/SCI)
2. Is RF shielding (TEMPEST) required?
3. What are the sound attenuation requirements?
4. Is visual surveillance inside the SCIF permitted or prohibited?
5. Who is the cognizant security agency (CSA)?

**Sovereign path** (if Phase 1 Q1 = Sovereign):
1. Which nation's requirements apply?
2. Is there a national operator requirement (citizens-only access)?
3. Are foreign-manufactured components restricted?
4. What government agency certifies the facility?

### Facility Type Refinements

**Colocation additions:**
1. How are tenant cage/suite boundaries secured?
2. Do tenants bring their own locks and access control within their cages?
3. What are cross-connect security requirements?
4. How is visitor access to shared corridors managed?

**Edge / unmanned additions:**
1. What remote intrusion detection is required?
2. What is the response time for security personnel to reach the site?
3. Are tamper-detection sensors required on enclosures?
4. What environmental monitoring substitutes for physical patrols?

## Security Zone Design

### Five-Tier Security Zone Model

| Zone | Name | Access Level | Authentication | Monitoring |
|------|------|-------------|----------------|------------|
| 1 | Public perimeter | Unrestricted approach | None (CCTV only) | Perimeter CCTV, motion detection |
| 2 | Restricted campus | Employees, scheduled visitors | Badge + vehicle gate | CCTV, license plate recognition |
| 3 | Secured building | Authorized personnel | Badge + anti-tailgating | CCTV, mantrap at entry |
| 4 | Controlled data hall | Operations staff | Badge + biometric | CCTV, cabinet-level audit |
| 5 | High-security cage/vault | Named individuals only | Badge + biometric + PIN | CCTV, motion, rack-level sensors |

### Zone-by-Zone Design

**Zone 1 -- Public Perimeter:**
- Setback distance from public road (minimum 100ft recommended)
- Perimeter fencing (anti-climb, anti-cut, minimum 8ft)
- Vehicle barriers (bollards, rated for vehicle impact per ASTM F2656)
- Perimeter CCTV with analytics (motion detection, loitering)
- Lighting: minimum 2 foot-candles at perimeter, 5 at entry points

**Zone 2 -- Restricted Campus:**
- Vehicle entry: manned gate or automated barrier with credential
- Pedestrian entry: badge access with visitor registration
- CCTV coverage: all vehicle and pedestrian paths, parking areas
- License plate recognition at vehicle gates

**Zone 3 -- Secured Building:**
- Mantrap or airlock entry (two interlocking doors, anti-tailgating)
- Badge + anti-tailgating (optical turnstile or mantrap)
- Visitor management system (pre-registration, photo ID, badge issuance)
- CCTV at all entry/exit points and corridors
- Loading dock security (separate entry, inspection area)

**Zone 4 -- Controlled Data Hall:**
- Biometric + badge authentication (fingerprint, iris, or facial recognition)
- No visitor access without escort by authorized operations staff
- CCTV recording with 90-day minimum retention (SOC 2 requirement)
- Cabinet-level electronic locking (optional per compliance level)

**Zone 5 -- High-Security Cage/Vault:**
- Three-factor authentication: badge + biometric + PIN
- Access limited to named, pre-approved individuals
- Dual-person integrity (two-person rule) for highest classification
- Motion sensors within cage perimeter
- Rack-level tamper detection (optional for classified)

## OT/IT Network Segmentation

### Architecture

Data center operational technology (BMS, EPMS, DCIM, fire alarm, CCTV) must be
segmented from corporate IT and tenant networks:

- **BMS (Building Management System):** Controls HVAC, lighting, environmental monitoring
- **EPMS (Electrical Power Monitoring System):** Power metering, UPS, generator control
- **DCIM (Data Center Infrastructure Management):** Capacity planning, asset tracking
- **Fire alarm:** Life safety, independent per code
- **CCTV / access control:** Physical security network

### Segmentation Levels

| Level | Approach | Use Case | Risk |
|-------|----------|----------|------|
| Shared | All on one network | Never acceptable for Tier III+ | Critical: compromised IT can reach BMS |
| Logical | VLAN + firewall | Commercial SOC 2 baseline | Moderate: misconfiguration exposes OT |
| Physical | Separate infrastructure | Government, Tier III+ | Low: no IP path between OT/IT |
| Air-gapped | No connectivity | Classified, sovereign | Minimal: requires physical access to OT |

### Zero-Trust Alignment

Zero-trust principles applied to physical security:

1. **Verify identity at every zone boundary** -- no inherited trust from outer zones
2. **Micro-segmentation** -- each tenant cage/suite is its own trust boundary
3. **Least-privilege access** -- minimum zone access required for job function
4. **Continuous monitoring** -- CCTV, audit logs, anomaly detection at every zone
5. **Assume breach** -- design so compromise of one zone does not cascade

## Output

This skill produces two files:
1. `<project-name>-security-design.md` -- Full report
2. `<project-name>-security-design.json` -- Structured data for downstream skills

### Physical Security Design Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-physical-security v1.0]

#### 1. Executive Summary
- Security classification: [commercial / government / sovereign]
- Security zones: [N] tiers
- Compliance targets: [SOC 2, ISO 27001, etc.]
- OT/IT segmentation: [shared / logical / physical / air-gapped]

#### 2. Security Zone Map
[Zone-by-zone design per Five-Tier model above, customized per discovery]

#### 3. CCTV Design
| Area | Camera Type | Coverage | Retention | Analytics |
|------|-------------|----------|-----------|-----------|
| Perimeter | PTZ + fixed | 100% | 90 days | Motion, loitering |
| Parking | Fixed | 100% | 90 days | LPR |
| Building entry | Fixed | 100% | 90 days | Facial capture |
| Data hall | Fixed | 100% | 90 days | Motion |
| Cage/vault | Fixed | 100% | 90 days | Tamper |

#### 4. Access Control Design
| Zone | Method | Hardware | Integration |
|------|--------|----------|-------------|
| Campus | Badge + vehicle | Gate controller, LPR | VMS |
| Building | Badge + mantrap | Optical turnstile | VMS, CCTV |
| Data hall | Badge + biometric | Biometric reader | VMS, CCTV, audit log |
| Cage | Badge + bio + PIN | Multi-factor reader | VMS, CCTV, rack sensors |

#### 5. OT/IT Segmentation
[Architecture diagram description with segmentation level per discovery]

#### 6. Compliance Mapping
| Requirement | Control | SOC 2 | ISO 27001 | NIST 800-53 |
|-------------|---------|-------|-----------|-------------|
| Physical access control | Zone model | CC6.4 | A.11.1 | PE-2, PE-3 |
| Video surveillance | CCTV | CC6.4 | A.11.1 | PE-6 |
| Visitor management | VMS | CC6.4 | A.11.1 | PE-8 |
| Environmental protection | OT segmentation | CC6.4 | A.11.2 | PE-14 |

### JSON Sidecar

```json
{
  "artifact_type": "security-design",
  "skill_version": "1.0",
  "project_name": "...",
  "classification": "commercial | government-unclassified | government-classified | sovereign",
  "security_zones": 5,
  "compliance_targets": ["SOC 2", "ISO 27001"],
  "ot_it_segmentation": "shared | logical | physical | air-gapped",
  "cctv_retention_days": 90,
  "access_control_layers": [
    {"zone": "campus", "method": "badge"},
    {"zone": "building", "method": "badge + mantrap"},
    {"zone": "data_hall", "method": "badge + biometric"},
    {"zone": "cage", "method": "badge + biometric + pin"}
  ],
  "zero_trust_aligned": true,
  "visitor_policy": "escorted | limited-unescorted | tenant-managed",
  "scif_required": false
}
```

## Gotchas

- **SOC 2 Type II requires 90-day CCTV retention minimum -- many facilities default to 30 days and fail audit.** The 90-day requirement applies to all security-relevant camera locations (entries, data halls, cages). Storage costs for 90-day retention at 4K resolution across 50+ cameras can exceed $100K/year. Plan storage capacity accordingly.

- **Biometric readers at exterior doors fail in extreme cold (<-10F) -- use card+PIN as primary with biometric as secondary for cold-climate sites.** Fingerprint readers are most susceptible; facial recognition and iris scanners have better cold tolerance but higher cost. Design exterior access points with weather-protected vestibules where biometrics are required.

- **OT network segmentation is not optional for Tier III+ -- a compromised BMS can shut down cooling and cause thermal runaway in minutes.** A cyberattack that gains access to BMS controls can disable cooling, open fire suppression, or manipulate power systems. Physical network segmentation (not just VLANs) is the minimum for critical infrastructure.

- **Anti-tailgating at mantraps must be tested under load -- a mantrap that works with 1 person fails when 5 people arrive simultaneously at shift change.** Design entry throughput for peak traffic (shift changes, emergency egress drills). A single mantrap handles approximately 6-8 people per minute. Multiple parallel mantraps or turnstile banks may be needed.

## Evaluations

See `evals/evals.json` for test scenarios covering commercial colo, government SCIF, and sovereign facility security.
