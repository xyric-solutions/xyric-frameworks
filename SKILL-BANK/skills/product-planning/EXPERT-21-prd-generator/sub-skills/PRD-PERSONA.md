---
name: PRD-PERSONA
parent: EXPERT-21
description: Develop detailed user personas from vision segments and the organization's audience segments with goal alignment and persona-feature mapping
version: "1.0"
domain: Persona development and user segmentation for PRDs
---

# Persona Development (PRD-PERSONA)

> Sub-skill of [PRD Generator (EXPERT-21)](../SKILL.md)

## Focus Area

Transforms target market segments from a Vision Document into 5 fully-realized user personas
with demographics, goals, pain points, success stories, and feature-priority mappings. This
sub-skill owns everything persona-related in the PRD — from identifying user segments to
mapping each persona's MoSCoW feature priorities.

Audience and segment context comes from the organization's audience segments (see the
parent's [`ADAPT.md`](../ADAPT.md)); ask via the parent's PRD Context Intake if not yet
decided. Does NOT cover feature specification,
acceptance criteria, epic structure, or competitive analysis — those belong to PRD-FEATURES
or the parent skill.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Segment-to-Persona Mapping | Converting vision / audience segments into named, detailed personas |
| Persona-Feature Alignment | Mapping each persona to Must/Should/Could Have features |
| User Segmentation | Defining P1 (primary) through P2-P5 hierarchy and anti-personas |

## Methodology

### Priority Order
1. **Vision segments are the foundation** — never invent personas that contradict the Vision
   Document or the organization's audience segments
2. **Primary persona (P1) drives MVP** — P1's Must Have features define the minimum viable product
3. **Personas must be specific** — real demographics, realistic backgrounds, product-specific pain points
4. **Every persona earns its place** — each persona must serve a distinct user need; merge overlapping ones
5. **Persona priorities inform MoSCoW** — if removing a feature breaks P1's workflow, it is Must Have

### Workflow
1. Extract target market segments from the Vision Document, the organization's audience
   segments, and the product's `personas` context file (if it exists)
2. Ask the user to confirm segments, identify the primary persona, and define anti-personas
   (Q4-Q5 from the parent)
3. Build 5 personas using the standard template: Demographics, Background, Goals, Pain Points,
   Success Story, Feature Priorities
4. Map each persona to relevant features using MoSCoW per persona
5. Validate: every persona has features; every Must Have feature maps to P1

## Key Patterns

1. **Enrich, Don't Replace** — if a `personas` context file exists, use it as the starting
   point. Add depth rather than discarding existing work.
2. **Pain Points in Their Words** — write pain points as direct quotes: "I spend 3 hours every
   week manually compiling reports", not "User needs automated reporting."
3. **Success Story as North Star** — each persona's success story anchors feature decisions.
   If a feature doesn't serve any success story, question its inclusion.
4. **Overlapping Needs Are Signals** — when multiple personas share a need, that feature is
   likely Must Have. Single-persona needs are Could Have unless that persona is P1.
5. **Demographics Drive Design** — age, technical proficiency, and geography directly inform
   accessibility, UI complexity, and localization.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Copy-paste generic personas from templates | Build personas specific to this product's vision and audience segments |
| Skip anti-persona definition | Always define who the product is NOT for to prevent scope creep |
| All personas have identical feature priorities | Each persona must have distinct Must/Should/Could Have mappings |
| Arbitrary persona count | Use 5 personas as the default; merge or split as the segments justify |
| Persona without feature mapping | Every persona must have a Feature Priorities table |

## Quality Gates

| Gate | Target |
|------|--------|
| Persona count | 5 (P1-P5) by default |
| Template completeness | All fields filled: Demographics, Background, Goals, Pain Points, Success Story, Feature Priorities |
| Primary persona identified | P1 clearly marked with rationale |
| Feature coverage | Every persona maps to at least 2 features |
| Anti-persona defined | At least 1 anti-persona documented |

## Deep Reference

For detailed patterns and methodology in this domain:
- Parent skill: `../SKILL.md` (full PRD philosophy, cross-skill integration)
- Reference sections: `../reference.md` → Phase 1: Questions, Persona questions Q4-Q5
- Checklists: `../forms.md` → User Personas template, Vision Alignment Check

## Team Integration

This sub-skill is designed for use in:
- **Product Design Teams** — as the persona specialist ensuring user-centered requirements
- Pairs well with: PRD-FEATURES (personas feed feature prioritization), UX/UI Designer
  sub-skills (UX alignment)
