# Skill Chain Map

Static mapping of project archetypes to ordered skill sequences. Loaded by dc-project-wizard during project plan generation. Each skill is annotated with availability status and dependency requirements.

**As-of:** 2026-03-28
**Total skills:** 49 (7 Wave 1 + 14 Wave 2 + 20 Wave 3 + 8 Wave 4) + 1 wizard
**Reference data files:** 10

## Legend

- `[AVAILABLE]` -- Skill exists in the library and can be executed immediately

---

## Archetype: Hyperscale Greenfield

### Skill Sequence

1. `predev-site-feasibility` [AVAILABLE] -- Site scoring with weighted multi-factor analysis producing GO/CONDITIONAL/NO-GO recommendation. No prerequisites.
2. `predev-market-study` [AVAILABLE] -- Requires: site-feasibility-report. Supply/demand analysis for target market including inventory, absorption rates, pricing trends, and anchor tenant identification. Run in parallel with #1 or immediately after.
3. `comp-sovereignty` [AVAILABLE] -- Run in parallel with #1 if international or government-adjacent project. Regulatory framework and data residency assessment. No prerequisites.
4. `predev-grid-interconnection` [AVAILABLE] -- Requires: site-feasibility-report. Utility interconnection queue position, application process, upgrade cost allocation, and alternative strategies. Run after site feasibility confirms utility access.
5. `predev-connectivity` [AVAILABLE] -- Carrier strategy, fiber entrance design, meet-me room, IX peering, and subsea cable proximity assessment. No prerequisites; run in parallel with grid interconnection.
6. `predev-mou-framework` [AVAILABLE] -- MOU/LOI framework for site options, utility commitments, and government agreements. Run in parallel with predevelopment.
7. `predev-stakeholder-map` [AVAILABLE] -- Stakeholder identification, influence mapping, and engagement strategy. Run early for community and government alignment.
8. `predev-permitting` [AVAILABLE] -- Permitting roadmap covering zoning, environmental, building, and specialty permits. Requires: site-feasibility-report.
9. `predev-environmental` [AVAILABLE] -- Environmental impact assessment covering water, noise, emissions, and ecological factors. Run in parallel with permitting.
10. `predev-project-narrative` [AVAILABLE] -- Requires: site-feasibility-report, market-study. 2-3 page concept paper synthesizing feasibility and market data for stakeholder communication.
11. `eng-power-model` [AVAILABLE] -- Requires: site-feasibility-report. Utility-to-rack power distribution with Tier I-IV redundancy modeling and PUE calculation.
12. `eng-btm-power` [AVAILABLE] -- Requires: power-capacity-model. Behind-the-meter power evaluation: gas, solar, wind, BESS, fuel cells, SMR with blended LCOE and ITC/PTC modeling.
13. `fin-ppa-analysis` [AVAILABLE] -- Requires: power-capacity-model. PPA vs self-gen vs grid levelized cost comparison with basis risk, curtailment, and additionality assessment. Run in parallel with BTM power analysis. References POWER-TARIFFS.md, SOLAR-WIND-RESOURCE.md, FEDERAL-TAX-GUIDE.md.
14. `eng-gpu-cluster` [AVAILABLE] -- Requires: power-capacity-model. GPU accelerator selection, rack density planning, interconnect fabric design. Parallel with cooling design.
15. `eng-cooling-design` [AVAILABLE] -- Requires: power-capacity-model. 14-technology evaluation with ASHRAE TC 9.9 compliance. Parallel with GPU cluster.
16. `eng-density-upgrade` [AVAILABLE] -- Optional. Requires: cooling-design-report. Air-to-liquid cooling retrofit planning for 30-100+ kW/rack AI/HPC density with CDU placement, piping routes, and phased live migration. Use when upgrading existing halls within a campus to higher density.
17. `eng-physical-layout` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Hall layout, containment strategy, rack placement, and structured cabling per BICSI 002-2024.
18. `eng-modular-design` [AVAILABLE] -- Optional. Requires: power-capacity-model. Modular/prefab pod sizing, factory vs field assembly, transport constraints, and phased rollout. Use when modular deployment is under consideration.
19. `eng-fire-life-safety` [AVAILABLE] -- Fire protection, detection, and life safety system design per NFPA 75/76/855 and local code requirements.
20. `eng-bms-dcim` [AVAILABLE] -- Building management system and DCIM architecture, integration strategy, and monitoring requirements.
21. `eng-commissioning` [AVAILABLE] -- Level 1-5 commissioning framework with structured test procedures and acceptance criteria.
22. `eng-ops-readiness` [AVAILABLE] -- Operations readiness planning: staffing, SOPs, maintenance programs, and Day 1 checklist.
23. `proc-rfp-generator` [AVAILABLE] -- Requires: site-feasibility-report, power-capacity-model, cooling-design-report. Complete RFP document generation with evaluation criteria and contract form selection.
24. `proc-equipment-spec` [AVAILABLE] -- Optional. Requires: power-capacity-model, cooling-design-report. Vendor-neutral equipment specifications for competitive procurement packages.
25. `proc-bid-evaluation` [AVAILABLE] -- Optional. Requires: rfp-document. Weighted bid evaluation with scoring matrix and recommendation memo. Run after RFP responses are received.
26. `proc-contract-structure` [AVAILABLE] -- Requires: rfp-package, bid-evaluation-report. FIDIC form selection, milestone payment schedule, retention, warranties, LDs, and performance guarantees. Consumes FIDIC-CONTRACTS.md.
27. `proc-supply-chain` [AVAILABLE] -- Requires: equipment-spec-package. Supply chain risk assessment with lead times, single-source risks, geopolitical factors, and alternative supplier strategies.
28. `proc-schedule` [AVAILABLE] -- Requires: contract-structure, supply-chain-assessment. Construction schedule with CPM analysis, resource loading, and critical path identification. Includes bundled Python script.
29. `comp-certification` [AVAILABLE] -- Certification roadmap for Uptime Tier, ISO 27001, SOC 2, and industry-specific certifications.
30. `comp-export-controls` [AVAILABLE] -- Export control compliance for GPU and technology procurement covering EAR, ITAR, and entity list screening.
31. `comp-data-classification` [AVAILABLE] -- Data classification framework with handling procedures and access controls.
32. `comp-sustainability-reporting` [AVAILABLE] -- Sustainability metrics and reporting framework for SEC, CSRD, SBTi, and GHG Protocol compliance. Includes bundled Python script.
33. `fin-project-tco` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. 10/20-year TCO with CapEx/OpEx breakdown, tax incentive modeling, and sensitivity analysis.
34. `fin-project-model` [AVAILABLE] -- Requires: tco-model. Full financial model with IRR/NPV/MOIC waterfall, multi-tranche capital structure, and deal structuring.
35. `fin-deal-structure` [AVAILABLE] -- Requires: financial-model. SPV/holding entity design with tax optimization stacking (OZ, ITC, cost segregation, MACRS, Section 179D), multi-entity equity waterfall, and exit modeling. References FEDERAL-TAX-GUIDE.md, US-STATE-INCENTIVES.md.
36. `fin-debt-sizing` [AVAILABLE] -- Requires: financial-model. DSCR-based debt capacity sizing with construction facility, term loan amortization, covenant testing, cash trap provisions, and sensitivity analysis.
37. `fin-investor-memo` [AVAILABLE] -- Investor memo with structural branching by investor type (VC, PE/infrastructure, DFI, sovereign wealth fund).
38. `fin-insurance-program` [AVAILABLE] -- Insurance program structure with 6 coverage types, coverage matrix, and premium driver analysis.
39. `bd-government-proposal` [AVAILABLE] -- Requires: site-feasibility-report. Government proposal with counterparty adaptation (federal, state, municipal, foreign government).
40. `bd-tenant-spec` [AVAILABLE] -- Tenant requirements discovery through structured questionnaire. Independent skill for DC operator use.
41. `bd-partnership-proposal` [AVAILABLE] -- Requires: site-feasibility-report, project-financial-model. Partnership/JV proposal with term sheet, adapted by partner type (technology, infrastructure, financial, government/sovereign).
42. `bd-economic-impact` [AVAILABLE] -- Requires: site-feasibility-report, project-financial-model. Economic impact analysis with I-O multipliers, tax revenue modeling, and community benefits. Consumes US-STATE-INCENTIVES.md.
43. `bd-national-compute` [AVAILABLE] -- Requires: site-feasibility-report. National AI compute strategy for government ministries and DFIs. Consumes DFI-FUNDING.md.

