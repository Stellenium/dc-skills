---
name: eng-sla-design
description: "Design SLA frameworks for data center facilities with availability modeling using serial/parallel reliability chains and financial penalty structures. Use when defining uptime commitments, modeling availability targets, designing SLA penalty structures, or calculating reliability for Tier III/IV configurations. Trigger with \"SLA design\", \"availability modeling\", \"uptime target\", \"SLA framework\", \"reliability calculation\", or \"five nines\"."
---

# SLA Framework Design

Design SLA frameworks with availability modeling using serial and parallel
reliability chains. Produces a complete SLA document with tier-to-availability
mapping, credit structure, measurement methodology, and contractual language
guidance. Consumes SLA-BENCHMARKS.md for industry-standard targets.

## What I Need from Upstream

This skill operates independently -- no required upstream inputs. Optionally
consumes power-capacity-model for redundancy scheme context (N, N+1, 2N)
to validate that the SLA target is achievable with the designed infrastructure.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the SLA framework approach.

**Project Context:**

1. What is the target availability?
   - 99.9% (8.76 hours downtime/year -- Tier I equivalent)
   - 99.99% (52.6 minutes downtime/year -- Tier II-III equivalent)
   - 99.995% (26.3 minutes downtime/year -- Tier IV designed)
   - 99.999% (5.3 minutes downtime/year -- beyond Tier IV operational)

2. What Uptime Institute Tier is the facility designed to?
   - Tier I (basic site infrastructure, single path, no redundancy)
   - Tier II (redundant site infrastructure components, N+1)
   - Tier III (concurrently maintainable, N+1 minimum, dual power path)
   - Tier IV (fault tolerant, 2N or 2N+1, dual everything)

3. What is the customer type?
   - Enterprise (single-tenant, internal SLA)
   - Hyperscale (cloud provider, fleet-level statistical SLA)
   - Government (FedRAMP-aligned metrics, penalty escalation)
   - Colocation multi-tenant (per-tenant SLA tiers, shared infrastructure)

4. What penalty structure is preferred?
   - Service credits (percentage of monthly recurring charge)
   - Financial rebates (fixed dollar amounts per incident)
   - Termination rights (right to exit contract after repeated failures)
   - Combination (credits + escalation to termination)

5. What is the maintenance window policy?
   - Scheduled maintenance windows (excluded from SLA)
   - Rolling maintenance (no scheduled windows, concurrent maintainability)
   - Zero-downtime maintenance (all maintenance concurrent, no exclusions)

6. What monitoring granularity is required?
   - 5-minute intervals (standard)
   - 1-minute intervals (high precision)
   - Real-time / sub-second (critical infrastructure)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Customer Type Refinements

**Enterprise:**
1. Is this an internal SLA (between IT and business units) or external (with a hosting provider)?
2. What are the business-critical applications and their individual uptime needs?
3. What is the financial impact of downtime per hour? (drives credit structure sizing)

**Hyperscale:**
1. Fleet-level SLA (aggregate across regions) or per-facility SLA?
2. What is the statistical model for availability reporting? (monthly, quarterly, annual)
3. Multi-region failover included in availability calculation?

**Government:**
1. Is FedRAMP High, Moderate, or Low baseline required?
2. What NIST SP 800-53 availability controls apply?
3. Are there specific agency uptime mandates (DoD: IL4/IL5, IC: TSP)?

**Colocation:**
1. How many SLA tiers will be offered? (typically 2-4: bronze, silver, gold, platinum)
2. Are per-tenant SLAs backed by per-cage/suite monitoring?
3. Shared infrastructure (power, cooling) SLA vs. dedicated infrastructure SLA?

### Tier-Specific Refinements

**Tier III and IV:**
1. Concurrent maintainability testing frequency? (annual, semi-annual)
2. Fault tolerance testing protocol? (simulated failure, load bank testing)
3. Are there redundancy components in the reliability chain beyond power and cooling?
   (network, fire suppression, physical security systems)

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical SLA | 99.99% | 99.99-99.999% | 99.999% | 99.9-99.999% | 99.9-99.99% | 99-99.9% |
| Credit cap | 25-30% MRC | 10-15% MRC | Penalty escalation | 25-30% MRC | 20-25% MRC | 10-20% MRC |
| Measurement | Per-facility | Fleet aggregate | Per-system | Per-tenant | Per-module | Per-site |
| Maintenance model | Scheduled windows | Rolling/zero-downtime | Zero-downtime | Scheduled + notification | Replacement swap | Remote + scheduled |
| Monitoring | 5-min | 1-min | Real-time | 5-min per tenant | 5-min | 5-min remote |

### Facility Type Refinements

**Hyperscale additions:**
- Statistical SLA across fleet or individual facility guarantees?
- Multi-site failover counted toward availability?
- Custom monitoring integration with cloud provider's control plane?

**Sovereign additions:**
- Cleared personnel requirement for maintenance affecting SLA?
- Separate SLA for physical security systems?
- Government-mandated incident reporting timelines?

**Edge additions:**
- Remote-only monitoring SLA (no on-site staff)?
- Travel time to site included in MTTR calculations?
- Partial outage weighting for single-site deployments?

## Analysis & Output

### Process

