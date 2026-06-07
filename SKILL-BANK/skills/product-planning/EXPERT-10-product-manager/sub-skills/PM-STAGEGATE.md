---
name: PM-STAGEGATE
parent: EXPERT-10
description: Lifecycle stage gate decisions, readiness checklists, and transition management
version: "1.0"
domain: Product lifecycle stage transitions
---

# Lifecycle Stage Gates (PM-STAGEGATE)

> Sub-skill of [Product Manager (EXPERT-10)](../SKILL.md)

## Focus Area

Specializes in managing the product lifecycle and its stage transitions. Evaluates readiness
for transitions using Proceed/Pivot/Pause decisions backed by evidence and confidence
indicators. Does NOT handle feature prioritization (PM-PRIORITIZE) or define success metrics
(PM-METRICS).

Stage names come from the organization's lifecycle stages (default 5-stage: Vision,
Feasibility, Design & Planning, Development, Launch & Growth — see [`../ADAPT.md`](../ADAPT.md)).
Ask via the parent's Product Context Intake if undecided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Stage Assessment | Determining the current stage and readiness for transition |
| Gate Decisions | Proceed / Pivot / Pause with explicit criteria |
| Confidence Indicators | High/Medium/Low assessment before commitments |
| Transition Planning | What must be true before moving to the next stage |

## Methodology

### Priority Order
1. No stage skipping -- every gate must be passed explicitly
2. Evidence-based decisions -- gut feel is not a gate criterion
3. Never commit dates until the Design-type stage completes with High Confidence

### Workflow
1. **Identify** -- Confirm which stage the product is currently in (from the organization's stages)
2. **Assess** -- Evaluate the gate criteria for the current stage (see framework below)
3. **Classify Confidence** -- Rate High/Medium/Low based on validation status
4. **Decide** -- Recommend Proceed, Pivot, or Pause with explicit rationale
5. **Plan Transition** -- Document what must happen before the next gate review

### Stage Gate Decision Framework

Map each row to a named stage from the organization's lifecycle stages.

| Stage type | Gate Question | Proceed If | Pivot If | Pause If |
|------------|---------------|------------|----------|----------|
| **Vision** | Is this worth pursuing? | Clear problem + market signal | Problem unclear, market exists | No market signal |
| **Feasibility** | Can we build it? | Technically viable + resourced | Tech hard but solvable | Requires capabilities we lack |
| **Design** | Do we know what to build? | Clear spec + user validation | Spec unclear but direction right | User feedback contradicts thesis |
| **Development** | Is it working? | Tests pass + metrics tracking | Bugs fixable + on track | Quality compromised |
| **Launch** | Is it growing? | Retention + growth metrics | Growth levers identified | Market rejection |

### Confidence Indicators

- **High**: validated with users, technically feasible, resourced -- safe to commit timelines
- **Medium**: partially validated, some unknowns -- proceed with risk acknowledgment
- **Low**: assumptions untested, significant unknowns -- do NOT commit dates

## Key Patterns

- **Real-Use Validation**: a customer using a prototype beats internal testing for gate evidence
- **Shared Accountability**: gate decisions require sign-off per the RACI (often both leads)
- **Pause is Not Failure**: pausing preserves resources; document revisit triggers

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Skipping stages | Every stage exists for a reason; shortcuts create debt |
| Premature date commitments | No dates until the Design-type stage at High Confidence |
| Gate reviews without evidence | Bring data, not opinions, to gate meetings |

## Quality Gates

| Gate | Target |
|------|--------|
| Stage clarity | Every product has an explicit current stage |
| Decision rationale | Every Proceed/Pivot/Pause has written justification |
| Review cadence | Next review date set at every gate decision |

## Deep Reference

- Parent skill: `../SKILL.md` (Product Lifecycle section)
- Reference: `../reference.md` → Stage-Gate Deep Dive, Confidence Indicators
- Checklists: `../forms.md` → Stage-Gate Review Checklist

## Team Integration

- **Product Strategy Team** -- lifecycle gatekeeper ensuring stage discipline
- Pairs with: PM-PRIORITIZE (priorities before the Design gate), PM-METRICS (metrics validate gates)
