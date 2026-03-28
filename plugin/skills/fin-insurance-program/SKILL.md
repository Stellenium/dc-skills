---
name: fin-insurance-program
description: "Design a data center insurance program covering 6 coverage types with recommended limits, retention strategy, and premium drivers. Use when designing insurance for a DC, evaluating coverage requirements, structuring retention and deductibles, or understanding what insurance a data center needs. Trigger with \"insurance program\", \"DC insurance\", \"coverage requirements\", \"builder's risk\", \"business interruption\", or \"what insurance does a data center need?\"."
---

# Insurance Program Design

Design a data center insurance program with coverage matrix across 6 policy types.
Produces recommended limits, retention strategy, premium driver analysis, key
exclusions to negotiate, and broker engagement guidance. NOT a premium calculator --
quantitative rate estimation requires broker market engagement. This skill structures
the program for informed broker negotiation.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. What is the project stage?
   - **Construction:** Builder's risk is primary; property transitions at substantial completion
   - **Operational:** Property, BI, cyber, environmental, E&O are primary

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the Total Insured Value (TIV)?
   - Building and site improvements ($)
   - IT equipment at replacement cost ($)
   - Mechanical/electrical infrastructure ($)
   - Total TIV ($)

4. What is the MW capacity?
   - Current operational MW
   - Planned capacity at full build-out

5. What is the facility location?
   - Natural catastrophe zone? (hurricane, earthquake, flood, wildfire)
   - FEMA flood zone designation?
   - Distance from coast (named storm exposure)?

6. What tenant type?
   - Enterprise (SLA-driven)
   - Hyperscale (custom contract terms)
   - Government (specialized requirements)
   - Mixed multi-tenant (colo)

7. Does the facility have an existing insurance program? (brownfield)
   - Current program summary (carrier, limits, retention)
   - Loss history (past 5 years)
   - Expiration dates for renewal planning

8. Is Battery Energy Storage (BESS) present?
   - Lithium-ion battery type and capacity
   - Other battery chemistry
   - No BESS

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Construction Path

If project stage is **Construction**:

1. Total construction value and timeline?
2. Construction type (steel frame, tilt-up concrete, modular)?
3. General contractor and key subcontractors?
4. Testing and commissioning period duration?
5. Soft cost exposure (delay costs, interest carry)?
6. Named storm season overlap with construction timeline?

### Operational Path

If project stage is **Operational**:

1. Annual revenue and revenue concentration?
2. Top customer percentage of total revenue?
3. SLA credit exposure (maximum annual SLA credits)?
4. Prior insurance claims in past 5 years?
5. Business continuity / disaster recovery capabilities?
6. Cybersecurity framework (SOC 2, ISO 27001)?

### BESS Path

If Battery Energy Storage (BESS) is present:

1. Battery chemistry (LFP, NMC, NCA)?
2. Total storage capacity (MWh)?
3. Fire suppression system for BESS area?
4. Distance from main building?
5. Thermal management system?
6. Prior thermal events or warranty claims?

## What I Need from Upstream

This skill can be invoked independently.

**If project-financial-model is available (from fin-project-model):**
- Total investment / TIV for limit sizing
- Revenue projections for BI calculations
- Debt covenants requiring insurance minimums
- Operating expense structure for coverage cost analysis

## Analysis & Output

### Process

1. **Assess risk profile** by facility type, location, and stage
2. **Design coverage matrix** across 6 policy types
3. **Size recommended limits** based on TIV, revenue, and exposure
4. **Determine retention strategy** (deductibles and self-insured retentions)
5. **Identify key exclusions** to negotiate with underwriters
6. **Analyze premium drivers** unique to data centers
7. **Produce broker requirements** for market engagement

### Coverage Types

#### 1. Builder's Risk (Construction Phase)

**Coverage:** Property damage during construction, soft costs (delay/interest),
testing/commissioning, materials in transit.

**Key Terms:**
- Policy period: construction start through substantial completion + testing
- Named storm deductible: 2-5% of TIV (hurricane zones)
- Flood/earthquake sub-limits: often 25-50% of TIV
- LEG 2/3 coverage: covers resulting damage from defective design (LEG 2) or
  defective design plus rectification cost (LEG 3)

**Premium Drivers:**
- TIV (primary driver)
- Construction type and fire protection
- Location (natural catastrophe exposure)
- Contractor experience and safety record
- Named storm season overlap

**Critical Negotiation Points:**
- LEG 2/3 coverage (2-3x more expensive than LEG 1 but essential for DC projects)
- Testing and commissioning coverage period and sub-limit
- Soft cost coverage for construction delay
- Hot testing / energization coverage

#### 2. Property (All-Risk -- Operational)

**Coverage:** Building, contents (IT equipment at replacement cost), mechanical/electrical
breakdown, utility service interruption.

