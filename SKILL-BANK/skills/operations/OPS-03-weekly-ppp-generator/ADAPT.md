# Adapting Weekly PPP Generator

**What this skill does:** generates a weekly Progress / Problems / Plans report — terminal
text plus an HTML dashboard with week-over-week metrics and an auto risk radar — from git
history, progress docs, and the work queue.

This skill is generic methodology — it never hardcodes a repository's layout. To use it for
your organization, decide the values below and either keep them in your run brief at use
time, or bake them into your forked copy of `SKILL.md`. Until they're decided, the skill
emits a labeled GENERIC DRAFT (git-only, neutral `PLACEHOLDER` paths) rather than inventing
paths, project names, or team members.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Units root** — path holding each per-unit (product/client/team) folder | Data Sources, Workflow (Phase 2) | Where progress + work-queue docs are found. |
| **Progress doc name** — the per-unit file for milestones and decisions | Data Sources, Workflow (Phase 2) | e.g. a progress / status doc. |
| **Work-queue doc name** — the per-unit file for the execution queue / blockers | Data Sources, Workflow (Phase 2) | e.g. a next-steps / backlog doc; source of the Plans section. |
| **Team registry** — file mapping members → git author aliases → unit assignments | Data Sources, Workflow (Phase 1), Author Normalization | Used to normalize commit authors; unmatched authors are reported, never dropped. |
| **Template locations** — where the plain-text PPP and HTML dashboard templates live | Related Files, HTML Dashboard | — |
| **Naming conventions** — work-item ID format (prefix + number) | Sample Output | e.g. `NS-XXX` / `TASK-XXX`. |
| **Report output dir** — where generated weekly reports are written | Workflow (Phase 3), Related Files | Default `reports/weekly/`; written as `YYYY-Www.html`. |
| **Timezone & week start** — for the "Generated" timestamp and Mon–Fri activity chart | Workflow (Phase 1), Week-Range Resolution | Default ISO week, Monday start. |

## How to gather these

The numbered **Workspace Intake** in [`forms.md`](forms.md) is the questionnaire for all of
the above — ask it once, record the answers wherever your team keeps these decisions.

## Platform-independent (do not change)

The PPP format, the risk-detection rules and thresholds, the week-over-week and activity-chart
calculations, the author-normalization logic, the output structure in [`forms.md`](forms.md),
and the patterns in [`reference.md`](reference.md) are universal — they work as-is for any
repository.
