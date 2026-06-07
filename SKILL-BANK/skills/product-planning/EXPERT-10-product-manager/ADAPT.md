# Adapting Product Manager (EXPERT-10)

**What this skill does:** applies product-management method — PRDs, MoSCoW prioritization,
lifecycle stage-gates, and success metrics — to one organization's products.

This skill is generic methodology — it never hardcodes a specific business model, product set,
or workspace. To use it for your organization, decide the values below and either keep them in
your product brief at use time, or bake them into your forked copy of `SKILL.md`. Until they're
decided, the skill emits a labeled GENERIC DRAFT (e.g. `[PRODUCT]`, `Stage 1…5`, placeholder
paths) rather than inventing them.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Business model** — one line on how the org makes money and whether business lines feed/fund each other | Business-model alignment; Core Principles (Model-Aligned) | If a single straightforward line, the cross-line review is skipped. |
| **Product taxonomy** — for each product: code prefix, name, current stage | Product Codes Convention; Context Checklist | Codes become PRD/task prefixes (e.g. `<CODE>-001`). |
| **Lifecycle stages** — the named stages a product passes through | Product Lifecycle; Stage Gates | Default is Vision → Feasibility → Design & Planning → Development → Launch & Growth. |
| **Audience / ICP tiers** — primary user segments, with device/connectivity/literacy context | Context Checklist; Core Competencies (User Research) | Drives PRD "Who has this problem" and research methods. |
| **Device strategy norm** — mobile-first, desktop-first, or responsive-equal default | Context Checklist | — |
| **Products root path** — where product folders live | Deep Reference (workspace integration, `reference.md`) | A path pattern that points at your product folders. |
| **Planning & execution files** — filenames for planning context and the execution queue | `reference.md` Workspace Integration | e.g. progress file + next-steps file. |
| **Template locations** — where doc templates live | `reference.md` Workspace Integration | — |
| **Naming conventions** — filename/ID rules for PRDs, stories, tasks, milestones | `reference.md` Workspace Integration | — |
| **Organization name / identity** — org or product name used in headers | PRD/update templates in `forms.md` | — |

## How to gather these

The numbered **Product Context Intake** in [`forms.md`](forms.md) is the questionnaire for all
of the above — ask it once, record the answers wherever your team keeps product decisions (a
brief, a wiki, or your forked `SKILL.md`).

## Platform-independent (do not change)

The methodology is universal and needs no adaptation: the MoSCoW criteria, the PRD template
structure, stage-gate questions, confidence indicators, the RACI matrix, the AI-native
stage table, and all checklists in `forms.md` and `reference.md`. Only the organization-specific
decisions above change between organizations.