### Dependency Graph

```
site-feasibility ──> market-study ──> project-narrative
       │          └──> grid-interconnection
       │          └──> permitting ──> environmental (parallel)
       │          └──> power-model ──> btm-power
       │                    │     └──> ppa-analysis (parallel with btm-power)
       │                    │     └──> gpu-cluster
       │                    │     └──> cooling-design ──> density-upgrade (optional)
       │                    │                        └──> physical-layout
       │                    │                        └──> rfp-generator ──> equipment-spec
       │                    │                        │                  └──> bid-evaluation ──> contract-structure
       │                    │                        │                  └──> supply-chain
       │                    │                        └──> tco ──> project-model ──> deal-structure
       │                    │                                                  └──> debt-sizing
       │                    │                                                  └──> investor-memo
       │                    │                                                  └──> insurance-program
       └──────────────────────────────────────────────> rfp-generator
       └──> government-proposal
       └──> partnership-proposal
       └──> economic-impact
       └──> national-compute
connectivity (independent, parallel)
sovereignty (independent, parallel)
mou-framework (independent, parallel)
stakeholder-map (independent, parallel)
modular-design (optional, after power-model)
fire-life-safety (after cooling-design)
bms-dcim (after physical-layout)
commissioning (after fire-life-safety)
ops-readiness (after commissioning)
contract-structure ──> supply-chain ──> schedule
certification (independent, after engineering)
export-controls (independent, parallel with procurement)
data-classification (independent, parallel)
sustainability-reporting (independent, after operations data)
tenant-spec (independent, early engagement)
ppa-analysis (after power-model, parallel with btm-power)
deal-structure (after project-model)
debt-sizing (after project-model)
```

