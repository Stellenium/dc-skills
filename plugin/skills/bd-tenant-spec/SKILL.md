---
name: bd-tenant-spec
description: "Discover tenant requirements through structured questionnaire covering power density, cooling, connectivity, SLA, and compliance needs. Use when onboarding a new colo tenant, gathering requirements from a prospective customer, or documenting what a tenant needs from a data center facility. Trigger with \"tenant spec\", \"tenant requirements\", \"colo tenant\", \"customer requirements\", \"onboarding questionnaire\", or \"what does the tenant need?\"."
---

# Tenant Requirements Discovery

Discover tenant requirements through a structured questionnaire on behalf of the
data center operator. This skill operates in **questionnaire mode** -- it gathers
requirements FROM the tenant, not FOR the tenant. The user is the DC operator
or leasing team collecting information to size, configure, and price a deployment.

The output is a structured tenant requirements document with conflict analysis
and resource estimates that feeds into engineering and procurement workflows.

## Phase 1: Tenant Questionnaire

> These questions are asked to the tenant by the DC operator.
> More questions than typical skills because the questionnaire IS the skill.

**Workload & Capacity:**

1. What is the primary workload type?
   - Cloud compute (general purpose VMs, containers)
   - AI/ML training (GPU-intensive, high power density)
   - AI inference (moderate density, latency-sensitive)
   - Storage / backup / archive (high capacity, lower density)
   - Enterprise applications (ERP, databases, web services)
   - HPC / scientific computing (CPU-intensive, high bandwidth)
   - Mixed workloads (specify proportions)

2. What is the initial power requirement?
   - Total power draw (kW)
   - Number of racks
   - Target power density per rack (kW/rack)

3. What is the cooling preference?
   - Air cooling (standard density, up to ~15 kW/rack)
   - Rear-door heat exchangers (medium density, 15-30 kW/rack)
   - Direct-to-chip liquid cooling (high density, 30-80 kW/rack)
   - Immersion cooling (ultra-high density, 50-100+ kW/rack)
   - No preference -- recommend based on density
   - Inlet temperature tolerance (ASHRAE class A1-A4)

**Connectivity:**

4. What are the connectivity requirements?
   - Carrier requirements (specific carriers or carrier-neutral)
   - Total bandwidth needed (Gbps)
   - Latency targets to key endpoints (ms)
   - Internet exchange (IX) peering requirements
   - Cross-connect requirements (to other tenants, cloud on-ramps)
   - Subsea cable proximity (for international traffic)

**SLA & Availability:**

5. What SLA tier is required?
   - Tier I (99.671% -- basic, single path)
   - Tier II (99.741% -- redundant components)
   - Tier III (99.982% -- concurrently maintainable)
   - Tier IV (99.995% -- fault tolerant)
   - Custom availability target: ____%

6. What are the specific SLA requirements?
   - Power availability guarantee
   - Cooling availability guarantee
   - Network availability guarantee
   - Target MTTR (mean time to repair)
   - SLA credit structure preference (service credits, penalty escalation)

**Compliance & Security:**

7. What compliance requirements apply?
   - SOC 2 Type II
   - ISO 27001
   - HIPAA (healthcare data)
   - PCI-DSS (payment card data)
   - FedRAMP (US federal workloads)
   - ITAR (defense/export controlled)
   - GDPR / data residency (specify jurisdictions)
   - Other: _____

8. What physical security requirements apply?
   - Shared hall (standard multi-tenant)
   - Private cage (dedicated fenced area within shared hall)
   - Private suite (dedicated room with walls to deck)
   - Escorted visitor policy (tenant personnel only, no shared access)
   - Man-trap entry
   - Biometric access control
   - 24/7 on-site security guard

**Growth & Contract:**

9. What is the growth projection?
   - 12-month growth: ____% increase in power/racks
   - 24-month growth: ____% increase in power/racks
   - 36-month growth: ____% increase in power/racks
   - Right of first refusal on adjacent capacity?

