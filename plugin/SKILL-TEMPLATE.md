# SKILL-TEMPLATE.md

> **Authoring template for Stellenium DC Skills (Cowork plugin format).**
> Copy this file into your skill directory as `SKILL.md`, then replace the worked example
> with your skill's domain content. Every section marked with `<!-- TEMPLATE: ... -->` must
> be customized. Sections without template annotations are boilerplate -- keep them as-is.
>
> **Cowork discovery:** Descriptions must include explicit "Use when..." and "Trigger with..."
> phrases with quoted example triggers. This allows Cowork to match user intent to skills.
>
> **Line budget:** When you create a skill from this template, the SKILL.md body
> (after the closing `---` of frontmatter) must be under 500 lines.
> Split longer content into `references/` files loaded on demand.

---

## Frontmatter

Copy this frontmatter block exactly, then replace values:

```yaml
---
name: eng-power-model
# <!-- TEMPLATE: Replace with your skill name. Must be 1-64 chars, lowercase
#      alphanumeric + hyphens only, no leading/trailing/consecutive hyphens.
#      Must match the directory name (e.g., skills/eng-power-model/). -->
description: >
  Model data center power capacity from utility feed to rack-level distribution.
  Use when designing electrical distribution for new facilities, expanded capacity,
  or brownfield conversions. Trigger with queries like "design power distribution",
  "size electrical infrastructure", "calculate PUE", or "model redundancy configuration".
  Produces component-level power chain analysis with Tier I-IV redundancy modeling
  and PUE calculations consumed by cooling design and TCO skills.
# <!-- TEMPLATE: Replace with your skill's description. Must include at least one
#      "Use when..." clause and a "Trigger with..." clause with 2-3 quoted example
#      phrases (like "design power distribution", "calculate X", etc.). Cowork uses
#      these to match user intent. Include key outputs at the end. Max 1024 characters. -->
argument-hint: "<power-scenario>"
# <!-- TEMPLATE: Optional. Brief hint for single-argument skills (e.g., "<project-name>",
#      "<financial-scenario>"). Omit if skill requires multi-turn discovery. -->
metadata:
  author: stellenium
  version: "1.0"
  effort: high
  # <!-- TEMPLATE: Set to "high" for compute-heavy skills that benefit from
  #      calculation scripts and validation loops. Omit for standard skills. -->
  tags: [data-center, engineering, power, electrical]
  # <!-- TEMPLATE: Replace with domain keywords for discovery. -->
  inputs: [site-feasibility-report]
  # <!-- TEMPLATE: List upstream artifact types this skill consumes.
  #      Use artifact type names, not file paths. Omit if no upstream dependency. -->
  outputs: [power-capacity-model]
  # <!-- TEMPLATE: List artifact types this skill produces.
  #      Downstream skills reference these in their inputs. -->
---
```

---

## Body Structure (Worked Example: eng-power-model)

Everything below this line is the SKILL.md body. Replace the worked example
content with your skill's domain content, keeping the section structure intact.
The progressive discovery pattern (Phase 1 -> Phase 2 conditional refinements)
works directly in Cowork and requires no modifications.

---

<!-- TEMPLATE: Replace title and overview with your skill's domain. 2-3 sentences. -->

# Power Capacity Model

Model data center power capacity from utility feed to rack-level distribution.
Produces a complete power chain analysis with redundancy modeling, PUE calculation,
and phased capacity planning. Consumes the upstream site feasibility report.

## Phase 1: Critical Discovery

> Answer these questions first. They determine the entire approach.

<!-- TEMPLATE: Keep questions 1 and 2 as-is for any skill involving physical
     facilities. Replace questions 3-7 with your domain-critical questions. -->

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

<!-- TEMPLATE: Replace questions 3-7 below with domain-critical questions
     specific to your skill. Keep 3-5 questions that fundamentally change
     the approach. -->

3. What is the total planned IT load (MW)?
   - Specify per phase if multi-phase deployment

4. What redundancy tier is required?
   - Tier I (basic, no redundancy)
   - Tier II (redundant components, N+1)
   - Tier III (concurrently maintainable, N+1 minimum)
   - Tier IV (fault tolerant, 2N or 2N+1)

5. What is the utility voltage and service configuration?
   - Single utility feed
   - Dual utility feed (diverse paths)
   - Specify voltage if known (e.g., 13.8kV, 34.5kV)

