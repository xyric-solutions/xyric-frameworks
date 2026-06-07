---
name: Task Generator
description: Break a technical specification into all implementation tasks with TDD ordering (ARCH->TEST->IMPL->INTG), MoSCoW priority distribution, dependency mapping, and engineer-role assignment. Use when turning an approved tech spec into an executable, assigned task breakdown; do not use for writing the spec itself or for ad-hoc to-do lists with no spec. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Task Generator

Transform an approved technical specification into ALL the implementation tasks needed to
build a story — each task small enough for one work session, with clear acceptance
criteria, an explicit dependency chain, a MoSCoW priority, and an assigned engineer role.
This skill is the **method**. The specifics it operates on — the team's actual engineer
roles, file-naming conventions, and document locations — are decided per organization. See
[`ADAPT.md`](ADAPT.md) for what to decide before using this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a clearly-labeled
**GENERIC DRAFT** using neutral PLACEHOLDER values (generic role names like `Architect` /
`Test Engineer` / `Backend`, a `<task-id>` token, and a `<task-file>` path) and list what is
missing. Never invent real team-member names, a house file-naming scheme, or a story-linking
convention.

**Core philosophy**: Tasks are the atomic units of engineering work. A task is small
enough to complete in one session, traces back to a spec section and an acceptance
criterion, and can be handed to exactly one engineer role.

Resolve every role from your team's role registry, every file path from your products
root and template locations, and every ID format and linking rule from your file-naming
conventions — never hardcode them.

## When to Activate

### Trigger Phrases
- "Generate tasks from the tech spec"
- "Create tasks for story [ID]"
- "Break down this spec into tasks"
- "Task breakdown for [story]"
- "Implementation tasks from spec"

### Workflow Position

```
Story Generator -> Story Spec Generator -> Task Generator -> Task Spec / Implementation Guide
                                           ^^^^^^^^^^^^^^^^
                                           YOU ARE HERE
```

The technical specification is the **upstream** input; a per-task implementation guide is
the **downstream** consumer. Names of those upstream/downstream skills come from your own
pipeline.

## Required Context Sources

Resolve each path from your workspace conventions; the IDs and filenames follow your
file-naming conventions.

| Priority | Source | Where it lives | Extract |
|----------|--------|----------------|---------|
| Critical | Technical Spec | your spec template location | All sections — primary input |
| High | Story file | your products root (stories) | Story context, acceptance criteria |
| Medium | Epic / feature PRD | your products root (epic PRDs) | Feature context |
| Medium | Planning / progress file | your planning/progress file | Team and milestone context |
| Low | Existing task files | your task template location | Reusable task patterns |

**Key principle:** the technical specification is the PRIMARY input. Every task maps to a
spec section and to one or more story acceptance criteria.

## Task Categories & TDD Ordering (MANDATORY)

Test-Driven Development order is universal and not org-specific — tests are written before
the implementation they validate.

| Category | Code | Description | Role (from your role registry) | Phase |
|----------|------|-------------|------------------------------|-------|
| **Architecture** | ARCH | Architecture / pattern decisions, ADRs | Architect | 1st |
| **Test** | TEST | Test specifications (before code) | Test Engineer | 2nd |
| **Implementation** | IMPL | Implementation code | Backend / Frontend / Fullstack | 3rd |
| **Integration** | INTG | Integration & code review | Reviewer | 4th |

```
PHASE 1: ARCH  -> Architecture decisions, ADR creation
PHASE 2: TEST  -> Test specs written BEFORE implementation (TDD)
PHASE 3: IMPL  -> Code written to make the TEST specs pass
PHASE 4: INTG  -> Integration testing and code review
```

### Implementation Types (within IMPL)

| Type | Typical role (resolve from your role registry) |
|------|---------------------------------------------|
| Backend | Backend engineer |
| Frontend | Frontend engineer |
| Fullstack | Fullstack engineer |
| DevOps | Fullstack / DevOps engineer |

## Task Complexity Sizing

Generic sizing — a task should be completable in roughly one work session.

