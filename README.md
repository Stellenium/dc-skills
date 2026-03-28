<p align="center">
  <img src="https://img.shields.io/badge/skills-50-blue?style=flat-square" alt="50 Skills" />
  <img src="https://img.shields.io/badge/platform-Cowork%20%7C%20Claude%20Desktop-8A2BE2?style=flat-square" alt="Platform" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License" />
  <img src="https://img.shields.io/badge/version-1.0.1-orange?style=flat-square" alt="Version" />
</p>

# Stellenium DC Skills

**50 AI skills for data center development** — from site selection to operations handoff. Each skill follows a structured workflow and produces a real deliverable: feasibility reports, power models, cooling designs, financial models, RFPs, due diligence trackers, and more.

Built as a [Cowork plugin](https://docs.claude.com) for Claude Desktop.

---

## Installation

### From GitHub (recommended)

```
1. Open Claude Desktop → Cowork tab
2. Customize (gear icon) → Personal plugins → Add marketplace
3. Paste: https://github.com/Stellenium/dc-skills.git
4. Install "stellenium-dc-skills" from the marketplace
```

All 50 skills become available in every Cowork session.

### From a local clone

```bash
git clone https://github.com/Stellenium/dc-skills.git
```

Then add the cloned folder as a **linked folder** in your Cowork session. Skills will be available only in that session.

---

## Quick Start

### 1. Run the project wizard

The wizard interviews you about your project and recommends which skills to run and in what order:

> *Run the dc-project-wizard skill to help me scope my data center project.*

### 2. Run individual skills

Once you know what you need, ask directly:

> *Run predev-site-feasibility for a 50 MW hyperscale facility in Northern Virginia.*

> *Run eng-cooling-design for a tropical climate site with 40 kW average rack density.*

> *Run fin-project-tco using the power model output from earlier.*

Claude follows the skill's structured workflow, asks clarifying questions, and produces a detailed deliverable.

---

## What Each Skill Produces

These aren't summaries. Each skill produces the kind of document a specialist consultant would deliver:

| Example Output | Skill |
|---|---|
| Site feasibility report with GO/NO-GO scoring across 12 factors | `predev-site-feasibility` |
| Power distribution model from utility feed to rack, Tier I-IV | `eng-power-model` |
| Cooling technology comparison ranked by CapEx, OpEx, and PUE | `eng-cooling-design` |
| GPU cluster layout with liquid cooling and interconnect fabric | `eng-gpu-cluster` |
| 10-year financial model with IRR/NPV/MOIC and equity waterfall | `fin-project-model` |
| Issuable RFP with evaluation criteria and scoring methodology | `proc-rfp-generator` |
| Due diligence tracker across technical, commercial, legal, financial | `fin-due-diligence` |

---

## All 50 Skills

### Predevelopment (9 skills)

| Skill | Description |
|---|---|
| `predev-site-feasibility` | GO/NO-GO site scoring across power, fiber, water, climate, seismic, incentives |
| `predev-market-study` | Supply/demand gap analysis with absorption rates, pricing, competitive landscape |
| `predev-connectivity` | Carrier strategy, fiber entrance, meet-me room, IX peering, subsea redundancy |
| `predev-grid-interconnection` | Utility interconnection queue position, study phases, upgrade costs, timeline |
| `predev-project-narrative` | 2-3 page concept paper synthesizing feasibility and market data |
| `predev-mou-framework` | MOU/LOI templates adapted for government, landowner, utility, anchor tenant |
| `predev-stakeholder-map` | Influence/interest scoring with engagement strategy and opposition risk |
| `predev-permitting` | Jurisdiction-specific permitting roadmap with dependency tracking and critical path |
| `predev-environmental` | EIA scoping, water rights analysis, LEED/BREEAM certification path |

### Engineering (14 skills)

| Skill | Description |
|---|---|
| `eng-power-model` | Power capacity from utility feed to rack with Tier I-IV redundancy and PUE calc |
| `eng-cooling-design` | 14 cooling technologies ranked with ASHRAE TC 9.9 compliance |
| `eng-gpu-cluster` | AI/HPC cluster facility design with rack layout, liquid cooling, storage tiers |
| `eng-btm-power` | Behind-the-meter generation: gas turbines, solar, wind, BESS, fuel cells with LCOE |
| `eng-modular-design` | Modular/prefab DC sizing with factory vs. field analysis and transport logistics |
| `eng-sla-design` | SLA framework with serial/parallel reliability chains and credit structures |
| `eng-physical-layout` | Hall layout, hot/cold aisle containment, cabling, meet-me room per BICSI 002 |
| `eng-physical-security` | Tiered security zones, CCTV, access control, OT/IT segmentation |
| `eng-fire-life-safety` | Detection, suppression, VESDA, NFPA 75/76/855 compliance, egress |
| `eng-commissioning` | Level 1-5 commissioning and IST procedures with acceptance criteria |
| `eng-bms-dcim` | BMS/DCIM architecture with sensor strategy, alarm hierarchy, digital twin |
| `eng-ops-readiness` | Operations handover with staffing models, SOPs, training, Day 1 checklist |
| `eng-brownfield-convert` | Building-to-DC conversion feasibility with weighted scoring |
| `eng-density-upgrade` | Air-to-liquid cooling retrofit for live facilities, 5 kW to 100+ kW/rack |

### Compliance (5 skills)

| Skill | Description |
|---|---|
| `comp-sovereignty` | Data sovereignty and regulatory compliance: residency, cross-border, AI regulation |
| `comp-certification` | ISO 27001, SOC 2, Uptime Tier, EN 50600, PCI DSS gap analysis and audit prep |
| `comp-export-controls` | GPU import/export compliance: EAR, ITAR, Wassenaar, sanctions, end-use monitoring |
| `comp-data-classification` | Classification levels, encryption requirements, mixed-sensitivity architecture |
| `comp-sustainability-reporting` | ESG reporting with Scope 1/2/3 carbon accounting, PUE/WUE/CUE, CSRD, SBTi |

### Procurement (6 skills)

| Skill | Description |
|---|---|
| `proc-rfp-generator` | Issuable RFP for EPC, design-build, CM-at-risk, or modular contracts |
| `proc-equipment-spec` | Vendor-neutral performance specs with compliance standards and acceptance criteria |
| `proc-bid-evaluation` | Weighted bid scoring with TCO normalization and recommendation memo |
| `proc-contract-structure` | FIDIC/NEC/AIA contract form selection with milestone payments and risk allocation |
| `proc-supply-chain` | Supply chain risk assessment with lead times, vendor diversification, mitigations |
| `proc-schedule` | Construction schedule with critical path, long-lead items, and risk register |

### Finance (8 skills)

| Skill | Description |
|---|---|
| `fin-project-tco` | 10/20-year TCO with CapEx/OpEx breakdown, MACRS, ITC/PTC, Opportunity Zone modeling |
| `fin-project-model` | Revenue, EBITDA waterfall, debt service, IRR/NPV/MOIC, sensitivity analysis |
| `fin-investor-memo` | Investment memo adapted for VC, PE/infrastructure, sovereign wealth, or DFI |
| `fin-insurance-program` | Builder's risk, property, BI, cyber, environmental, terrorism coverage design |
| `fin-deal-structure` | SPV design, tax equity, co-investment waterfall, promote structure, exit modeling |
| `fin-debt-sizing` | DSCR-based debt capacity with construction facility and covenant structuring |
| `fin-due-diligence` | Technical, commercial, legal, and financial DD tracker with red flag scoring |
| `fin-ppa-analysis` | PPA vs. self-gen vs. grid with LCOE comparison, term analysis, risk assessment |

### Business Development (7 skills)

| Skill | Description |
|---|---|
| `bd-government-proposal` | Government pitch with strategy alignment, economic impact, ask/offer matrix |
| `bd-tenant-spec` | Tenant requirements discovery: power density, cooling, SLA, connectivity, growth |
| `bd-partnership-proposal` | JV proposal with contribution framework, governance, and exit mechanisms |
| `bd-economic-impact` | Quantified jobs, procurement, tax revenue, and GDP impact using I-O multipliers |
| `bd-national-compute` | National AI compute strategy with sovereign capacity modeling and phased buildout |
| `bd-rfp-response` | RFP response with compliance matrix, technical narrative, and win themes |
| `bd-colo-business-model` | Colo pricing, interconnection revenue, occupancy ramp, tenant mix |

### Project Wizard (1 skill)

| Skill | Description |
|---|---|
| `dc-project-wizard` | Interactive project scoping that recommends which skills to run and in what order |

---

## How Skills Chain Together

Skills are designed to feed into each other. The wizard maps this for you, but here are two common paths:

**Greenfield hyperscale build:**

```
predev-site-feasibility
  → predev-grid-interconnection
    → eng-power-model
      → eng-cooling-design
        → eng-gpu-cluster
          → fin-project-tco
            → fin-project-model
              → fin-investor-memo
```

**Brownfield AI retrofit:**

```
eng-brownfield-convert
  → eng-density-upgrade
    → eng-power-model
      → eng-cooling-design
        → fin-project-tco
          → proc-rfp-generator
            → proc-bid-evaluation
```

---

## Reference Data

11 reference files are bundled in `plugin/references/` and loaded automatically by skills that need them:

| File | Contents |
|---|---|
| `GPU-REFERENCE.md` | Accelerator specs, interconnect bandwidth, cooling requirements, rack density |
| `COST-BENCHMARKS.md` | Regional $/MW construction costs for North America, EMEA, APAC |
| `POWER-TARIFFS.md` | Industrial grid tariffs by market |
| `SOLAR-WIND-RESOURCE.md` | GHI by region, wind capacity factors, seasonal variation |
| `FEDERAL-TAX-GUIDE.md` | ITC/PTC rates, MACRS, Section 179D, safe harbor rules |
| `US-STATE-INCENTIVES.md` | State-level tax programs, thresholds, exemptions, clawbacks |
| `REGULATORY-MATRIX.md` | Country-specific data protection, AI regulation, residency rules |
| `DFI-FUNDING.md` | Development finance institution profiles, eligibility, strategic priorities |
| `FIDIC-CONTRACTS.md` | Red/Yellow/Silver/Gold Book comparison and risk allocation |
| `SLA-BENCHMARKS.md` | Tier I-IV availability targets, MTTR/MTBF benchmarks |
| `DISCLAIMER-FRAMEWORK.md` | Required financial, engineering, and regulatory disclaimer language |

You don't need to manage these. Skills load what they need on demand.

---

## Tips

**Start with the wizard.** It asks about your project and produces a tailored execution plan. You don't need to know which skills exist.

**Be specific.** The more detail you provide (location, MW capacity, rack density, facility type, development stage), the better the output.

**Ask for the full deliverable.** Each skill produces a structured document. If Claude gives you a summary, say: *"Give me the full deliverable with all sections."*

**Skills chain together.** Many skills consume output from earlier skills. The wizard tells you the right order, or see the dependency chains above.

---

## Disclaimer

These skills produce engineering estimates, financial models, and regulatory summaries intended as starting points for professional review. They do not replace licensed engineers, attorneys, or financial advisors.

## License

MIT
