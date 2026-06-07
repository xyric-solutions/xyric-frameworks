---
name: TASK-ASSIGN
parent: EXPERT-15
description: Map tasks to engineer roles with MoSCoW distribution, workload balancing, and skill matching.
version: "1.0"
domain: Task assignment, role mapping, workload distribution
---

# Task Assignment (TASK-ASSIGN)

> Sub-skill of [Task Generator (EXPERT-15)](../SKILL.md)

## Focus Area

Assigns implementation tasks to the correct engineer roles (Architect, Test Engineer,
Backend, Frontend, Fullstack, Reviewer), enforces MoSCoW priority distribution (60/20/20),
and balances workload across the team. Does NOT handle execution ordering or dependency
chains — those belong to TASK-SEQUENCE.

Concrete roles and owners resolve from your team's role registry; gather them via the
parent's Workspace Intake if not yet decided (see `../ADAPT.md`). Story-linking rules come
from your file-naming conventions.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Role Mapping | Match task type (Backend/Frontend/Fullstack/Test/Review) to the correct role |
| MoSCoW Distribution | Enforce ~60% MUST / ~20% SHOULD / ~20% COULD across the task set |
| Workload Balancing | Distribute effort hours evenly; no single role overloaded beyond 60% |
| Skill Matching | Route complex tasks to specialists, simple tasks to generalists |

## Methodology

### Priority Order
1. Map task categories to roles first — ARCH->Architect, TEST->Test Engineer, IMPL by layer, INTG->Reviewer
2. Assign MoSCoW priorities based on acceptance-criteria coverage — critical-path tasks are MUST
3. Balance total effort hours per role — flag imbalances exceeding 60% of total effort
4. Verify every task has exactly one assignee with clear ownership

### Workflow
1. Receive the sequenced task list (from TASK-SEQUENCE or the parent skill)
2. For each task, determine the primary role based on task type and technical domain
3. Assign MoSCoW priority: MUST for tasks blocking acceptance criteria, SHOULD for quality improvements, COULD for polish
4. Calculate the effort distribution per role and validate balance
5. Generate an effort-by-role summary table and flag any overloaded roles

## Key Patterns

**Category-to-Role Matrix**: ARCH tasks always go to the Architect. TEST tasks to the Test
Engineer. IMPL:Backend to the Backend role, IMPL:Frontend to the Frontend role,
IMPL:Fullstack/DevOps to the Fullstack role. INTG review alignment to the Reviewer. Resolve
the concrete owner of each role from your team's role registry.

**MoSCoW Guardrails**: MUST exceeding 70% signals over-scoping — split some MUST items into
SHOULD. COULD exceeding 30% signals scope creep — demote or defer excess items.

**Effort Distribution Rule**: No single role should carry more than 60% of total estimated
hours. If Backend has 80% of the work, consider splitting tasks or reclassifying some as
Fullstack.

**Complexity-Aware Assignment**: XL tasks (8+ hours) should be flagged for splitting. L tasks
go to the specialist role. S/M tasks can go to a generalist (Fullstack) when specialists are
overloaded.

**Sprint-Aware Distribution**: Within a sprint, each engineer should have a mix of MUST and
SHOULD/COULD tasks to maintain momentum when blocked.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Leaving tasks unassigned ("TBD") | Every task needs exactly one owner role |
| All tasks marked MUST | Apply 60/20/20 MoSCoW; demote non-critical tasks |
| One engineer gets 80%+ of effort | Rebalance; split tasks or reclassify domains |
| Assigning Backend tasks to a Frontend specialist | Match the task domain to role expertise strictly |

## Quality Gates

| Gate | Target |
|------|--------|
| MoSCoW distribution | MUST ~60%, SHOULD ~20%, COULD ~20% (warn if MUST >70%) |
| Assignment coverage | 100% of tasks have an assigned role |
| Workload balance | No single role exceeds 60% of total effort hours |
| Effort estimates present | Every task has an hour estimate (S/M/L/XL) |

## Deep Reference

- Parent skill: `../SKILL.md` (full methodology, cross-role integration)
- Reference sections: `../reference.md` → Engineer Roles Reference, Q3 Engineer Assignments
- Checklists: `../forms.md` → Effort by Role, MoSCoW Distribution Validation

## Team Integration

Designed for use in:
- **Sprint Planning teams** — as the assignment specialist ensuring balanced workloads
- Pairs well with: TASK-SEQUENCE (receives ordered tasks, adds role assignments)