### Notes

- `fin-deal-structure` and `fin-debt-sizing` run after the financial model is complete -- deal structure feeds into investor memo and BD skills.
- `fin-ppa-analysis` runs in parallel with `eng-btm-power` -- both consume the power capacity model and address power procurement strategy from different angles.
- `eng-density-upgrade` is optional for greenfield but relevant when upgrading existing halls within a hyperscale campus for AI/HPC density.

### Reference Data Needed

- GPU-REFERENCE.md (GPU TDP and cooling requirements for cluster sizing)
- COST-BENCHMARKS.md (Regional construction cost per MW)
- POWER-TARIFFS.md (Industrial grid tariffs for energy cost projections)
- SOLAR-WIND-RESOURCE.md (Solar GHI and wind capacity factors for BTM power and PPA analysis)
- US-STATE-INCENTIVES.md (if US project -- state tax incentive programs)
- FEDERAL-TAX-GUIDE.md (if US project -- OZ eligibility, ITC/PTC, bonus depreciation, deal structure tax optimization)
- REGULATORY-MATRIX.md (if international project -- data residency, AI regulation, ownership restrictions)
- SLA-BENCHMARKS.md (SLA tier availability targets and credit structures)
- FIDIC-CONTRACTS.md (Contract form comparison, risk allocation, and key clause summaries)
- DFI-FUNDING.md (if DFI-funded -- development finance institution profiles and programs)

---

## Archetype: Enterprise Colo

### Skill Sequence

1. `predev-site-feasibility` [AVAILABLE] -- Site scoring for colocation facility development. No prerequisites.
2. `predev-market-study` [AVAILABLE] -- Requires: site-feasibility-report. Colo market supply/demand analysis with pricing trends and tenant pipeline assessment.
3. `predev-connectivity` [AVAILABLE] -- Carrier-neutral connectivity assessment, meet-me room design, IX peering strategy. Critical for colo tenant attraction.
4. `predev-mou-framework` [AVAILABLE] -- MOU framework for site options and utility commitments.
5. `predev-stakeholder-map` [AVAILABLE] -- Stakeholder engagement strategy for community and government alignment.
6. `predev-permitting` [AVAILABLE] -- Permitting roadmap for zoning, building, and specialty permits.
7. `bd-tenant-spec` [AVAILABLE] -- Tenant requirements discovery through structured questionnaire. Gathers power density, cooling, SLA, compliance, and growth needs from prospective tenants. No prerequisites; can run early to inform engineering.
8. `eng-power-model` [AVAILABLE] -- Requires: site-feasibility-report. Power distribution with multi-tenant metering considerations.
9. `eng-cooling-design` [AVAILABLE] -- Requires: power-capacity-model. Mixed-density cooling for diverse tenant workloads.
10. `eng-sla-design` [AVAILABLE] -- SLA framework with availability modeling, tier-to-SLA mapping, and credit structures. Consumes SLA-BENCHMARKS.md. Run after cooling design to validate availability claims.
11. `eng-physical-layout` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Multi-tenant hall layout with cage/suite configurations and containment strategy.
12. `eng-physical-security` [AVAILABLE] -- Physical security design for multi-tenant environments including tiered access zones, CCTV, and visitor management.
13. `eng-fire-life-safety` [AVAILABLE] -- Fire protection and life safety system design per NFPA 75/76/855.
14. `eng-bms-dcim` [AVAILABLE] -- BMS and DCIM architecture for multi-tenant monitoring and billing.
15. `eng-commissioning` [AVAILABLE] -- Level 1-5 commissioning framework with test procedures.
16. `eng-ops-readiness` [AVAILABLE] -- Operations readiness planning for Day 1 tenant onboarding.
17. `proc-rfp-generator` [AVAILABLE] -- Requires: site-feasibility-report, power-capacity-model, cooling-design-report. RFP generation for construction or equipment procurement.
18. `proc-equipment-spec` [AVAILABLE] -- Optional. Requires: power-capacity-model, cooling-design-report. Vendor-neutral equipment specifications.
19. `proc-bid-evaluation` [AVAILABLE] -- Optional. Requires: rfp-document. Bid evaluation after RFP responses received.
20. `proc-contract-structure` [AVAILABLE] -- Contract form selection and structure with milestones, retention, warranties, and LDs. Consumes FIDIC-CONTRACTS.md.
21. `proc-supply-chain` [AVAILABLE] -- Supply chain risk assessment for equipment procurement.
22. `proc-schedule` [AVAILABLE] -- Construction schedule with CPM analysis and resource loading.
23. `comp-certification` [AVAILABLE] -- Certification roadmap for Uptime Tier, ISO 27001, SOC 2.
24. `comp-sustainability-reporting` [AVAILABLE] -- Sustainability metrics and reporting for ESG compliance.
25. `fin-project-tco` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. TCO analysis with colo-specific revenue modeling.
26. `fin-project-model` [AVAILABLE] -- Requires: tco-model. Financial model with colo revenue assumptions, occupancy ramp, and multi-tranche capital structure.
27. `fin-deal-structure` [AVAILABLE] -- Requires: financial-model. SPV/holding entity design with tax optimization for colo investment. References FEDERAL-TAX-GUIDE.md, US-STATE-INCENTIVES.md.
28. `fin-debt-sizing` [AVAILABLE] -- Requires: financial-model. DSCR-based debt capacity sizing for colo project finance.
29. `fin-investor-memo` [AVAILABLE] -- Investor memo adapted for colo business model.
30. `fin-insurance-program` [AVAILABLE] -- Insurance program structure for multi-tenant facility.
31. `bd-colo-business-model` [AVAILABLE] -- Colocation business model with pricing calculator, occupancy ramp, tenant mix optimization, interconnection revenue modeling, and revenue waterfall. References SLA-BENCHMARKS.md. Run after engineering to inform pricing strategy.
32. `bd-economic-impact` [AVAILABLE] -- Economic impact analysis for government incentive negotiations.
33. `bd-rfp-response` [AVAILABLE] -- RFP response with compliance matrix, win themes, and case studies. Use when responding to enterprise or government RFPs for colo services.

