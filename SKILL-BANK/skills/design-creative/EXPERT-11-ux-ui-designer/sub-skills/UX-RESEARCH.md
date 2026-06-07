---
name: UX-RESEARCH
parent: EXPERT-11
description: User research methodologies, usability testing, persona development, journey mapping, and competitive analysis
version: "1.0"
domain: User Research & Discovery
---

# User Research & Discovery (UX-RESEARCH)

> Sub-skill of [UX/UI Designer (EXPERT-11)](../SKILL.md)

## Focus Area

Specializes in understanding users before design begins: research planning, usability
testing, persona development, journey mapping, and competitive analysis. This sub-skill
owns the "why" behind design decisions. It does NOT cover visual design, interaction
design, or accessibility auditing — those belong to UI-DESIGN and UX-A11Y.

Audience and segment context is decided per organization (the target users / ICP
segments) — see the parent's [`ADAPT.md`](../ADAPT.md); ask via the parent's Design Context
Intake if not yet decided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Research Planning | Study design, methodology selection, participant recruiting criteria |
| Usability Testing | Task-based testing scripts, observation frameworks, think-aloud protocols |
| Persona Development | Data-driven personas, behavioral archetypes, real user segments |
| Journey Mapping | End-to-end user flows, pain-point identification, opportunity mapping |
| Competitive Analysis | Feature comparison, UX benchmarking, gap identification |

## Methodology

### Priority Order
1. **Research before design** — never skip discovery to save time
2. **Real users over assumptions** — test with actual target segments, not proxies
3. **Context-appropriate methods** — constrained-context audiences need field research, not just surveys
4. **Product-dependent strategy** — mobile-first products need mobile-context research

### Workflow
1. **Define research goals** — primary question + secondary questions, tied to product decisions
2. **Select methodology** — interviews for exploratory, usability tests for validation, surveys for scale
3. **Recruit participants** — must-have criteria, exclusion criteria, sample-size justification
4. **Conduct sessions** — structured scripts (60 min: welcome, background, main activity, follow-up, close)
5. **Synthesize findings** — patterns across participants, severity of pain points, actionable recommendations

## Key Patterns

**Constrained-context research**: When the organization's audience uses low-end devices,
intermittent connectivity, outdoor environments, or multiple languages, account for those
conditions in the study. Field observation often beats remote testing for these segments.

**Think-aloud protocol**: Participants verbalize their thought process. Observe where they
look first, what they tap, where they hesitate. Success: unassisted completion, time under
threshold, confidence > 3/5.

**Assumption challenge**: When research findings contradict design assumptions, surface the
assumption and its alternative explicitly before re-deciding.

**Persona grounding**: Ground personas in research data, not demographics. Include
behavioral patterns, tech comfort, device capabilities, and connectivity constraints.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Designing without research | Always conduct discovery before wireframing |
| Testing with colleagues instead of real users | Recruit from actual target user segments |
| Leading questions in usability tests | Use neutral scenarios in the participant's own words |
| Ignoring constrained-context audiences | Account for device diversity, connectivity, literacy |
| Over-researching before any design | Timebox research; iterate with design cycles |

## Quality Gates

| Gate | Target |
|------|--------|
| Research coverage | Primary question answered with evidence from 5+ participants |
| Usability task completion | > 90% unassisted completion rate |
| Persona validation | Validated against real user data, not assumptions |
| Findings actionability | Every finding maps to a specific design recommendation |

## Deep Reference

- Parent: `../SKILL.md` | Reference: `../reference.md` → Mobile-First Patterns, Constrained-Context
- Checklists: `../forms.md` → Research Plan, Usability Script, Constrained-Context Checklist

## Team Integration

- **Product Discovery / Design Sprint** teams — as lead researcher
- Pairs with: UI-DESIGN (design handoff), product manager (requirements alignment)
