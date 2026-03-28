---
name: comp-sustainability-reporting
description: "Generate ESG framework and sustainability report for data center facilities with Scope 1/2/3 carbon accounting, water usage tracking, and renewable energy certificates. Use when preparing sustainability reports, calculating carbon footprint for a DC, tracking PUE/WUE/CUE metrics, or meeting ESG reporting requirements. Trigger with \"sustainability report\", \"ESG\", \"carbon accounting\", \"Scope 1 2 3\", \"PUE WUE CUE\", \"renewable energy certificates\", or \"DC carbon footprint\"."
---

# Sustainability & ESG Reporting

Generate ESG framework and sustainability report for data center facilities. Calculates
Scope 1/2/3 carbon emissions using location-based and market-based methodologies, tracks
PUE/WUE/CUE efficiency metrics, and produces compliance gap analysis for SEC Climate
Disclosure, EU CSRD, and SBTi. Includes bundled calculator script for deterministic results.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

**Project Context:**

1. Is this a greenfield site or brownfield conversion?
   - **Greenfield:** Sustainability targets inform design decisions
   - **Brownfield:** Baseline current emissions and efficiency for improvement planning

2. What facility type?
   - Traditional enterprise (single-tenant, 2-20MW)
   - Hyperscale (cloud provider, 20-500MW+)
   - Sovereign (government/national security)
   - Colocation (multi-tenant, retail or wholesale)
   - Modular/prefab (factory-built, rapid deployment)
   - Edge (1-5MW, distributed)

3. What is the facility location? (for grid carbon intensity)
   - Country and region/state code (e.g., US-TX, EU-NO, SG)
   - Reference POWER-TARIFFS.md for grid carbon intensity data

4. What is the total IT load (MW)?
   - Current operational load
   - Planned capacity at full build-out

5. What is the PUE? (measured or design target)
   - Measured annual PUE (if operational)
   - Design PUE target (if greenfield)

6. What cooling type is deployed?
   - Air-cooled (raised floor, in-row, containment)
   - Direct liquid cooling
   - Immersion cooling
   - Hybrid air + liquid
   - Evaporative / adiabatic

7. What is annual water consumption (gallons/year)?
   - Metered consumption if operational
   - Design estimate if greenfield

8. Is there on-site power generation?
   - None (grid-only)
   - Natural gas generators/turbines (specify MW)
   - Diesel backup generators (specify MW and annual run hours)
   - Fuel cells (specify type and MW)

9. Is Scope 3 emissions reporting required?
   - Scope 1+2 only (SEC Climate Disclosure minimum)
   - Scope 1+2+3 (EU CSRD requirement, SBTi requirement)

10. What reporting frameworks are targeted?
    - SEC Climate Disclosure (effective 2026)
    - EU CSRD (Corporate Sustainability Reporting Directive)
    - SBTi (Science Based Targets initiative)
    - CDP (Carbon Disclosure Project)
    - GRI (Global Reporting Initiative)

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

### Scope 3 Path

If Scope 3 reporting is required:

1. Embodied carbon data available for IT equipment?
2. Supply chain emissions data from key vendors?
3. Employee commuting and business travel data?
4. Upstream fuel and energy-related activities tracked?
5. End-of-life treatment for decommissioned equipment?

### SBTi Path

If SBTi target-setting is a goal:

1. What is the baseline year for target-setting?
2. Near-term target horizon (5-10 years)?
3. Long-term (net-zero) target horizon?
4. Sector-specific pathway (ICT sector guidance)?
5. Current renewable energy procurement strategy?

### Renewable Energy Path

If renewable energy is part of the strategy:

1. On-site renewable generation (solar/wind MW)?
2. Power Purchase Agreements (PPAs) in place or planned?
3. Renewable Energy Certificates (RECs) purchased annually (MWh)?
4. Green tariff program participation?

## What I Need from Upstream

This skill can be invoked independently.

**If power-capacity-model is available (from eng-power-model):**
- Total facility power consumption (IT + overhead)
- PUE calculation with component-level detail
- On-site generation capacity and fuel type
- Grid interconnection capacity

## Calculation Scripts

