---
name: TASK-SEQUENCE
parent: EXPERT-15
description: Order implementation tasks using TDD phasing (ARCH->TEST->IMPL->INTG) with critical-path and dependency-chain analysis.
version: "1.0"
domain: Task sequencing, dependency mapping, critical path identification
---

# Task Sequencing (TASK-SEQUENCE)

> Sub-skill of [Task Generator (EXPERT-15)](../SKILL.md)

## Focus Area

Determines the correct execution order for implementation tasks using strict TDD phasing
(ARCH->TEST->IMPL->INTG), builds dependency graphs, and identifies the critical path. Does
NOT handle role assignment, workload balancing, or MoSCoW distribution — those belong to
TASK-ASSIGN.

Task and story ID formats follow your file-naming conventions; gather them via the parent's
Workspace Intake if not yet decided (see `../ADAPT.md`).

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| TDD Phasing | Enforce ARCH->TEST->IMPL->INTG ordering across all tasks |
| Dependency Graphs | Map upstream/downstream relationships, detect circular dependencies |
| Critical Path | Identify the longest dependency chain that determines minimum duration |
| Parallel Lanes | Find tasks that can execute concurrently within each phase |

## Methodology

### Priority Order
1. Architecture decisions unblock everything — always Phase 1
2. Tests define contracts before code exists — always Phase 2
3. Implementation makes tests pass — Phase 3, ordered by layer dependencies
4. Integration validates the whole — always the final phase

### Workflow
1. Receive the task list from the parent skill (or tech-spec sections mapped to tasks)
2. Classify each task into a TDD category: ARCH, TEST, IMPL, or INTG
3. Build a dependency table: for each task, identify what it depends on and what it blocks
4. Validate the dependency graph is acyclic — if circular, restructure by extracting a shared foundation
5. Identify the critical path and calculate the minimum duration
6. Mark parallel execution lanes within each phase

## Key Patterns

**Foundation-First**: Database schemas and core models are always ARCH tasks — they unblock
both TEST and IMPL.

**Test-Before-Code**: Every IMPL task must have a corresponding upstream TEST task. If a
test spec does not exist, the IMPL task cannot begin.

**Layer Ordering Within IMPL**: Backend before Frontend when Frontend depends on API
contracts. Fullstack tasks bridge layers and typically come after both Backend and Frontend
foundations exist.

**Integration as Gatekeeper**: INTG tasks depend on ALL related IMPL tasks completing. Never
schedule integration mid-implementation.

**Parallel Lanes**: Independent components (e.g., two unrelated API endpoints) can run in
parallel within the same phase. Identify these to reduce total duration.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Scheduling IMPL before TEST specs exist | Always sequence TEST -> IMPL; tests define the contract |
| Creating circular dependencies between tasks | Extract the shared dependency into a new foundation task |
| Treating all tasks as sequential | Identify parallel lanes within phases to optimize throughput |
| Skipping the ARCH phase for "simple" features | Even simple features need pattern decisions documented |

## Quality Gates

| Gate | Target |
|------|--------|
| Dependency graph is acyclic | 100% — no circular dependencies |
| TDD phase ordering respected | Every TEST before its IMPL, every ARCH before its TEST |
| Critical path identified | A single clear path with a duration estimate |
| Parallel lanes documented | All independent task groups identified |

## Deep Reference

- Parent skill: `../SKILL.md` (full methodology, cross-role integration)
- Reference sections: `../reference.md` → Phase 2: Task Generation, Phase 3: Validation
- Checklists: `../forms.md` → Dependency Graph, Structure Checks

## Team Integration

Designed for use in:
- **Sprint Planning teams** — as the sequencing specialist ensuring TDD ordering
- Pairs well with: TASK-ASSIGN (hands off ordered tasks for role mapping)