### Notes

- `eng-gpu-cluster` is typically not needed for general colocation. Flag as optional if AI/HPC tenants are expected.
- `comp-sovereignty` is typically not needed unless government tenants or data residency requirements apply.
- `bd-tenant-spec` can run at any point -- early engagement with anchor tenants informs engineering decisions.
- `bd-partnership-proposal` optional if seeking JV/partnership capital for the colo development.
- `bd-colo-business-model` produces the pricing and occupancy model that informs financial projections and investor materials.
- `fin-deal-structure` and `fin-debt-sizing` enable capital structuring after the financial model is complete.
- `bd-rfp-response` is used when the colo operator responds to enterprise or government procurement RFPs.

### Reference Data Needed

- COST-BENCHMARKS.md (Regional construction cost benchmarks)
- POWER-TARIFFS.md (Industrial grid tariffs for operating cost projections)
- SLA-BENCHMARKS.md (SLA tier availability targets, MTTR/MTBF benchmarks, credit structures -- also consumed by bd-colo-business-model for pricing differentiation)
- FIDIC-CONTRACTS.md (Contract form selection for construction packages)
- US-STATE-INCENTIVES.md (if US project -- state tax incentive programs, also consumed by fin-deal-structure)
- FEDERAL-TAX-GUIDE.md (if US project -- federal tax incentive applicability, also consumed by fin-deal-structure)

---

## Archetype: Sovereign AI Facility

### Skill Sequence