6. Is behind-the-meter generation planned?
   - Grid-only
   - Solar/wind + grid
   - Gas turbine + grid
   - Full microgrid capability

7. What is the target PUE?
   - < 1.2 (aggressive, likely requires liquid cooling)
   - 1.2 - 1.4 (standard modern facility)
   - 1.4 - 1.6 (traditional air-cooled)
   - No target specified

## Phase 2: Context Refinement

> Based on Phase 1 answers, gather additional detail.

<!-- TEMPLATE: Replace these conditional sections with refinements
     specific to your domain. Show different questions based on
     Phase 1 answers. -->

### Greenfield Path

If Phase 1 answer is **Greenfield**:

1. Has the utility interconnection agreement been signed?
2. What is the available utility capacity at the site boundary?
3. Are there any utility feed routing constraints (easements, rights-of-way)?
4. What is the planned build-out timeline (phases and target dates)?

### Brownfield Path

If Phase 1 answer is **Brownfield**:

1. What is the existing electrical infrastructure?
   - Utility service entrance capacity (voltage/amperage)
   - Existing switchgear and distribution
   - UPS systems (make, model, capacity, age)
   - Generator systems (fuel type, capacity, runtime)
2. What is the current IT load vs. available capacity?
3. Are there known electrical code compliance gaps?
4. What is the maximum allowable downtime for electrical upgrades?

### Facility Type Refinements

<!-- TEMPLATE: Add facility-type-specific questions that change the analysis.
     Not every type needs a section -- only add where the approach differs materially. -->

**Hyperscale additions:**
- Campus-level power distribution strategy?
- Standardized power module size (e.g., 4MW blocks)?
- Custom vs. vendor-standard UPS platforms?

**Sovereign additions:**
- Dual utility feed from separate substations required?
- On-site fuel storage requirements (days of autonomy)?
- SCIF or classified space power isolation requirements?

**Edge additions:**
- Single-phase or three-phase utility service?
- Containerized/pre-integrated power solution preferred?
- Remote monitoring requirements (unmanned site)?

## Analysis & Output

<!-- TEMPLATE: Replace this section with your skill's core workflow.
     Describe the step-by-step process, reference shared data files,
     and include the validation loop. -->

### Process

1. **Map the power chain:** Utility service entrance -> ATS/STS -> main switchgear -> UPS input -> UPS -> PDU/RPP -> rack-level distribution
2. **Size each component** based on IT load, redundancy tier, and growth plan
3. **Calculate losses** at each conversion stage (transformer, UPS, PDU)
4. **Compute PUE** from component-level efficiency data
5. **Model redundancy** scenarios (N, N+1, 2N, 2N+1) with failure analysis
6. **Phase the build-out** if multi-phase deployment

### Reference Data

Load these files on demand -- do not read upfront:

<!-- TEMPLATE: Replace with references your skill needs. Use relative paths
     from the skill directory (skills/<name>/). One level of depth only. -->

- [GPU specifications](../../references/GPU-REFERENCE.md) -- TDP, cooling, interconnect data for per-rack power sizing
- [Cost benchmarks](../../references/COST-BENCHMARKS.md) -- Regional $/kW for power infrastructure

### Validation Loop

<!-- TEMPLATE: Include this pattern for compute-heavy skills (effort: high).
     For standard skills, replace with a simpler quality check. -->

1. Compute initial power model from Phase 1 and Phase 2 inputs
2. Cross-check per-rack power against GPU-REFERENCE.md TDP data
3. Validate PUE is physically possible (PUE < 1.0 is impossible; PUE < 1.1 requires liquid cooling)
4. Verify total load does not exceed utility feed capacity (including redundancy overhead)
5. Check that redundancy tier matches component configuration (e.g., Tier III requires N+1 minimum, not just N)
6. If any constraint violated: flag the error, adjust assumptions, recompute from step 1
7. Repeat until all constraints satisfied

## Output Template

<!-- TEMPLATE: Replace with the exact artifact structure your skill produces.
     This is the contract downstream skills depend on. Can be inline here
     or placed in assets/output-template.md. -->

### Power Capacity Model

**Project:** [Project Name]
**Date:** [Date]
**Prepared by:** [Skill: eng-power-model v1.0]

