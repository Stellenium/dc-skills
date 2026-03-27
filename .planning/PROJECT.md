# Stellenium DC Skills

## What This Is

An open source skill library for AI/HPC data center development — 50 skills, 10 reference data files, and a project wizard covering predevelopment through operations handoff. Each skill is a full-package deliverable (SKILL.md + references + scripts + evaluations) compliant with the agentskills.io specification. Targets Claude Code, OpenAI Codex, Gemini CLI, Cursor, OpenClaw, and any SKILL.md-compatible agent. Built and maintained by Stellenium Corporation.

## Core Value

Domain-expert AI skills that produce actionable data center development artifacts — feasibility reports, power models, cooling designs, financial models, RFPs — that a generalist AI cannot replicate.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] 50 skills + 1 wizard, each as a full package: SKILL.md (agentskills.io compliant) + references/ + scripts/ + evals/
- [ ] 10 reference data files consumed by skills at runtime (GPU-REFERENCE.md, COST-BENCHMARKS.md, POWER-TARIFFS.md, REGULATORY-MATRIX.md, US-STATE-INCENTIVES.md, FEDERAL-TAX-GUIDE.md, SOLAR-WIND-RESOURCE.md, DFI-FUNDING.md, SLA-BENCHMARKS.md, FIDIC-CONTRACTS.md)
- [ ] Formal skill chaining: skills declare inputs/outputs, downstream skills consume upstream artifacts
- [ ] Progressive discovery: Phase 1 (critical questions) → Phase 2 (context refinement) within each skill
- [ ] Brownfield awareness: shared skills branch on greenfield/brownfield; dedicated brownfield skills for conversion, density upgrade, capacity planning
- [ ] Facility type coverage: every relevant skill handles traditional, hyperscale, sovereign, colo, modular/prefab, and edge through discovery branching
- [ ] Plugin manifest (plugin.json) for Claude Code Marketplace and ClawHub registry
- [ ] SKILL-TEMPLATE.md that all skills follow
- [ ] platform-guide.md for cross-platform install instructions (Claude Code, Codex, Gemini CLI, Cursor, OpenClaw, Claude.ai/Desktop)
- [ ] dc-project-wizard as the interactive entry point — scopes project type, location, stage, counterparty, scale, facility type and produces customized project plan
- [ ] Effort tagging: `effort: high` on compute-heavy skills via metadata field
- [ ] Category prefix naming: predev-, eng-, comp-, proc-, fin-, bd-

### Out of Scope

- Runtime infrastructure (no hosted APIs, no SaaS) — skills are static files consumed by AI agents
- Custom AI model training — skills leverage existing foundation models
- Proprietary vendor integrations — skills are vendor-neutral
- Real-time data feeds — reference data files are point-in-time snapshots updated periodically

## Context

### Domain

AI/HPC data center development is a specialized domain spanning predevelopment (site feasibility, market study, grid interconnection), engineering (power, cooling, GPU clusters, modular design), compliance (sovereignty, export controls, sustainability), procurement (RFPs, equipment specs, supply chain), finance (TCO, financial models, deal structure), and business development (government proposals, tenant specs, national compute strategy).

### Competitive Positioning

No comparable open source skill library exists for this domain. Generalist AI struggles with: GPU TDP/cooling specifics, Tier I-IV redundancy modeling, ASHRAE TC 9.9 thermal guidelines, FIDIC contract structures, US state-by-state tax incentives, sovereign AI regulatory matrices, and grid interconnection queue strategies.

### Technical Approach

- **Specification**: agentskills.io compliant — `name` (lowercase-hyphen, ≤64 chars), `description` (≤1024 chars), optional `license`, `compatibility`, `metadata` (author, version, effort, tags, compatible-with), `allowed-tools`
- **Directory structure**: Each skill is a directory with SKILL.md + optional scripts/, references/, assets/, evals/
- **Progressive disclosure**: Frontmatter (~100 tokens at startup) → SKILL.md body (<5000 tokens when activated) → reference files (on demand)
- **SKILL.md body**: Under 500 lines; split longer content into referenced files one level deep
- **Skill chaining**: Skills declare `inputs` and `outputs` in metadata; downstream skills reference upstream artifacts
- **Reference data files**: Standalone .md files in a shared references/ directory, consumed by multiple skills
- **Wave plan**: Wave 1 (8 skills + 6 refs + infrastructure), Wave 2 (14 skills + 3 refs), Wave 3 (20 skills + 1 ref), Wave 4 (10 skills)

### Standards Coverage

Uptime Tier, EN 50600, ASHRAE TC 9.9, TIA-942, BICSI 002-2024, ISO 27001/27017/27018, SOC 2, NFPA 75/76/855, IEC 62040, IEEE 3006.5, LEED/BREEAM, FIDIC, NERC CIP, GHG Protocol, SBTi, CSRD.

### Cooling Technologies (14)

Raised-floor air, in-row, containment, rear-door HEX, direct-to-chip liquid, single-phase immersion, two-phase immersion, adiabatic/evaporative, dry coolers, cooling towers, free cooling/economizer, geothermal, absorption cooling, heat reuse.

### Power Sources (11)

Grid utility, gas turbines, reciprocating engines, fuel cells, solar PV, wind, BESS, diesel backup, SMRs (emerging), hydrogen-ready, microgrid/islanding.

## Constraints

- **Specification**: agentskills.io compliant — all skills must pass `skills-ref validate`
- **Token budget**: SKILL.md body under 500 lines; reference files loaded on demand
- **Cross-platform**: Must work on Claude Code, Codex, Gemini CLI, Cursor, OpenClaw, and paste-as-project-instruction on Claude.ai/Desktop
- **Licensing**: MIT license (open source)
- **Naming**: Category prefix required (predev-, eng-, comp-, proc-, fin-, bd-); must match directory name

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| agentskills.io spec compliance | Cross-platform standard adopted by 30+ agent products; maximizes distribution | — Pending |
| Full package per skill (SKILL.md + refs + scripts + evals) | Matches quality bar of top skill libraries (gstack, claude-skills); enables validation and artifact chaining | — Pending |
| Formal skill chaining with declared inputs/outputs | Skills in DC development naturally chain (feasibility → power model → cooling → TCO); formal contracts prevent downstream guessing | — Pending |
| All 4 waves in one milestone | Ambitious but complete — delivers the full 50-skill library as a cohesive product | — Pending |
| Custom metadata extensions (effort, tags, compatible-with) | Domain-specific needs beyond base spec; metadata field is the sanctioned extension point | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd:transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-03-27 after initialization*
