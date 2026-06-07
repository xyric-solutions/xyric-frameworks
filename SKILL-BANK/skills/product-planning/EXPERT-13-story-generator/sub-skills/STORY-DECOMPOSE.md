---
name: STORY-DECOMPOSE
parent: EXPERT-13
description: Decompose Epic features into well-sized user stories with INVEST criteria and dependency mapping
version: "1.0"
domain: Feature-to-story breakdown and sizing
---

# Story Decomposition (STORY-DECOMPOSE)

> Sub-skill of [Story Generator (EXPERT-13)](../SKILL.md)

## Focus Area

Specializes in breaking Epic features into appropriately-sized user stories, applying
INVEST criteria, and building dependency graphs between stories. Handles feature grouping,
story-splitting decisions, and implementation phasing. Does NOT validate coverage
completeness or verify persona mapping (use STORY-VALIDATE).

Where stories are written and the filename pattern are decided per organization (the story
folder and story filename pattern — see the parent's [`ADAPT.md`](../ADAPT.md)); ask via the
parent's Workspace & Conventions Intake if not yet decided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Feature-to-Story Grouping | Map each Epic feature (F[X.Y]) to one or more stories |
| Story Sizing | Classify as S (1–2 day), M (3–5 day), L (5–8 day); split L stories |
| INVEST Criteria | Independent, Negotiable, Valuable, Estimable, Small, Testable |
| Dependency Mapping | Build an acyclic dependency graph across stories |
| Split Decisions | Evidence-based splitting using cognitive load, persona, and error-handling signals |

## Methodology

### Priority Order
1. Stories define WHAT, never HOW — implementation deferred to task breakdown
2. Combine feature variants by default — split only when complexity demands it
3. Cognitive load drives splitting — not arbitrary size rules
4. Dependencies must be acyclic — verify the DAG at every addition

### Workflow
1. **Extract** — read Epic PRD features (F[X.Y]) with complexity classifications from the
   Phase 0 analysis
2. **Group** — map features to initial story candidates; combine related variants
3. **Size** — apply S/M/L sizing; flag any L stories for potential splitting
4. **Split** — for flagged stories, apply the split signals (below); verify each half
   passes INVEST
5. **Sequence** — build the dependency graph; assign implementation phases (Foundation,
   Core, Enhancement)
6. **Output** — generate story files using the configured template with BDD acceptance
   criteria

## Key Patterns

- **Split Signal: Cognitive Load** — if describing the story requires >3 distinct user
  flows, split by flow
- **Split Signal: Persona Divergence** — if two personas have fundamentally different needs
  from the same feature, split by persona
- **Split Signal: Error Complexity** — if error handling is substantial enough to obscure
  the happy path, extract it into a dedicated story
- **Variant Combining** — feature modes (e.g., text vs voice input) stay in one story
  unless each mode requires distinct infrastructure
- **Phase Sequencing** — foundation stories (data models, auth) first; core experience
  second; enhancements third

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Splitting by technical layer (frontend/backend) | Split by user-facing capability |
| One story per feature regardless of complexity | Size-based splitting; simple features get one story, complex get multiple |
| Prescribing implementation in story scope | Describe what the user experiences, not how it is built |
| Generating all stories in parallel | Sequential generation preserves context and prevents overlaps |

## Quality Gates

| Gate | Target |
|------|--------|
| INVEST compliance | Every story passes all 6 criteria |
| Size distribution | No story exceeds L (8 days); majority are S or M |
| DAG validity | Zero circular dependencies in the story graph |
| BDD criteria | Every story has Given/When/Then acceptance criteria |

## Deep Reference

- Parent skill: `../SKILL.md` (full philosophy and the 4-phase workflow)
- Reference: `../reference.md` → Phase 2: Story Generation; Assumption Challenge; INVEST &
  sizing reminders
- Checklists: `../forms.md` → Story Template; Activation Checklist (Phase 2)

## Team Integration

- **Product Planning Team** — as the story-breakdown specialist converting epics into
  sprint-ready stories
- Pairs well with: STORY-VALIDATE (validates what this sub-skill produces), a
  prioritization sub-skill (MoSCoW inputs for story priority)