1. `comp-sovereignty` [AVAILABLE] -- FIRST for sovereign projects. Regulatory framework assessment, data residency obligations, classification requirements. No prerequisites.
2. `predev-site-feasibility` [AVAILABLE] -- Run in parallel with #1. Site scoring incorporates sovereignty constraints (jurisdiction, ownership restrictions, security perimeter requirements).
3. `predev-grid-interconnection` [AVAILABLE] -- Requires: site-feasibility-report. Utility interconnection assessment with energy independence considerations for sovereign facilities.
4. `predev-mou-framework` [AVAILABLE] -- MOU framework for government land, utility, and sovereignty agreements.
5. `predev-stakeholder-map` [AVAILABLE] -- Stakeholder mapping for government, military, and community alignment.
6. `predev-permitting` [AVAILABLE] -- Permitting roadmap including government/military facility requirements.
7. `predev-environmental` [AVAILABLE] -- Environmental impact assessment for sovereign facility siting.
8. `bd-government-proposal` [AVAILABLE] -- Requires: site-feasibility-report. Government proposal with sovereignty framing -- federal (national security/compute sovereignty), state, or foreign government counterparty adaptation. Run early to align project with government priorities.
9. `bd-national-compute` [AVAILABLE] -- National AI compute strategy for government ministries and DFIs. Models sovereign demand and distribution strategy. Consumes DFI-FUNDING.md.
10. `bd-economic-impact` [AVAILABLE] -- Economic impact analysis for government incentive and DFI funding applications.
11. `bd-partnership-proposal` [AVAILABLE] -- Optional. Partnership/JV proposal if co-investment with SWF, DFI, or technology partner.
12. `bd-rfp-response` [AVAILABLE] -- RFP response with compliance matrix and win themes. Use when responding to government RFPs for sovereign compute facilities.
13. `eng-power-model` [AVAILABLE] -- Requires: site-feasibility-report. Enhanced redundancy modeling for sovereign-grade reliability (typically Tier III or IV).
14. `eng-btm-power` [AVAILABLE] -- Requires: power-capacity-model. Behind-the-meter power for energy independence -- gas turbines, solar, BESS, microgrid for sovereign resilience.
15. `fin-ppa-analysis` [AVAILABLE] -- Requires: power-capacity-model. PPA evaluation for sovereign energy procurement with additionality assessment. References POWER-TARIFFS.md, SOLAR-WIND-RESOURCE.md.
16. `eng-gpu-cluster` [AVAILABLE] -- Requires: power-capacity-model. Training vs inference workload branching with export-controlled GPU considerations.
17. `eng-cooling-design` [AVAILABLE] -- Requires: power-capacity-model. Cooling design with sovereign facility security constraints.
18. `eng-physical-security` [AVAILABLE] -- Enhanced security design for sovereign facilities including SCIF requirements, classified space access controls, and tiered perimeter zones.
19. `eng-physical-layout` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Secure layout with classified/unclassified zone separation and mantrap positioning.
20. `eng-fire-life-safety` [AVAILABLE] -- Fire protection and life safety for sovereign-grade facilities.
21. `eng-bms-dcim` [AVAILABLE] -- BMS and DCIM architecture with security-hardened monitoring.
22. `eng-commissioning` [AVAILABLE] -- Level 1-5 commissioning with enhanced security protocols.
23. `eng-ops-readiness` [AVAILABLE] -- Operations readiness for sovereign facility including cleared personnel and security procedures.
24. `comp-export-controls` [AVAILABLE] -- Export control compliance for GPU and technology procurement. Critical for sovereign AI facilities with restricted hardware.
25. `comp-data-classification` [AVAILABLE] -- Data classification framework for sovereign data handling (classified, CUI, unclassified).
26. `comp-certification` [AVAILABLE] -- Certification roadmap including government-specific certifications (FedRAMP, IL4/IL5).
27. `comp-sustainability-reporting` [AVAILABLE] -- Sustainability reporting for government ESG requirements.
28. `proc-rfp-generator` [AVAILABLE] -- Requires: site-feasibility-report, power-capacity-model, cooling-design-report. Sovereign procurement adds security clearance and domestic sourcing requirements.
29. `proc-equipment-spec` [AVAILABLE] -- Optional. Requires: power-capacity-model, cooling-design-report. Equipment specs with domestic sourcing and security screening requirements.
30. `proc-bid-evaluation` [AVAILABLE] -- Optional. Requires: rfp-document. Bid evaluation with enhanced security and qualifications weighting.
31. `proc-contract-structure` [AVAILABLE] -- Contract structure with sovereign-specific addenda. Consumes FIDIC-CONTRACTS.md.
32. `proc-supply-chain` [AVAILABLE] -- Supply chain assessment with allied-nation sourcing restrictions and domestic content requirements.
33. `proc-schedule` [AVAILABLE] -- Construction schedule with security-constrained resource access.
34. `fin-project-tco` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Sovereign premium typically 30-50% above commercial equivalent.
35. `fin-project-model` [AVAILABLE] -- Requires: tco-model. Financial model with sovereign funding structures and government cost-sharing.
36. `fin-deal-structure` [AVAILABLE] -- Requires: financial-model. Deal structure with sovereign-specific entities, government co-investment, and tax optimization.
37. `fin-debt-sizing` [AVAILABLE] -- Requires: financial-model. Debt sizing for sovereign projects, often with government-backed or DFI credit facilities.
38. `fin-due-diligence` [AVAILABLE] -- Structured DD checklist across technical, commercial, legal, financial workstreams. Use for sovereign asset evaluation or DFI investment processes.
39. `fin-investor-memo` [AVAILABLE] -- Investor memo for DFI or sovereign wealth fund audience.
40. `fin-insurance-program` [AVAILABLE] -- Insurance program for sovereign facility including political risk coverage.

