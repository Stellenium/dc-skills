---
name: bd-national-compute
description: "Develop national AI compute strategy for government ministries and development finance institutions with sovereign capacity modeling and phased buildout. Use when advising a government on national compute infrastructure, modeling sovereign AI capacity needs, planning national data center strategy, or preparing DFI funding proposals. Trigger with \"national compute\", \"sovereign AI\", \"national strategy\", \"government AI infrastructure\", \"DFI proposal\", or \"country-level compute planning\"."
argument-hint: "<country>"
---

# National Compute Strategy

Develop a national AI compute strategy for government ministries and development
finance institutions. Models sovereign AI compute demand, evaluates geographic
distribution, and designs phased capacity buildout aligned with national AI
strategies and DFI funding requirements.

Target audience: government planners, ministry of ICT officials, and DFI
investment teams evaluating sovereign digital infrastructure investments.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the strategy framework.

**National Context:**

1. What country or region is this strategy for?
   - Country name
   - Region (if sub-national strategy)
   - Neighboring countries (for regional compute hub analysis)

2. What is the current domestic compute capacity estimate?
   - Existing public cloud availability (hyperscaler regions present?)
   - Existing private/government DC capacity (MW)
   - Current import dependency (% of compute accessed from foreign providers)
   - If unknown, state "unknown -- to be assessed"

3. Does a national AI strategy exist?
   - **Yes:** Name the strategy document and key goals
   - **In development:** What ministry is leading? What timeline?
   - **No:** What is the government's stated digital transformation agenda?

4. What are the target workloads?
   - **Research:** University and national lab AI research computing
   - **Enterprise:** Private sector AI adoption across industries
   - **Government:** E-government, defense, healthcare AI, smart city
   - **All of the above** (comprehensive national strategy)

5. What is the country's population?
   - Total population
   - Urban vs rural distribution
   - Key population centers and their sizes

6. What is the GDP and GDP per capita?
   - Current GDP ($)
   - GDP per capita ($)
   - GDP growth rate (%)

7. How many universities and research institutions exist?
   - Total count
   - Count with active AI/ML research programs
   - Annual STEM graduate output

8. What is the existing DC and fiber infrastructure?
   - Number and capacity of existing data centers
   - Fiber backbone maturity (national backbone, last-mile penetration)
   - Submarine cable connectivity (number of landing points, bandwidth)
   - Internet exchange points (IXPs) and capacity

## Phase 2: Context Refinement

> Based on Phase 1 answers, refine the strategy scope.

### Research Compute Path

If target workloads include **Research:**

1. What is the current research computing capacity? (university clusters, HPC centers)
2. What is the researcher-to-GPU ratio? (benchmark: leading nations at 0.5-2.0 GPU-hours/researcher/year)
3. What are the priority research domains? (NLP in local languages, drug discovery, climate modeling, agriculture AI)
4. Is there a national research and education network (NREN)?

### Enterprise Compute Path

If target workloads include **Enterprise:**

1. What is the enterprise AI adoption rate? (% of enterprises using AI tools)
2. What is the largest industry vertical? (financial services, agriculture, manufacturing, extractives)
3. What is the current cloud spending? (domestic vs foreign providers)
4. What regulatory barriers exist? (data localization requirements, cloud-first policies)

### Government Compute Path

If target workloads include **Government:**

1. What government digitization index is applicable? (UN E-Government Development Index rank)
2. What government AI use cases are prioritized? (tax administration, healthcare, defense, border management)
3. What security classification requirements exist? (classified vs unclassified workloads)
4. What is the government IT procurement framework?

## What I Need from Upstream

**From site-feasibility-report (predev-site-feasibility):**
- Power availability and grid capacity at candidate sites
- Climate data for cooling design
- Regulatory environment summary
- Fiber connectivity assessment

If upstream artifact is not available, I will develop the national compute
strategy from discovery questions and publicly available country data.

## Reference Data

Load on demand -- do not read upfront:

- [DFI funding guide](../../references/DFI-FUNDING.md) -- DFI institution profiles, mandates, eligible countries, ticket sizes, and DC-relevant programs for funding strategy alignment
- [GPU reference](../../references/GPU-REFERENCE.md) -- GPU TDP and performance data for compute-to-MW conversion

## Demand Modeling Methodology

### Research Compute Demand

| Input | Formula | Benchmark |
|-------|---------|-----------|
| Active AI researchers | Count from universities + national labs | Leading nations: 50-200 per million population |
| GPU-hours per researcher per year | 0.5 - 2.0 (varies by funding level) | US/China: 2.0; mid-income: 0.5-1.0 |
| Total research GPU-hours/year | Researchers * hours/researcher | -- |
| Research PetaFLOPS sustained | GPU-hours * GPU PFLOPS / 8760 | Reference GPU-REFERENCE.md |
| Research MW | PetaFLOPS / efficiency factor | Current: ~5 PFLOPS per MW (H100-class) |

