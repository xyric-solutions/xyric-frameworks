# Adapting Task Generator

**What this skill does:** breaks an approved technical specification into a complete,
TDD-ordered (ARCH→TEST→IMPL→INTG), MoSCoW-prioritized, dependency-mapped task breakdown with
each task assigned to one engineer role.

This skill is generic methodology — it never hardcodes a team, file scheme, or folder layout.
To use it for your organization, decide the values below and either keep them in your brief
at use time, or bake them into your forked copy of `SKILL.md`. Until they're decided, the
skill emits a labeled GENERIC DRAFT (placeholder role names, `<task-id>`, `<task-file>`)
rather than inventing your team or conventions.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Engineer roles / registry** — who or what owns each task category (Architect, Test Engineer, Backend, Frontend, Fullstack, Reviewer) | Task Categories & TDD Ordering, Implementation Types, Anti-Patterns | The TDD category→role mapping is the generic default; you supply concrete owners. |
| **Products root** — parent path where product/story folders live | Required Context Sources | Where stories and epic PRDs are read from. |
| **Template locations** — where spec, story, and task-breakdown files live | Required Context Sources, Phase 4: Output & Tracking, Output | Source of the tech spec; destination of the task file. |
| **Task file naming** — task / task-breakdown filename pattern and where task IDs come from | Phase 4: Output & Tracking, Output | Substitutes for the `<task-file>` / `<task-id>` placeholders. |
| **Story & spec naming** — story and spec filename patterns + ID formats | Required Context Sources, Phase 0 | Substitutes for `<story-id>` / `<spec-file>`. |
| **Story-linking rule** — how a task references its parent story so it isn't orphaned | Phase 4, Anti-Patterns (#7) | E.g. a `story_ids` field in the task YAML. Mandatory for traceability. |
| **Tracking files** — the planning/progress file and the execution-queue file to update on completion | Four-Phase Workflow (Phase 4) | Whatever files your team uses for planning status and the work queue. |

## How to gather these

The numbered **Workspace Intake** in [`forms.md`](forms.md) is the questionnaire for all of
the above — ask it once, record the answers wherever your team keeps these decisions (your
brief, or baked into your fork).

## Platform-independent (do not change)

The following are universal facts that need no adaptation:

- **TDD category ordering** (ARCH→TEST→IMPL→INTG) and the four-phase workflow.
- **MoSCoW distribution** (~60% MUST / ~20% SHOULD / ~20% COULD) and its over-scoping warnings.
- **Task complexity sizing** (S/M/L/XL) and the one-session-per-task principle.
- `forms.md` templates and quality/activation checklists, and `reference.md` patterns,
  question frameworks, and validation gates — all org-neutral.