### Notes

- `fin-ppa-analysis` runs in parallel with `eng-btm-power` for comprehensive power procurement analysis.
- `fin-deal-structure` and `fin-debt-sizing` enable sophisticated capital structuring for sovereign projects with government co-investment.
- `fin-due-diligence` is particularly important for DFI-funded sovereign projects requiring formal investment review.
- `bd-rfp-response` supports responding to government RFPs for sovereign compute facility construction or operation.

### Reference Data Needed

- REGULATORY-MATRIX.md (critical -- country-level data protection, AI regulation, ownership restrictions)
- GPU-REFERENCE.md (GPU specifications with export control awareness)
- COST-BENCHMARKS.md (Construction costs with sovereign premium factors)
- POWER-TARIFFS.md (Energy costs for the target jurisdiction, also consumed by fin-ppa-analysis)
- SOLAR-WIND-RESOURCE.md (Solar/wind resources for sovereign BTM energy independence and PPA analysis)
- DFI-FUNDING.md (Development finance institution funding for foreign sovereign projects)
- FIDIC-CONTRACTS.md (Contract forms with sovereign-specific amendments)
- SLA-BENCHMARKS.md (Availability targets for sovereign-grade SLAs)
- US-STATE-INCENTIVES.md (if US sovereign -- state incentive programs, also consumed by fin-deal-structure)
- FEDERAL-TAX-GUIDE.md (if US sovereign -- federal incentives, ITC/PTC for on-site generation, also consumed by fin-deal-structure and fin-ppa-analysis)

---

## Archetype: Brownfield Conversion

### Skill Sequence

1. `eng-brownfield-convert` [AVAILABLE] -- Brownfield conversion feasibility assessment with 8-factor weighted scoring (structural capacity, power infrastructure, fiber access, contamination risk, seismic zone, zoning compatibility, logistics access, HVAC compatibility). Produces GO/CONDITIONAL/NO-GO recommendation. Run first to determine conversion viability. Includes bundled Python scoring script. References COST-BENCHMARKS.md.
2. `predev-site-feasibility` [AVAILABLE] -- Brownfield path with existing building assessment informed by conversion scoring results. No prerequisites but benefits from #1.
3. `predev-market-study` [AVAILABLE] -- Requires: site-feasibility-report. Market analysis to validate demand for converted facility in target geography.
4. `predev-mou-framework` [AVAILABLE] -- MOU framework for building acquisition and utility commitments.
5. `predev-stakeholder-map` [AVAILABLE] -- Stakeholder engagement for community impact of conversion.
6. `predev-permitting` [AVAILABLE] -- Permitting roadmap for change-of-use, building, and environmental permits.
7. `predev-environmental` [AVAILABLE] -- Environmental assessment including existing contamination and remediation requirements.
8. `eng-power-model` [AVAILABLE] -- Requires: site-feasibility-report. Existing electrical infrastructure analysis with upgrade path modeling.
9. `eng-cooling-design` [AVAILABLE] -- Requires: power-capacity-model. Retrofit constraints including ceiling height, floor loading, and existing HVAC integration.
10. `eng-density-upgrade` [AVAILABLE] -- Optional. Requires: cooling-design-report. Air-to-liquid cooling retrofit for higher density AI/HPC workloads in converted facilities. Use when target density exceeds air-cooled capacity of the brownfield structure.
11. `eng-physical-layout` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Layout within existing building constraints (column spacing, floor loading, ceiling height).
12. `eng-fire-life-safety` [AVAILABLE] -- Fire protection assessment and upgrade for building conversion.
13. `eng-bms-dcim` [AVAILABLE] -- BMS integration with existing building systems.
14. `eng-commissioning` [AVAILABLE] -- Commissioning for converted facility with existing system integration testing.
15. `eng-ops-readiness` [AVAILABLE] -- Operations readiness for converted facility Day 1.
16. `proc-rfp-generator` [AVAILABLE] -- Requires: site-feasibility-report, power-capacity-model, cooling-design-report. RFP generation for renovation and conversion scope.
17. `proc-equipment-spec` [AVAILABLE] -- Optional. Requires: power-capacity-model, cooling-design-report. Equipment specifications for brownfield-compatible equipment (retrofit dimensions, existing infrastructure interfaces).
18. `proc-bid-evaluation` [AVAILABLE] -- Optional. Requires: rfp-document. Bid evaluation for conversion contractors.
19. `proc-contract-structure` [AVAILABLE] -- Contract structure for renovation scope. Consumes FIDIC-CONTRACTS.md.
20. `proc-supply-chain` [AVAILABLE] -- Supply chain assessment for retrofit equipment.
21. `proc-schedule` [AVAILABLE] -- Construction schedule with brownfield-specific tasks (demolition, abatement). Includes CPM script with brownfield mode.
22. `comp-certification` [AVAILABLE] -- Certification roadmap for converted facility.
23. `comp-sustainability-reporting` [AVAILABLE] -- Sustainability reporting including building reuse credits.
24. `fin-project-tco` [AVAILABLE] -- Requires: power-capacity-model, cooling-design-report. Brownfield TCO differs significantly from greenfield (lower land cost, higher renovation cost, shorter timeline).
25. `fin-project-model` [AVAILABLE] -- Requires: tco-model. Financial model accounting for renovation vs new-build economics.
26. `fin-deal-structure` [AVAILABLE] -- Requires: financial-model. Deal structure with brownfield-specific considerations (historic preservation credits, building acquisition structuring).
27. `fin-debt-sizing` [AVAILABLE] -- Requires: financial-model. Debt sizing for brownfield conversion with construction risk adjustments.
28. `fin-due-diligence` [AVAILABLE] -- Structured DD checklist critical for brownfield acquisitions covering environmental, structural, and title diligence in addition to standard workstreams.
29. `fin-investor-memo` [AVAILABLE] -- Investor memo for brownfield conversion opportunity.
30. `fin-insurance-program` [AVAILABLE] -- Insurance program including builder's risk for renovation.
31. `bd-economic-impact` [AVAILABLE] -- Economic impact for government incentive negotiations.

