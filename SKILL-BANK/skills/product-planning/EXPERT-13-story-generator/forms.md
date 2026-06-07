# Story Generator (EXPERT-13) — Forms & Templates

Intake questions, output templates, quality checklists, activation checklist, and
validation criteria. Where stories and tasks live, the filename conventions, and the
story-linking field are decided per organization (see [`ADAPT.md`](ADAPT.md)); this file
never hardcodes them.

---

## Workspace & Conventions Intake (the questionnaire for adapting this skill)

This is the intake for adapting the skill to an organization (see [`ADAPT.md`](ADAPT.md)).
Ask as one numbered list and **WAIT** for answers; then record them wherever your team keeps
workspace/convention decisions. Ask only what's missing.

**Where things live:**
1. **Products root** — where does each product's folder live (e.g. a `products_root`
   pattern like `<root>/<product>`)?
2. **Story folder** — inside a product, which sub-folder holds stories (e.g. `stories/`)?
3. **Task / work-item folder** — which sub-folder holds implementation tasks?
4. **Planning/context file** — what is the per-product file that records decisions and
   session history (the file the workflow updates after generation)?
5. **Template locations** — where do the story template and the Epic-index template live?

**Naming conventions:**
6. **Story filename pattern** — e.g. `S<Epic>-<Seq>-<slug>.md`?
7. **Epic-index filename pattern** — e.g. `Epic-<NN>-Stories-Index.md`?
8. **Task filename pattern** — e.g. `<prefix>-<NNN>-<slug>.md`?
9. **Story-linking field** — the YAML field a task file uses to reference its parent
   story/stories (the field that makes work traceable; tasks without it are orphaned)?

**Products:**
10. **Product taxonomy** — the list of products and each one's lifecycle stage, so the
    skill can identify the right product folder from an Epic reference?

---

## Activation Checklist

**Phase 0: Research**
1. [ ] Confirm Epic number/path and identify the product (from the product taxonomy)
2. [ ] Gather context from the product folder (see Required Context Sources)
3. [ ] Generate the Epic Analysis Summary (~500 words)

**Phase 1: Analysis**
4. [ ] Present the Epic summary to the user
5. [ ] Run the light assumption challenge (question-why)
6. [ ] Ask the 9 tailored clarification questions
7. [ ] **WAIT for user responses**

**Phase 2: Generation**
8. [ ] Apply user decisions to the story breakdown
9. [ ] Generate stories sequentially (no overlaps)
10. [ ] Build the dependency graph and coverage matrix

**Phase 3: Validation (Blocking)**
11. [ ] Verify 100% feature coverage
12. [ ] Check no duplicate/overlapping stories
13. [ ] Validate template compliance and DAG acyclicity
14. [ ] If any critical check fails → return to Phase 2 and fix

**Phase 4: Output**
15. [ ] Write individual story files (use the story filename pattern)
16. [ ] Write the Epic index (use the Epic-index filename pattern)
17. [ ] Update the planning/context file
18. [ ] Emit pipeline hooks and present a completion summary

---

## The 9 Clarification Questions (tailored — Phase 1)

Always inject the actual Epic features and context; never ask these generically.

**STRATEGIC**

- **Q1 — Priority Validation.** Show all features with current priorities in a table.
  Ask: adjust any MoSCoW priorities? Any features explicitly "Won't Have" for MVP?