10. What are the contract preferences?
    - Contract term (1 year, 3 years, 5 years, 10+ years)
    - Deployment timeline (when must the space be ready?)
    - Pricing model preference (per kW, per rack, per sqft, blended)
    - Expansion options (contractual right to scale)

**Geographic & Environmental:**

11. Are there geographic constraints?
    - Data residency requirements (data must stay in specific country/region)
    - Latency requirements to specific cities or user populations
    - Disaster recovery distance from primary site (minimum miles)
    - Climate / natural disaster avoidance (hurricane, earthquake, flood zones)

## Phase 2: Workload-Specific Refinement

> Based on workload type, gather deeper technical detail.

### AI/ML Training Path

If workload is AI/ML training:

1. What GPU platform is planned? (NVIDIA H100/B200, AMD MI300X, custom ASIC)
2. What interconnect fabric? (InfiniBand NDR/XDR, RoCE v2, proprietary)
3. What is the expected job duration? (hours, days, weeks)
4. What storage requirements for training data? (TB/PB, IOPS, bandwidth)
5. Is GPU-to-GPU east-west bandwidth critical? (affects hall placement)

### Enterprise Application Path

If workload is enterprise applications:

1. What database workloads? (Oracle, SQL Server, PostgreSQL -- affects I/O profile)
2. What backup and DR requirements? (RPO, RTO targets)
3. Is hybrid cloud connectivity needed? (AWS Direct Connect, Azure ExpressRoute, GCP Interconnect)
4. What are the peak vs baseline power profiles? (steady-state vs burst)

### Storage Path

If workload is storage-intensive:

1. What storage media? (HDD, SSD, NVMe, tape)
2. Floor loading requirements? (dense HDD arrays can exceed 250 lbs/sqft)
3. What data retention requirements? (years, regulatory holds)
4. What data transfer rates are needed for ingest/egress? (Gbps)

## Conflict Analysis

After gathering requirements, flag conflicts and impossibilities:

### Common Conflicts

| Tenant Request | Conflict | Resolution |
|----------------|----------|------------|
| 50kW/rack + air cooling | Air cooling cannot support >15-20 kW/rack | Recommend direct liquid cooling or immersion |
| Tier IV + 1-year contract | Tier IV premium cannot be amortized in 1 year | Recommend Tier III with enhanced SLA credits, or longer term |
| ITAR + shared hall | ITAR requires dedicated controlled space | Upgrade to private suite with restricted access |
| 50% annual growth + no expansion clause | Growth cannot be guaranteed without contractual commitment | Add right of first refusal and expansion options |
| Low latency (<2ms) + remote/cheap location | Low cost and low latency are inversely correlated | Identify metro edge locations that balance both |

### Resource Estimation

Based on questionnaire responses, estimate:

1. **Power:** Total kW = racks x kW/rack + cooling overhead (PUE factor)
2. **Space:** Sqft = racks x sqft/rack (varies 20-30 sqft/rack including hot/cold aisle)
3. **Cooling:** Technology recommendation based on density tier
4. **Connectivity:** Number of cross-connects, required carriers, IX access
5. **Timeline:** Deployment feasibility given current facility availability

## What I Need from Upstream

This skill is independent -- no upstream artifacts required. The user is the
DC operator; the "upstream" is the tenant being interviewed.

If the operator has existing facility specifications, provide them as context
for matching tenant requirements against available inventory.

## Output Template

This skill produces two files:

### Requirements Document: `<tenant-name>-tenant-requirements.md`

**Tenant:** [Tenant Name / Code]
**Date:** [Date]
**Prepared by:** [Skill: bd-tenant-spec v1.0]
**DC Operator:** [Operator Name]

#### 1. Tenant Profile
- Company / tenant identifier
- Primary workload type
- Industry vertical
- Compliance environment

#### 2. Capacity Requirements

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| Initial power | [kW] | |
| Initial racks | [count] | |
| Power density | [kW/rack] | |
| Cooling type | [air/liquid/hybrid] | |
| Floor space | [estimated sqft] | |

