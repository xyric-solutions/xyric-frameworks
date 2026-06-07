# Weekly PPP Generator — Reference

Deep patterns and detailed guidance. Load on demand. Repo paths and file names are
organization-specific (see [`ADAPT.md`](ADAPT.md)); the calculations and detection rules
below are universal and repo-independent.

---

## Organization-specific inputs

The skill operates on these per-organization decisions:

- **Units root** — path that holds each per-unit folder.
- **Progress doc name** — progress-doc file name within a unit.
- **Work-queue doc name** — work-queue file name within a unit.
- **Team registry** — file mapping members → git aliases → units.
- **Template locations** — where the PPP + HTML templates live.
- **Naming conventions** — work-item ID format (prefix + number).

Use the concrete paths at run time. If one is undecided, treat it as unanswered — ask the
Workspace Intake in [`forms.md`](forms.md), or fall back to a labeled `PLACEHOLDER` path
and note the gap in the report.

---

## Week-over-Week Comparison

If the previous week's report exists in the weekly output directory (`YYYY-Www-1.html` or
the matching markdown):

1. Parse the previous metrics row.
2. Calculate deltas (this week − last week).
3. Show change indicators (`+X`, `-X`, `=`); for rates, show percentage change.

If no previous report exists, omit the comparison column and note "first report".

---

## Activity Chart Calculation

Aggregate commits per weekday (Mon–Fri), then scale bar heights to the busiest day:

```
max_commits = max(mon, tue, wed, thu, fri)
bar_height  = (day_commits / max_commits) * 100px
```

---

## HTML Dashboard Features

| Component | Data Source |
|-----------|-------------|
| Metrics Cards | Week totals with week-over-week comparison |
| Activity Chart | Bar chart showing commits per day (Mon–Fri) |
| Team Cards | Members with weekly stats and focus areas |
| Progress Bars | Unit / milestone completion percentages |
| Blocked Alert | Alert (e.g. red) for blocked items with durations |
| Plans Table | Next week's priority queue |

The HTML structure comes from your configured HTML dashboard template; populate it with the
data gathered in the workflow.

---

## Author Normalization

Git records `author.name` and `author.email`, which vary per machine and per contributor.
Map each commit to a canonical team member using the alias list in your team/author-alias
registry (name variants, multiple emails, and git aliases). Commits whose
author matches no entry are reported under an "Unrecognized authors" note so the registry
can be updated — never silently dropped.

---

## Risk Detection Details

### Stalled Item Detection
Items with `in_progress` status for more than 7 days should be flagged. Recommend reviewing
scope and considering splitting the work.

### Silent Project Detection
Units that appear in the work-queue docs but have 0 commits this week need attention. This
could indicate blocked work, reassigned priorities, or forgotten tasks.

### Growing Blockers
If the count of blocked items this week exceeds last week, this is an escalating risk
signal. Include escalation recommendations in the report.

### Unassigned Priority
A P0 or P1 item with no assignee is a coordination gap — flag it so an owner can be named
before the week starts.

### Long Queue
A queue exceeding ~10 items signals over-commitment or under-prioritization. Recommend a
triage pass.

---

## Week-Range Resolution

| Day report is run | Window used | Rationale |
|-------------------|-------------|-----------|
| Friday | Current week, Mon–Fri | End-of-week wrap-up |
| Monday | Previous week, Mon–Fri | Catch-up on the week just finished |
| Any other day | Trailing 7 days | Ad-hoc; note the non-standard window |

Format the label as `Mon DD–DD, YYYY (YYYY-Www)` using the ISO week number, adjusted for the
week start and timezone your organization uses.

---

## Integration with other skills

| Skill | Connection |
|-------|------------|
| Daily report generator | Daily reports feed the weekly aggregation; share author-normalization logic |
| Progress doc workflow | Source of milestones completed / in progress |
| Work-queue workflow | Source of completed, in-progress, and blocked items |
| Audit / consistency check | Risk patterns overlap with audit checks |

> All paths, file names, and team aliases are organization-specific (see [`ADAPT.md`](ADAPT.md)).
> This file stays portable across repositories — only those decisions change.