| Size | Effort | Typical duration | Example |
|------|--------|------------------|---------|
| **S** | 1-2 hours | Half day | Add validation, fix a bug |
| **M** | 2-4 hours | Full day | New component, simple API |
| **L** | 4-8 hours | 1-2 days | Complex feature, integration |
| **XL** | 8+ hours | 2-4 days | Major feature (consider splitting) |

## MoSCoW Priority Distribution (MANDATORY)

MoSCoW is a universal prioritization method.

| Priority | Target | Description |
|----------|--------|-------------|
| **MUST** | ~60% | Critical path; the story fails without these |
| **SHOULD** | ~20% | Important, but the story functions without them |
| **COULD** | ~20% | Nice-to-have; quality improvements |

**Warning:** MUST > 70% indicates over-scoping. COULD > 30% indicates scope creep.

## Four-Phase Workflow (Overview)

### Phase 0: Research (automated)
1. Read the technical specification for the target story.
2. Extract API contracts, data models, UI components, integrations, and testing strategy.
3. Map spec sections to task categories.
4. OUTPUT: Spec Task Analysis (~250 words).

### Phase 1: Analysis & Questions
5. Present the spec analysis to the user.
6. Ask 4 tailored questions (Structure x2, Assignment x1, Priority x1).
7. **WAIT FOR USER INPUT** (blocking).

### Phase 2: Generation (TDD sequential)
8. Apply the user's decisions; generate tasks in STRICT TDD order:
   ARCH first → TEST second → IMPL third → INTG last.
9. Validate the MoSCoW distribution (60/20/20).
10. OUTPUT: TDD-ordered task breakdown + dependency graph.

### Phase 3: Validation (blocking)
11. Check spec coverage, acceptance-criteria coverage, TDD order, and MoSCoW balance.
12. Check dependencies (no cycles) and assignments (every task owned).
13. IF ANY CHECK FAILS → return to Phase 2, fix, re-validate.

### Phase 4: Output & Tracking
14. Write the task breakdown to the task file location and name from your template
    locations + file-naming conventions.
15. Link each task back to its story per your file-naming conventions (so no task is
    orphaned work), and update your planning/progress file and execution-queue file.

> Step-by-step instructions, question frameworks, and generation patterns: [`reference.md`](reference.md).
> Output templates and quality checklists: [`forms.md`](forms.md).

## Anti-Patterns

1. **Generate without a tech spec** — always read the spec first; tasks must map to spec sections.
2. **Create oversized tasks** — split XL tasks; each should be completable in a day.
3. **Skip dependencies** — make every dependency explicit; the execution order must be clear.
4. **Leave tasks unassigned** — every task needs one owner role from your role registry.
5. **Forget testing tasks** — testing is not optional; TEST tasks are always in the breakdown.
6. **Miss acceptance criteria** — every story AC must map to a task; 100% coverage required.
7. **Orphan a task** — every task links back to its story per your file-naming conventions.

## Output

- **File:** the task-breakdown file, at the path and name from your template locations
  + file-naming conventions.
- **Typical length:** 300-500 lines per story.
- **Quality bar:** 100% spec coverage, TDD ordering enforced, every task linked to its story.
- **Pipeline hook:** a `TASK_SPEC_READY: <task-id>` marker per task for the downstream guide.

## Sub-Skills

Focused sub-skills for targeted activation and team compositions:

| Sub-Skill | Focus |
|-----------|-------|
| [TASK-SEQUENCE](sub-skills/TASK-SEQUENCE.md) | TDD ordering, critical path, dependency chains |
| [TASK-ASSIGN](sub-skills/TASK-ASSIGN.md) | Role mapping, MoSCoW distribution, workload balancing |

Use the parent skill for full-scope work; use a sub-skill for focused team compositions.

> All roles, paths, and naming rules are decided per organization (see [`ADAPT.md`](ADAPT.md)).
> This skill stays portable across organizations — only those values change.
>
> *4-phase tech spec → TDD-ordered task breakdown with blocking validation |
> TDD: ARCH → TEST → IMPL → INTG | MoSCoW: 60/20/20*
