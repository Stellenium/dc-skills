# CLAUDE.md

This file provides guidance when working with code in this repository.

## Project Overview

**Stellenium DC Skills** — a Cowork plugin for AI/HPC data center development. 50 skills, 11 reference data files, and a project wizard covering predevelopment through operations handoff. Distributed as a Cowork plugin for Claude Desktop.

## Repository Structure

- `.claude-plugin/plugin.json` — Cowork plugin manifest
- `skills/<name>/SKILL.md` — one directory per skill with YAML frontmatter (`name`, `description`, `argument-hint`, `metadata`)
- `references/` — shared reference data files (`.md`) consumed by skills at runtime
- `SKILL-TEMPLATE.md` — authoring template for new skills

## Naming Conventions

Skills use category prefixes: `predev-`, `eng-`, `comp-`, `proc-`, `fin-`, `bd-`. The wizard is `dc-project-wizard`.

## Skill Design Principles

- **Progressive discovery**: Phase 1 (critical questions) → Phase 2 (context refinement). Consume upstream skill output when available.
- **Brownfield awareness**: Shared skills branch on greenfield/brownfield. Dedicated brownfield skills exist for conversion, density upgrade, capacity planning.
- **Facility type coverage**: Every relevant skill handles traditional, hyperscale, sovereign, colo, modular/prefab, and edge through discovery branching.
- **Effort tagging**: `effort: high` on compute-heavy skills (marked ⚡ in roadmap).

## Distribution

Distributed as a Cowork plugin for Claude Desktop. Install by adding the repository folder in a Cowork project.

## Project

**Stellenium DC Skills**

A Cowork plugin for AI/HPC data center development — 50 skills, 11 reference data files, and a project wizard covering predevelopment through operations handoff. Each skill is a full-package deliverable (SKILL.md + references + scripts + evaluations). Built and maintained by Stellenium Corporation.

**Core Value:** Domain-expert AI skills that produce actionable data center development artifacts — feasibility reports, power models, cooling designs, financial models, RFPs — that a generalist AI cannot replicate.

### Constraints

- **Format**: Cowork plugin with YAML frontmatter + Markdown body SKILL.md files
- **Token budget**: SKILL.md body under 500 lines; reference files loaded on demand
- **Descriptions**: Must include explicit trigger phrases ("Use when...", "Trigger with...") for Cowork skill discovery
- **Licensing**: MIT license (open source)
- **Naming**: Category prefix required (predev-, eng-, comp-, proc-, fin-, bd-); must match directory name

## Technology Stack

### Plugin Format

| Component | Path | Purpose |
|-----------|------|---------|
| Plugin manifest | `.claude-plugin/plugin.json` | Required. Name, version, description, author. |
| Skill definition | `skills/<name>/SKILL.md` | YAML frontmatter + Markdown body. `name` must match directory. |
| Scripts | `skills/<name>/scripts/` | Optional. Python/Bash helpers for compute-heavy skills. |
| References | `skills/<name>/references/` | Optional. Supplementary docs loaded on demand. |
| Evaluations | `skills/<name>/evals/` | Optional. `evals.json` with test cases per skill. |
| Shared references | `references/` | 11 reference files consumed by multiple skills. |

### SKILL.md Frontmatter Schema (Cowork)

| Field | Required | Our Usage |
|-------|----------|-----------|
| `name` | Yes | 1-64 chars, lowercase + hyphens, must match directory name. Category prefix enforced. |
| `description` | Yes | Domain description with "Use when..." and "Trigger with..." phrases for Cowork discovery. |
| `argument-hint` | No | Documents expected argument for autocomplete (e.g., `"<IT-load-MW>"`). |
| `metadata` | No | `author`, `version`, `effort`, `tags`, `inputs`, `outputs`. |

### Validation

CI runs `scripts/validate-all.sh` on push/PR to check that every SKILL.md has valid frontmatter with `name` matching its directory.

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd:quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd:debug` for investigation and bug fixing
- `/gsd:execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd:profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
