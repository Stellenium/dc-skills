---
name: predev-site-feasibility
description: "Evaluate data center site feasibility with weighted multi-factor scoring producing GO, CONDITIONAL, or NO-GO recommendations. Use when screening potential DC sites, comparing multiple locations, performing site due diligence, or assessing power, fiber, water, climate, seismic, tax incentive, and zoning factors for a data center. Trigger with \"is this site good for a data center?\", \"site feasibility\", \"compare DC sites\", \"site selection\", or \"evaluate this location for a DC\"."
argument-hint: "<site-address or region>"
---

# Site Feasibility Assessment

Evaluate data center site feasibility across 9 weighted factors producing a GO, CONDITIONAL,
or NO-GO recommendation with confidence scoring. Supports multi-site comparison for up to
5 candidate locations. Consumes shared reference data for tax incentives, power tariffs,
and construction cost benchmarks.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** New construction from bare site -- proceed to Greenfield Path below
   - **Brownfield:** Conversion of existing building or facility upgrade -- proceed to Brownfield Path below

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the target IT capacity (MW)? Single site or multi-site evaluation?
   - Specify MW per site if comparing candidates
   - Multi-site comparison supports up to 5 candidate locations

4. What is the geographic preference or specific candidate site(s)?
   - Country, state/province, city, or specific address
   - If multi-site: list all candidate locations

5. What is the primary workload type?
   - AI training (high density, liquid cooling likely)
   - AI inference (moderate density, mixed cooling)
   - Enterprise / general compute (standard density)
   - Mixed workloads

6. Are there regulatory or sovereignty constraints?
   - Data sovereignty / data residency requirements
   - Government / defense classification
   - Commercial (no special constraints)

7. What are your priority factors? Select your top 3:
   - Power availability and cost
   - Network connectivity
   - Construction and land cost
   - Tax incentives
   - Climate suitability
   - Labor availability
   - Sovereignty / regulatory alignment

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. What is the total land area available (acres)?
2. Current zoning status? (industrial, agricultural, unzoned, requires rezoning)
3. Nearest utility substation and available capacity?
4. Fiber route access? (on-site, adjacent, within 1 mile, >1 mile)
5. Water source for cooling? (municipal, well, reclaimed, none/dry cooling planned)

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. Existing building type and size (sqft)?
2. Current electrical service capacity (voltage/amperage)?
3. Structural load capacity (psf floor loading)?
4. Environmental remediation needed? (asbestos, soil contamination, UST)
5. Existing fiber or telecom infrastructure?

### Facility Type Refinements

**Hyperscale additions:**
- Campus deployment or single building?
- Phased build-out plan (number of phases, timeline)?
- Custom power/cooling specifications or vendor-standard?

**Sovereign additions:**
- Security clearance level required for construction/operations?
- Physical security perimeter requirements (setback, SCIF)?
- Dual utility feed from separate substations required?

**Edge additions:**
- Number of distributed locations in evaluation?
- Unmanned operation required?
- Containerized/modular deployment preference?

## What I Need from Upstream

This skill is the entry point of the chain -- no upstream artifacts required.

If the user has existing reports, market studies, or site data, provide them as context
for richer analysis. The skill will incorporate any available information.

## Analysis & Output

### Process

1. **Identify applicable factors** based on location and facility type
2. **Score each factor 1-5** using defined thresholds (see Factor Scoring below)
3. **Apply weights** based on user priority (Q7) or defaults
4. **Calculate weighted average** and apply override rules
5. **Check Opportunity Zone eligibility** using FEDERAL-TAX-GUIDE.md
6. **Generate recommendation** with confidence range
7. **If multi-site:** produce comparison matrix ranking all candidates

### Factor Scoring (1-5 Scale)

