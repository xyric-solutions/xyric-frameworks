# Task Generator — Forms & Checklists

Output templates, quality checklists, and validation criteria for the Task Generator. The
team roles, file-naming scheme, and document paths are decided per organization (see
[`ADAPT.md`](ADAPT.md)); this file never hardcodes them. Bracketed `[tokens]` are fill-ins;
`<task-id>`, `<story-id>`, and `<task-file>` follow your file-naming conventions.

---

## Workspace Intake (the questionnaire for adapting this skill)

Ask as one numbered list and **WAIT** for answers; then record the decisions wherever your
team keeps them (your design brief, or baked into your forked copy of this skill). Ask only
what's missing.

1. **Engineer roles** — who/what owns each task category? (Architect, Test Engineer,
   Backend, Frontend, Fullstack, Reviewer.) Names or role labels from your team's role
   registry.
2. **Task file naming** — how are task / task-breakdown files named, and where do task IDs
   come from?
3. **Story & spec naming** — how are story files and spec files named, and what is the
   story/spec ID format?
4. **Story linking rule** — how does a task link back to its parent story so it isn't
   orphaned (e.g. a story-ID field in the task)?
5. **Document locations** — where do stories, specs, and task files live? (products root
   and template locations.)
6. **Tracking files** — which files record planning progress and the execution queue?

---

## Task Breakdown Document Template

Resolve role names from your team's role registry; IDs and the file path follow your
file-naming conventions + template locations.

