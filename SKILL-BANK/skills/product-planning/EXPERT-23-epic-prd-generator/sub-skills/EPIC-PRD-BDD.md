---
name: EPIC-PRD-BDD
parent: EXPERT-23
description: BDD acceptance criteria with Given/When/Then scenarios, error handling, edge cases, and recovery paths.
version: "1.0"
domain: Behavioral specification and error scenario design
---

# BDD Acceptance Criteria (EPIC-PRD-BDD)

> Sub-skill of [Epic PRD Generator (EXPERT-23)](../SKILL.md)

## Focus Area

Specializes in writing testable BDD acceptance criteria for epic features: Given/When/Then
scenarios organized by category (core, UX, edge cases, performance), comprehensive error
scenario tables with user-facing messages and recovery paths, and integration test
scenarios. Does NOT cover feature descriptions, user stories, screen specs, or success
metrics — defer to [EPIC-PRD-FEATURES](EPIC-PRD-FEATURES.md) for feature definition work.

Output paths resolve from the organization's decided workspace conventions (see the parent
skill's `ADAPT.md`); ask via the parent's Workspace Intake if not yet decided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| BDD Scenarios | Given/When/Then criteria organized by category |
| Error Scenarios | User messages, system actions, recovery paths per feature |
| Edge Cases & Boundaries | Empty states, concurrent access, overflow, limit conditions |
| Performance & Integration | Load targets, throughput limits, cross-feature data flow verification |

## Methodology

### Priority Order
1. Every feature needs a minimum of 3 BDD criteria — validation blocks on fewer
2. All criteria use strict Given/When/Then format — no exceptions
3. Error messages must be user-friendly, never raw technical errors
4. Recovery paths are mandatory — every error must have a way forward
5. Criteria must be independently testable — one behavior per scenario

### Workflow
1. Read the feature definition (from EPIC-PRD-FEATURES output or the Epic PRD draft)
2. Identify happy-path behaviors for Core Functionality criteria
3. Write UX-specific criteria (loading states, feedback, transitions)
4. Design edge case scenarios (empty data, boundary values, concurrent users)
5. Define performance criteria with numeric thresholds
6. Build the error scenario table: scenario, user message, system action, recovery
7. Add integration test scenarios for cross-feature and cross-epic data flows
8. Validate: minimum 3 criteria per feature, all in BDD format

## Key Patterns

**Category-Organized Criteria**: Four standard categories — Core Functionality (happy
paths), User Experience (feedback, transitions), Edge Cases (boundaries, empty states),
Performance (load, response time). Ensures complete coverage.

**Error Scenario Tables**: Four columns per feature — Scenario, User Message, System Action,
Recovery. Never leave recovery blank.

**One Behavior Per Criterion**: Each Given/When/Then tests exactly one thing. Compound
criteria ("saved AND email sent") must be split into separate scenarios.

**Stress the Boundaries**: Zero items, max items, at-limit, over-limit, empty strings,
special characters, concurrent modifications. Test what breaks.

**Recovery-First Error Design**: Start from "how does the user recover?" Auto-retry for
transient failures, state preservation for form errors, clear guidance for validation.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Missing Given/When/Then structure | Strict BDD format for every criterion |
| Compound criteria testing multiple behaviors | One behavior per Given/When/Then scenario |
| Technical error messages ("500 Internal Server Error") | User-friendly messages with clear next steps |
| Error scenarios without recovery paths | Every error must have explicit recovery |
| Only testing happy paths | Minimum: core + UX + edge cases + performance |
| Vague performance targets ("should be fast") | Numeric thresholds ("response < 200ms at 1000 concurrent users") |

## Quality Gates

| Gate | Target |
|------|--------|
| BDD criteria per feature | Minimum 3, complex features 6-10 |
| BDD format compliance | 100% Given/When/Then (no exceptions) |
| Error scenario coverage | Every feature has an error table with 3+ scenarios |
| Recovery path coverage | Every error scenario has explicit recovery |
| Category coverage | All 4 categories (core, UX, edge, performance) |

## Deep Reference

- Parent skill: `../SKILL.md` (BDD format specification, validation rules)
- Reference: `../reference.md` → Phase 3: Validation, BDD Completeness checks
- Checklists: `../forms.md` → Validation Criteria, Quality Checks

## Team Integration

- **QA Planning Team** — acceptance-criteria author feeding test generation
- **Product Documentation Team** — BDD specialist alongside feature definition
- Pairs with: EPIC-PRD-FEATURES (feature definitions), a test-spec author, and a QA engineer
