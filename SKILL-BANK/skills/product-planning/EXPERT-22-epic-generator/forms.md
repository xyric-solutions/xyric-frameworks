# Epic Generator — Forms & Templates

Output templates, quality checklists, activation checklists, and validation criteria.
Repository paths, filenames, and lifecycle vocabulary are decided per organization (see
[`ADAPT.md`](ADAPT.md)); this file never hardcodes them.

---

## Epic Generation Context Intake (the questionnaire for adapting this skill)

This is the questionnaire for adapting the skill to an organization. Ask as one numbered
list and **WAIT** for answers; record them wherever your team keeps project/pipeline
decisions. Ask only what's missing.

**Workspace paths & naming:**
1. **Products root** — where do product folders live, and what is the per-product folder pattern?
2. **PRD filename** — what is the Master PRD file called inside a product folder?
3. **Technical Architecture filename** — what is that document called (if your pipeline has one)?
4. **Epic subfolder** — where do detailed Epic PRDs live, and what are example files?
5. **Epic Overview output** — what filename should the generated overview use?
6. **Progress file** — what is the per-product progress-tracking file called?
7. **Epic-PRD template** — where does the epic-PRD template live?
8. **ID / naming conventions** — epic ID format (e.g. `E01`), feature ID format (e.g. `F1.1`),
   filename casing?

**Business / lifecycle vocabulary:**
9. **Lifecycle stages** — what MVP/stage labels do you use (default: Core / MVP / Enhanced / Future)?
10. **Product taxonomy** — any product codes or naming the Epic Overview header should reflect?

---

## Activation Checklist

When this skill is activated:

**Phase 0: Research**
1. [ ] Locate Master PRD for product (via your products-root path + PRD filename)
2. [ ] Extract all features (F[X.Y] pattern, per your naming conventions)
3. [ ] Extract existing epic structure from PRD
4. [ ] Generate PRD Feature Inventory (~300 words)

**Phase 1: Analysis**
5. [ ] Present Feature Inventory to user
6. [ ] Ask 5 tailored clarification questions
7. [ ] **WAIT for user responses**
8. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
9. [ ] Apply user decisions to epic structure
10. [ ] Generate epics sequentially
11. [ ] Build coverage matrix
12. [ ] Create dependency diagram

**Phase 3: Validation (Blocking)**
13. [ ] Verify 100% feature coverage
14. [ ] Verify no duplicate assignments
15. [ ] Verify no circular dependencies
16. [ ] If fails -> return to Phase 2 and fix

**Phase 4: Output**
17. [ ] Write the Epic Overview file (your products-root path + epic-overview filename)
18. [ ] Update the progress file (your per-product progress file)
19. [ ] Include pipeline hooks for the epic-PRD generator
20. [ ] Present completion summary

---

## Quality Checklist

### Coverage Checks
- [ ] 100% of PRD features assigned to epics
- [ ] No feature appears in multiple epics
- [ ] Every persona has at least one epic
- [ ] MVP features clearly identified

### Structure Checks
- [ ] Epic Index table complete
- [ ] Dependency diagram present
- [ ] Each epic has full outline (statement, goal, features, personas, dependencies)
- [ ] Coverage matrix complete
- [ ] MVP roadmap defined

### Quality Standards
- [ ] All epics have clear goals
- [ ] All dependencies are logical
- [ ] No circular dependencies
- [ ] Epic sizing is reasonable (4-12 features)
- [ ] Development order makes sense

---

## Epic Overview Document Template