### Enterprise Compute Demand

| Input | Formula | Benchmark |
|-------|---------|-----------|
| Total enterprises | Business registry count | -- |
| AI adoption rate | % currently using or planning AI | Leading: 30-50%; emerging: 5-15% |
| Average compute per AI-active enterprise | Scaled by GDP per capita | Leading: 50 GPU-hours/mo; emerging: 10 |
| Total enterprise GPU-hours/year | Enterprises * adoption * avg compute * 12 | -- |
| Enterprise MW | Convert via GPU efficiency | -- |

### Government Compute Demand

| Input | Formula | Benchmark |
|-------|---------|-----------|
| E-government index (EGDI) | UN ranking 0-1.0 | Leading: >0.9; emerging: 0.4-0.7 |
| Government AI budget | % of IT budget allocated to AI | Leading: 5-10%; emerging: 1-3% |
| Government workloads MW | Budget / cost per MW per year | Varies by workload type |
| Defense/classified MW | Separate budget line | Country-specific |

### Total Demand Summary

- **Total demand** = research + enterprise + government (PetaFLOPS sustained)
- **Total MW** = demand / efficiency factor (currently ~5 PFLOPS per MW)
- **Growth trajectory:** 2x every 18-24 months (driven by model scaling and adoption)

## Supply Assessment

- **Current domestic capacity:** Existing DC infrastructure (MW)
- **Foreign provider capacity:** Hyperscaler cloud regions serving the country
- **Import dependency:** % of compute accessed from foreign jurisdictions
- **Sovereign capacity gap:** Total demand - domestic capacity
- **Connectivity constraint:** Submarine cable bandwidth and latency to nearest compute hub

## Distribution Strategy

### Centralized Model
- **Description:** Single national data center facility
- **Pros:** Lowest cost, economies of scale, simpler operations
- **Cons:** Higher latency for remote regions, single point of failure, political concentration
- **Best for:** Small nations (<10M population), limited budget, initial phase

### Distributed Model
- **Description:** Multiple smaller DCs across geographic regions
- **Pros:** Lower latency nationwide, greater resilience, political inclusivity
- **Cons:** Higher total cost, operational complexity, smaller economies of scale
- **Best for:** Large nations (>50M population), archipelagos, nations with regional governments

### Hybrid Model (Recommended for most countries)
- **Description:** 1-2 primary facilities (70-80% of capacity) + edge/regional sites (20-30%)
- **Pros:** Balances cost efficiency with coverage, resilience through geographic diversity
- **Cons:** Requires robust national fiber backbone for inter-site connectivity
- **Best for:** Mid-size nations (10-50M population), nations with established fiber backbone

**Decision factors:** Geography, population distribution, fiber backbone maturity, disaster resilience requirements, political considerations.

## Phased Buildout

### Phase 1: Foundation (Years 1-2)
- Anchor facility with immediate research and government workloads
- Minimum viable capacity: 5-20MW depending on country size
- Focus: national AI research cluster + government cloud pilot
- Funding: sovereign equity + DFI concessional debt
- Target: operational within 24 months

### Phase 2: Expansion (Years 3-5)
- Expand anchor facility to meet enterprise demand growth
- Add secondary site(s) if distributed model selected
- Focus: enterprise AI adoption, commercial tenant onboarding
- Funding: PPP structures, commercial co-investment
- Target: 2-3x Phase 1 capacity

### Phase 3: Maturity (Years 5-10)
- Full national coverage per distribution strategy
- Regional connectivity and edge network
- Export capacity (serving neighboring countries)
- Workforce at scale, local manufacturing/assembly
- Funding: sustainable commercial operations + reinvestment

## Funding Strategy

Reference DFI-FUNDING.md for institution-specific alignment.

**Typical sovereign DC funding structure:**

| Source | Share | Terms | Role |
|--------|-------|-------|------|
| Sovereign equity | 20-30% | Government budget allocation or SWF | Anchor commitment, demonstrates sovereignty |
| DFI concessional debt | 30-40% | IFC/AfDB/ADB/EBRD; 15-20 year tenor, below-market rate | De-risks project for private capital |
| Private co-investment | 20-30% | Market-rate equity or mezzanine | Operational expertise, commercial discipline |
| Grants/TA | 5-10% | USTDA/bilateral; non-repayable | Feasibility studies, technical assistance |

