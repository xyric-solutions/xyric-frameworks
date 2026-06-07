---
name: PRD-FEATURES
parent: EXPERT-21
description: Define feature specifications with acceptance criteria, MoSCoW classification, success metrics, and dependency mapping
version: "1.0"
domain: Feature definition and prioritization for PRDs
---

# Feature Definition (PRD-FEATURES)

> Sub-skill of [PRD Generator (EXPERT-21)](../SKILL.md)

## Focus Area

Transforms vision objectives and epic structures into detailed feature specifications with
testable acceptance criteria, MoSCoW priority tags, quantified success metrics, and
cross-feature dependency mapping. Owns the Epic Overview Map, MVP Scope Matrix, feature
templates, and all feature-level content in the PRD.

Does NOT cover persona creation, user segmentation, or persona-level goal analysis — those
belong to PRD-PERSONA. Receives persona-feature mappings as input.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Feature Specification | F[Epic].[Seq] format with user stories, acceptance criteria, error scenarios |
| MoSCoW & Dependency Mapping | Priority tagging based on persona impact; epic/feature dependency chains |
| MVP Scope & Metrics | Feature-level scope matrix across versions; quantified success metrics |

## Methodology

### Priority Order
1. **Every feature traces to a vision objective** — no orphaned features; 100% coverage of strategic goals
2. **Features must be testable** — if you cannot write acceptance criteria, the feature is too vague
3. **MoSCoW follows persona impact** — Must Have = breaks P1's core workflow if removed
4. **Dependencies determine build order** — Layer 1 (foundation) before Layer 2 (core) before Layer 3 (enhanced)
5. **Metrics are numbers, not adjectives** — "95% uptime", not "high availability"

### Workflow
1. Map vision objectives to epic groupings; propose epic structure to the user (Q3 from parent)
2. Define features within each epic using F[Epic].[Seq] format
3. Write acceptance criteria, user stories, error scenarios, and success metrics per feature
4. Assign MoSCoW tags using persona priorities from PRD-PERSONA
5. Build the dependency graph: epic-level (Depends On, Blocks, Parallel With) and feature-level cross-references
6. Generate the MVP Scope Matrix and Vision Coverage Matrix
7. Validate: every vision objective covered, every feature has a MoSCoW tag, no placeholder text

## Key Patterns

1. **Feature Format is Sacred** — every feature includes: Priority, MVP Status, Personas, User
   Story, Metrics, Acceptance Criteria, Error Scenarios, Dependencies. No shortcuts.
2. **Layered Development Order** — Layer 1 (Foundation, no deps) → Layer 2 (Core) → Layer 3
   (Enhanced) → Layer 4 (Advanced). This determines build sequence.
3. **Vision Coverage Matrix** — map every vision objective to epics and features. Coverage must
   reach 100%. Gaps mean missing features.
4. **MoSCoW Decision Framework** — breaks primary journey = Must Have. Degrades but doesn't
   break = Should Have. Subset notices = Could Have. Out of scope = Won't Have.
5. **Cross-Epic Dependencies Are Explicit** — document as `F2.3 depends on F1.1: [reason]`.
   Never leave dependencies implicit.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Vague acceptance criteria ("works well") | Testable criteria: "User receives confirmation within 2 seconds" |
| Features without MoSCoW tags | Every feature gets Must/Should/Could/Won't Have classification |
| Missing dependency mapping between epics | Every epic declares Depends On, Blocks, and Parallel With |
| Unquantified success metrics | All metrics have numbers: percentages, counts, time targets |
| Features that don't trace to vision objectives | Every feature must map to at least one strategic objective |

## Quality Gates

| Gate | Target |
|------|--------|
| Vision coverage | 100% of objectives mapped to features |
| MoSCoW tagging | Every feature has a priority tag |
| Acceptance criteria | Every feature has 3+ testable criteria |
| Dependency mapping | Every epic has Depends On / Blocks / Parallel With |
| Metrics quantified | Zero unquantified success metrics |
| No placeholders | Zero instances of TBD, [fill in], or empty fields |

## Deep Reference

For detailed patterns and methodology in this domain:
- Parent skill: `../SKILL.md` (full PRD philosophy, cross-skill integration)
- Reference sections: `../reference.md` → Feature Categorization Patterns, Dependency Mapping, MoSCoW Guidance
- Checklists: `../forms.md` → Feature Template Reference, MVP vs Future Scope, Vision Coverage Matrix

## Team Integration

This sub-skill is designed for use in:
- **Product Design Teams** — as the feature-specification specialist ensuring complete,
  testable requirements
- Pairs well with: PRD-PERSONA (persona priorities feed MoSCoW), Software Architect sub-skills
  (technical feasibility), the epic-generator skill (epic breakdown downstream)
