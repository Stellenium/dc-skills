---
name: bd-colo-business-model
description: "Develop a colocation business model with pricing calculator by tier and product type, occupancy ramp projections, and revenue waterfall. Use when building a colo business case, designing pricing tiers, modeling occupancy ramps, or evaluating the commercial viability of a colocation facility. Trigger with \"colo business model\", \"colocation pricing\", \"colo revenue model\", \"occupancy ramp\", \"colo business case\", or \"is this colo viable?\"."
---

# Colocation Business Model

Develop a comprehensive colocation business model with pricing calculator, occupancy
ramp projections, tenant mix optimization, interconnection revenue modeling, and
revenue waterfall. The JSON sidecar IS the primary analytical output -- the markdown
report provides narrative summary, key metrics dashboard, and investment highlights.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire model structure.

**Market and Facility Context:**

1. What is the facility location and market tier?
   - **Tier 1 market:** Primary metro (Ashburn, Dallas, Chicago, Phoenix, Santa Clara)
   - **Tier 2 market:** Secondary metro (Nashville, Salt Lake City, Columbus, Portland)
   - **Tier 3 market:** Emerging / tertiary (Reno, Cheyenne, Omaha)
   - Specific city and state for market-adjusted assumptions

2. What is the total facility capacity?
   - Total IT load (MW)
   - Total whitespace (sqft)
   - Number of cabinets at full build
   - Phased build-out if applicable (MW per phase)

3. What is the colocation product mix?
   - **Retail colocation:** Individual cabinets or cages (1-20 cabinets)
   - **Wholesale colocation:** Dedicated suites or halls (500kW-5MW+)
   - **Hybrid:** Both retail and wholesale in the same facility
   - Percentage split if hybrid

4. What is the target tenant profile?
   - **Enterprise:** Financial services, healthcare, SaaS companies (higher margin, smaller footprint)
   - **Hyperscale wholesale:** Cloud providers, large SaaS (lower margin, fills capacity fast)
   - **Network/carrier:** Telecom providers, content delivery, IX participants (drives interconnection revenue)
   - Target percentage by segment

5. What is the competitive landscape?
   - Number of competing colo providers in market
   - Market vacancy rate (if known)
   - Competitive pricing range (if known)
   - Your competitive positioning (price leader, premium, niche)

6. What SLA tier will you offer?
   - Tier II (99.741% availability) -- budget colo
   - Tier III (99.982% availability) -- standard colo
   - Tier IV (99.995% availability) -- premium / financial sector
   - Multiple tiers with pricing differentiation

7. What is the interconnection strategy?
   - Carrier-dense facility (10+ carriers on-net)
   - Moderate connectivity (3-10 carriers)
   - Limited connectivity (1-3 carriers)
   - Internet exchange (IX) presence planned

8. What is the target ramp timeline?
   - Aggressive (stabilized in 2-3 years)
   - Standard (stabilized in 3-5 years)
   - Conservative (stabilized in 5+ years)
   - Pre-leased anchor tenant capacity (specify MW)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather market-specific detail.

### Pricing Refinement

1. What are the prevailing market rates?
   - Retail per-cabinet pricing in your market
   - Wholesale per-kW pricing in your market
   - Cross-connect pricing (single-mode fiber, multi-mode, copper)
   - Power pricing model (metered, blended, inclusive)

2. What is your power cost basis?
   - Utility rate ($/kWh) at the facility
   - PUE target (affects effective power cost to tenants)
   - Power markup strategy (pass-through, blended markup, metered + margin)

3. What contract terms will you offer?
   - Retail: 1-3 year terms typical
   - Wholesale: 5-10 year terms typical
   - Renewal terms and escalation rates

### Tenant Pipeline

1. Do you have anchor tenants identified?
   - Pre-signed LOIs or commitments
   - Pipeline stage (prospect, qualified, LOI, signed)
   - MW commitment per anchor

2. What is the expected churn rate?
   - Retail churn: 5-15% annually (industry average)
   - Wholesale churn: 2-5% annually (longer contracts)
   - Churn mitigation strategy (contract length, switching costs)

## Pricing Calculator

Pricing varies by product type, SLA tier, and market. Reference SLA-BENCHMARKS.md
for tier-based availability targets and credit structures that justify pricing
differentiation.