### Notes

- `eng-brownfield-convert` is the dedicated conversion assessment skill -- run first to determine if conversion is viable before investing in full engineering.
- `eng-density-upgrade` is valuable for brownfield conversions targeting AI/HPC workloads where air cooling may be insufficient for the building's constraints.
- `eng-gpu-cluster` is optional -- include only if AI/HPC workloads are planned for the converted facility.
- `comp-sovereignty` is optional -- include only if government tenant or data residency requirements apply.
- `eng-modular-design` may be relevant for brownfield conversions using modular/prefab deployments within existing shells.
- `fin-deal-structure` and `fin-debt-sizing` enable proper capital structuring for brownfield conversion investment.
- `fin-due-diligence` is particularly important for brownfield acquisitions where hidden liabilities (contamination, structural defects, title issues) are common.

### Reference Data Needed

- COST-BENCHMARKS.md (Brownfield conversion cost premiums vs greenfield, also consumed by eng-brownfield-convert)
- POWER-TARIFFS.md (Energy costs for the target location)
- FIDIC-CONTRACTS.md (Contract forms for renovation scope)
- US-STATE-INCENTIVES.md (if US project -- state incentive programs, also consumed by fin-deal-structure)
- FEDERAL-TAX-GUIDE.md (if US project -- federal incentives including historic preservation credits, also consumed by fin-deal-structure)

---

## Skill Availability Summary

