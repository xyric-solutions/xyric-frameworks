# Daily Report Generator — Forms & Checklists

Intake, output templates, and quality checklist. File paths are organization-specific
decisions (see [`ADAPT.md`](ADAPT.md)); this file never hardcodes them.

---

## Workspace Intake (the questionnaire for adapting this skill)

Ask as one numbered list and **WAIT** for answers; record the answers wherever your team
keeps these decisions (your design brief, or your forked copy of `SKILL.md`). Ask only
what's missing.

1. **Progress doc filename** — what file records decisions/blockers per area (e.g. a
   per-product progress markdown)?
2. **Work-queue filename** — what file holds the execution queue with item status
   (`in_progress` / `blocked` / `queued`)?
3. **Areas root** — the folder glob where those files live per project or area
   (e.g. one folder per product)?
4. **Team registry** — where the author/team registry lives, and whether members declare
   git aliases or emails for normalization?
5. **Report templates** — folder holding the plain-text and HTML report templates, if any
   (skip to inline generation if none)?
6. **Other tracked areas** — any roots outside the main areas root that also carry progress
   docs (e.g. client engagements, a company-level area)?
7. **Output directory** — where to write the rendered HTML report (default
   `reports/daily/`, gitignored)?
8. **Timezone label** — the timezone to stamp on the report header (e.g. local office
   timezone)?

---

## Terminal Output Structure

Replace the bracketed placeholders with real values from your configured file paths.

```
=== DAILY REPORT — [ORG OR PRODUCT NAME] ===
Date: [YYYY-MM-DD] ([Weekday])
Generated: [YYYY-MM-DD HH:MM] [TZ]

---

## At a Glance

| Metric | Value |
|--------|-------|
| Commits Today | [n] |
| Active Contributors | [n] |
| Projects Touched | [n] |
| Items In Progress | [n] |
| Items Blocked | [n] |

---

## Executive Summary

[2–3 sentences: the day's focus, what shipped, and any concern. Facts only — no spin.
"0 commits today" is a valid summary.]

---

## Activity by Project

### [project-or-area-a] ([n] commits)

| Author | Commit | Message |
|--------|--------|---------|
| [Member Name] | [short-sha] | feat(scope): [message] |
| [Member Name] | [short-sha] | fix(scope): [message] |
...

### [project-or-area-b] ([n] commits)

| Author | Commit | Message |
|--------|--------|---------|
| [Member Name] | [short-sha] | docs: [message] |
...

---

## Activity by Team Member

### [Member Name] ([n] commits)

**Focus Areas:** [project-a], [project-b]

| Type | Count |
|------|-------|
| feat | [n] |
| fix  | [n] |
| docs | [n] |

### [Member Name] ([n] commits)

**Focus Areas:** [project-a]

| Type | Count |
|------|-------|
| fix  | [n] |

---

## Work Queue Status

### Currently In Progress

| ID | Task | Project | Assignee |
|----|------|---------|----------|
| [task-id] | [task title] | [project] | [Member] |
| [task-id] | [task title] | [project] | [Member] |

### Blocked Items ([n])

| ID | Task | Project | Blocker Reason |
|----|------|---------|----------------|
| [task-id] | [task title] | [project] | [reason from the queue item] |

---

## Key Decisions Today

| Decision | Project | Context |
|----------|---------|---------|
| [decision summary] | [project] | [session ref / date] |

---

## Tomorrow's Priorities

1. [Top queued item] — [why it matters / what it unblocks]
2. [Unblock action for a blocked item]
3. [Continue an in-progress item]

---

=== Report saved to: [output-dir]/[YYYY-MM-DD].html ===
```

> Conventional-commit type names (feat, fix, docs, refactor, test, chore) are a universal
> convention — keep them verbatim. Item-ID prefixes, project names, and assignee names all
> come from your queue/registry files, not from this template.

---

## Quality Checklist

Use before sharing the report.

### Data integrity
- [ ] Git log captured with `--since="00:00"` for the correct day
- [ ] All authors resolved to registry names, or explicitly tagged `(external)`
- [ ] Commit counts in "At a Glance" match the per-project/per-member tables
- [ ] Zero-activity days reported honestly ("No commits today")

### Context accuracy
- [ ] Decisions pulled from the progress doc, not invented
- [ ] Blocked items show the real reason from the queue item
- [ ] Tomorrow's priorities drawn from actual queued items, in priority order

### Honesty
- [ ] Executive summary states facts only — no optimistic spin
- [ ] No hallucinated accomplishments, owners, or milestones

### Output
- [ ] HTML rendered to the gitignored output directory (not committed)
- [ ] Metrics cards, team cards, and a blocked-items alert all present
- [ ] Header date, weekday, and timezone correct