```markdown
# [Product Name] -- EPIC OVERVIEW DOCUMENT
**[Tagline from PRD]**

---

## DOCUMENT INFORMATION

| Attribute | Value |
|-----------|-------|
| **Product** | [Product Name] |
| **Version** | 1.0 |
| **Status** | Draft / Review / Approved |
| **Owner** | [Product Owner] |
| **Last Updated** | [Date] |
| **PRD Reference** | [Link to PRD] |

---

## EPIC SUMMARY

### Overview Statistics

| Metric | Value |
|--------|-------|
| Total Epics | [X] |
| Total Features | [X] |
| MVP Epics | [X] |
| Post-MVP Epics | [X] |
| Personas Covered | [X]/[X] |

### Epic Index

| Epic | Name | Features | Priority | MVP Status | Dependencies |
|------|------|----------|----------|------------|--------------|
| E01 | [Name] | [Count] | P0 | Core | None |
| E02 | [Name] | [Count] | P0 | Core | E01 |
| ... | ... | ... | ... | ... | ... |

---

## DEPENDENCY DIAGRAM

[ASCII dependency diagram here]

### Parallel Development Opportunities

| Phase | Epics | Notes |
|-------|-------|-------|
| Phase 1 | E01 | Foundation only |
| Phase 2 | E02, E04 | Can develop in parallel |
| ... | ... | ... |

---

## EPIC DETAILS

### E01: [Epic Name]

**Epic Statement:** [1-2 sentences]
**Goal:** [Primary objective]
**Hypothesis:** [Product hypothesis this validates]

**Key Questions:**
- [Constraint discovery question]
- [Assumption validation question]
- [Scope clarity question]

**MoSCoW Distribution:**
- MUST: [X] features ([Y]%)
- SHOULD: [X] features ([Y]%)
- COULD: [X] features ([Y]%)

**Features:**
| Feature | Name | Priority | MoSCoW | MVP |
|---------|------|----------|--------|-----|
| F1.1 | [Name] | P0 | MUST | Yes |
| ... | ... | ... | ... | ... |

**Personas Served:**
- **Primary:** P1 ([Persona Name])
- **Secondary:** P2, P3

**Dependencies:**
- **Upstream:** None (foundation)
- **Downstream:** E02, E03, E04
- **Complexity Score:** [X] ([Level])

**MVP Status:** Core (Required for launch)

**Success Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Estimated Complexity:** [S/M/L/XL]

<!-- EPIC_PRD_READY: E01 -->

---

[Continue for all epics...]

---

## COVERAGE MATRIX

### PRD Feature -> Epic Mapping

| Feature | Feature Name | Epic | Priority | MoSCoW | MVP | Persona |
|---------|--------------|------|----------|--------|-----|---------|
| F1.1 | [Name] | E01 | P0 | MUST | Yes | P1 |
| ... | ... | ... | ... | ... | ... | ... |

**Coverage Summary:**
- **Total Features:** [X]
- **Features Assigned:** [X] (100%)
- **Unassigned:** 0

### Epic Complexity Summary

| Epic | Features | MUST | SHOULD | COULD | Complexity Score | Dependencies |
|------|----------|------|--------|-------|------------------|--------------|
| E01 | [X] | [X] | [X] | [X] | [Score] ([Level]) | [Count] |
| ... | ... | ... | ... | ... | ... | ... |

### Persona Coverage Matrix

| Persona | E01 | E02 | E03 | ... | Total Features |
|---------|-----|-----|-----|-----|----------------|
| P1 | Yes | Yes | | | [X] |
| ... | ... | ... | ... | ... | ... |

---

## MVP ROADMAP

### MVP v1.0 Scope

| Epic | Status | Features | Notes |
|------|--------|----------|-------|
| E01 | Core | All ([X]) | Must complete |
| ... | ... | ... | ... |

### Post-MVP Roadmap

| Version | Epics | Theme |
|---------|-------|-------|
| v1.1 | [Epics] | [Theme] |
| v2.0 | [Epics] | [Theme] |

---

## DEVELOPMENT ORDER

### Recommended Sprint Allocation

| Sprint | Epic(s) | Focus | Dependencies |
|--------|---------|-------|--------------|
| 1-2 | E01 | Foundation | None |
| 3-4 | E02, E04 | Core features | E01 complete |
| ... | ... | ... | ... |

### Critical Path

[Critical path description]

---

## DOCUMENT GOVERNANCE

### Next Steps
1. [ ] Review Epic Overview with stakeholders
2. [ ] Generate detailed Epic PRDs (epic-PRD generator)
3. [ ] Begin story generation (story generator)

---

<!-- EPIC_OVERVIEW_COMPLETE: [PRODUCT-CODE] -->
```

---

## Validation Criteria

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Coverage** | 100% of PRD features assigned | Assign missing features |
| **Uniqueness** | No feature in multiple epics | Remove duplicates |
| **No Circular Dependencies** | Dependency graph is acyclic | Resolve cycles |
| **Persona Coverage** | Every persona has features | Add features/adjust |

### Quality Checks (Warning -> Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Epic Sizing** | 4-12 features per epic | Consider split/merge |
| **Dependency Depth** | Max 3 levels deep | Restructure if needed |
| **MVP Balance** | At least 50% MVP | Review priorities |
| **Description Quality** | All epics have goals | Add descriptions |
| **MoSCoW Distribution** | ~60/20/20 (±15%) per epic | Rebalance priorities |
| **Hypothesis Defined** | Each epic has hypothesis | Add validation hypothesis |
| **Complexity Scored** | All epics have complexity score | Calculate scores |

---

## Complexity Matrix Template

```markdown
| Epic | Upstream | Downstream | Integrations | Score | Level |
|------|----------|------------|--------------|-------|-------|
| E01 | 0 | 4 | 0 | 4 | Medium |
| E02 | 1 | 2 | 1 | 7 | High |
| E03 | 2 | 1 | 0 | 5 | Medium |
| E04 | 1 | 1 | 2 | 9 | Critical |
```