| Factor | Weight (Default) | Score 5 (Excellent) | Score 3 (Adequate) | Score 1 (Critical Risk) |
|--------|-----------------|--------------------|--------------------|------------------------|
| Power | 20% | >100MW available, <6mo interconnect | 10-50MW, 12-18mo queue | <5MW, >24mo or no capacity |
| Connectivity | 15% | 3+ diverse fiber routes, carrier hotel <5mi | 2 routes, carrier <20mi | Single route, >50mi |
| Cost | 15% | <$10M/MW construction, <5c/kWh power | $10-15M/MW, 5-8c/kWh | >$18M/MW, >12c/kWh |
| Tax Incentives | 10% | Sales + property tax exemption, OZ eligible | Sales tax exemption only | No DC incentives, high tax burden |
| Climate | 10% | ASHRAE A1, <500 cooling degree days | ASHRAE A2, 500-2000 CDD | ASHRAE A4, >3500 CDD, hurricane/tornado zone |
| Labor | 10% | Skilled DC workforce available, <80 labor index | Moderate pool, 80-110 index | Severe shortage, >130 index |
| Sovereignty | 10% | No restrictions, favorable regulatory | Moderate compliance burden | Blocking restrictions, adverse regulation |
| Seismic | 5% | Zone 0-1, minimal risk | Zone 2, moderate risk | Zone 3-4, significant seismic activity |
| Water | 5% | Abundant municipal supply, no restrictions | Moderate supply, some allocation limits | Severe scarcity, prior appropriation limits |

**Weight adjustment:** When the user selects top-3 priorities (Q7), boost each selected factor
by +5% and reduce remaining factors proportionally to maintain 100% total.

### Decision Thresholds

| Weighted Average | Recommendation | Condition |
|-----------------|----------------|-----------|
| >= 3.5 | **GO** | Proceed with detailed design and due diligence |
| 2.5 - 3.49 | **CONDITIONAL** | Proceed with specific mitigations for low-scoring factors |
| < 2.5 | **NO-GO** | Site does not meet minimum feasibility threshold |

**Override rule:** Any single factor scoring 1 triggers automatic CONDITIONAL regardless of
weighted average. Document the blocking factor and required mitigation.

### Reference Data

Load these files on demand -- do not read upfront:

- [US state tax incentives](../../references/US-STATE-INCENTIVES.md) -- Section matching candidate state for tax incentive scoring
- [Federal tax guide](../../references/FEDERAL-TAX-GUIDE.md) -- Section: "Opportunity Zones" for OZ eligibility check
- [Construction cost benchmarks](../../references/COST-BENCHMARKS.md) -- Section matching region for construction cost context
- [Industrial power tariffs](../../references/POWER-TARIFFS.md) -- Section matching region for power cost scoring

### Quality Check

1. Verify all 9 factors are scored (no gaps)
2. Confirm weights sum to 100%
3. Cross-check power cost score against POWER-TARIFFS.md data for the region
4. Cross-check tax incentive score against US-STATE-INCENTIVES.md for the state
5. Validate OZ eligibility against FEDERAL-TAX-GUIDE.md census tract data
6. If multi-site: verify same scoring methodology applied consistently across all sites

## Output Template

This skill produces two files:
1. `<project-name>-site-feasibility-report.md` -- Full report
2. `<project-name>-site-feasibility-report.json` -- Structured data for downstream skills

### Markdown Report Structure

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: predev-site-feasibility v1.0]

#### 1. Executive Summary
- **Recommendation:** GO / CONDITIONAL / NO-GO
- **Weighted Score:** [X.XX] / 5.00 (confidence range: [low] - [high])
- **Key Strengths:** [top 2-3 factors]
- **Key Risks:** [bottom 2-3 factors]
- **Opportunity Zone Eligible:** Yes / No

#### 2. Factor Scoring Matrix