**DFI alignment checklist:**
- Development impact metrics (jobs, digital access, gender inclusion)
- Environmental and social safeguards (IFC Performance Standards)
- Procurement standards (international competitive bidding)
- Reporting and monitoring framework
- Local content and technology transfer commitments

## Output Template

This skill produces two files:

### Strategy Document: `<country-name>-national-compute-strategy.md`

**Country:** [Country Name]
**Date:** [Date]
**Prepared by:** [Skill: bd-national-compute v1.0]

#### 1. Executive Summary
- Current compute capacity gap
- Recommended strategy (centralized/distributed/hybrid)
- Total investment required and phasing
- Key recommendations for government action

#### 2. Demand Assessment
- Research, enterprise, and government demand modeling
- Total demand in PetaFLOPS and MW
- Growth trajectory (5-year and 10-year)

#### 3. Supply Assessment
- Current domestic and foreign provider capacity
- Import dependency analysis
- Sovereign capacity gap

#### 4. Distribution Strategy
- Recommended model with rationale
- Site selection criteria and candidate locations
- Inter-site connectivity requirements

#### 5. Phased Buildout Plan
- Phase 1-3 capacity, investment, timeline, and milestones
- Technology roadmap (GPU generations, cooling evolution)
- Workforce development plan

#### 6. Funding Strategy
- Funding structure with source allocations
- DFI alignment and application roadmap
- PPP structure for long-term operations

#### 7. Policy Recommendations
- Data sovereignty legislation needed
- Compute procurement framework
- Workforce development initiatives
- Regional cooperation opportunities

### JSON Sidecar: `<country-name>-national-compute-strategy.json`

```json
{
  "artifact_type": "national-compute-strategy",
  "skill_version": "1.0",
  "country": "...",
  "demand": {
    "research_pflops": 0,
    "enterprise_pflops": 0,
    "government_pflops": 0,
    "total_pflops": 0,
    "total_mw": 0
  },
  "supply": {
    "current_mw": 0,
    "gap_mw": 0,
    "import_dependency_pct": 0
  },
  "distribution": {
    "model": "centralized | distributed | hybrid",
    "sites": [
      {"name": "National DC 1", "capacity_mw": 20, "role": "primary"}
    ]
  },
  "phased_buildout": {
    "phases": [
      {
        "name": "Phase 1: Foundation",
        "years": "1-2",
        "capacity_mw": 10,
        "investment": 150000000,
        "milestones": ["Site selection", "Ground-breaking", "Commissioning"]
      }
    ]
  },
  "funding": {
    "total_investment": 0,
    "sovereign_equity_pct": 25,
    "dfi_debt_pct": 35,
    "private_pct": 30,
    "grants_pct": 10,
    "institutions": ["IFC", "AfDB"]
  },
  "timeline_years": 10
}
```

## Gotchas

- **Most national AI strategies overestimate research demand by 5-10x and underestimate enterprise demand.** Government planners anchor on prestigious AI research use cases, but 70-80% of national compute demand comes from enterprise workloads (financial services AI, agriculture optimization, supply chain) within 5 years of launch. Size the facility for enterprise demand, not research headlines.

- **Submarine cable connectivity is the binding constraint for island nations.** A national compute strategy for Jamaica, Sri Lanka, or the Philippines is meaningless without latency-adequate connectivity. If round-trip latency to the nearest cloud region exceeds 100ms, enterprise AI workloads will not perform acceptably. Address connectivity before compute capacity.

- **DFIs will not fund compute infrastructure that primarily serves foreign cloud providers.** The "sovereignty test" applies: if the primary tenant is a US hyperscaler using the facility as a local PoP, the project fails DFI development impact criteria. DFIs require demonstrable sovereign utility -- government workloads, local enterprise demand, domestic research compute.

- **GPU technology refresh cycles (3-5 years) are rarely budgeted in national strategies.** A 20MW sovereign AI facility built with H100-class GPUs in 2026 will need $200M+ in GPU replacement by 2030 to remain competitive. National strategies must include technology refresh CapEx in the funding model, not just initial buildout.

- **"National AI compute" is not the same as "national data center."** A hyperscale facility hosting cloud storage, CDN, and general-purpose VMs is a data center, not an AI compute facility. Sovereign AI compute requires high-density GPU infrastructure (40-100+ kW/rack), high-bandwidth interconnects (InfiniBand or equivalent), and liquid cooling -- fundamentally different engineering from traditional DCs. Strategy documents must specify the distinction.

## Evaluations

See `evals/evals.json` for test scenarios covering mid-income Asian, Sub-Saharan African, and Gulf state national compute strategies.
