# Adapting Daily Report Generator

**What this skill does:** generates an end-of-day report from git commits, your work queue,
and your progress docs — terminal text plus an HTML dashboard.

This skill is generic methodology — it never hardcodes where your files live. To use it for
your organization, decide the values below and either keep them in your run brief at use
time, or bake them into your forked copy of `SKILL.md`. Until they're decided, the skill
emits a labeled GENERIC DRAFT (git history only) rather than inventing file paths, team
names, decisions, or queue items.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Progress doc filename** — file that records decisions/blockers per area | Data Sources, Phase 2 | e.g. a per-project progress markdown. Skip "Key Decisions" if none. |
| **Work-queue filename** — file holding the execution queue + item status | Data Sources, Phase 2 | Statuses used: `in_progress` / `blocked` / `queued`. |
| **Areas root** — folder glob where those files live, one per project/area | Data Sources, Phase 2 | e.g. one folder per product. |
| **Other tracked areas** — extra roots outside the main areas root that also carry progress docs | Phase 2 | e.g. client engagements, a company-level area. Optional. |
| **Team registry** — where the author/team registry lives (names, IDs, git aliases, emails) | Phase 1, author normalization | If absent, all authors tagged `(external)`. |
| **Report template location** — folder holding plain-text / HTML report templates | Phase 3 | Optional; falls back to inline HTML generation. |
| **Output directory** — where rendered HTML reports are written | Phase 3 | Default `reports/daily/YYYY-MM-DD.html`, gitignored — never committed. |
| **Timezone label** — timezone stamped on the report header | forms.md output template | e.g. local office timezone. |

## How to gather these

The numbered **Workspace Intake** in [`forms.md`](forms.md) is the questionnaire for all of
the above — ask it once, record the answers wherever your team keeps these decisions.

## Platform-independent (do not change)

These are universal facts and need no adaptation:

- The **conventional-commit type reference** (feat, fix, docs, refactor, test, chore) in
  `reference.md` — a portable convention independent of any organization.
- The **author-normalization algorithm** (alias → email → name-contains → external) in
  `reference.md` — structural, only the registry it reads is organization-specific.
- The **output structure** and **quality checklist** in `forms.md` — fill the bracketed
  placeholders with your real values.