1. **Build reliability block diagram:** Map all components in serial and parallel chains
2. **Calculate component availability:** A = MTBF / (MTBF + MTTR) for each component using SLA-BENCHMARKS.md data
3. **Model redundancy:** Parallel: A_parallel = 1 - (1-A)^k for k redundant units. Serial: A_system = product of all serial component availabilities
4. **Map to tier:** Compare calculated availability against Tier I-IV targets (I: 99.671%, II: 99.741%, III: 99.982%, IV: 99.995%)
5. **Design credit structure:** Map downtime duration bands to service credit percentages using SLA-BENCHMARKS.md templates
6. **Define measurement methodology:** Monitoring intervals, exclusion windows, partial outage weighting, planned maintenance treatment
7. **Generate contractual language guidance:** SLA definition, measurement, credits, escalation, force majeure

### Reference Data

Load these files on demand -- do not read upfront:

- [SLA benchmarks](../../references/SLA-BENCHMARKS.md) -- Tier I-IV availability targets, component MTTR/MTBF data, credit structure templates, measurement methodology

### Validation Loop

1. Compute system availability from component reliability data
2. Cross-check calculated availability against SLA-BENCHMARKS.md tier targets
3. Verify that the redundancy configuration (N, N+1, 2N) achieves the stated tier
4. Check that MTTR assumptions are realistic for the facility staffing model
5. Validate credit structure caps against industry norms (typically 25-30% MRC)
6. If calculated availability is below target: identify weakest serial link and recommend redundancy upgrade
7. Recompute until target met or upgrade path documented

## Output

This skill produces two files:
1. `<project-name>-sla-framework.md` -- Full SLA framework report
2. `<project-name>-sla-framework.json` -- Structured data for downstream skills

### SLA Framework Report

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-sla-design v1.0]

#### 1. Executive Summary
- Facility tier: [Tier I/II/III/IV]
- Designed availability: [X.XXX%]
- Calculated availability: [X.XXXXX%] (from reliability model)
- Annual downtime budget: [X minutes]
- Credit structure: [summary]

#### 2. Reliability Block Diagram
- Component chain (serial): [list of serial components]
- Redundant groups (parallel): [list of parallel-redundant subsystems]
- Weakest serial link: [component with lowest individual availability]

#### 3. Availability Model

| Component | MTBF (hrs) | MTTR (hrs) | Redundancy | Count | Component A | Group A |
|-----------|-----------|-----------|------------|-------|-------------|---------|
| UPS | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |
| Generator | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |
| CRAH | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |
| Chiller | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |
| PDU | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |
| ATS/STS | [X] | [X] | [N+1/2N] | [X] | [X.XXXXX] | [X.XXXXXXX] |

**System availability:** [X.XXXXX%] (product of all group availabilities)
**Annual downtime:** [X.X minutes]

#### 4. Tier Classification
- Target tier: [Tier X]
- Target availability: [X.XXX%]
- Calculated availability: [X.XXXXX%]
- Meets target: [YES/NO]
- Margin: [+X.XXX% above target / -X.XXX% below target]

#### 5. Credit Structure

| Downtime Band | Duration | Service Credit |
|---------------|----------|---------------|
| Level 1 | [X-Y minutes/month] | [X% of MRC] |
| Level 2 | [X-Y minutes/month] | [X% of MRC] |
| Level 3 | [X+ minutes/month] | [X% of MRC (cap)] |

- Credit cap: [X% of monthly recurring charges]
- Measurement period: [monthly/quarterly]
- Exclusions: [planned maintenance, force majeure, customer-caused]

#### 6. Measurement Methodology
- Monitoring interval: [X minutes]
- Downtime definition: [complete loss of power/cooling/connectivity to customer space]
- Partial outage: [weighted at X% of full outage]
- Planned maintenance: [excluded/included with X hours advance notice]
- Reporting: [monthly SLA report within X business days]

### JSON Sidecar

```json
{
  "artifact_type": "sla-framework",
  "skill_version": "1.0",
  "project_name": "<project-name>",
  "facility_tier": "III",
  "target_availability": 99.982,
  "calculated_availability": 99.995,
  "annual_downtime_minutes": 26.3,
  "meets_target": true,
  "components": [],
  "credit_structure": [],
  "measurement_interval_minutes": 5,
  "confidence_range_low": 99.990,
  "confidence_range_high": 99.999
}
```

## Gotchas

- **Uptime Institute Tier IV requires 99.995% designed availability (26.3 min/year downtime)** -- but this is DESIGNED availability, not OPERATIONAL. Real-world Tier IV facilities average 99.999%+ because designs have margin. Do not confuse design target with operational performance.
- **SLA credits typically cap at 30% of monthly recurring charges -- never 100%.** Uncapped credits are a red flag in contract negotiation. If a provider offers uncapped SLA credits, the base pricing already accounts for expected payouts.
- **Planned maintenance windows are EXCLUDED from availability calculations in most SLA contracts.** Verify the exclusion clause carefully -- a facility with 4 hours/month of scheduled maintenance windows loses 0.55% of potential uptime before SLA measurement even begins. Your "99.99%" could actually be 99.44% of total time.
- **MTTR for generators assumes fuel is available and transfer switch operates.** A generator MTBF of 2,000 hours (start attempts) with 24-hour MTTR assumes the generator starts on the first attempt. Real-world first-start reliability is 94-97% -- model the start failure scenario separately.

## Calculation Scripts

For deterministic availability calculations, use the bundled script:

- `scripts/availability-model.py` -- Availability modeling with serial/parallel reliability chains, tier classification, and credit structure generation

Requires: Python 3.11+ (stdlib only, no external dependencies)

## Evaluations

See `evals/evals.json` for test scenarios covering SLA framework design across
different facility tiers, customer types, and redundancy configurations.