| Factor | Score (1-5) | Weight | Weighted Score | Notes |
|--------|-------------|--------|----------------|-------|
| Power | [X] | [X%] | [X.XX] | [assessment detail] |
| Connectivity | [X] | [X%] | [X.XX] | [assessment detail] |
| Cost | [X] | [X%] | [X.XX] | [assessment detail] |
| Tax Incentives | [X] | [X%] | [X.XX] | [assessment detail] |
| Climate | [X] | [X%] | [X.XX] | [assessment detail] |
| Labor | [X] | [X%] | [X.XX] | [assessment detail] |
| Sovereignty | [X] | [X%] | [X.XX] | [assessment detail] |
| Seismic | [X] | [X%] | [X.XX] | [assessment detail] |
| Water | [X] | [X%] | [X.XX] | [assessment detail] |
| **Total** | | **100%** | **[X.XX]** | |

#### 3. Site Comparison Table (Multi-Site Only)

| Factor | Site A | Site B | Site C |
|--------|--------|--------|--------|
| Power | [score] | [score] | [score] |
| ... | ... | ... | ... |
| **Weighted Total** | **[X.XX]** | **[X.XX]** | **[X.XX]** |
| **Recommendation** | [GO/COND/NO-GO] | [GO/COND/NO-GO] | [GO/COND/NO-GO] |

#### 4. Key Risks and Mitigations

| Risk | Severity | Mitigation | Timeline | Cost Impact |
|------|----------|------------|----------|-------------|
| [risk] | High/Med/Low | [action] | [months] | [estimate] |

#### 5. Tax Incentive Summary
- State program details and qualification status
- Opportunity Zone eligibility and benefit estimate
- Federal incentive applicability (ITC/PTC for on-site renewables, bonus depreciation)

#### 6. Recommended Next Steps
- Immediate actions for GO recommendation
- Required mitigations for CONDITIONAL recommendation
- Alternative site suggestions for NO-GO recommendation

### JSON Sidecar Schema

```json
{
  "artifact_type": "site-feasibility-report",
  "skill_version": "1.0",
  "project_name": "...",
  "recommendation": "GO | CONDITIONAL | NO-GO",
  "weighted_score": 0.00,
  "confidence_range": { "low": 0.00, "high": 0.00 },
  "factors": [
    {
      "name": "power",
      "score": 0,
      "weight": 0.00,
      "weighted_score": 0.00,
      "notes": "..."
    }
  ],
  "oz_eligible": false,
  "state_incentives": {
    "state": "...",
    "program": "...",
    "qualified": false,
    "estimated_annual_benefit": "..."
  },
  "sites_compared": 1,
  "site_rankings": []
}
```

## Gotchas

- **Utility capacity on paper vs actually available.** Utilities report total substation capacity, but queued interconnection requests may consume most of it. A substation showing 200MW available may have 150MW in queue. Always ask about interconnection queue depth -- actual available capacity can be 2-5 years out.

- **OZ designation does not guarantee state-level incentives.** Opportunity Zone tax benefits are federal; state sales tax and property tax exemptions have entirely separate qualification criteria (investment thresholds, job creation). Check both independently -- a site can be OZ-eligible but in a state with no DC incentive program.

- **Fiber route diversity matters more than proximity.** A site 2 miles from a carrier hotel with 3 diverse fiber paths is better connected than a site adjacent to a carrier hotel with a single path. Diverse physical routes (different conduit paths, separate utility poles) prevent single-point-of-failure outages.

- **Seismic zone 4 does not make a site infeasible.** It changes foundation and structural costs by 15-30% and requires seismic bracing for all equipment racks, but Tokyo and the San Francisco Bay Area operate major data centers in high-seismic zones. Score it, don't disqualify on seismic alone.

- **Water scarcity scoring must account for future allocation.** Western US states under prior appropriation doctrine may have fully allocated water rights even where current supply appears adequate. Future DC water needs compete with agricultural and municipal senior rights holders. Check water rights availability, not just current supply volume.

## Evaluations

See `evals/evals.json` for test scenarios covering hyperscale greenfield, multi-site comparison,
and sovereign facility evaluation.
