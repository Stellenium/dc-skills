---
name: dc-project-wizard
description: "Interactively scope a data center project and produce a customized execution plan. Use when starting any data center development project, when asking \"where do I start with a data center?\", when scoping a new DC build, when planning a data center from scratch, or when determining which DC skills to run and in what order. Trigger with \"new data center project\", \"scope a DC\", \"data center wizard\", \"plan a data center build\", or \"which skills do I need?\"."
argument-hint: "<project-type or location>"
---

# Data Center Project Wizard

Interactive scoping tool and entry point to the Stellenium DC Skills library.
Guides users through a structured discovery process to understand project parameters,
then produces a customized project plan with ordered skill execution sequence,
reference data requirements, and location-specific risk flags. Consumes up to 6
shared reference data files for cross-referencing during risk assessment.

## Phase 1: Critical Discovery

> Answer these 6 questions first. They determine the archetype, skill sequence, and risk profile.

**1. Project Type**

What kind of development is this?

- **New Build (Greenfield):** Construction from bare or undeveloped site
- **Expansion:** Adding capacity to an existing data center campus
- **Conversion (Brownfield):** Repurposing an existing building (warehouse, factory, office) into a data center

**2. Location**

Where will the facility be located?

- **Country and region** (required for all projects)
- **For US projects:** State and metro area (enables state-level tax incentive matching from US-STATE-INCENTIVES.md and FEDERAL-TAX-GUIDE.md)
- **For international projects:** Country and region matching REGULATORY-MATRIX.md granularity (enables regulatory risk flagging)

**3. Development Stage**

What stage is the project currently at?

- **Concept:** Initial feasibility exploration, no site commitment
- **Feasibility:** Site shortlisted, conducting due diligence
- **Design:** Engineering underway, key decisions being made
- **Construction:** Permits obtained, build in progress

**4. Counterparty**

Who is the primary stakeholder?

- **Owner-Operator:** Building and operating the facility for own use
- **Developer/Builder:** Building to sell, lease, or operate as a business
- **Investor:** Private equity, infrastructure fund, or sovereign wealth fund evaluating the opportunity
- **Government/DFI:** Government agency or development finance institution funding sovereign or national compute

**5. Scale**

What is the planned IT load?

- **Edge:** Less than 5 MW
- **Enterprise:** 5-20 MW
- **Hyperscale:** 20-100 MW
- **Campus:** 100 MW+

**6. Facility Type**

What type of data center?

- **Traditional Enterprise:** Single-tenant, purpose-built for one organization
- **Hyperscale:** Cloud provider or large-scale compute, standardized modules
- **Sovereign:** Government, defense, or national security requirements
- **Colocation:** Multi-tenant, retail or wholesale
- **Modular/Prefab:** Factory-built, rapid deployment
- **Edge:** Distributed, low-latency, typically unmanned

## Phase 2: Context Refinement

> Based on Phase 1 answers, ask 3-5 follow-up questions from the relevant blocks below.

### If Sovereign Facility

- What are the data residency requirements? (data must stay in-country, in-region, or in specific facility)
- What security clearance level applies? (unclassified, confidential, secret, top secret)
- Government tenants, commercial tenants, or mixed?
- Are there domestic sourcing or ownership restrictions on equipment procurement?
- Is this part of a national AI compute strategy or standalone facility?

### If Brownfield Conversion

- What is the existing building type? (warehouse, factory, office, retail, other)
- What are the known physical constraints? (floor load capacity in psf, ceiling height, column spacing, dock access)
- What is the existing electrical service? (voltage, amperage, number of feeds)
- Is there any known contamination history or environmental remediation requirement?
- What is the target conversion capacity (MW) relative to the building footprint?

### If Hyperscale

- Campus build-out or single building?
- How many phases are planned, and what is the Phase 1 capacity?
- Anchor tenant (pre-leased) or speculative build?
- Standardized power/cooling module size (e.g., 4 MW blocks)?
- On-site power generation planned (solar, gas turbine, fuel cells)?

### If US Location

- Are you aware of state-specific data center incentive programs (sales tax exemption, property tax abatement)?
- Is the site in or near a designated Opportunity Zone?
- Is the utility provider known? (affects power tariff and interconnection timeline)
- Any local zoning or permitting constraints already identified?

### If International Location

- Are data localization requirements already known for the target jurisdiction?
- Are there foreign ownership restrictions on data center operations?
- Is a local partner or joint venture required by regulation?
- What is the status of grid power availability and renewable energy access?

## Archetype Selection

Map Phase 1 answers to one of 4 project archetypes defined in the reference file.

**Process:**

1. Load `references/SKILL-CHAIN-MAP.md`
2. Match the project to the closest archetype:
   - New build + hyperscale/enterprise + AI/HPC workloads -> **Hyperscale Greenfield**
   - New build or expansion + colocation focus -> **Enterprise Colo**
   - Any facility type + sovereign/government/defense requirements -> **Sovereign AI Facility**
   - Conversion of existing building -> **Brownfield Conversion**
3. If no exact match, use the closest archetype and note deviations (e.g., "Using Hyperscale Greenfield archetype with modifications for modular/prefab deployment")
4. Extract the skill sequence, dependency graph, and reference data list from the matched archetype

## Risk Flagging

Cross-reference the project location and parameters against shared reference data files to produce project-specific risk flags.

**Reference file cross-checks:**

1. **REGULATORY-MATRIX.md** (for the specified country) -- Flag data residency requirements, AI regulation frameworks, foreign ownership restrictions, and cross-border data transfer constraints. Critical for international and sovereign projects.

