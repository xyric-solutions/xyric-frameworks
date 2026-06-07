---
name: PM-METRICS
parent: EXPERT-10
description: Product metrics definition, success criteria, validation plans, and objective alignment
version: "1.0"
domain: Product measurement and validation
---

# Product Metrics & Validation (PM-METRICS)

> Sub-skill of [Product Manager (EXPERT-10)](../SKILL.md)

## Focus Area

Specializes in defining what success looks like for a product or feature: North Star metrics,
supporting KPIs, guardrail metrics, and validation methodology. Aligns product metrics with
company objectives. Does NOT handle feature prioritization (PM-PRIORITIZE) or lifecycle stage
decisions (PM-STAGEGATE).

Product context — the product taxonomy and audience/positioning — is the organization's
decision (see [`../ADAPT.md`](../ADAPT.md)); ask via the parent's Product Context Intake if
undecided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| North Star Definition | Single metric that captures product value delivery |
| KPI Framework | Supporting + guardrail metrics hierarchy |
| Validation Planning | A/B testing methodology, success/failure criteria |
| Objective Alignment | Connecting product metrics to company objectives |

## Methodology

### Priority Order
1. Outcomes over output -- measure user value, not feature count
2. Guardrails protect quality -- track what must NOT get worse
3. Every metric needs a baseline, target, and timeframe

### Workflow
1. **Define North Star** -- One metric that best represents value delivery for this product/feature
2. **Add Supporting Metrics** -- 2-4 metrics that lead to or explain the North Star
3. **Set Guardrails** -- Metrics that must not degrade (load time, error rate, existing retention)
4. **Establish Baselines** -- Current values for all metrics before launch
5. **Create Validation Plan** -- How and when to measure, success/failure thresholds

### Metrics Hierarchy

- **North Star**: core value metric (e.g., monthly active users of the core value action)
- **Supporting**: leading indicators (2-4 metrics explaining the North Star)
- **Guardrail**: must not degrade (load time, error rate, existing retention)
- **Diagnostic**: debug when metrics move (funnel steps, cohort breakdowns)

### Validation Methodology

- **Pre-launch**: document baselines + expected impact range
- **Soft launch**: release to a 10-20% subset, measure against guardrails
- **Evaluation**: minimum 2 weeks behavioral, 4 weeks retention
- **Decision criteria**: pre-define success, failure, and inconclusive thresholds

### Objective Connection

Trace: `Company Objective -> Department KR -> Product Metric -> Feature Success Criteria`.
Use the organization's objective/OKR system if one exists.

## Key Patterns

- **Anti-Vanity**: track retention and engagement, not downloads -- vanity metrics hide problems
- **Cross-Line Metrics**: when the business model has a field-to-product loop, field signals
  (customer NPS, repeat rate) validate product-market fit
- **Confidence-Gated Targets**: before the Design-type stage, express targets as ranges, not fixed numbers

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Feature factory mentality | Measure outcomes (user value), not output (features shipped) |
| Vanity metrics focus | Track retention and engagement, not raw downloads |
| No baseline measurement | Always capture current state before launching changes |

## Quality Gates

| Gate | Target |
|------|--------|
| North Star defined | Every product has exactly one North Star metric |
| Baseline documented | All metrics have current values before launch |
| Guardrails set | At least 2 guardrail metrics per feature launch |

## Deep Reference

- Parent skill: `../SKILL.md` (Success Criteria, anti-patterns)
- Reference: `../reference.md` → Depth Requirements
- Checklists: `../forms.md` → PRD Success Metrics, Stakeholder / Investor Update Template

## Team Integration

- **Product Strategy Team** -- measurement specialist ensuring data-driven decisions
- Pairs with: PM-PRIORITIZE (metrics validate priorities), PM-STAGEGATE (metrics inform gates)
