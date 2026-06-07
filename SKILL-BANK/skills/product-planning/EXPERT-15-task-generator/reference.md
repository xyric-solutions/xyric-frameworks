# Task Generator — Reference

Deep patterns, step-by-step instructions, and examples. Roles come from your team's role
registry; file paths from your products root / template locations; ID and naming rules from
your file-naming conventions (see [`ADAPT.md`](ADAPT.md)). The TDD and MoSCoW methodology
below is universal.

---

## Phase 0: Research & Context Gathering (detailed)

### Step 1: Read the technical specification

Locate the spec at the spec path from your template locations, named per your file-naming
conventions.

### Step 2: Extract spec components

Parse each spec section:
- API Contracts → Backend tasks
- Data Models → Database / Backend tasks
- UI Components → Frontend tasks
- Integration Points → Integration / Fullstack tasks
- Testing Strategy → Test tasks
- Security Requirements → Security tasks

### Step 3: Map to tasks

| Spec Section | Components | Task Type |
|--------------|------------|-----------|
| API Contracts | [Count] endpoints | Backend |
| Data Models | [Count] entities | Backend |
| UI Components | [Count] components | Frontend |
| Integration | [Count] integrations | Fullstack |
| Testing | [Layers] | Mixed |

### Step 4: Create the Spec Task Analysis

```markdown
## Spec Task Analysis: Story <story-id>

### Story Summary
**ID:** <story-id>
**Title:** [Title]
**Spec Location:** <spec-file>

### Spec Components

**API Contracts:**
- [Count] endpoints to implement
- [List of endpoints]

**Data Models:**
- [Count] entities
- [Count] schema changes

**UI Components:**
- [Count] components
- [List of components]

**Integrations:**
- [Count] internal integrations
- [Count] external integrations

**Testing:**
- Unit tests: [Scope]
- Integration tests: [Scope]
- E2E tests: [Scope]

### Proposed Task Breakdown

| Type | Count | Assignee (role) |
|------|-------|-----------------|
| Backend | [X] | Backend |
| Frontend | [X] | Frontend |
| Fullstack | [X] | Fullstack |
| Testing | [X] | Test Engineer |
| **Total** | **[X]** | |

### Acceptance Criteria to Cover
- AC1: [Criterion] -> [Tasks]
- AC2: [Criterion] -> [Tasks]
```

---

## Phase 1: Questions & User Input (detailed)

### Q1. Task Granularity (Structure)

```markdown
Based on the spec, I propose [X] tasks:

| Category | Tasks | Example |
|----------|-------|---------|
| Backend | [X] | Create API endpoint for [resource] |
| Frontend | [X] | Build [Component] component |
| Integration | [X] | Wire [frontend] to [API] |
| Testing | [X] | Write unit tests for [layer] |

Questions:
a) Is this granularity appropriate?
   - Too granular (combine some)?
   - Too coarse (split some)?
   - Just right
b) Any areas needing more detail?
c) Any areas that can be simplified?
```

### Q2. Task Dependencies (Structure)

```markdown
Proposed execution order:

**Phase 1 (Foundation):**
- T1: [Database/Schema tasks]
- T2: [Core API tasks]

**Phase 2 (Features):**
- T3-T5: [Remaining API tasks]
- T6-T8: [UI component tasks]

**Phase 3 (Integration):**
- T9-T10: [Integration tasks]

**Phase 4 (Quality):**
- T11-T13: [Testing tasks]

Questions:
a) Does this execution order make sense?
b) Any tasks that can run in parallel?
c) Any dependencies I missed?
```

### Q3. Engineer Assignments (Assignment)

Roles resolve from your team's role registry.

```markdown
Proposed assignments:

| Role | Tasks | Effort |
|------|-------|--------|
| Backend | T1, T2, T3, T11 | [X] hours |
| Frontend | T6, T7, T8, T12 | [X] hours |
| Fullstack | T4, T5, T9, T10, T13 | [X] hours |

Questions:
a) Are these assignments appropriate?
b) Any tasks needing a different engineer?
c) Is the workload balance acceptable?
```

### Q4. Priority & Scheduling (Priority)

```markdown
Questions:
a) Task priorities - any critical-path items?
   - P0 (blocking): [Suggested]
   - P1 (high): [Suggested]
   - P2 (medium): [Suggested]
b) Sprint allocation:
   - Sprint 1: [Tasks]
   - Sprint 2: [Tasks]
c) Any time-sensitive tasks?
d) Definition of done for this story?
```

---

## Phase 2: Task Generation (detailed)

### Step 1: Apply user decisions

| Decision | Impact on tasks |
|----------|-----------------|
| Granularity | Task count and scope |
| Dependencies | Execution order |
| Assignments | Roles (from your role registry) |
| Priorities | MoSCoW distribution |