```markdown
# Task Breakdown: Story <story-id>
**[Story Title]**

---

## DOCUMENT INFORMATION

| Attribute | Value |
|-----------|-------|
| **Story ID** | <story-id> |
| **Story Title** | [Title] |
| **Tech Spec** | <spec-file> |
| **Version** | 1.0 |
| **Status** | Draft / Review / Approved |
| **Author** | [Name] |
| **Last Updated** | [Date] |

---

## TASK SUMMARY

### Overview Statistics

| Metric | Value |
|--------|-------|
| Total Tasks | [X] |
| Backend Tasks | [X] |
| Frontend Tasks | [X] |
| Fullstack Tasks | [X] |
| Testing Tasks | [X] |
| Total Estimated Effort | [X] hours |

### Task Index (TDD Ordered)

| Task | Category | Title | Type | Assignee (role) | MoSCoW | Complexity | Est. |
|------|----------|-------|------|------------------|--------|------------|------|
| T1 | ARCH | [Architecture Decision] | Architecture | Architect | MUST | M | 2h |
| T2 | TEST | [Unit Test Spec] | Test | Test Engineer | MUST | M | 4h |
| T3 | TEST | [Integration Test Spec] | Test | Test Engineer | MUST | M | 3h |
| T4 | IMPL | [Backend Implementation] | Backend | Backend | MUST | L | 6h |
| T5 | IMPL | [Frontend Implementation] | Frontend | Frontend | MUST | M | 4h |
| T6 | IMPL | [API Integration] | Fullstack | Fullstack | SHOULD | M | 4h |
| T7 | INTG | [E2E Integration] | Integration | Fullstack | SHOULD | S | 2h |
| T8 | INTG | [Code Review Alignment] | Review | Reviewer | COULD | S | 1h |

### Effort by Role

| Role (from your role registry) | Tasks | Total Effort |
|---------------------------|-------|--------------|
| Architect | T1 | [X] hours |
| Test Engineer | T2, T3 | [X] hours |
| Backend | T4 | [X] hours |
| Frontend | T5 | [X] hours |
| Fullstack | T6, T7 | [X] hours |
| Reviewer | T8 | [X] hours |
| **Total** | **[X] tasks** | **[X] hours** |

### MoSCoW Distribution

| Priority | Count | Percentage | Target | Status |
|----------|-------|------------|--------|--------|
| MUST | [X] | [Y]% | ~60% | [check] |
| SHOULD | [X] | [Y]% | ~20% | [check] |
| COULD | [X] | [Y]% | ~20% | [check] |

### TDD Category Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| ARCH | [X] | [Y]% |
| TEST | [X] | [Y]% |
| IMPL | [X] | [Y]% |
| INTG | [X] | [Y]% |

---

## DEPENDENCY GRAPH

### Dependency Table

| Task | Depends On | Blocks |
|------|------------|--------|
| T1 | None | T2, T3 |
| T2 | T1 | T4 |
| T3 | T1 | T4 |
| T4 | T2, T3 | T5 |
| T5 | T4 | None |

### Critical Path
```
T1 --> T2 --> T4 --> T5
```
**Critical Path Duration:** [X] hours

---

## TASK DETAILS

### T1: [Architecture Decision - Title]

**Category:** ARCH
**Type:** Architecture
**Assignee:** Architect (from your role registry)
**MoSCoW:** MUST
**Priority:** P0
**Complexity:** M
**Estimated Effort:** 2 hours

#### Description
[2-3 sentences describing the architecture decision needed]

#### Decision Points
- [ ] [Decision 1]
- [ ] [Decision 2]

#### Acceptance Criteria
- [ ] ADR document created (if significant)
- [ ] Pattern selection documented
- [ ] Rationale captured

#### Skill / Role Invocation
- **Invoke:** the Architect role for the architecture decision
- **Output:** ADR document or decision record

#### Dependencies
- **Upstream:** None (foundation task)
- **Downstream:** TEST tasks depend on this

#### Definition of Done
- [ ] Decision documented
- [ ] Rationale clear
- [ ] Downstream tasks unblocked

<!-- TASK_SPEC_READY: T1 -->

---

### T2: [Test Specification - Title]

**Category:** TEST
**Type:** Test
**Assignee:** Test Engineer (from your role registry)
**MoSCoW:** MUST
**Priority:** P0
**Complexity:** M
**Estimated Effort:** 4 hours

#### Description
[2-3 sentences describing the test specifications needed. Tests are written BEFORE implementation (TDD).]

#### Test Coverage Required
- [ ] Unit tests for [components]
- [ ] Integration tests for [integrations]
- [ ] Edge cases covered

#### Acceptance Criteria
- [ ] Test specification complete
- [ ] Expected behavior documented
- [ ] Test data defined

#### Skill / Role Invocation
- **Invoke:** the Test Engineer role for the test specification

#### Dependencies
- **Upstream:** T1 (ARCH)
- **Downstream:** IMPL tasks implement to pass these tests

#### Definition of Done
- [ ] Test specification documented
- [ ] Expected outcomes defined
- [ ] Ready for IMPL phase

<!-- TASK_SPEC_READY: T2 -->

---

### T4: [Implementation - Title]

**Category:** IMPL
**Type:** Backend
**Assignee:** Backend engineer (from your role registry)
**MoSCoW:** MUST
**Priority:** P1
**Complexity:** L
**Estimated Effort:** 6 hours

#### Description
[2-3 sentences describing what needs to be implemented]

#### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] All TEST spec tests pass

#### Technical Notes
- Reference: Tech Spec Section [X]
- Architecture decision: T1
- Tests to pass: T2

#### Skill / Role Invocation
- **Invoke:** the Backend engineer role for implementation
- **Handoff:** the downstream implementation-guide skill

#### Dependencies
- **Upstream:** T1 (ARCH), T2 (TEST)
- **Downstream:** T7 (INTG)

#### Definition of Done
- [ ] Code complete and committed
- [ ] All tests from T2 passing
- [ ] Ready for integration

<!-- TASK_SPEC_READY: T4 -->

---

### T7: [Integration - Title]

**Category:** INTG
**Type:** Integration
**Assignee:** Fullstack engineer (from your role registry)
**MoSCoW:** SHOULD
**Priority:** P2
**Complexity:** M
**Estimated Effort:** 4 hours

#### Description
[2-3 sentences describing integration work]

#### Acceptance Criteria
- [ ] All IMPL tasks integrated
- [ ] E2E tests passing
- [ ] No regression in existing functionality

#### Integration Points
- [ ] [Component A] <-> [Component B]
- [ ] [API] <-> [Frontend]

#### Skill / Role Invocation
- **Invoke:** the Reviewer role for review alignment

#### Dependencies
- **Upstream:** All IMPL tasks
- **Downstream:** None (final integration)

#### Definition of Done
- [ ] All components integrated
- [ ] E2E tests passing
- [ ] Ready for code review

<!-- TASK_SPEC_READY: T7 -->

---

[Continue for all tasks in TDD order: ARCH -> TEST -> IMPL -> INTG]

---

## SPRINT ALLOCATION

| Sprint | Tasks | Focus | Total Effort |
|--------|-------|-------|--------------|
| Sprint 1 | T1, T2, T3 | Foundation + Core | [X] hours |
| Sprint 2 | T4, T5, T6 | Integration + Testing | [X] hours |

---

## SPEC COVERAGE MATRIX

| Spec Section | Component | Task(s) | Status |
|--------------|-----------|---------|--------|
| API Contracts | POST /resource | T1 | [check] |
| Data Models | Entity | T1 | [check] |
| UI Components | ComponentA | T3 | [check] |
| Integration | API -> UI | T5 | [check] |
| Testing | Unit tests | T6 | [check] |
| **Coverage** | | | **100%** |

### Acceptance Criteria -> Task Mapping

| Story AC | Description | Task(s) | Status |
|----------|-------------|---------|--------|
| AC1 | [Criterion 1] | T1, T3 | [check] |
| AC2 | [Criterion 2] | T2, T4 | [check] |
| **Coverage** | | | **100%** |

---

## RISK ASSESSMENT

| Risk | Impact | Mitigation | Owner (role) |
|------|--------|------------|--------------|
| [Risk 1] | [Impact] | [Mitigation] | Backend |
| [Risk 2] | [Impact] | [Mitigation] | Frontend |

---

## DOCUMENT GOVERNANCE

### Related Documents
| Document | Location (from your workspace conventions) | Status |
|----------|------------------------------|--------|
| Story | story file (products root) | Approved |
| Tech Spec | spec file (template location) | Approved |
| Task Specs | task-spec location (template location) | [Status] |

### Completion Tracking
| Task | Status | Completed By | Date |
|------|--------|--------------|------|
| T1 | Not Started | - | - |
| T2 | Not Started | - | - |

---

*Task Breakdown v1.0 | Story <story-id> | [Date]*

<!-- TASKS_COMPLETE: <story-id> -->
```