#### 3. Connectivity Requirements

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| Carriers | [list] | |
| Bandwidth | [Gbps] | |
| Latency target | [ms to endpoint] | |
| Cross-connects | [count] | |
| IX peering | [yes/no, which IX] | |

#### 4. SLA and Availability

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| SLA tier | [I/II/III/IV] | |
| Availability target | [%] | |
| Power SLA | [%] | |
| Network SLA | [%] | |
| MTTR target | [hours] | |

#### 5. Compliance and Security
- Certifications required: [list]
- Physical security model: [shared/cage/suite]
- Access policy: [escorted/tenant-only/shared]
- Data residency: [jurisdictions]

#### 6. Growth Projection

| Timeline | Power Growth | Rack Growth | Notes |
|----------|-------------|-------------|-------|
| 12 months | [%] | [count] | |
| 24 months | [%] | [count] | |
| 36 months | [%] | [count] | |

#### 7. Conflict Flags
- [List any conflicts identified with resolution recommendations]

#### 8. Resource Estimate
- Estimated total power (with PUE): [kW]
- Estimated floor space: [sqft]
- Recommended cooling technology: [type]
- Recommended deployment configuration: [description]

#### 9. Contract Summary
- Requested term: [years]
- Deployment timeline: [date]
- Pricing model: [per kW / per rack / per sqft]
- Expansion provisions: [details]

### JSON Sidecar: `<tenant-name>-tenant-requirements.json`

```json
{
  "artifact_type": "tenant-requirements",
  "skill_version": "1.0",
  "tenant_name": "...",
  "workload_type": "cloud | ai-training | ai-inference | storage | enterprise | hpc | mixed",
  "initial_power_kw": 0,
  "rack_count": 0,
  "power_density_kw_per_rack": 0,
  "cooling_type": "air | liquid | hybrid | immersion",
  "sla_tier": "I | II | III | IV",
  "availability_target": 99.982,
  "compliance": ["SOC2", "ISO27001"],
  "security_model": "shared | cage | suite",
  "growth_projection": {
    "12_month_pct": 0,
    "24_month_pct": 0,
    "36_month_pct": 0
  },
  "contract_term_years": 0,
  "conflicts": ["..."],
  "estimated_total_power_kw": 0,
  "estimated_sqft": 0
}
```

## Gotchas

- **Tenants underestimate power growth by 40-60% on average.** Always ask for 36-month projections and plan for 1.5x the stated Year 1 requirements. AI/ML tenants are the worst offenders -- a tenant starting at 2MW of GPU training typically reaches 5MW within 18 months as models scale.

- **AI/ML tenants often don't know their cooling requirements.** Translate kW/rack into cooling technology for them: up to 15 kW/rack = standard air cooling, 15-30 kW = rear-door heat exchangers, 30-50 kW = direct-to-chip liquid cooling, 50+ kW = immersion cooling. Most AI tenants requesting "air cooling" actually need liquid cooling based on their density requirements.

- **SLA requirements from tenants rarely match Uptime Tier definitions.** A tenant asking for "99.999% uptime" (five nines = 5.26 minutes/year downtime) may actually need Tier III (99.982% = 1.6 hours/year) with contractual SLA credits bridging the gap. True five-nines requires Tier IV infrastructure plus redundant network -- quote accordingly.

- **Compliance requirements compound cost non-linearly.** SOC 2 alone adds 5-10% to operating cost. Adding HIPAA adds another 10-15%. Adding FedRAMP adds 20-30%. PCI-DSS plus HIPAA plus SOC 2 does not equal the sum of individual premiums -- there is overlap, but the audit burden and physical separation requirements escalate. Price compliance stacks, not individual certifications.

- **Floor loading is the hidden constraint for storage tenants.** Dense HDD arrays (84-drive 4U chassis) can exceed 250 lbs/sqft loaded. Standard raised floor supports 150 lbs/sqft. Storage tenants must be asked about media type and density early -- a floor reinforcement requirement discovered after lease signing is a project killer.

## Evaluations

See `evals/evals.json` for test scenarios covering AI training, enterprise, and hyperscale pre-lease tenants.