For deterministic carbon and efficiency calculations, use the bundled script:

- `scripts/sustainability-calculator.py` -- Scope 1/2/3 carbon accounting, PUE/WUE/CUE metrics

Requires: Python 3.11+ (stdlib only, no external dependencies)

**Usage:**
```bash
python3 scripts/sustainability-calculator.py \
  --it-load-mw 10 \
  --pue 1.3 \
  --location US-TX \
  --water-gallons 50000000 \
  --gen-type gas \
  --gen-mw 5 \
  --gen-hours 8760 \
  --cooling-type hybrid \
  --rec-mwh 0
```

## Analysis & Output

### Process

1. **Gather facility data** from Phase 1/Phase 2 discovery
2. **Run sustainability calculator** with facility parameters
3. **Validate results** against POWER-TARIFFS.md grid carbon intensity for location
4. **Verify PUE/WUE** within reasonable ranges for facility type and cooling
5. **Fix inputs** if validation identifies anomalies (PUE > 2.0, negative values)
6. **Re-run calculator** after input corrections
7. **Assess compliance gaps** against targeted reporting frameworks
8. **Produce sustainability report** with carbon accounting and efficiency metrics

### Validation Loop

1. Run calculator with input parameters
2. Cross-check Scope 2 against POWER-TARIFFS.md grid carbon intensity for location
3. Validate PUE (must be >= 1.0; flag if > 2.0 as unusually high)
4. Validate WUE against cooling type benchmarks (air: 0-0.5, hybrid: 0.5-1.5, evaporative: 1.5-2.5 L/kWh)
5. If any value out of range: flag, request input correction, re-run
6. Repeat until all values within acceptable ranges

### Carbon Accounting Methodology

**Scope 1 (Direct Emissions):**
- On-site combustion: generators, turbines, fuel cells
- Refrigerant leaks from cooling systems (estimated via GWP factors)
- Natural gas: 0.91 lbs CO2/kWh * generation * 0.000453592 = tCO2e
- Diesel: 1.21 lbs CO2/kWh equivalent

**Scope 2 (Indirect -- Purchased Energy):**
- Location-based: grid_carbon_intensity * total_facility_power * 8760
- Market-based: location-based minus REC/PPA offsets (floor at zero)
- CRITICAL: Location-based and market-based produce wildly different results. A DC in Norway (15 gCO2/kWh grid) reporting market-based WITHOUT RECs shows European residual mix (~450 gCO2/kWh)

**Scope 3 (Value Chain):**
- Category 1: Purchased goods (embodied carbon in servers, networking)
- Category 2: Capital goods (construction materials, MEP equipment)
- Category 3: Fuel/energy upstream activities
- Category 5: Waste from operations
- Category 6: Business travel
- Category 7: Employee commuting

### Efficiency Metrics

| Metric | Formula | Benchmark (Good) | Benchmark (Average) |
|--------|---------|------------------|-------------------|
| PUE | Total Facility Power / IT Load | < 1.3 | 1.3-1.6 |
| WUE | Water Consumption (L) / IT Energy (kWh) | < 0.5 L/kWh | 0.5-1.8 L/kWh |
| CUE | Scope 1 CO2 (kg) / IT Energy (kWh) | < 0.05 | 0.05-0.20 |
| ERE | Total Energy Reuse / Total Facility Energy | > 0.10 | 0-0.10 |

### Compliance Framework Comparison

| Requirement | SEC Climate | EU CSRD | SBTi | CDP | GRI |
|------------|------------|---------|------|-----|-----|
| Scope 1 | Required | Required | Required | Required | Required |
| Scope 2 | Required | Required | Required | Required | Required |
| Scope 3 | NOT required | Required | Required | Required | Optional |
| Baseline year | Flexible | 2019-2024 | Self-selected | Self-selected | Self-selected |
| Verification | Reasonable assurance | Limited → Reasonable | Third-party | Self/third-party | Self/third-party |
| Financial impact | Required | Required | Not required | Scored | Optional |
| Timeline | Effective 2026 | Effective 2024-2026 | 5-10 year targets | Annual cycle | Annual cycle |

### Reference Data

Load these files on demand -- do not read upfront:

