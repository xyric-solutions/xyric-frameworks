# Epic PRD Generator — Forms & Templates

Output templates, quality checklists, activation checklists, and validation criteria.
All paths resolve from your organization's decided workspace conventions (see
[`ADAPT.md`](ADAPT.md)); this file never hardcodes a folder layout. The BDD, MoSCoW, and
feature-spec structures below are universal methodology, independent of any organization.

---

## Workspace Intake (the questionnaire for adapting this skill)

Ask as one numbered list and **WAIT** for answers; then record them wherever your team
keeps workspace decisions (your generation brief, a fork of `SKILL.md`, or your own
conventions doc). Ask only what's missing.

1. **Products root** — where product folders live (the parent path for `<product>/`)?
2. **Epic Overview file** — filename/pattern that holds epic outlines for a product?
3. **Master PRD file** — filename/pattern of the master requirements document?
4. **Epic PRD output directory** — folder where detailed Epic PRDs are written?
5. **Epic PRD filename convention** — pattern for the output file (e.g. an `Epic-XX-Name`
   pattern; include the prefix and separators you use)?
6. **Stories index path** — where the per-epic stories index lives (for governance links)?
7. **Progress file** — the file updated at the end of a session for continuity?
8. **Vision / design locations** — optional paths for strategic and UI/UX context?
9. **Naming conventions** — any house rules for IDs (epic `E[XX]`, feature `F[X.Y]`),
   casing, and separators?

---

## Activation Checklist

When this skill is activated:

**Phase 0: Research**
1. [ ] Resolve all input/output paths from your decided workspace conventions
2. [ ] Identify the target epic (E[XX])
3. [ ] Read the Epic Overview for the epic outline
4. [ ] Read the Master PRD for feature details
5. [ ] Read existing Epic PRDs for patterns
6. [ ] Generate an Epic Context Summary (~250 words)

**Phase 1: Analysis**
7. [ ] Present the Epic Context to the user
8. [ ] Ask 4 tailored clarification questions
9. [ ] **WAIT for user responses**
10. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
11. [ ] Apply user decisions to feature specs
12. [ ] Generate features sequentially
13. [ ] Include all required elements per feature
14. [ ] Build the integration-points section

**Phase 3: Validation (Blocking)**
15. [ ] Verify all epic features are specified
16. [ ] Verify all features have BDD acceptance criteria
17. [ ] Verify all features have error scenarios
18. [ ] If fails → return to Phase 2 and fix

**Phase 4: Output**
19. [ ] Write the Epic PRD to `<epic-prd-dir>` using the naming convention
20. [ ] Update the progress file
21. [ ] Emit the story-generation handoff hook
22. [ ] Present the completion summary

---

## Quality Checklist

### Section Completeness
- [ ] Epic Overview (statement, goal, philosophy, feature summary)
- [ ] Personas Served (primary and secondary)
- [ ] All features specified (F[X.1] through F[X.N])
- [ ] Integration Points (within epic, cross-epic, external)
- [ ] Priority Legend
- [ ] MVP Status
- [ ] Success Criteria Summary
- [ ] Document Governance

### Feature Specification Checks
- [ ] Every feature has a description (2+ paragraphs)
- [ ] Every feature has a user story (As a… I want… so that…)
- [ ] Every feature has a success-metrics table (3+ metrics)
- [ ] Every feature has BDD acceptance criteria (3+ criteria)
- [ ] Every feature has an error-scenarios table (3+ scenarios)
- [ ] Every feature has dependencies documented

### Quality Standards
- [ ] All metrics have quantified targets
- [ ] All acceptance criteria use BDD Given/When/Then format
- [ ] All error messages are user-friendly
- [ ] All dependencies are explicit
- [ ] Consistent feature ID format (F[X.Y])
- [ ] No placeholder text in the final document

---

## Epic PRD Document Template