### Wholesale Pricing

| Market Tier | Base Rate ($/kW/month) | Tier III Premium | Tier IV Premium | Typical Term |
|-------------|----------------------|-----------------|-----------------|-------------|
| Tier 1 metro | $100-130 | Included | +15-25% | 5-10 years |
| Tier 2 metro | $110-150 | Included | +20-30% | 5-7 years |
| Tier 3 / emerging | $90-120 | Included | +25-35% | 3-5 years |

### Retail Pricing

| Product | Price Range ($/month) | Typical Density | SLA Tier III | SLA Tier IV |
|---------|----------------------|----------------|-------------|-------------|
| Single cabinet | $800-1,500 | 5-10 kW | Standard | +20-30% |
| Half cage (4-8 cabs) | $4,000-10,000 | 5-10 kW/cab | Standard | +20-30% |
| Full cage (10-20 cabs) | $10,000-25,000 | 8-15 kW/cab | Standard | +15-25% |
| Private suite | $25,000-100,000 | 10-20 kW/cab | Standard | +15-25% |

### Interconnection Pricing

| Product | Price Range ($/month) | Revenue Margin | Notes |
|---------|----------------------|---------------|-------|
| Single-mode fiber cross-connect | $200-350 | 80-90% | Highest margin product |
| Multi-mode fiber cross-connect | $150-250 | 80-90% | Shorter distance |
| Copper cross-connect | $100-200 | 75-85% | Legacy, declining |
| Virtual cross-connect (cloud on-ramp) | $250-500 | 70-80% | Growing fastest |
| Blended IP transit (per Mbps) | $0.50-2.00 | 40-60% | Commodity, margin pressure |

## Occupancy Ramp Projections

Ramp curves vary by market tier, product mix, and anchor tenant strategy.
Overly aggressive ramp assumptions are the #1 cause of failed colo investments.

### Ramp by Market Tier

| Year | Tier 1 Metro | Tier 2 Metro | Tier 3 / Emerging |
|------|-------------|-------------|-------------------|
| Year 1 | 30-40% | 20-30% | 15-25% |
| Year 2 | 55-70% | 40-55% | 30-45% |
| Year 3 | 75-85% | 60-75% | 50-65% |
| Year 4 | 85-92% | 75-85% | 65-80% |
| Year 5 (stabilized) | 90-95% | 85-92% | 75-88% |

### Ramp by Product Type

| Year | Retail Only | Wholesale Only | Hybrid (50/50) |
|------|-----------|---------------|----------------|
| Year 1 | 15-25% | 40-60% (if anchor) | 30-40% |
| Year 2 | 35-50% | 60-80% | 50-65% |
| Year 3 | 55-70% | 80-90% | 70-80% |
| Stabilized | 85-92% | 90-95% | 88-93% |

Pre-leased wholesale capacity counts as Day 1 occupancy -- adjust ramp accordingly.

## Tenant Mix Optimization

| Segment | Margin Profile | Fill Rate | Interconnection Value | Churn Risk |
|---------|---------------|----------|----------------------|-----------|
| Enterprise | High (60-70% gross) | Slow (5-15 cabs/quarter) | Medium | Medium (5-10% annual) |
| Hyperscale wholesale | Low-Medium (35-50%) | Fast (500kW-5MW blocks) | Low | Low (2-5% annual) |
| Network/carrier | High (70-80%) | Moderate | Very High | Low (3-5% annual) |

**Target mix by strategy:**
- **Revenue maximizer:** 50% enterprise, 20% carrier, 30% wholesale
- **Fast fill:** 60% wholesale anchor, 25% enterprise, 15% carrier
- **Interconnection play:** 40% carrier/network, 35% enterprise, 25% wholesale

## Revenue Waterfall

### Revenue Components

| Component | % of Total Revenue | Margin | Growth Driver |
|-----------|--------------------|--------|--------------|
| Base power + space (wholesale) | 40-55% | 35-50% | Occupancy ramp |
| Base power + space (retail) | 20-35% | 55-70% | Occupancy ramp + density |
| Interconnection (cross-connects) | 10-20% | 80-90% | Carrier density |
| Managed services | 5-10% | 50-65% | Enterprise attach rate |
| Installation / setup fees | 2-5% | 90%+ | New tenant volume |
| Power markup / metered overage | 5-10% | 20-40% | Usage growth |