- [Power tariffs](../../references/POWER-TARIFFS.md) -- Grid carbon intensity by region for Scope 2 calculations
- [Disclaimer framework](../../references/DISCLAIMER-FRAMEWORK.md) -- Required disclaimer language

### Facility Type Parameters

| Parameter | Traditional | Hyperscale | Sovereign | Colo | Modular | Edge |
|-----------|------------|------------|-----------|------|---------|------|
| Typical PUE | 1.4-1.8 | 1.1-1.3 | 1.3-1.6 | 1.3-1.6 | 1.2-1.4 | 1.4-2.0 |
| Scope 3 complexity | Low | Very High | Medium | High | Low | Low |
| Water consumption | High | Medium-High | Medium | Medium | Low | Very Low |
| Reporting frameworks | GRI | SEC+CDP+SBTi | Government-specific | CDP+GRI | Limited | None |

## Output Template

This skill produces two files:
1. `<project-name>-sustainability-report.md` -- Full report
2. `<project-name>-sustainability-report.json` -- Structured data

### JSON Sidecar Schema

```json
{
  "artifact_type": "sustainability-report",
  "skill_version": "1.0",
  "project_name": "...",
  "carbon": {
    "scope_1_tco2e": 0,
    "scope_2_location_tco2e": 0,
    "scope_2_market_tco2e": 0,
    "scope_3_tco2e": 0,
    "total_tco2e": 0
  },
  "efficiency": {
    "pue": 0,
    "wue": 0,
    "cue": 0,
    "ere": 0
  },
  "compliance": {
    "sec": { "gaps": [], "readiness_pct": 0 },
    "csrd": { "gaps": [], "readiness_pct": 0 },
    "sbti": {
      "target_type": "...",
      "baseline_year": 0,
      "reduction_path": "..."
    }
  },
  "recommendations": []
}
```

## Gotchas

- **Location-based vs market-based Scope 2 accounting produces wildly different results.** A DC in Norway using 100% hydro grid power (15 gCO2/kWh) but reporting market-based WITHOUT RECs shows the European residual mix (~450 gCO2/kWh). Conversely, a Texas DC buying wind RECs can report zero market-based Scope 2 despite the grid being 380 gCO2/kWh. Both are technically correct under GHG Protocol.

- **WUE below 0.5 L/kWh is only achievable with air-cooled or direct liquid cooling.** Evaporative cooling (cooling towers, adiabatic systems) consumes 1.5-2.5 L/kWh. Claims of low WUE with evaporative cooling should be challenged. Many facilities report WUE excluding cooling tower water, which is misleading.

- **SEC Climate Disclosure rules (effective 2026) require Scope 1+2 but NOT Scope 3.** EU CSRD requires all three scopes. SBTi requires Scope 3 if it exceeds 40% of total emissions. For most DC operators, Scope 3 (embodied carbon in servers) is 50-70% of total emissions, making SBTi Scope 3 inclusion mandatory in practice.

- **PUE is measured, not designed.** A design PUE of 1.2 often results in a measured PUE of 1.3-1.5 due to operational realities (partial loading, seasonal variation, non-IT loads incorrectly classified). Always distinguish between design and operational PUE in reporting.

- **Refrigerant leaks are Scope 1 emissions that many operators forget to report.** HFC refrigerants (R-134a, R-410A) have GWP of 1,430 and 2,088 respectively. A single cooling system with a 5% annual leak rate can add hundreds of tCO2e to Scope 1. This is increasingly scrutinized by auditors.

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

---

FINANCIAL DISCLAIMER: The financial projections, cost estimates, and economic
analyses produced by this skill are for preliminary planning and evaluation
purposes only. This is not investment advice, financial advice, or
a recommendation to proceed with any transaction. Actual costs, revenues, and
returns will vary based on market conditions, vendor negotiations, site-specific
factors, and regulatory changes not modeled here.

See [Disclaimer Framework](../../references/DISCLAIMER-FRAMEWORK.md) for full terms.

---

## Evaluations

See `evals/evals.json` for test scenarios covering Texas hyperscale with gas generation,
Nordic near-zero carbon, and Singapore SBTi full carbon accounting.
