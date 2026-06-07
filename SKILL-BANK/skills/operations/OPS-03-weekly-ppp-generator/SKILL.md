---
name: Weekly PPP Generator
description: Generate a weekly Progress / Problems / Plans (PPP) report from git history, progress docs, and the work queue — terminal text plus an HTML dashboard with week-over-week metrics and an auto risk radar. Use at week boundary (Fri EOD / Mon morning) for a multi-day trajectory report; do not use for a single-day standup (use the daily report skill) or for ad-hoc summaries with no repo. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Weekly PPP Generator

Produce a weekly **Progress, Problems, Plans** report that summarizes the week's
accomplishments, blockers, and upcoming priorities — as terminal-friendly plain text and
a visual HTML dashboard with an activity chart and week-over-week metrics. This skill is
the **method**; the specifics it operates on — the repository's actual paths, file names,
and team aliases — are decided per organization. See [`ADAPT.md`](ADAPT.md) for what to
decide before using this for a given repository.

When those specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** that reads only git history, uses neutral `PLACEHOLDER`
paths, and lists what is missing. Never invent file paths, project names, team members, or
accomplishments. The PPP format, risk thresholds, and HTML structure below are universal.

## Purpose

Generates weekly PPP reports summarizing the week's accomplishments, challenges, and
upcoming priorities. Outputs both terminal-friendly plain text and a visual HTML dashboard
with activity charts.

## Philosophy

The PPP framework answers three questions stakeholders care about: "What happened?",
"What's in the way?", and "What's next?" Everything else is noise.

**Weekly cadence matters.** Daily reports capture activity. Weekly reports capture
trajectory. A daily report might show 5 commits on Monday and 0 on Tuesday — that is normal
variation. A weekly report showing 45 commits this week vs. 12 last week tells a story about
momentum. Week-over-week comparison is the earliest signal that a project is accelerating or
stalling.

**Problems deserve equal billing with Progress.** Most status reports bury blockers in
footnotes because surfacing problems feels uncomfortable. The PPP format gives Problems its
own section with the same visual weight as Progress. This is intentional: a blocker that has
been sitting for 5 days is more important than 10 completed commits, because it represents
work that is NOT happening.

**Plans create commitment.** Writing "Next week: complete the queued item, unblock the
stalled one" in a shared report creates a soft commitment. When next week arrives and neither
happened, the follow-up PPP makes that gap visible without anyone needing to call it out
directly. The report does the accountability work so humans do not have to.

**Risk detection is the report's highest-value feature.** Stalled items (in_progress > 7
days), silent projects (0 commits this week), and growing blocker counts are patterns humans
miss when heads-down in daily work. The weekly report surfaces these patterns automatically.

---

## When to Activate

**Triggers**:
- A weekly-PPP slash command (e.g. `/weekly-ppp` or `/ppp`) if your repo defines one
- "Generate weekly PPP"
- "Weekly progress report"
- "What did we accomplish this week?"
- End of week (Friday EOD or Monday morning)

---

## Data Sources

The bracketed paths are organization-specific (see ADAPT.md); the rest are tool/universal
facts.

| Source | Purpose | Command / Path |
|--------|---------|----------------|
| Git commits | Week's activity | `git log --since="7 days ago"` |
| Team registry | Author normalization | your team/author-alias registry |
| Progress docs | Milestones, decisions | your units root + your progress doc |
| Work-queue docs | Queue status, blockers | your units root + your work-queue doc |
| Previous PPP | Week-over-week comparison | the weekly report output dir |

---

## Workflow

### Phase 1: Gather and Normalize Data

1. Determine week range: if Friday, use Mon–Fri of the current week; if Monday, use the
   previous Mon–Fri; otherwise the last 7 days. Format as `Mon DD–DD, YYYY (YYYY-Www)`.