### Operating Cost Model

| Category | % of Revenue | Notes |
|----------|-------------|-------|
| Power cost (PUE-adjusted) | 30-45% | Largest single cost; PUE has outsized margin impact |
| Facility maintenance | 5-8% | HVAC, electrical, structural |
| Staffing (NOC, facilities, sales) | 10-15% | Scales sub-linearly with capacity |
| Insurance | 1-3% | Property + liability + cyber |
| Property tax | 3-6% | Varies by jurisdiction; some states exempt DC equipment |
| SGA (sales, general, admin) | 5-8% | Marketing, corporate overhead |
| **Total OpEx** | **55-75%** | **Target operating margin: 25-45%** |

### Key Performance Metrics

| Metric | Benchmark Range | Notes |
|--------|----------------|-------|
| Revenue per installed kW | $1,200-3,000/year | Retail higher, wholesale lower |
| Revenue per cabinet | $12,000-30,000/year | Varies by density and SLA tier |
| Interconnection attach rate | 2-5 cross-connects per cabinet | Carrier-dense markets higher |
| Blended gross margin | 45-65% | Wholesale drags, interconnection lifts |
| Breakeven occupancy | 35-55% | Below 35% indicates overbuilt or underpriced |
| Stabilized NOI margin | 40-55% | Tier 1 operators target 50%+ |
| Customer acquisition cost | $5,000-15,000 per retail customer | Enterprise segment higher |

## Reference Data

Load on demand -- do not read upfront:

- [SLA benchmarks](../../references/SLA-BENCHMARKS.md) -- Tier-based availability targets and credit structures for SLA-based pricing differentiation

## Output Template

This skill produces two files:

### Summary Report: `<project-name>-colo-business-model.md`

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: bd-colo-business-model v1.0]

#### 1. Executive Summary
- Market: [city, state] -- [Tier 1/2/3] market
- Facility: [MW] total capacity, [product mix]
- Target stabilized occupancy: [X%] by Year [N]
- Stabilized annual revenue: [$X M]
- Stabilized NOI margin: [X%]
- Breakeven occupancy: [X%]

#### 2. Pricing Summary
| Product | Rate | SLA Tier | Term |
|---------|------|----------|------|
| Wholesale | [$X/kW/month] | [Tier] | [years] |
| Retail cabinet | [$X/month] | [Tier] | [years] |
| Cross-connect | [$X/month] | -- | Monthly |

#### 3. Occupancy Ramp
| Year | Wholesale (%) | Retail (%) | Blended (%) | Revenue ($M) |
|------|--------------|-----------|-------------|-------------|
| 1 | [X%] | [X%] | [X%] | [$X] |
| 2 | [X%] | [X%] | [X%] | [$X] |
| ... | ... | ... | ... | ... |

#### 4. Revenue Waterfall
| Component | Year 1 | Stabilized | % of Total |
|-----------|--------|-----------|-----------|
| Wholesale power + space | [$X] | [$X] | [X%] |
| Retail power + space | [$X] | [$X] | [X%] |
| Interconnection | [$X] | [$X] | [X%] |
| Managed services | [$X] | [$X] | [X%] |
| Other | [$X] | [$X] | [X%] |
| **Total** | **[$X]** | **[$X]** | **100%** |

#### 5. Operating Cost Summary
| Category | Year 1 | Stabilized | % of Revenue |
|----------|--------|-----------|-------------|
| Power | [$X] | [$X] | [X%] |
| Staffing | [$X] | [$X] | [X%] |
| Maintenance | [$X] | [$X] | [X%] |
| Other | [$X] | [$X] | [X%] |
| **Total OpEx** | **[$X]** | **[$X]** | **[X%]** |
| **NOI** | **[$X]** | **[$X]** | **[X%] margin** |

#### 6. Key Metrics Dashboard
| Metric | Value | Benchmark |
|--------|-------|-----------|
| Revenue per installed kW | [$X/year] | [$X-Y range] |
| Revenue per cabinet | [$X/year] | [$X-Y range] |
| Interconnection attach rate | [X.X/cab] | [X-Y range] |
| Blended gross margin | [X%] | [X-Y% range] |
| Breakeven occupancy | [X%] | [X-Y% range] |
| Stabilized NOI margin | [X%] | [X-Y% range] |