### Step 2: Generate tasks in TDD order (MANDATORY)

```
1. ARCH Tasks (Architecture Decisions)
   +-- Invoke: Architect role
   +-- ADR creation for significant decisions
   +-- Design patterns to apply

2. TEST Tasks (Test Specifications)
   +-- Invoke: Test Engineer role
   +-- Unit test specifications
   +-- Integration test specifications
   +-- E2E test specifications

3. IMPL Tasks (Implementation)
   +-- IMPL:Backend   --> Backend role
   +-- IMPL:Frontend  --> Frontend role
   +-- IMPL:Fullstack --> Fullstack role

4. INTG Tasks (Integration & Review)
   +-- Integration testing
   +-- Review criteria alignment
   +-- Invoke: Reviewer role
```

### Step 3: For each task, define sequentially

1. Task category (ARCH/TEST/IMPL/INTG)
2. Task title and description
3. Assign to the correct role (from your role registry)
4. Set MoSCoW priority
5. Set complexity
6. Write acceptance criteria
7. Document dependencies
8. Add technical notes

### Step 4: Build the dependency graph

```
T1 (Database) ------+-----> T3 (API 1) -----+-----> T6 (UI 1) ----+
                    |                       |                      |
T2 (Schema) --------+                       +-----> T7 (UI 2) -----+--> T9 (Integration)
                    |                       |                      |
                    +-----> T4 (API 2) -----+-----> T8 (UI 3) ----+
                                |
                                +-----> T5 (API 3) --> T10 (E2E Tests)
```

---

## Phase 3: Validation (detailed)

### Critical checks (block if fail)

| Check | Criteria | Action if fail |
|-------|----------|----------------|
| Spec Coverage | All spec sections have tasks | Add missing tasks |
| Criteria Coverage | All acceptance criteria addressed | Map to tasks |
| TDD Order | ARCH → TEST → IMPL → INTG sequence | Reorder tasks |
| MoSCoW Distribution | ~60% MUST / ~20% SHOULD / ~20% COULD | Adjust priorities |
| Role Assignment | Correct role for each category | Fix assignments |
| Story Linking | Every task links to its story (no orphans) | Add the link per naming conventions |
| No Circular Dependencies | Dependency graph is acyclic | Resolve cycles |

### Quality checks (warning; block if >3 fail)

| Check | Criteria | Action if fail |
|-------|----------|----------------|
| Task Sizing | No XL tasks without justification | Consider splitting |
| Acceptance Criteria | All tasks have 2+ criteria | Add criteria |
| Technical Notes | Complex tasks have hints | Add notes |
| Effort Estimates | All tasks have estimates | Add estimates |
| Role Invocation | Complex tasks reference a role | Add invocation |

---

## Engineer Roles Reference

Resolve concrete roles/owners from your team's role registry. The category-to-role mapping
is the generic default:

| Role | Expertise | Task types |
|------|-----------|------------|
| **Architect** | Architecture | ARCH tasks, ADR creation |
| **Test Engineer** | Testing | TEST tasks, TDD guidance |
| **Backend** | Backend | IMPL:Backend, INTG:Backend |
| **Frontend** | Frontend | IMPL:Frontend, INTG:Frontend |
| **Fullstack** | Fullstack / DevOps | IMPL:Fullstack, IMPL:DevOps, INTG:E2E |
| **Reviewer** | Code review | INTG review alignment |

---

## Integration Patterns

### Upstream: the Story Spec Generator
- Input: a technical specification with API contracts, data models, and UI components.

### Role invocations during task generation

| Category | Role (from your role registry) | Purpose |
|----------|---------------------------|---------|
| ARCH | Architect | Architecture decisions, ADR creation |
| TEST | Test Engineer | Test specifications, TDD guidance |
| IMPL | Backend / Frontend / Fullstack | Implementation by layer |
| INTG | Reviewer | Review criteria alignment |

### Downstream: the Implementation-Guide generator
- Output: a task list for high-level implementation guides.
- Handoff marker: `TASK_SPEC_READY: <task-id>`.
- Each task gets high-level guidance (no code).

### Invocation flow

```
Task Generator produces the task breakdown
    |
    +-- ARCH tasks --> invoke Architect role
    |                  Output: ADR, architecture decisions
    |
    +-- TEST tasks --> invoke Test Engineer role
    |                  Output: test specifications
    |
    +-- IMPL tasks --> route to Backend / Frontend / Fullstack
    |                  Handoff to the implementation-guide generator
    |
    +-- INTG tasks --> invoke Reviewer role
                       Output: review alignment
```

---

*Reference | Task Generator | All roles, paths, and naming rules are decided per organization (see `ADAPT.md`).*
