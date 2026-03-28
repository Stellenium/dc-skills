---
name: proc-contract-structure
description: "Structure procurement contracts for data center projects with FIDIC-aligned terms, milestone payments, performance guarantees, and risk allocation. Use when structuring a DC construction contract, defining milestone payment schedules, allocating risk in procurement agreements, or selecting contract types (EPC, design-build, CM-at-risk). Trigger with \"contract structure\", \"EPC contract\", \"FIDIC\", \"milestone payments\", \"procurement contract\", \"DC construction contract\", or \"risk allocation\"."
---

# Contract Structure & Form Selection

Generate contract form selection and structure for data center construction and
fit-out. Recommends the appropriate FIDIC contract form based on design
responsibility and risk appetite, then produces a complete contract structure
with milestone payment schedule, retention terms, warranties, liquidated damages,
and performance guarantees.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the contract structure approach.

**Project Context:**

1. What is the project type?
   - **Shell-and-core:** Building structure only, MEP by others
   - **Fit-out:** White space to operational data hall
   - **EPC turnkey:** Complete facility from greenfield
   - **Design-build:** Contractor designs and builds to requirements
   - **Modular/prefab:** Factory-built modules with site assembly

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the approximate contract value range?
   - Under $50M
   - $50M - $200M
   - $200M - $500M
   - $500M - $2B
   - Over $2B (campus or multi-phase)

4. Who bears design responsibility?
   - **Employer:** Employer has full design team; contractor builds to employer's design
   - **Contractor:** Contractor provides design-build services to employer's requirements
   - **Full EPC:** Contractor performs all engineering, procurement, and construction
   - **Split:** Employer designs some systems (e.g., IT/network), contractor designs others (MEP/structural)

5. What is the jurisdiction (legal system)?
   - **Common law** (US, UK, Australia, Singapore, Hong Kong)
   - **Civil law** (Continental Europe, Middle East, Latin America, parts of Africa/Asia)
   - **Mixed/hybrid** (South Africa, Scotland, Philippines)

6. How many contract packages?
   - **Single EPC:** One contractor for entire scope
   - **Multi-trade:** Separate packages (civil, structural, MEP, IT)
   - **Two-package:** Shell-and-core + fit-out
   - **Hybrid:** EPC for base building, design-build for IT infrastructure

7. What is the employer's risk appetite?
   - **Low:** Maximum risk transfer to contractor (Silver Book approach)
   - **Medium:** Shared risk with employer design control (Yellow/Red Book)
   - **High:** Employer retains most risk for cost savings (Red Book with employer design)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### EPC Turnkey Path

If project type is **EPC turnkey:**

1. Is this a repeat build or first-of-kind design?
2. What performance guarantees are required? (PUE target, cooling capacity, power availability)
3. What is the maximum acceptable delay from notice to proceed to substantial completion?
4. Is there a parent company guarantee or performance bond preference?

### Multi-Trade Path

If contract structure is **Multi-trade:**

1. How many trade packages? List the scope divisions.
2. Who is the construction manager / coordination entity?
3. How are interface risks allocated between packages?
4. Is there a schedule coordination mechanism between trade contractors?

### Sovereign/Government Path

If facility type is **Sovereign:**

1. Are there domestic content requirements for contractors?
2. What security clearance requirements apply to construction personnel?
3. Is there a government procurement framework that must be followed?
4. Are there sovereign immunity or dispute resolution constraints?

## What I Need from Upstream

**From rfp-package (proc-rfp-generator):**
- Scope of work definition
- Evaluation criteria and weights
- Commercial terms framework
- Technical requirements and specifications

**From bid-evaluation-report (proc-bid-evaluation):**
- Recommended contractor and rationale
- Negotiation points identified during evaluation
- Risk factors from bid analysis

If upstream artifacts are not available, I will gather project details
directly through discovery questions.

## Reference Data

Load on demand -- do not read upfront:

- [FIDIC contract forms](../../references/FIDIC-CONTRACTS.md) -- Contract form comparison, risk allocation matrix, key clause summaries for Red/Yellow/Silver/Gold Book selection
- [SLA benchmarks](../../references/SLA-BENCHMARKS.md) -- Tier I-IV availability targets, MTTR/MTBF benchmarks for performance guarantee thresholds

## Contract Structure Analysis

### Step 1: Contract Form Selection

Recommend FIDIC Red/Yellow/Silver/Gold Book based on design responsibility and risk appetite. Reference FIDIC-CONTRACTS.md risk allocation matrix.

