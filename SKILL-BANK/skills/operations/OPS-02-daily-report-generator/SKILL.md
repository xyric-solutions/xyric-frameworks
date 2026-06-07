---
name: Daily Report Generator
description: Generate an end-of-day progress report from git commits, the work queue, and progress docs — terminal text plus an HTML dashboard. Use for an end-of-day standup, "what did we accomplish today", or an EOD summary; do not use for weekly rollups (use the weekly PPP skill) or for ad-hoc git log inspection. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Daily Report Generator

Produce a single end-of-day report that triangulates three sources — git commits (what
was done), the progress doc (what was decided), and the work queue (what is queued) — into
an accountability-and-momentum snapshot. This skill is the **method**; the specifics it
operates on — your progress/queue file names, the folder where they live per project, and
your team registry — are decided per organization. See [`ADAPT.md`](ADAPT.md) for what to
decide before using this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT**: scan only the git history available in the current repo,
label missing-source sections as `PLACEHOLDER (no progress/queue source configured)`, and
list what's missing. **Never invent** file paths, team names, decisions, or queue items.

## Philosophy

Daily reports exist for two reasons: **accountability** and **momentum**.

**Accountability** means making work visible. In a small team it is easy for days to pass
without anyone noticing that a task has stalled or a blocker has gone unaddressed. A daily
report forces that visibility — if there are zero commits, that fact is stated plainly, not
hidden. This is not surveillance; it is catching drift early. A single day of zero activity
is normal. Three consecutive days signals a problem worth discussing.

**Momentum** means ending each day knowing what was accomplished and what comes next. The
"Tomorrow's Priorities" section ensures no morning is wasted on "what should I work on?"
The executive summary connects individual commits to project goals — turning a list of code
changes into a story of progress.

The triangulation across the three sources catches gaps: work without decisions backing it,
decisions without work following them, or queued items that never start.

## When to Activate

**Triggers**:
- `/daily-report` or `/eod` slash commands
- "Generate daily report"
- "What did we accomplish today?"
- "End of day summary"

## Data Sources

| Source | Purpose | Where it comes from |
|--------|---------|---------------------|
| Git commits | Today's activity | `git log --since="00:00"` in the current repo |
| Team registry | Author normalization | your team registry file |
| Progress docs | Blockers, decisions | your progress-doc files under each project/area root and other tracked areas |
| Work queue | Queue status (in_progress / blocked / queued) | your work-queue files under each project/area root |

## Workflow

### Phase 1: Gather data

1. Read your team registry for member names, IDs, and any git aliases. If absent, skip
   normalization and tag authors `(external)`.
2. Run `git log --since="00:00" --format="%H|%an|%ae|%s|%ai" --all` and parse into
   structured rows (hash, author, email, message, timestamp).
3. Normalize each git author against the registry: check declared git aliases first, then
   email match, then name-contains, then fall back to `"<raw-author> (external)"`.
4. Parse commit messages for conventional-commit types (feat, fix, docs, refactor, test,
   chore). These type names are a universal convention — keep them verbatim.
5. Group commits by project/area (inferred from path or commit scope) and by team member.

### Phase 2: Read context

1. Read each progress doc found under each project/area root (and any other tracked areas
   you list) — extract today's session logs, milestones in progress, and blockers.
2. Read each work-queue file found under each project/area root — extract items with status
   `in_progress`, `blocked` (with reasons), and the top queued items for tomorrow.

### Phase 3: Generate report

1. Write a 2–3 sentence executive summary covering the day's focus, accomplishments, and
   concerns — facts only, no optimistic spin.
2. Output the plain-text report following the structure in [`forms.md`](forms.md).
3. Generate the HTML dashboard. Use your HTML report template if you have one; otherwise
   generate inline HTML. Save to a gitignored output directory (default
   `reports/daily/YYYY-MM-DD.html`).

## Anti-Patterns

| Anti-Pattern | Why It Hurts | Do This Instead |
|--------------|--------------|-----------------|
| Running mid-day | Incomplete data produces a misleading picture of the day's work | Generate at end of work day, after final commits |
| Manually editing reports | Edits get lost on regeneration and create a false record | Regenerate from source data if corrections are needed |
| Committing reports to git | Reports are ephemeral snapshots, not source of truth | Keep reports in a gitignored output directory |
| Skipping zero-activity days | Hiding quiet days masks patterns (e.g., every Thursday is slow) | Generate the report anyway — "0 commits" is useful data |
| Inflating the executive summary | Optimistic spin undermines trust in the report | State facts plainly: "0 commits today", not "the team is regrouping" |

## Success Criteria

- [ ] All git authors resolved to registry names (or tagged `(external)`)
- [ ] Executive summary accurately reflects the day (no hallucinated accomplishments)
- [ ] Blocked items prominently displayed with reasons
- [ ] Tomorrow's priorities drawn from the work queue (not invented)
- [ ] HTML dashboard renders correctly with metrics, team cards, and alerts
- [ ] Report generated in under 30 seconds

## Error Handling

| Scenario | Action |
|----------|--------|
| No commits today | Show "No commits today" in the Activity section |
| No progress doc found | Skip the "Key Decisions" section |
| No work-queue file found | Skip the "Work Queue" section |
| No team registry found | Skip author normalization; tag all authors `(external)` |
| Git command fails | Report the error and continue with available data |
| HTML template not found | Use inline HTML generation |

## Integration

| Skill | Integration |
|-------|-------------|
| Commit-message skill | Parses the conventional-commit messages it generates |
| Weekly PPP skill | Weekly rollup aggregates these daily reports |
| Progress skill | Reads progress-doc updates |
| Work-queue skill | Reads work-queue status |

## Deep Reference

- Author-normalization logic and HTML dashboard components: [`reference.md`](reference.md)
- Output structure, intake, and quality checklist: [`forms.md`](forms.md)

> File paths and the team registry are organization-specific decisions — see
> [`ADAPT.md`](ADAPT.md). This skill stays portable across organizations; only those
> decisions change.
