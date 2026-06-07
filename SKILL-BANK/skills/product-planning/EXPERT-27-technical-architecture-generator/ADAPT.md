# Adapting Technical Architecture Generator

**What this skill does:** transforms a completed PRD into a Technical Architecture document
(with ADRs and an Epic-Component Mapping Matrix) so independent teams can execute epics in
parallel.

This skill is generic methodology — the 4-phase workflow and quality gates never hardcode a
specific organization. To use it for yours, decide the values below and either keep them in your
design brief at use time, or bake them into your forked copy of `SKILL.md`. Until they're decided,
the skill emits a labeled GENERIC DRAFT (e.g. a `PLACEHOLDER STACK`, relative `./` paths) rather
than inventing a stack, deployment target, portfolio model, or repository paths.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Default / standard tech stack** — frontend, backend, client/server state, database, deployment target | Portfolio context, Default Stack First, Anti-Patterns | If you have no standard, the skill picks per-product and records the choice in an ADR. |
| **Portfolio model** — one line on how products relate (shared dev pool / single product / agency work) | Portfolio context | Sets how strict stack coherence should be; drives the deviation-needs-an-ADR rule. |
| **Lifecycle stages** — your named stages, if different from defaults | Practical Over Perfect; reference.md PRD Analysis template | Defaults: Vision / Feasibility / Design & Planning / Development / Launch & Growth. |
| **Products root** — `{products_root}`, the parent folder pattern for product docs | Required Context Sources, Output Summary | e.g. a products directory with a sub-folder per product. |
| **Progress file name** — `{progress_file}`, the per-product session/progress doc | Required Context Sources; Phase 4 output | e.g. a per-product progress/continuity markdown file. |
| **Naming conventions** — filename patterns for architecture, ADRs, milestones | Output Summary; Phase 4 ADR output | Controls the ADR filename pattern if you have one. |
| **Template location** — where reusable doc templates (e.g. an architecture template) live | References; Phase 2/4 generation | Optional — falls back to the built-in 12-section order. |

## How to gather these

The numbered **Architecture Context Intake** in [`forms.md`](forms.md) is the questionnaire for all
of the above — ask it once, record the answers wherever your team keeps these decisions (a design
brief, or your forked `SKILL.md`).

## Platform-independent (do not change)

The 4-phase workflow, the 6-question framework, the 12-section generation order, the quality gates,
the Epic-Component Mapping Matrix rules, and all checklists/templates in `forms.md` and
`reference.md` are method facts — they work as-is for any organization. Only the values in the
table above change.