#### 1. Utility Service
- Utility feed: [voltage] / [amperage]
- Service configuration: [single/dual feed]
- Contracted capacity: [MW]
- Redundancy: [N / N+1 / 2N / 2N+1]

#### 2. Power Chain
| Stage | Equipment | Capacity | Redundancy | Efficiency |
|-------|-----------|----------|------------|------------|
| Utility entrance | [Transformer] | [MVA] | [config] | [%] |
| Transfer switch | [ATS/STS] | [A] | [config] | [%] |
| Main switchgear | [Type] | [A] | [config] | [%] |
| UPS | [Type] | [kVA] | [config] | [%] |
| PDU/RPP | [Type] | [kVA] | [config] | [%] |

#### 3. Capacity Summary
- Total IT load: [MW]
- Total facility load: [MW]
- PUE: [calculated value]
- Available capacity margin: [%]

#### 4. Phased Build-out
| Phase | IT Load | Facility Load | Timeline | Capital Estimate |
|-------|---------|---------------|----------|-----------------|
| Phase 1 | [MW] | [MW] | [date] | [$M] |
| Phase 2 | [MW] | [MW] | [date] | [$M] |

#### 5. Redundancy Analysis
- Configuration: [N / N+1 / 2N / 2N+1]
- Single point of failure: [identified / none]
- Concurrent maintainability: [yes / no]
- Fault tolerance: [yes / no]

## Gotchas

<!-- TEMPLATE: Replace with 3-5 domain-specific non-obvious facts that
     trip up generalist AI models. These are the key value-add of each skill. -->

- Tier III does NOT mean 2N redundancy -- it means Concurrently Maintainable (N+1 minimum). Tier IV is fault tolerant (2N or 2N+1).
- PUE below 1.1 requires liquid cooling; claiming sub-1.1 PUE with air cooling only is a red flag in any feasibility study.
- Utility feed sizing must account for ALL planned phases even if only Phase 1 is being built -- utility upgrades have 2-5 year lead times.
- UPS efficiency varies dramatically with load percentage: a 2N UPS system at 25% load per unit has significantly worse efficiency than N+1 at 60% load per unit.
- Generator sizing must include motor starting current for cooling systems -- a common oversight that causes undersizing by 15-20%.

## Calculation Scripts

<!-- TEMPLATE: Include this section for compute-heavy skills (effort: high).
     List bundled scripts in the scripts/ directory. For standard skills,
     omit this section entirely. -->

For deterministic calculations, use bundled scripts:

- `scripts/pue-calculator.py` -- PUE calculation with component-level losses
- `scripts/redundancy-model.py` -- Redundancy analysis for N through 2N+1 configurations

Requires: Python 3.11+

## Disclaimer

<!-- TEMPLATE: Include this section ONLY for fin-* and comp-* skills.
     For engineering, procurement, and predevelopment skills, omit entirely. -->

> **For fin-* and comp-* skills only.** Engineering skills like this example
> do not require the disclaimer framework. When authoring a financial or
> compliance skill, include the relevant verbatim paragraphs below.

This skill produces estimates for planning purposes.
See [Disclaimer Framework](../../references/DISCLAIMER-FRAMEWORK.md) for full terms.

**fin-* skills must include:**
- Financial Disclaimer (always)
- Tax Disclaimer (if referencing FEDERAL-TAX-GUIDE.md)

**comp-* skills must include:**
- Regulatory and Compliance Disclaimer (always)

## Evaluations

<!-- TEMPLATE: Every skill ships with an evals/ directory containing evals.json.
     This is used for internal validation and benchmarking. Copy the stub from
     skills/_template/evals/evals.json into your skill's evals/ directory and
     replace the placeholder content. -->

See `evals/evals.json` for test scenarios.

Example structure (see `skills/_template/evals/evals.json` for the copy-ready stub):

```json
{
  "skill_name": "eng-power-model",
  "evals": [
    {
      "id": 1,
      "prompt": "Design the electrical distribution for a 10MW Tier III data center in Northern Virginia with N+1 UPS redundancy.",
      "expected_output": "A power capacity model showing utility feed through ATS, switchgear, UPS, PDU to rack-level distribution with redundancy analysis and PUE estimate.",
      "assertions": [
        "Output includes complete utility-to-rack power chain",
        "Tier III redundancy (N+1) is correctly modeled",
        "PUE estimate is provided with component-level methodology"
      ]
    }
  ]
}
```