| Skill | Status | Wave | Category |
|-------|--------|------|----------|
| `predev-site-feasibility` | [AVAILABLE] | 1 | Predevelopment |
| `eng-power-model` | [AVAILABLE] | 1 | Engineering |
| `eng-cooling-design` | [AVAILABLE] | 1 | Engineering |
| `eng-gpu-cluster` | [AVAILABLE] | 1 | Engineering |
| `comp-sovereignty` | [AVAILABLE] | 1 | Compliance |
| `proc-rfp-generator` | [AVAILABLE] | 1 | Procurement |
| `fin-project-tco` | [AVAILABLE] | 1 | Finance |
| `predev-market-study` | [AVAILABLE] | 2 | Predevelopment |
| `predev-connectivity` | [AVAILABLE] | 2 | Predevelopment |
| `predev-grid-interconnection` | [AVAILABLE] | 2 | Predevelopment |
| `predev-project-narrative` | [AVAILABLE] | 2 | Predevelopment |
| `eng-btm-power` | [AVAILABLE] | 2 | Engineering |
| `eng-modular-design` | [AVAILABLE] | 2 | Engineering |
| `eng-sla-design` | [AVAILABLE] | 2 | Engineering |
| `eng-physical-layout` | [AVAILABLE] | 2 | Engineering |
| `eng-physical-security` | [AVAILABLE] | 2 | Engineering |
| `proc-equipment-spec` | [AVAILABLE] | 2 | Procurement |
| `proc-bid-evaluation` | [AVAILABLE] | 2 | Procurement |
| `fin-project-model` | [AVAILABLE] | 2 | Finance |
| `bd-government-proposal` | [AVAILABLE] | 2 | Business Development |
| `bd-tenant-spec` | [AVAILABLE] | 2 | Business Development |
| `predev-mou-framework` | [AVAILABLE] | 3 | Predevelopment |
| `predev-stakeholder-map` | [AVAILABLE] | 3 | Predevelopment |
| `predev-permitting` | [AVAILABLE] | 3 | Predevelopment |
| `predev-environmental` | [AVAILABLE] | 3 | Predevelopment |
| `eng-fire-life-safety` | [AVAILABLE] | 3 | Engineering |
| `eng-commissioning` | [AVAILABLE] | 3 | Engineering |
| `eng-bms-dcim` | [AVAILABLE] | 3 | Engineering |
| `eng-ops-readiness` | [AVAILABLE] | 3 | Engineering |
| `comp-certification` | [AVAILABLE] | 3 | Compliance |
| `comp-export-controls` | [AVAILABLE] | 3 | Compliance |
| `comp-data-classification` | [AVAILABLE] | 3 | Compliance |
| `comp-sustainability-reporting` | [AVAILABLE] | 3 | Compliance |
| `proc-contract-structure` | [AVAILABLE] | 3 | Procurement |
| `proc-supply-chain` | [AVAILABLE] | 3 | Procurement |
| `proc-schedule` | [AVAILABLE] | 3 | Procurement |
| `fin-investor-memo` | [AVAILABLE] | 3 | Finance |
| `fin-insurance-program` | [AVAILABLE] | 3 | Finance |
| `bd-partnership-proposal` | [AVAILABLE] | 3 | Business Development |
| `bd-economic-impact` | [AVAILABLE] | 3 | Business Development |
| `bd-national-compute` | [AVAILABLE] | 3 | Business Development |
| `eng-brownfield-convert` | [AVAILABLE] | 4 | Engineering |
| `eng-density-upgrade` | [AVAILABLE] | 4 | Engineering |
| `fin-deal-structure` | [AVAILABLE] | 4 | Finance |
| `fin-debt-sizing` | [AVAILABLE] | 4 | Finance |
| `fin-due-diligence` | [AVAILABLE] | 4 | Finance |
| `fin-ppa-analysis` | [AVAILABLE] | 4 | Finance |
| `bd-rfp-response` | [AVAILABLE] | 4 | Business Development |
| `bd-colo-business-model` | [AVAILABLE] | 4 | Business Development |

### Category Summary

| Category | Count | Skills |
|----------|-------|--------|
| Predevelopment | 9 | site-feasibility, market-study, connectivity, grid-interconnection, project-narrative, mou-framework, stakeholder-map, permitting, environmental |
| Engineering | 14 | power-model, cooling-design, gpu-cluster, btm-power, modular-design, sla-design, physical-layout, physical-security, fire-life-safety, bms-dcim, commissioning, ops-readiness, brownfield-convert, density-upgrade |
| Compliance | 4 | sovereignty, certification, export-controls, data-classification, sustainability-reporting |
| Procurement | 6 | rfp-generator, equipment-spec, bid-evaluation, contract-structure, supply-chain, schedule |
| Finance | 8 | project-tco, project-model, deal-structure, debt-sizing, due-diligence, ppa-analysis, investor-memo, insurance-program |
| Business Development | 7 | government-proposal, tenant-spec, partnership-proposal, economic-impact, national-compute, rfp-response, colo-business-model |
| **Total** | **49** | |

### Reference Data Files

| File | Status | Skills That Consume It |
|------|--------|----------------------|
| GPU-REFERENCE.md | [AVAILABLE] | eng-gpu-cluster, eng-cooling-design, bd-national-compute |
| COST-BENCHMARKS.md | [AVAILABLE] | predev-site-feasibility, proc-equipment-spec, fin-project-tco, eng-brownfield-convert |
| POWER-TARIFFS.md | [AVAILABLE] | eng-btm-power, fin-project-tco, comp-sustainability-reporting, fin-ppa-analysis |
| REGULATORY-MATRIX.md | [AVAILABLE] | comp-sovereignty, bd-government-proposal, bd-national-compute |
| US-STATE-INCENTIVES.md | [AVAILABLE] | bd-government-proposal, bd-economic-impact, fin-project-tco, fin-deal-structure |
| FEDERAL-TAX-GUIDE.md | [AVAILABLE] | fin-project-tco, fin-project-model, bd-government-proposal, fin-deal-structure, fin-ppa-analysis |
| SOLAR-WIND-RESOURCE.md | [AVAILABLE] | eng-btm-power, fin-ppa-analysis |
| DFI-FUNDING.md | [AVAILABLE] | bd-government-proposal, bd-national-compute, bd-partnership-proposal |
| SLA-BENCHMARKS.md | [AVAILABLE] | eng-sla-design, proc-contract-structure, bd-colo-business-model |
| FIDIC-CONTRACTS.md | [AVAILABLE] | proc-contract-structure, proc-rfp-generator |

**Last updated:** 2026-03-28