### JSON Sidecar: `<project-name>-colo-business-model.json`

```json
{
  "artifact_type": "colo-business-model",
  "skill_version": "1.0",
  "project_name": "...",
  "market": {
    "city": "...",
    "state": "...",
    "tier": "tier-1 | tier-2 | tier-3"
  },
  "facility": {
    "total_capacity_mw": 0,
    "total_cabinets": 0,
    "whitespace_sqft": 0,
    "product_mix": "retail | wholesale | hybrid"
  },
  "pricing": {
    "wholesale_per_kw_month": 0,
    "retail_per_cabinet_month": 0,
    "cross_connect_per_month": 0,
    "sla_tier": "tier-iii | tier-iv",
    "power_rate_kwh": 0,
    "pue": 0
  },
  "occupancy_ramp": [
    {"year": 1, "wholesale_pct": 0, "retail_pct": 0, "blended_pct": 0},
    {"year": 2, "wholesale_pct": 0, "retail_pct": 0, "blended_pct": 0}
  ],
  "tenant_mix": {
    "enterprise_pct": 0,
    "hyperscale_pct": 0,
    "carrier_pct": 0
  },
  "revenue_waterfall": {
    "wholesale_power_space": 0,
    "retail_power_space": 0,
    "interconnection": 0,
    "managed_services": 0,
    "installation_fees": 0,
    "power_markup": 0,
    "total_stabilized_annual": 0
  },
  "operating_costs": {
    "power": 0,
    "staffing": 0,
    "maintenance": 0,
    "insurance": 0,
    "property_tax": 0,
    "sga": 0,
    "total_opex": 0
  },
  "key_metrics": {
    "revenue_per_kw_year": 0,
    "revenue_per_cabinet_year": 0,
    "interconnection_attach_rate": 0,
    "blended_gross_margin_pct": 0,
    "breakeven_occupancy_pct": 0,
    "stabilized_noi_margin_pct": 0
  },
  "reference_data_used": ["SLA-BENCHMARKS.md"]
}
```

## Gotchas

- **Power cost is typically 50-60% of colo COGS -- PUE has an outsized impact on margins.** A PUE improvement from 1.4 to 1.2 on a 20MW facility at $0.06/kWh saves approximately $2.1M annually. This flows directly to NOI because it does not require additional revenue to capture. Always model PUE sensitivity before finalizing the business case.

- **Interconnection revenue is high-margin but requires a carrier-dense market.** Cross-connect margins of 80-90% make interconnection the most profitable product, but only in markets with 10+ carriers on-net. In secondary markets with 3-5 carriers, interconnection revenue may only be 5-10% of total revenue versus 15-20% in primary markets. Do not project primary-market interconnection revenue in a secondary-market facility.

- **Wholesale contracts are 5-10 year terms but lower margin -- retail is higher margin but higher churn.** The classic colo dilemma: wholesale anchor tenants fill capacity fast (solving the occupancy ramp problem) but at 35-50% margins, while retail tenants deliver 55-70% margins but take years to accumulate. Most successful facilities use a 60/40 or 50/50 hybrid strategy -- wholesale for base load, retail for margin optimization.

- **Occupancy ramp is the number one determinant of project IRR -- overly aggressive ramp assumptions destroy real projects.** Industry data shows that new colo facilities in Tier 2 markets average 25% occupancy at Month 12, not the 40-50% that optimistic models project. A 12-month delay in ramp shifts breakeven by 18-24 months and can turn a viable project into a restructuring candidate. Use conservative ramp assumptions and stress-test at minus 20%.

- **SLA tier drives pricing power but also drives cost structure.** Tier IV availability (99.995%) commands a 15-35% pricing premium over Tier III (99.982%), but 2N redundancy roughly doubles the mechanical and electrical infrastructure cost. The premium must cover the incremental capital cost over the asset life. Model both the revenue uplift and the CapEx/OpEx increase before committing to Tier IV.

## Evaluations

See `evals/evals.json` for test scenarios covering primary market hybrid, secondary market retail, and wholesale-focused facilities.