**Key Terms:**
- Agreed amount endorsement (eliminates coinsurance penalty)
- Equipment breakdown coverage (essential for MEP systems)
- Utility service interruption (power feed failure from utility, not facility)
- Ordinance or law coverage (code upgrade costs after loss)

**Premium Drivers:**
- TIV (primary driver)
- Construction class (fire-resistive preferred)
- Protection class (sprinkler, detection, suppression)
- Loss history (past 5-10 years)
- Location (natural catastrophe exposure)

**Critical Negotiation Points:**
- IT equipment at actual replacement cost (not depreciated)
- Equipment breakdown included vs. standalone boiler & machinery
- Flood and earthquake sub-limits adequate for site exposure
- Ordinance or law limit sufficient for code-required upgrades

#### 3. Business Interruption (BI)

**Coverage:** Gross earnings loss from covered property events, extra expense to maintain
operations, contingent BI (key customer/supplier), service interruption from utility failure.

**Key Terms:**
- Waiting period: 24-72 hours (shorter = more expensive)
- Period of indemnity: 12-24 months (time to restore)
- Coinsurance: typically 50-80% (penalty for underinsurance)
- Contingent BI: covers loss from key customer or supplier disruption

**Premium Drivers:**
- Annual revenue (primary driver)
- Customer concentration risk
- SLA credit exposure
- Redundancy level (Tier III/IV reduces BI exposure)
- Disaster recovery / failover capability

**Critical Negotiation Points:**
- Waiting period alignment with SLA credit trigger periods
- Service interruption coverage for utility-caused outages
- Extra expense limit adequate for temporary capacity procurement
- Contingent BI for key customer dependencies

#### 4. Cyber Insurance

**Coverage:** First-party (forensics, notification, data restoration, business interruption)
and third-party (liability, regulatory fines, defense costs). Cyber extortion / ransomware.

**Key Terms:**
- Retroactive date: covers prior unknown breaches discovered in policy period
- War exclusion: expanded post-NotPetya to exclude "state-sponsored" attacks
- Systemic risk exclusion: may exclude widespread events (e.g., cloud provider outage)
- Sublimits for notification costs, regulatory fines, forensics

**Premium Drivers:**
- Revenue (primary driver)
- Data volume and sensitivity
- Security posture (SOC 2, ISO 27001 certification reduces premium)
- Prior incidents and claims history
- Multi-factor authentication deployment

**Critical Negotiation Points:**
- War exclusion scope (overly broad exclusions may deny most nation-state attacks)
- Systemic risk carvebacks for colo operators
- Regulatory fine coverage (jurisdiction-dependent insurability)
- Ransomware coverage and sub-limits
- Business interruption waiting period within cyber policy

#### 5. Environmental / Pollution Liability

**Coverage:** On-site remediation, third-party bodily injury/property damage from pollution
conditions, transportation pollution, disposal site liability.

**Key Terms:**
- Known conditions exclusion: pre-existing contamination not covered
- PFAS coverage: per- and polyfluoroalkyl substances from fire suppression chemicals
- Storage tank coverage: diesel fuel tanks for generators
- Mold and microbial matter: relevant for water-cooled facilities

**Premium Drivers:**
- Generator fuel storage volume and type (diesel, natural gas)
- Battery chemistry (lithium-ion thermal runaway risk)
- Fire suppression agent type (PFAS-containing foam vs. clean agent)
- Proximity to sensitive receptors (water bodies, residential)
- Environmental site assessment results

**Critical Negotiation Points:**
- PFAS coverage (rapidly evolving exclusions as PFAS litigation increases)
- Lithium-ion BESS thermal event coverage
- Emergency response cost coverage
- Transportation coverage for fuel delivery and waste removal

#### 6. E&O / Professional Liability (Colo/Managed Services)

**Coverage:** Errors in service delivery, SLA failures, data loss from operational errors,
contractual liability for service level breaches.

**Key Terms:**
- Claims-made vs. occurrence: claims-made is standard (tail coverage needed at exit)
- Defense costs: inside limits (erodes coverage) vs. outside limits (preferred)
- Contractual liability coverage: for SLA and contractual obligations
- Technology E&O: combined professional and technology liability

**Premium Drivers:**
- Revenue from managed/professional services
- Service scope (colocation vs. managed hosting vs. cloud)
- Contractual SLA credit exposure
- Prior claims history
- Customer concentration

**Critical Negotiation Points:**
- Defense costs outside limits
- Contractual liability for SLA obligations
- Technology E&O vs. standard professional liability
- Tail coverage period at policy termination

### Coverage Matrix Output Template

