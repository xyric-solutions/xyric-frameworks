# Adapting PRD Generator

**What this skill does:** transforms a finished Product Vision Document into a comprehensive
Product Requirements Document — features, personas, acceptance criteria, MoSCoW scope, success
metrics, and an epic breakdown.

This skill is generic methodology — the workflow, section template, and validation gates are
universal. To use it for your organization, decide the values below and either keep them in
your working brief at PRD time, or bake them into your forked copy of `SKILL.md` and the
companion files. Until they're decided, the skill emits a labeled GENERIC DRAFT (with neutral
`PLACEHOLDER` values) rather than inventing your audience, product names, pricing, or file
paths.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Audience segments** — your primary user/customer segments (one line each), and which is primary | PRD Philosophy, Required Context Sources; drives the Personas section | Personas are derived from these — never invent them. |
| **Key messages** — the 5–9 messages each persona/feature should reinforce | PRD Philosophy (persona-driven prioritization) | Inherited from your vision/positioning. |
| **Differentiators** — what makes this product different from alternatives | Executive Summary, Competitive Analysis (in `forms.md`/`reference.md`) | Used for the inspiration-focused competitive analysis. |
| **Product taxonomy** — the product code/name (or service line) this PRD belongs to | Output naming, pipeline hook `<!-- ARCHITECTURE_READY: ... -->` | — |
| **Lifecycle stage** — what stage the product is in (e.g. design/planning, development) | PRD Philosophy, Peer: Product Manager alignment (`reference.md`) | — |
| **Monetization** — monetized at MVP, or "not monetized yet" | Success criteria questions (`reference.md` Q6) | — |
| **Product folder location** — where product folders live; the Vision filename pattern | Workflow Position, Required Context Sources, Phase 0/4 | The Vision input and PRD output both resolve from here. |
| **PRD output name** — the filename convention for the requirements document | Workflow Position, Phase 4 output | — |
| **Progress file** — the per-product status file to append a session entry to | Phase 4 output, Required Context Sources | — |
| **Template location** — where PRD/section templates and reference PRDs live | Phase 0 research, Required Context Sources | Used to calibrate length/structure against existing PRDs. |
| **Epic-PRD folder** — where detailed Epic PRDs live (downstream) | Cross-Reference Index, Required Context Sources | — |

## How to gather these

The numbered **PRD Context Intake** in [`forms.md`](forms.md) is the questionnaire for all of
the above — ask it once at the start of a PRD run, record the answers wherever your team keeps
product decisions (a working brief, a per-product context file, or your forked `SKILL.md`).

## Platform-independent (do not change)

The following are universal facts that work as-is for any organization:

- `forms.md` — the PRD output template, quality checklists, activation checklist, and
  section-by-section validation criteria.
- `reference.md` — the 4-phase methodology, question frameworks, MoSCoW guidance, Mermaid
  diagram types and color scheme, dependency-mapping patterns, and competitive-analysis
  structure.
- `sub-skills/PRD-PERSONA.md` and `sub-skills/PRD-FEATURES.md` — the persona and feature
  methodology, anti-patterns, and quality gates.