2. **POWER-TARIFFS.md** (for the specified region) -- Flag if industrial power cost exceeds $0.08/kWh (high-cost market warning). Note renewable energy availability and behind-the-meter potential.

3. **COST-BENCHMARKS.md** (for the specified region) -- Flag if construction cost exceeds $12M/MW (premium market warning). Note brownfield conversion premium if applicable.

4. **US-STATE-INCENTIVES.md** (if US project) -- Flag available tax incentives with eligibility criteria, sunset dates, and clawback provisions. Note if the state has no data center incentive program.

5. **FEDERAL-TAX-GUIDE.md** (if US project) -- Flag Opportunity Zone eligibility for the project site, ITC/PTC applicability for on-site renewables, bonus depreciation status, and Section 179D deduction eligibility.

6. **GPU-REFERENCE.md** (if AI/HPC workloads) -- Flag cooling requirements for the specified GPU type (air-cooled vs liquid-cooled threshold), power density per rack, and interconnect bandwidth requirements.

**Risk flag format:** Each flag should include: risk category, severity (HIGH/MEDIUM/LOW), description, source reference file, and recommended mitigation action.

## Output Template

Generate the project plan using this structure:

```markdown
# Project Plan: {Project Name}

## Project Summary

- **Project Type:** {greenfield/expansion/brownfield}
- **Location:** {country, region, state/metro if applicable}
- **Stage:** {concept/feasibility/design/construction}
- **Counterparty:** {owner-operator/developer/investor/government}
- **Scale:** {MW range and specific target}
- **Facility Type:** {type}
- **Archetype:** {matched archetype from SKILL-CHAIN-MAP.md}

## Recommended Skill Sequence

{Numbered list pulled from the matched SKILL-CHAIN-MAP.md archetype.
For each skill include:
- Skill name and availability status
- What it produces (output artifact)
- Why it is needed for this specific project
- Prerequisites (upstream artifacts required)}

## Reference Data Required

{List of reference files that apply to this project, with brief rationale:
- Which of the 6 shared reference files are relevant
- Why each is needed based on project parameters}

## Risk Flags

{Location-specific and project-specific risks identified from cross-referencing
reference data files. Each flag includes:
- Risk category and severity
- Description of the risk
- Source reference file
- Recommended mitigation or next step}

## Execution Order

{Dependency graph showing which skills run in parallel vs sequential:
- Text-based graph notation from SKILL-CHAIN-MAP.md
- Highlight parallel execution opportunities
- Note any skills that can be skipped based on project parameters}
```

## JSON Sidecar

Alongside the markdown project plan, produce a JSON sidecar for programmatic consumption:

```json
{
  "project_type": "",
  "location": {
    "country": "",
    "region": "",
    "state": ""
  },
  "stage": "",
  "counterparty": "",
  "scale_mw": 0,
  "facility_type": "",
  "archetype": "",
  "skill_sequence": [
    {
      "order": 1,
      "skill": "",
      "status": "available|wave-N",
      "requires": [],
      "parallel_with": []
    }
  ],
  "risk_flags": [
    {
      "category": "",
      "severity": "HIGH|MEDIUM|LOW",
      "description": "",
      "source": "",
      "mitigation": ""
    }
  ],
  "reference_data_needed": []
}
```

## Paste-Mode Version

For Claude.ai and Desktop users who cannot load skills from directories.

Generate a condensed project plan that can be pasted as a Project Instruction. The paste-mode version must:

- Include the project summary, skill names in execution order, key risk flags, and abbreviated instructions for each skill
- Omit detailed reference data cross-referencing (users will paste reference data separately as needed)
- Omit JSON sidecar and dependency graph notation
- Target under 5000 tokens (~3500 words) total
- Be self-contained -- a user pasting this into Claude.ai should be able to start executing skills without additional context

**Generation instruction:** After producing the full project plan, automatically generate the paste-mode version as a second output block.

## Skill Availability

Only recommend skills with `[AVAILABLE]` status in SKILL-CHAIN-MAP.md.

For skills marked `[WAVE N]`, output the following in the project plan:

> `{skill-name}` is planned for Wave {N} and not yet available. Manual analysis recommended for: {brief description of what the skill would cover}.

Never silently include unavailable skills in the recommended sequence. Always flag gaps explicitly so users know where manual analysis is needed.

When new skills are added to the library, update SKILL-CHAIN-MAP.md to change their status from `[WAVE N]` to `[AVAILABLE]`.

## Gotchas

- **Brownfield cost paradox:** Brownfield conversion often costs 60-80% of greenfield but takes 40% less time. Do not assume cheaper equals better -- structural limitations, contamination, and ceiling height constraints can eliminate brownfield savings entirely.

- **Sovereign premium:** Sovereign facilities typically carry 30-50% CapEx premium over commercial equivalents for the same MW capacity. This premium comes from enhanced redundancy, domestic sourcing requirements, security infrastructure, and compliance overhead.

- **Hyperscale phasing trap:** Hyperscale campus phasing means Phase 1 site feasibility must account for the ultimate build-out capacity, not just initial phase. Utility interconnection, water rights, and zoning must support the full campus plan.

- **GPU-before-cooling rule:** GPU cluster design should precede cooling design because GPU selection determines heat density, which drives the cooling technology choice. Running cooling design first forces assumptions about rack density that may not hold.

- **Reference data staleness:** Location-specific risk flags may change between project concept and construction phases. Reference data files include staleness dates -- check the as-of date before relying on risk flags for active procurement decisions.

- **No calendar timelines:** This wizard produces skill execution order and dependency graphs only. It does not generate calendar-based project timelines, milestone dates, or construction schedules. Skill sequencing shows what runs before what, not when.

## Evaluations

See `evals/evals.json` for test scenarios.
