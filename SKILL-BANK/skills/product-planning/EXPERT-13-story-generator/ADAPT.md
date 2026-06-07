# Adapting Story Generator

**What this skill does:** breaks product Epics into well-defined user stories with BDD
acceptance criteria, INVEST sizing, 100% feature-coverage validation, and a blocking quality
gate — then writes story files and an Epic index into your repository.

This skill is generic methodology — the INVEST/MoSCoW/BDD method and the 4-phase workflow
never change. What it needs from your organization is *where* stories and tasks live, *how*
your files are named, the field that links a task back to its story, and your product list.
Decide the values below and either keep them in your generation brief at use time, or bake
them into your forked copy of `SKILL.md`. Until they're decided, the skill emits a labeled
GENERIC DRAFT (stories in a neutral `stories/` folder, `PLACEHOLDER` naming) rather than
inventing your real layout.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Product folder root** — how each product's folder is located (e.g. a `{root}/{product}` path) | Required Context Sources; Four-Phase Workflow (Phase 0) | All other paths resolve relative to this. |
| **Story folder** — sub-folder inside a product that holds story files (e.g. `stories/`) | Output (Phase 4); Required Context Sources | — |
| **Story filename pattern** — e.g. `S<Epic>-<Seq>-<slug>.md` | Output (Phase 4) | Slugs lowercase, hyphenated, ≤40 chars. |
| **Epic-index filename pattern** — e.g. `Epic-<NN>-Stories-Index.md` | Output (Phase 4) | One index file per Epic. |
| **Task / work-item folder** — sub-folder that holds implementation tasks | Output (Phase 4); pipeline hooks | The downstream task-generation skill writes here. |
| **Task filename pattern** — e.g. `<prefix>-<NNN>-<slug>.md` | Output (Phase 4) | — |
| **Story-linking field** — the YAML field a task uses to reference its parent story/stories | Output (Phase 4); Cross-Skill Integration | This is what keeps work traceable; tasks without it are orphaned. |
| **Story & Epic-index templates** — where your canonical templates live | Output (Phase 4); `forms.md` fallback templates | If none, the skill falls back to the templates in `forms.md`. |
| **Planning/context file** — the per-product file recording decisions and session history (e.g. a `progress` or status doc) | Four-Phase Workflow; Output (Phase 4) | Updated after each generation run. |
| **Product taxonomy** — the list of products and each one's lifecycle stage | Four-Phase Workflow (Phase 0) | Lets the skill resolve the right product folder from an Epic reference. |

## How to gather these

The numbered **Workspace & Conventions Intake** in [`forms.md`](forms.md) is the
questionnaire for all of the above — ask it once, then record the answers wherever your
team keeps workspace/convention decisions (a fork of `SKILL.md`, a generation brief, or your
own conventions doc).

## Platform-independent (do not change)

The methodology is universal and needs no adaptation:

- `forms.md` — the 9 clarification questions, the activation checklist, the story and
  Epic-index fallback templates, the quality checklist, and the validation criteria.
- `reference.md` — the 4-phase step-by-step, the assumption-challenge guidance, and the
  INVEST / MoSCoW / BDD sizing reminders.
- The validation gate (Coverage / Duplicate / Template / DAG critical checks; BDD /
  Quantified-metrics / Edge-case / Open-question quality checks).

These work as-is for any organization; only the workspace decisions in the table above change.
