# Weekly PPP Generator — Forms & Checklists

Loaded on demand for intake, output templates, and validation criteria. Repo paths, file
names, and team aliases are organization-specific (see [`ADAPT.md`](ADAPT.md)); this file
never hardcodes them.

---

## Workspace Intake (the questionnaire for adapting this skill)

This is the questionnaire to gather the organization-specific decisions. Ask as one
numbered list and **WAIT** for answers; then record them wherever your team keeps these
decisions (e.g. your design/work brief or your forked `SKILL.md`). Ask only what's missing.

1. **Units root** — where do the per-unit folders live (the path that holds each
   product/client/team folder)?
2. **Progress doc name** — the file each unit uses for milestones and decisions (e.g. a
   progress doc)?
3. **Work-queue doc name** — the file each unit uses for the execution queue / blockers?
4. **Team registry** — the file listing team members, their git author aliases, and unit
   assignments?
5. **Template locations** — where do the weekly-PPP plain-text template and the HTML
   dashboard template live?
6. **Naming conventions** — how are work-item IDs formatted (e.g. a prefix + number)?
7. **Report output dir** — where should generated weekly reports be written? (default: a
   `reports/weekly/` folder)
8. **Timezone & week start** — for the "Generated" timestamp and the Mon–Fri activity
   chart (default: ISO week, Monday start).

---

## Terminal Output Structure

A complete reference layout. Names, units, IDs, and dates are illustrative — fill from your
organization's decisions and the repo at run time. The section structure is fixed; the
content is not.

```
=== WEEKLY PPP ===
Week: Dec 16–20, 2025 (2025-W51)
Generated: 2025-12-20 18:00

---

## Week at a Glance

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Total Commits | 45 | 38 | +18% |
| Contributors | 4 | 3 | +1 |
| Milestones Completed | 2 | 1 | +1 |
| Items Completed | 8 | 5 | +60% |
| Items Blocked | 2 | 1 | +1 |

---

## Executive Summary

This week marked significant progress on the platform unit with 45 commits
across 4 contributors. Key accomplishments include completing the
onboarding-epic stories and setting up the development environment. The team
faces two blockers related to cloud infrastructure, but momentum remains strong.
Next week's focus will be completing the epic review and unblocking cloud setup.

---

## PROGRESS (What We Accomplished)

### By Unit

#### platform
**Commits:** 32 | **Contributors:** A, B, C

**Key Accomplishments:**
- Completed onboarding-epic stories (18 stories)
- Set up development environment with hot reload
- Migrated the progress doc to the milestone format

**Milestones Completed:**
- M-004: Development Environment Setup (Dec 18)

**Notable Commits:**
- feat(auth): implement JWT refresh token flow
- feat(profile): add settings panel component

#### data-product
**Commits:** 13 | **Contributors:** A, D

**Key Accomplishments:**
- Released a version with monitoring and caching
- Implemented progress streaming for long operations

**Milestones Completed:**
- M-004: Monitoring, Caching & Progress (Dec 17)

---

### By Team Member

| Member | Commits | Units | Focus Area |
|--------|---------|-------|------------|
| Member A | 28 | platform, data | Architecture, auth |
| Member B | 8 | platform | UI development |
| Member C | 5 | platform | Code review |
| Member D | 4 | data-product | Data analytics |

**Member A** led development efforts with 28 commits, focusing on
authentication architecture for the platform and monitoring for the data product.

---

### Completed Work Items

| ID | Task | Unit | Completed |
|----|------|------|-----------|
| TASK-003 | Story Breakdown | platform | Dec 17 |
| TASK-004 | Version Release | data-product | Dec 18 |

---

## PROBLEMS (Challenges & Blockers)

### Currently Blocked (2)

#### [TASK-007] Cloud Provider Setup
- **Unit:** ops-product
- **Blocked by:** Awaiting cloud-credit approval
- **Days blocked:** 5
- **Impact:** Blocks deployment pipeline setup
- **Resolution path:** Escalate to finance for credit approval

#### [TASK-002] Roles & Responsibilities Doc
- **Unit:** org
- **Blocked by:** Waiting on TASK-001 (Org Structure)
- **Days blocked:** 3
- **Impact:** Delays governance documentation
- **Resolution path:** Complete TASK-001 first

---

### Resolved This Week

| Item | Was Blocked By | Resolution |
|------|----------------|------------|
| TASK-005 | Design incomplete | Design completed Dec 16 |

---

### Risk Radar

| Risk | Indicator | Recommendation |
|------|-----------|----------------|
| Epic stalled | In progress 14+ days | Review scope, consider splitting |
| No org-unit commits | 0 commits this week | Schedule governance session |
| Cloud blocker growing | 5 days blocked | Escalate cloud credits |

---

## PLANS (Next Week's Focus)

### Priority Queue

| Priority | ID | Task | Unit | Assignee |
|----------|-----|------|------|----------|
| P0 | TASK-001 | Complete Epic Review | platform | A |
| P0 | TASK-007 | Cloud Provider Setup | ops-product | C |
| P1 | TASK-002 | Story Breakdown | platform | A |
| P1 | TASK-005 | Core App UI | platform | B |
| P2 | TASK-008 | Batch Upload Feature | data-product | D |

---

### Team Focus

| Member | Primary Focus | Key Items |
|--------|---------------|-----------|
| A | platform stories | TASK-001, TASK-002 |
| B | platform development | TASK-005 |
| C | infrastructure | TASK-007 |
| D | data-product features | TASK-008 |

---

### Dependencies to Resolve

| Blocker | Owner | Needed By | Impact |
|---------|-------|-----------|--------|
| Cloud credits | Finance | Dec 22 | Unblocks TASK-007, deployment |
| Epic completion | A | Dec 23 | Unblocks TASK-002 |

---

### Milestones to Target

| Unit | Milestone | Target | Status |
|------|-----------|--------|--------|
| platform | M-005: Epic Complete | Dec 23 | 60% |
| ops-product | M-001: Cloud Setup | Dec 27 | Blocked |

---

## Appendix: Full Commit Log

<details>
<summary>All 45 commits this week</summary>

| Date | Author | Unit | Message |
|------|--------|------|---------|
| Dec 20 | A | platform | feat(auth): add password reset |
| Dec 20 | B | platform | fix(ui): button alignment |
...

</details>

---

=== Report saved to: <weekly report dir>/2025-W51.html ===
```

---

## Pre-Generation Checklist

Run before generating the report.

- [ ] Organization-specific decisions resolved (paths, file names, team registry, template locations)
- [ ] Week range determined correctly (Fri → current Mon–Fri; Mon → previous Mon–Fri)
- [ ] Git log pulled for the full 7-day window
- [ ] Authors normalized against your team/author-alias registry
- [ ] Progress docs and work-queue docs located under your units root
- [ ] Previous week's report located (or "first report" noted)

## Quality Checklist

Run before publishing the report.

- [ ] All three PPP sections present with substantive content
- [ ] Week-over-week deltas shown when previous data exists
- [ ] Risk radar applies the detection rules mechanically (not blanket "On Track")
- [ ] Every blocked item shows duration, impact, and a resolution path
- [ ] Plans drawn from the actual work-queue docs, not invented
- [ ] Executive summary matches the data — no hallucinated wins
- [ ] HTML dashboard renders: metrics cards, activity chart, team cards, blocked alert
- [ ] Report written to the configured weekly output directory as `YYYY-Www.html`