**DC-specific form mapping:**
- **Silver Book** for turnkey data halls -- maximum risk transfer, lump sum, performance guarantee
- **Yellow Book** for design-build MEP packages -- contractor designs mechanical/electrical to employer requirements
- **Red Book** for employer-designed shell-and-core -- employer retains design consultant, contractor builds to drawings
- **Gold Book** for design-build-operate (DBO) arrangements -- managed DC platforms where same entity designs, builds, and operates

### Step 2: Milestone Payment Schedule

Typical DC milestone progression (adjust by facility type and scope):

| Milestone | Typical % | Cumulative | Trigger |
|-----------|-----------|------------|---------|
| Mobilization / advance payment | 5-10% | 5-10% | Notice to proceed + advance payment guarantee |
| Foundations complete | 15% | 20-25% | Foundation inspection certificate |
| Structural steel / building envelope | 20% | 40-45% | Structural completion certificate |
| MEP rough-in | 25% | 65-70% | MEP rough-in inspection |
| MEP finishings and equipment install | 15% | 80-85% | Equipment energization certificate |
| Commissioning (Level 2-3) | 10% | 90-95% | Commissioning completion certificate |
| Substantial completion | 5-10% | 100% | Substantial completion certificate |
| Retention release | (held from above) | -- | End of defects liability period |

### Step 3: Retention Terms

- **Retention rate:** Typically 5-10% withheld from each progress payment
- **First release:** 50% of retention at substantial completion
- **Final release:** Remaining 50% at end of defects liability period (12-24 months)
- **Performance bond alternative:** Contractor may substitute a performance bond (typically 10-15% of contract value) in lieu of cash retention
- **Retention cap:** Some jurisdictions cap retention at 5% by statute

### Step 4: Warranty Provisions

| Scope | Duration | Responsible Party | Notes |
|-------|----------|-------------------|-------|
| General construction | 2 years | Contractor | Defects liability period per FIDIC |
| Mechanical systems (HVAC, cooling) | 2-5 years | Contractor + manufacturer | Manufacturer warranty assigned to employer |
| Electrical systems (switchgear, UPS) | 2-5 years | Contractor + manufacturer | Include commissioning verification |
| Roofing and waterproofing | 10-20 years | Manufacturer (NDL) | No-dollar-limit manufacturer warranty |
| UPS and generators | 5 years (manufacturer) | Manufacturer + extended service | Extended service agreement separate from construction contract |
| Cooling equipment (chillers, CRAHs) | Manufacturer warranty + performance guarantee | Manufacturer | Performance guarantee tied to design ambient conditions |
| Fire suppression systems | 2-5 years | Contractor + manufacturer | Annual inspection and testing obligation |
| BMS/DCIM software | 1-3 years | Software vendor | License and maintenance separate from construction |

### Step 5: Liquidated Damages Framework

**Delay LDs:**
- Typical rate: 0.1-0.5% of contract value per day of delay
- Cap: 10-15% of contract value (uncapped LDs are unenforceable in most jurisdictions)
- Trigger: Each day beyond the contractual substantial completion date
- Exclusions: Force majeure events, employer-caused delays, variations

**Performance LDs:**

| Metric | Threshold | LD Formula | Measurement |
|--------|-----------|------------|-------------|
| PUE guarantee | Design PUE target (e.g., 1.25) | Per 0.01 PUE exceedance: $X per MW per year | Measured at design ambient over 30-day test period |
| Cooling capacity | Design capacity at specified ambient | Per kW shortfall: replacement cost + lost revenue | Tested at design wet-bulb/dry-bulb conditions |
| Power availability | Tier-specific availability target | Per hour of unplanned downtime: $X | Measured over 12-month operational period |
| Noise exceedance | Property boundary dBA limit | Per dBA exceedance: remediation cost + fines | Measured per local code requirements |

### Step 6: Performance Guarantees

Reference SLA-BENCHMARKS.md for availability targets by Tier:

- **PUE design target** as contractual performance metric with measurement methodology
- **Cooling capacity guarantee** at design ambient (wet-bulb for evaporative, dry-bulb for air-cooled)
- **Power availability** per Uptime Tier target (e.g., Tier III: 99.982%)
- **Commissioning success criteria** per eng-commissioning Level 1-5 framework

## Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|-------------|------------|-----------|------|---------|------|
| Typical form | Yellow Book | Silver Book | Silver + addenda | Yellow Book | Silver Book | Simplified |
| Milestone granularity | Standard | Detailed | Detailed | Standard | Factory + site | Minimal |
| Retention rate | 10% | 5% | 10% | 10% | 5% | 5-10% |
| Defects liability | 12 months | 24 months | 24 months | 12 months | 12 months | 12 months |
| Delay LD rate | 0.1%/day | 0.3-0.5%/day | 0.5%/day | 0.1-0.2%/day | 0.3%/day | 0.1%/day |
| Performance LDs | PUE only | PUE + capacity + availability | Full suite | PUE + availability | PUE + capacity | Minimal |

## Output Template

This skill produces two files:

### Markdown Report: `<project-name>-contract-structure.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: proc-contract-structure v1.0]

#### 1. Contract Form Recommendation
- Recommended FIDIC form with rationale
- Risk allocation summary referencing FIDIC-CONTRACTS.md
- Particular conditions and amendments needed

#### 2. Milestone Payment Schedule
- Milestone table with percentages, cumulative totals, and triggers
- Advance payment guarantee requirements
- Progress payment certification process

#### 3. Retention and Security
- Retention rate and release schedule
- Performance bond requirements
- Parent company guarantee (if applicable)

#### 4. Warranty Provisions
- Warranty schedule by system/scope
- Manufacturer warranty assignment mechanism
- Extended service agreement recommendations

#### 5. Liquidated Damages
- Delay LD rate, cap, and trigger conditions
- Performance LD metrics, thresholds, and formulas
- Exclusions and relief events

#### 6. Performance Guarantees
- PUE guarantee with measurement methodology
- Cooling capacity guarantee at design conditions
- Availability guarantee per SLA-BENCHMARKS.md targets
- Commissioning success criteria

### JSON Sidecar: `<project-name>-contract-structure.json`

```json
{
  "artifact_type": "contract-structure",
  "skill_version": "1.0",
  "project_name": "...",
  "form": {
    "recommended": "silver | yellow | red | gold",
    "rationale": "...",
    "fidic_book": "Silver Book 2017 2nd Edition"
  },
  "milestones": [
    {
      "name": "Mobilization",
      "percentage": 10,
      "cumulative_pct": 10,
      "trigger": "Notice to proceed + advance payment guarantee"
    }
  ],
  "retention": {
    "rate_pct": 5,
    "release_schedule": [
      "50% at substantial completion",
      "50% at end of defects liability period"
    ]
  },
  "warranties": [
    {
      "scope": "General construction",
      "duration_years": 2,
      "responsible_party": "Contractor"
    }
  ],
  "liquidated_damages": {
    "delay": {
      "rate_per_day_pct": 0.3,
      "cap_pct": 10
    },
    "performance": [
      {
        "metric": "PUE",
        "threshold": 1.25,
        "ld_formula": "Per 0.01 PUE exceedance above target"
      }
    ]
  },
  "performance_guarantees": [
    {
      "metric": "PUE",
      "target": 1.25,
      "measurement_method": "30-day average at design ambient"
    }
  ]
}
```

## Gotchas

- **FIDIC Silver Book shifts ALL ground conditions risk to contractor.** This is inappropriate for greenfield DC sites where geotechnical surprises are common (unexpected rock, high water table, contaminated soil). Use Silver Book only when site investigation is complete and ground conditions are well-characterized. Otherwise, use Yellow Book with a Geotechnical Baseline Report (GBR) mechanism.

- **Delay LDs capped at 10% of contract value may be unenforceable as penalties in many civil law jurisdictions.** Civil law systems (Continental Europe, Middle East, parts of Asia) require LDs to reflect genuine pre-estimate of loss. If actual daily loss from DC delay is $200K but the LD rate calculates to $2M/day, a court may strike the LD clause entirely. Always document the loss calculation methodology.

- **Performance bonds from contractors' surety companies typically cap at 10-15% of contract value, not 100%.** An employer requesting a 100% performance bond will either receive no bids or pay a significant premium. Standard practice: 10% performance bond + 5-10% retention + parent company guarantee for the balance.

- **Multi-trade contract structures require explicit interface risk allocation.** When separate contractors handle civil, MEP, and IT infrastructure, the interface between packages (e.g., who commissions the handoff between electrical and cooling) must be defined in each contract. Interface disputes are the #1 cause of multi-trade DC project delays.

- **Advance payment guarantees must be unconditional, on-demand bank guarantees.** Conditional guarantees (that require proof of contractor default before calling) are worthless in practice because contractors dispute the default claim. Specify "unconditional, irrevocable, on-demand" guarantee language explicitly.

## Evaluations

See `evals/evals.json` for test scenarios covering EPC turnkey, multi-trade campus, and modular DC contract structures.