---

## Quality Checklist

### Coverage Checks
- [ ] All spec sections have tasks
- [ ] All acceptance criteria addressed
- [ ] All APIs have implementation tasks
- [ ] All UI components have tasks
- [ ] Testing strategy has tasks

### Task Quality Checks
- [ ] Every task has a description
- [ ] Every task has acceptance criteria (2+)
- [ ] Every task has an assignee role (from your role registry)
- [ ] Every task has an estimate
- [ ] Every task has dependencies documented
- [ ] Every task links back to its story per your file-naming conventions (no orphans)

### Structure Checks
- [ ] Task index table complete
- [ ] Dependency graph present
- [ ] Sprint allocation suggested
- [ ] Coverage matrix complete
- [ ] No circular dependencies

### MoSCoW Distribution Validation

| Priority | Count | Percentage | Target | Status |
|----------|-------|------------|--------|--------|
| MUST | [X] | [Y]% | ~60% | [check] |
| SHOULD | [X] | [Y]% | ~20% | [check] |
| COULD | [X] | [Y]% | ~20% | [check] |

WARNING: MUST > 70% indicates over-scoping
WARNING: COULD > 30% indicates scope creep

---

## Activation Checklist

When this skill is activated:

**Phase 0: Research**
1. [ ] Read your workspace conventions (roles, naming, paths, tracking files)
2. [ ] Identify the target story's tech spec
3. [ ] Read the technical specification
4. [ ] Extract all spec components
5. [ ] Generate the Spec Task Analysis (~250 words)

**Phase 1: Analysis**
6. [ ] Present the analysis to the user
7. [ ] Ask 4 tailored questions
8. [ ] **WAIT for user responses**
9. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
10. [ ] Apply user decisions to the task structure
11. [ ] Generate all tasks sequentially in TDD order
12. [ ] Build the dependency graph
13. [ ] Create the coverage matrix

**Phase 3: Validation (Blocking)**
14. [ ] Verify all spec sections covered
15. [ ] Verify all acceptance criteria addressed
16. [ ] Verify no circular dependencies
17. [ ] If fails → return to Phase 2 and fix

**Phase 4: Output**
18. [ ] Write to the task-file location/name from your template locations + file-naming conventions
19. [ ] Link each task to its story; update your planning/progress file and execution-queue file
20. [ ] Include pipeline hooks for the downstream guide
21. [ ] Present the completion summary

---

*Forms | Task Generator*
