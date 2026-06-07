---
name: EPIC-PRD-FEATURES
parent: EXPERT-23
description: Comprehensive feature definitions within an epic — user flows, screen specs, data requirements, and success metrics.
version: "1.0"
domain: Epic feature specification and user flow design
---

# Epic Feature Definitions (EPIC-PRD-FEATURES)

> Sub-skill of [Epic PRD Generator (EXPERT-23)](../SKILL.md)

## Focus Area

Specializes in transforming epic outlines into comprehensive feature definitions: detailed
descriptions, persona-driven user stories, screen-by-screen specifications, data
requirements, success metrics, and dependency mapping. Does NOT cover BDD acceptance criteria
or error scenario tables — defer to [EPIC-PRD-BDD](EPIC-PRD-BDD.md) for Given/When/Then
scenarios and edge case handling.

Output paths and naming conventions resolve from the organization's decided workspace
conventions (see the parent skill's `ADAPT.md`); ask via the parent's Workspace Intake if
not yet decided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Feature Description | 2-3 paragraph specs with include/exclude scope boundaries |
| User Stories | Persona-driven "As a / I want / so that" with MoSCoW tagging |
| Screen Specs & Data | Screen flows, UI states, data models, field constraints |
| Success Metrics | Quantified targets with measurement methods per feature |
| Dependency Mapping | Prerequisite features, cross-epic links, external integrations |

## Methodology

### Priority Order
1. Features must match the Epic Overview list exactly — never invent new features
2. Every feature gets a user story tied to a named persona from the PRD
3. Success metrics must be quantified numbers, not vague goals
4. Dependencies are explicit — both within-epic and cross-epic
5. MoSCoW priority (P0-P3) and MVP status are mandatory per feature

### Workflow
1. Extract the feature list from the Epic Overview (F[X.Y] IDs)
2. Map each feature to primary/secondary personas from the Master PRD
3. Write the feature description with include/exclude scope boundaries
4. Define the user story with persona name, action, and value
5. Specify the screen flow (entry, key screens, data, exit points) and data requirements
6. Set the success-metrics table with quantified targets
7. Map dependencies: prerequisite features, cross-epic, external systems

## Key Patterns

**Persona-First Features**: Start with "who uses it" before "what it does." Generic features
indicate missing persona mapping.

**Screen-by-Screen Thinking**: Describe what the user sees at each step — which screen, what
data, what actions, where next. Bridges PRD and implementation.

**Metric Triples**: Name + numeric target + measurement method. "User engagement" is not a
metric. "DAU > 500, measured via analytics" is.

**Feature Boundaries**: State what a feature includes AND excludes. "Profile management
includes avatar, display name, email. Does NOT include password reset (see F[X.3])."

**Integration Surface**: Document data flows between features, shared state, and handoff
points to other epics.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Vague feature descriptions ("handles user data") | Specific scope with include/exclude boundaries |
| User stories without named personas | Always use the persona ID and name from the PRD |
| Metrics without numbers ("improve performance") | Quantified targets ("response time < 200ms") |
| Missing dependency documentation | Explicit prerequisite features and cross-epic links |
| Inventing features not in the Epic Overview | Only specify features from the epic outline |

## Quality Gates

| Gate | Target |
|------|--------|
| Feature coverage | 100% of Epic Overview features specified |
| User story format | Every feature has "As a [persona] / I want / so that" |
| Success metrics | 3+ quantified metrics per feature |
| Dependencies documented | Every feature has a dependency section (even if "None") |
| Screen flow coverage | Key user flows described with entry/exit points |

## Deep Reference

- Parent skill: `../SKILL.md` (full Epic PRD Philosophy, 4-phase workflow)
- Reference: `../reference.md` → Phase 2: Generation, Feature Specification Structure
- Checklists: `../forms.md` → Feature Specification Checks, Epic PRD Template

## Team Integration

- **Product Documentation Team** — feature-specification writer
- **Design Sprint Team** — feature-scope definer before UX work
- Pairs with: EPIC-PRD-BDD (acceptance criteria), and a story generator (downstream)