- **Q2 — Scope Boundaries.** List the MVP-Core features. Ask: any to explicitly EXCLUDE
  from MVP (marked post-MVP / Won't Have, not deleted)?
- **Q3 — Story Granularity.** Present features with complexity classification. Ask:
  Granular (1–3 day each), Larger (5–7 day each), or Mixed (granular for complex, larger
  for simple)?

**TECHNICAL**

- **Q4 — Tech-Stack Constraints.** List the Epic's technical dependencies. Ask: specific
  APIs already selected? Framework preferences? Architectural patterns to follow?
- **Q5 — Integration Priority.** List the integrations. Ask: which are MVP-critical vs
  deferrable to post-MVP?

**UX**

- **Q6 — Feature Variants** (skip if none). List features with variants/modes. Ask: which
  variant gets more detail — Primary-first, Full-coverage, or N/A?
- **Q7 — Error-Handling Depth.** List the defined error scenarios. Ask: Basic (happy path
  + critical), Comprehensive (all defined), or Enterprise-grade (beyond defined)?

**TIMELINE**

- **Q8 — Implementation Phasing.** Suggest phases (Foundation → Core Experience →
  Enhancement) grouped by dependency. Ask: agree, or adjust?
- **Q9 — External Dependencies.** List external dependencies with known status. Ask: any
  blockers affecting story sequencing? Any not listed that you should know about?

---

## Story Template

Read the organization's canonical story template and follow it. If no template is
configured, fall back to this structure (resolve `id` / filename from your story filename
pattern):

```markdown
---
type: story
id: <story id, e.g. S<Epic>.<Feature>.<Seq>>
title: [Story Title]
epic: <epic id, e.g. E<XX>>
epic_name: [Epic Name]
feature: <feature id, e.g. F<XX>.<Feature>>
feature_name: [Feature Name]
product: [product-name]
priority: P0
status: Draft
created: [YYYY-MM-DD]
---

# <story id>: [Story Title]

## User Story

**As a** [persona],
**I want to** [action/capability],
**So that** [benefit/value].

---

## Story Type

- [ ] Feature | Enhancement | Technical | Integration

## Priority

- [ ] Must Have (P0) | Should Have (P1) | Could Have (P2) | Won't Have (P3)

---

## Scope Description

**User Experience:**
[What the user sees/experiences]

**Feature Variants (If Applicable):**
- **[Variant A]:** [Description]
- **[Variant B]:** [Description]

**Data Captured:**
| Field | Format | Validation | Privacy |
|-------|--------|------------|---------|
| ... | ... | ... | ... |

**Behaviors:**
[Expected system behaviors]

---

## Acceptance Criteria

Given [context],
When [action],
Then [expected outcome].

(Include criteria for: happy path, edge cases, error states)

---

## Success Metrics

- [Metric 1]: [Target]
- [Metric 2]: [Target]

---

## Constraints & Requirements

| Performance | Security | Privacy | Accessibility | Compatibility |
|-------------|----------|---------|---------------|---------------|
| [Requirement] | [Requirement] | [Requirement] | [Requirement] | [Requirement] |

---

## Dependencies

- **Prerequisite Stories:** [Stories that must be done first]
- **Related Stories:** [Stories that share components/data]
- **External Dependencies:** [APIs, services, approvals needed]

---

## Edge Cases & Errors

| Scenario | Expected Behavior |
|----------|-------------------|
| [Edge case 1] | [What should happen] |
| [Error state 1] | [How to handle gracefully] |

---

## Open Questions

- [Questions for task breakdown]
- [Technical decisions deferred to implementation]

---

## Definition of Done

- [ ] Acceptance criteria met
- [ ] Error scenarios handled
- [ ] Accessibility requirements verified
- [ ] Security requirements verified
- [ ] Performance requirements verified
```

The "11 required sections" the Template check counts are: YAML frontmatter, User Story,
Story Type, Priority, Scope Description, Acceptance Criteria, Success Metrics, Constraints
& Requirements, Dependencies, Edge Cases & Errors, and Definition of Done. (Adjust the set
to match the configured template if it differs.)

---

## Epic Index Template

Read the organization's canonical Epic-index template. Fallback structure (resolve file
links from your story/Epic-index filename patterns):

```markdown
# Epic XX: [Name] - Story Index

> **Epic:** E[XX] - [Name]
> **Source:** <Epic PRD path>
> **Created:** [Date]   **Updated:** [Date]
> **Stories:** [Count] ([Must Have count] Must Have, [Should Have count] Should Have)

---

## Story Index

| Story ID | Title | Feature | Priority | Status | File |
|----------|-------|---------|----------|--------|------|
| S[XX].1.1 | [Title] | F[X.1] | P0 (Must) | Draft | [View](<story file>) |
| S[XX].1.2 | [Title] | F[X.1] | P1 (Should) | Draft | [View](<story file>) |

---

## Dependency Diagram

```
PHASE 1: [NAME]
S[XX].1.1 --+--> S[XX].1.2
            +--> S[XX].1.3
                    |
                    v
PHASE 2: [NAME]
...
```

---

## Feature -> Story Coverage Matrix

| Epic Feature | Story ID(s) | Files | Coverage |
|--------------|-------------|-------|----------|
| F[X.1]: [Name] | S[XX].1.1, S[XX].1.2 | [Links] | 100% |

**Completeness Verification:** All [N] features mapped to stories.

---

## Implementation Phases

| Phase | Sprint | Stories | Files | Deliverable |
|-------|--------|---------|-------|-------------|
| 1: [Name] | Sprint 1 | S[XX].1.1, ... | [Links] | [What's delivered] |

---

## Quick Links

| Resource | Link |
|----------|------|
| Epic PRD | [View](<Epic PRD path>) |
| Product PRD | [View](<Product Requirements path>) |
| Planning/context file | [View](<planning/context file path>) |
```

---

## Quality Checklist

### Completeness (Critical)
- [ ] All Epic features covered by at least one story
- [ ] No gaps between stories
- [ ] Error-handling scenarios addressed
- [ ] Cross-cutting concerns embedded (security, accessibility, performance)
- [ ] All personas served by this Epic have relevant stories

### Scope Clarity
- [ ] Each story clearly describes WHAT (not HOW)
- [ ] Acceptance criteria are specific and testable
- [ ] Constraints and requirements are explicit
- [ ] Open questions documented for task breakdown

### Consistency
- [ ] Story naming follows the organization's story filename pattern
- [ ] All stories use the same template structure
- [ ] Priority distribution is realistic
- [ ] Dependencies are logical (no circular deps)

### Traceability
- [ ] Every story links back to its Epic feature(s)
- [ ] Dependencies map correctly
- [ ] Success metrics align with Epic success criteria
- [ ] Pipeline hooks emitted so downstream tasks can link via the organization's
      story-linking field

---

## Validation Criteria

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Coverage** | Every feature has >=1 story | Return to Phase 2, add missing stories |
| **Duplicate** | No overlapping story scopes | Merge or differentiate stories |
| **Template** | All required template sections present | Add missing sections |
| **DAG** | Dependencies are acyclic | Fix circular dependencies |

### Quality Checks (Warning -> Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **BDD Format** | Acceptance criteria in Given/When/Then | Reformat criteria |
| **Quantified Metrics** | Success metrics are numeric | Add specific targets |
| **Edge Cases** | Error scenarios addressed | Document edge cases |
| **Open Questions** | Deferred decisions documented | List open questions |