2. Read your team registry for team members, author/git aliases, and unit assignments.
3. Run `git log --since="7 days ago" --format="%H|%an|%ae|%s|%ai" --all` and parse.
4. Normalize authors against the team registry (same logic as the daily report skill).
5. Aggregate commits by day (Mon–Fri) for the activity chart.
6. Parse conventional-commit types from messages.

### Phase 2: Extract Context and Metrics

1. Read each progress doc under your units root — extract milestones completed this week,
   milestones in progress, key decisions, blockers.
2. Read each work-queue doc under your units root — extract completed items (archive),
   in_progress items, blocked items (with reasons and duration), and the top queued items
   for next week.
3. Calculate metrics: total commits, unique contributors, units touched, milestones
   completed, work items completed, items blocked, items in progress.
4. If the previous week's report exists, calculate week-over-week deltas.

### Phase 3: Generate Report

1. Write a 4–5 sentence executive summary covering the week's theme, accomplishments,
   challenges, and outlook.
2. Build the **PROGRESS** section: accomplishments by unit and by team member, milestones
   completed, notable commits.
3. Build the **PROBLEMS** section: currently blocked items (with duration and resolution
   path), items resolved this week, risk radar (auto-detected patterns).
4. Build the **PLANS** section: priority queue (top 5–7 items), team assignments,
   dependencies to resolve, milestones to target.
5. Output the plain-text report, then generate an HTML dashboard to the weekly report output
   directory as `YYYY-Www.html`.

---

## Risk Detection Rules

| Risk Pattern | Detection Logic | Threshold |
|--------------|-----------------|-----------|
| Stalled Item | in_progress > X days without commits | 7 days |
| Silent Project | 0 commits this week | 1 week |
| Growing Blockers | blocked_count > last_week | +1 |
| Unassigned Priority | P0/P1 item with no assignee | Any |
| Long Queue | queued items > X | 10 items |

---

## Sample Output

Names, units, and IDs below are illustrative — use the real ones from your repo. Work-item
IDs follow your organization's naming conventions.

```
=== WEEKLY PPP ===
Week: Mar 3–7, 2026 (2026-W10)
Generated: 2026-03-07 18:00

## Week at a Glance

| Metric              | This Week | Last Week | Change |
|---------------------|-----------|-----------|--------|
| Total Commits       | 45        | 38        | +18%   |
| Contributors        | 4         | 3         | +1     |
| Milestones Completed| 2         | 1         | +1     |
| Items Completed     | 8         | 5         | +60%   |
| Items Blocked       | 2         | 1         | +1     |

## Executive Summary

This week marked significant progress on the platform unit with 45
commits across 4 contributors. Key accomplishments include completing
the onboarding-epic stories and setting up the development environment.
The team faces two blockers related to cloud infrastructure, but
momentum remains strong. Next week's focus will be completing the epic
review and unblocking the cloud setup.

## PROGRESS (What We Accomplished)

### By Unit

#### platform
Commits: 32 | Contributors: A, B, C

Key Accomplishments:
- Completed onboarding-epic stories (18 stories)
- Set up development environment with hot reload
- Migrated the progress doc to the milestone format

Milestones Completed:
- M-004: Development Environment Setup (Mar 4)

#### data-product
Commits: 13 | Contributors: A, D

Key Accomplishments:
- Released a version with monitoring and caching
- Implemented progress streaming

### By Team Member

| Member       | Commits | Units              | Focus Area         |
|--------------|---------|--------------------|--------------------|
| Member A     | 28      | platform, data     | Architecture, auth |
| Member B     | 8       | platform           | UI development     |
| Member C     | 5       | platform           | Code review        |
| Member D     | 4       | data-product       | Data analytics     |

## PROBLEMS (Challenges & Blockers)

### Currently Blocked (2)

[TASK-007] Cloud Provider Setup
- Unit: ops-product
- Blocked by: Awaiting cloud-credit approval
- Days blocked: 5
- Impact: Blocks deployment pipeline setup
- Resolution path: Escalate to finance

[TASK-002] Roles & Responsibilities Doc
- Unit: org
- Blocked by: Waiting on TASK-001 (Org Structure)
- Days blocked: 3
- Resolution path: Complete TASK-001 first

### Risk Radar

| Risk                 | Indicator             | Recommendation          |
|----------------------|-----------------------|-------------------------|
| Epic stalled         | In progress 14+ days  | Review scope, split     |
| No org-unit commits  | 0 commits this week   | Schedule governance     |
| Cloud blocker growing| 5 days blocked        | Escalate cloud credits  |

## PLANS (Next Week's Focus)

### Priority Queue

| Priority | ID       | Task                  | Unit         | Assignee |
|----------|----------|-----------------------|--------------|----------|
| P0       | TASK-001 | Complete Epic Review  | platform     | A        |
| P0       | TASK-007 | Cloud Provider Setup  | ops-product  | C        |
| P1       | TASK-002 | Story Breakdown       | platform     | A        |
| P1       | TASK-005 | Core App UI           | platform     | B        |
| P2       | TASK-008 | Batch Upload Feature  | data-product | D        |

### Dependencies to Resolve

| Blocker         | Owner   | Needed By | Impact            |
|-----------------|---------|-----------|-------------------|
| Cloud credits   | Finance | Mar 10    | Unblocks TASK-007 |
| Epic completion | A       | Mar 11    | Unblocks TASK-002 |

=== Report saved to: <weekly report dir>/2026-W10.html ===
```