| Coverage | Recommended Limit | Retention | Premium Range (% TIV/Rev) | Key Exclusions | Negotiation Priority |
|----------|------------------|-----------|--------------------------|----------------|---------------------|
| Builder's Risk | 100% TIV | 1-2% TIV | 0.15-0.35% TIV | Named storm, flood, quake sub-limits | LEG 2/3, testing period |
| Property | 100% TIV | 0.5-1% TIV | 0.10-0.25% TIV | Flood/quake sub-limits | Equipment breakdown, agreed amount |
| Business Interruption | 12-24 months gross earnings | 24-72 hrs | 0.05-0.15% revenue | Waiting period gap | Service interruption, contingent BI |
| Cyber | $25M-100M | $250K-1M | 0.5-2.0% revenue | War, systemic risk | War exclusion scope, BI sublimit |
| Environmental | $10M-50M | $50K-250K | 0.01-0.05% TIV | Known conditions, PFAS | PFAS, BESS coverage |
| E&O | $10M-50M | $100K-500K | 0.3-1.0% services rev | Contractual exclusions | Defense outside limits |

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Primary coverages | Property, BI | Property, BI, Builder's | Property, BI, Cyber | All 6 | Property, Builder's | Property |
| TIV range | $50-500M | $500M-5B | $200M-2B | $100M-1B | $10-100M | $5-50M |
| Cyber priority | Medium | High | Very High | Very High | Low | Low |
| E&O needed | No | No | No | Yes | No | No |
| BESS exposure | Rare | Growing | Possible | Rare | Common | Common |

### Reference Data

Load these files on demand -- do not read upfront:

- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

## Output Template

This skill produces two files:
1. `<project-name>-insurance-program.md` -- Full program recommendation
2. `<project-name>-insurance-program.json` -- Structured data

### JSON Sidecar Schema

```json
{
  "artifact_type": "insurance-program",
  "skill_version": "1.0",
  "project_name": "...",
  "coverages": [
    {
      "type": "...",
      "recommended_limit": "...",
      "retention": "...",
      "premium_range_pct": "...",
      "key_exclusions": [],
      "negotiation_points": []
    }
  ],
  "total_program": {
    "estimated_annual_premium_range": "...",
    "tiv": 0,
    "retention_strategy": "..."
  },
  "risk_engineering": {
    "recommendations": []
  },
  "broker_requirements": []
}
```

## Gotchas

- **Lithium-ion BESS systems are becoming uninsurable through standard property markets.** Underwriters are increasingly excluding or sub-limiting lithium-ion battery storage after multiple thermal runaway events. BESS coverage often requires specialty placement through London or Bermuda markets at 3-5x standard property rates. Budget accordingly and engage BESS-specialist brokers early.

- **Cyber insurance war exclusions were expanded after NotPetya and now specifically exclude "state-sponsored" attacks, which is most DC cyber risk.** Lloyd's Market Bulletin Y5381 (2023) requires cyber policies to exclude state-backed attacks. Since most sophisticated DC-targeted attacks are nation-state affiliated, the war exclusion can effectively void cyber coverage for the highest-severity scenarios. Negotiate carvebacks carefully.

- **Builder's risk LEG 2/3 coverage costs 2-3x more than LEG 1 but is essential for DC projects.** LEG 1 covers only defective materials; LEG 2 covers resulting damage from defective design; LEG 3 covers rectification of the defective design itself. DC projects with complex MEP systems need at minimum LEG 2 to cover cascading failures from design errors.

- **Business interruption waiting periods must align with SLA credit triggers.** If the BI policy has a 72-hour waiting period but SLA credits trigger at 4 hours, there is a 68-hour gap where the operator absorbs SLA credit liability without insurance coverage. Negotiate the shortest achievable waiting period or budget for the gap.

- **Equipment breakdown is the #1 property claim type for data centers but is often an optional endorsement.** Mechanical and electrical breakdown (transformers, UPS, generators, chillers) is more frequent than fire, flood, or wind damage. Ensure equipment breakdown is included in the property policy, not overlooked as an optional add-on.

## Disclaimer

---

FINANCIAL DISCLAIMER: The financial projections, cost estimates, and economic
analyses produced by this skill are for preliminary planning and evaluation
purposes only. This is not investment advice, financial advice, or
a recommendation to proceed with any transaction. Actual costs, revenues, and
returns will vary based on market conditions, vendor negotiations, site-specific
factors, and regulatory changes not modeled here.

All financial outputs are presented as ranges where possible. Point estimates
should be treated as order-of-magnitude guidance, not bankable figures. Users
must engage qualified financial advisors, tax professionals, and legal counsel
before making investment decisions based on these outputs.

Sensitivity analyses are provided to illustrate the impact of key variable
changes. They do not represent probabilistic forecasts or guarantee that
outcomes will fall within the stated ranges.

See [Disclaimer Framework](../../references/DISCLAIMER-FRAMEWORK.md) for full terms.

---

## Evaluations

See `evals/evals.json` for test scenarios covering construction-phase hurricane zone,
operational colo multi-coverage, and sovereign DC with BESS.
