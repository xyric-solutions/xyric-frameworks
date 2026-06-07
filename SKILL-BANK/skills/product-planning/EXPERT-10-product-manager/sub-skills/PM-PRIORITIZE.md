---
name: PM-PRIORITIZE
parent: EXPERT-10
description: Feature prioritization using MoSCoW, effort/impact scoring, and evidence-based triage
version: "1.0"
domain: Feature prioritization and backlog decisions
---

# Feature Prioritization (PM-PRIORITIZE)

> Sub-skill of [Product Manager (EXPERT-10)](../SKILL.md)

## Focus Area

Specializes in classifying, scoring, and triaging features using MoSCoW as the primary
method, supplemented by effort/impact analysis. Handles stakeholder alignment on priority
conflicts and trade-off decisions. Does NOT write full PRDs (parent skill), define stage
gates (PM-STAGEGATE), or set success metrics (PM-METRICS).

Product codes come from the organization's product taxonomy (see [`../ADAPT.md`](../ADAPT.md));
ask via the parent's Product Context Intake if undecided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| MoSCoW Classification | Evidence-backed Must/Should/Could/Won't decisions |
| Effort/Impact Scoring | Relative sizing, capacity allocation (60/20/20 rule) |
| Stakeholder Alignment | Resolving priority conflicts with data, not opinions |
| Scope Management | Explicit Won't-have documentation to prevent creep |

## Methodology

### Priority Order
1. Evidence over intuition -- every MUST requires proof
2. Capacity-aware -- MUSTs cannot exceed 60% of capacity
3. Explicit exclusions -- Won't-haves are decisions, not omissions

### Workflow
1. **Gather** -- Collect feature candidates from backlog, customer feedback, cross-line signals
2. **Classify** -- Apply MoSCoW to each item using the decision criteria below
3. **Score** -- Estimate effort (T-shirt: XS/S/M/L/XL) and impact (1-5 scale)
4. **Validate** -- Cross-check MUSTs against evidence; run an assumption challenge for contested items
5. **Align** -- Present the prioritized list to stakeholders using the RACI from the parent reference

### MoSCoW Decision Criteria

| Category | Decision Question | Evidence Required |
|----------|-------------------|-------------------|
| **MUST** | Will users abandon without this? | User research showing a dealbreaker |
| **SHOULD** | Does this significantly improve experience? | Usage data or feedback pattern |
| **COULD** | Is this a nice enhancement? | Occasional requests, not blocking |
| **WON'T** | Why are we saying no (for now)? | Resource constraints or strategic focus |

Acceptable evidence: user research, customer feedback patterns (3+ customers), analytics data,
competitive analysis, regulatory requirements.

## Key Patterns

- **Cross-Line Signal**: when the business model has a field-to-product loop, 3+ customers with
  the same pain escalates to product review automatically
- **Capacity Guard**: if MUSTs exceed 60%, re-examine -- something is likely a SHOULD
- **Trade-off Framing**: present SHOULDs as "what we lose if cut" for tangible trade-offs
- **Scope Creep Prevention**: Won't-haves with a "when to revisit" date prevent re-litigation

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| HiPPO-driven priorities | Validate with users/customers first; evidence trumps authority |
| Unlabeled backlog items | Every item gets a MoSCoW tag before sprint planning |
| MUSTs without evidence | Challenge classification; downgrade to SHOULD until proven |
| Missing Won't-haves | Explicitly document exclusions with rationale |

## Quality Gates

| Gate | Target |
|------|--------|
| MUST coverage | Every MUST item has linked evidence |
| Capacity fit | MUSTs <= 60%, SHOULDs ~20%, COULDs ~20% buffer |
| Won't documentation | All excluded items have rationale + revisit date |
| Stakeholder sign-off | Priority list reviewed per the RACI matrix |

## Deep Reference

- Parent skill: `../SKILL.md` (full method, cross-skill integration)
- Reference: `../reference.md` → MoSCoW Decision Criteria, Evidence-Based Prioritization
- Checklists: `../forms.md` → MoSCoW Prioritization Template, MoSCoW Quick Decision Checklist

## Team Integration

This sub-skill is designed for use in:
- **Product Strategy Team** -- as the prioritization specialist driving backlog decisions
- Pairs well with: PM-STAGEGATE (gate readiness depends on priority clarity), PM-METRICS
  (success criteria validate priority choices)