---

## Anti-Patterns

| Anti-Pattern | Why It Hurts | Do This Instead |
|--------------|-------------|-----------------|
| Running mid-week | Incomplete data skews metrics and week-over-week comparisons | Generate Friday EOD or Monday morning |
| Burying blockers | Unreported blockers compound — a 5-day blocker becomes 12 days by next report | Give PROBLEMS equal visual weight to PROGRESS |
| Optimistic risk radar | Marking everything "On Track" eliminates the report's early-warning value | Apply detection rules mechanically — if an item is in_progress > 7 days, flag it |
| Skipping week-over-week comparison | Without a baseline, "45 commits" is meaningless — is that good or bad? | Load the previous week's data when available |
| Manually editing generated reports | Edits get overwritten and create discrepancies between data and narrative | Regenerate from source data if corrections are needed |

---

## Success Criteria

- [ ] All three PPP sections present with substantive content
- [ ] Week-over-week comparison included when previous data exists
- [ ] Risk radar populated with auto-detected patterns (not empty when issues exist)
- [ ] Blocked items include duration, impact, and resolution path
- [ ] Plans section draws from the work-queue docs (not invented priorities)
- [ ] Executive summary accurately reflects the data (no hallucinated accomplishments)
- [ ] HTML dashboard renders with activity chart, team cards, and alerts

---

## Error Handling

| Scenario | Action |
|----------|--------|
| No commits this week | Show warning, continue with queue data |
| No progress doc found | Skip milestone sections |
| No work-queue doc found | Skip work-queue sections |
| No previous-week data | Skip comparison columns, note "first report" |
| Partial data | Generate report with available data, note gaps |

---

## Integration

| Skill | Integration |
|-------|-------------|
| Daily report generator | Daily reports feed into weekly aggregation |
| Commit-message parser | Parses commit messages |
| Progress doc workflow | Reads the progress doc for milestones |
| Work-queue workflow | Reads queue status |
| Audit / consistency check | Risk patterns overlap with audit checks |

---

## Related Files

The bracketed locations are organization-specific (see ADAPT.md).

| File | Purpose |
|------|---------|
| your template location → weekly-ppp template | Plain-text template |
| your template location → report-html template | HTML dashboard template |
| your team/author-alias registry | Team member / author-alias registry |
| Weekly report output directory | Output directory for generated reports |

> All paths, file names, and team aliases are organization-specific (see [`ADAPT.md`](ADAPT.md)).
> This skill stays portable across repositories — only those decisions change.