```markdown
# Epic [XX]: [Epic Name] — PRD

**Product:** [Product Name]
**Epic ID:** E[XX]
**Version:** 1.0
**Status:** Draft / Review / Approved
**Last Updated:** [Date]

---

## EPIC OVERVIEW

### Epic Statement
[1-2 sentences describing what this epic achieves]

### Epic Goal
[Primary objective - clear and measurable]

### Core Philosophy
[Guiding principle for this epic]

### Feature Summary

| Feature | Name | Priority | MVP | Status |
|---------|------|----------|-----|--------|
| F[X.1] | [Name] | P0 | Yes | Specified |
| F[X.2] | [Name] | P0 | Yes | Specified |
| ... | ... | ... | ... | ... |

**Total Features:** [X]
**MVP Features:** [Y]
**Post-MVP Features:** [Z]

---

## PERSONAS SERVED

### Primary Persona
**P[X]: [Persona Name]**
- **Role:** [From PRD]
- **Goal:** [What they want from this epic]
- **Key Features:** F[X.1], F[X.2], F[X.3]

### Secondary Personas
**P[Y]: [Persona Name]**
- **Goal:** [What they want]
- **Key Features:** F[X.2], F[X.4]

---

## FEATURE SPECIFICATIONS

### F[X.1]: [Feature Name]

**Priority:** P0 (Critical)
**MVP Status:** Core
**Personas:** P[X] (Primary), P[Y], P[Z]

#### Description
[2-3 paragraphs]

#### User Story
**As a** [persona name],
**I want to** [action/capability],
**so that** [benefit/value].

#### Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| [Metric] | [Target] | [How measured] |

#### Acceptance Criteria (BDD Format)

**Core Functionality:**
- **Given** [context], **When** [action], **Then** [outcome]

**User Experience:**
- **Given** [context], **When** [action], **Then** [outcome]

**Edge Cases:**
- **Given** [edge case], **When** [action], **Then** [graceful handling]

**Performance:**
- **Given** [load condition], **When** [action], **Then** [response within target]

#### Error Scenarios
| Scenario | User Message | System Action | Recovery |
|----------|--------------|---------------|----------|
| Network timeout | "Connection lost…" | Retry 3x | Retry button |
| Invalid input | "[Field] is invalid…" | Highlight field | Clear guidance |
| Server error | "Something went wrong…" | Log error | Retry button |

#### Dependencies
- **Prerequisite Features:** None / F[X.Y]
- **Cross-Epic:** E[YY] - [Reason]
- **External:** [API, service, etc.]

---

[Continue for all features...]

---

## INTEGRATION POINTS

### Within This Epic
| Source Feature | Target Feature | Integration Type |
|----------------|----------------|------------------|
| F[X.1] | F[X.2] | Data flow |

### Cross-Epic Integration
| This Epic Feature | Other Epic | Other Feature | Integration |
|-------------------|------------|---------------|-------------|
| F[X.2] | E[YY] | F[Y.1] | Shared data |

### External Integrations
| Feature | External System | Integration Type |
|---------|-----------------|------------------|
| F[X.1] | [System] | API |

---

## ARCHITECTURE DECISIONS (Epic-Level)

| Decision | Choice | ADR Required | Owner |
|----------|--------|--------------|-------|
| [Decision topic] | [Selected approach] | Yes / No | Software architect |

---

## MVP STATUS

### MVP v1.0 Features
| Feature | Status | Notes |
|---------|--------|-------|
| F[X.1] | Core | Required |

### Post-MVP Features
| Feature | Target Version | Notes |
|---------|----------------|-------|
| F[X.5] | v1.1 | [Reason for deferral] |

---

## SUCCESS CRITERIA SUMMARY

### Epic Completion Criteria
- [ ] All P0 features implemented and tested
- [ ] All P1 features implemented and tested
- [ ] Performance targets met
- [ ] Error scenarios handled

### Epic-Level Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Feature Completion | 100% | [X]% |
| Test Coverage | [X]% | [X]% |

---

## DOCUMENT GOVERNANCE

| Document | Location | Status |
|----------|----------|--------|
| Master PRD | [Link] | Approved |
| Epic Overview | [Link] | Approved |
| Stories | [Stories index path from your conventions] | [Status] |

---

**Epic PRD Established:** [Date]
**Epic Owner:** [Name/Role]

<!-- STORY_READY: E[XX] -->
```

---

## Validation Criteria

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Feature Coverage** | All epic features specified | Add missing features |
| **BDD Format** | All criteria use Given/When/Then | Convert to BDD format |
| **ADR Flagging** | Significant decisions flagged | Add ADR flags |
| **Acceptance Criteria** | Every feature has 3+ criteria | Add criteria |
| **Error Scenarios** | Every feature has error table | Add scenarios |
| **Success Metrics** | Every feature has metrics | Add metrics |

### Quality Checks (Warning → Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **User Story** | Proper format (As a… I want… so that…) | Reformat |
| **BDD Completeness** | Given/When/Then all present | Complete BDD |
| **Metric Quantification** | Targets are numbers | Add targets |
| **Dependency Clarity** | Dependencies specified | Document |
| **Architecture Pattern** | Complex features have patterns | Add pattern reference |
