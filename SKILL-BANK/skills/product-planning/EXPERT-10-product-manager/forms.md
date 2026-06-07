# Product Manager — Forms & Checklists

Ready-to-use intake, templates, and checklists. Product, lifecycle, audience, and path
specifics are the organization's decisions (see [`ADAPT.md`](ADAPT.md)); this file never
hardcodes them.

---

## Product Context Intake (the questionnaire for adapting this skill)

This is the questionnaire that captures the organization-specific decisions from `ADAPT.md`.
Ask as one numbered list and **WAIT** for answers; then record them wherever your team keeps
product decisions (a brief, a wiki, or your forked `SKILL.md`). Ask only what's missing.

**Business model & taxonomy:**
1. **Business model** — one line describing how the organization makes money and whether any
   business lines feed or fund each other.
2. **Product taxonomy** — for each product: a short code prefix, name, and current stage.
3. **Lifecycle stages** — the named stages a product passes through (or confirm the generic
   5-stage default: Vision → Feasibility → Design & Planning → Development → Launch & Growth).

**Audience:**
4. **Target users / ICP tiers** — primary segments, with device type / connectivity / literacy
   context where relevant.
5. **Device strategy norm** — mobile-first, desktop-first, or responsive-equal as the default,
   and why.

**Workspace / paths:**
6. **Products root** — where product folders live (path pattern).
7. **Progress file & next-steps file** — the filenames used for planning context and the
   execution queue.
8. **Template locations** — where document templates live.
9. **Naming conventions** — filename conventions for PRDs, stories, tasks, milestones.

---

## PRD Template (All Stages)

Use this same structure regardless of lifecycle stage. Content depth varies, but structure
stays consistent. Fill `Product`, `Code`, and `Stage` from the organization's product taxonomy
and lifecycle stages.

```markdown
# PRD: [Feature Name]

**Product**: [name from the product taxonomy]
**Code**: [code from the product taxonomy]-XXX
**Stage**: [stage from the lifecycle stages]
**Owner**: [Name]
**Status**: [Draft/Review/Approved]
**Last Updated**: [YYYY-MM-DD]

---

## 1. Executive Summary
[2-3 sentences: What are we building and why does it matter?]

## 2. Problem Statement

### 2.1 The Problem
[Specific problem we're solving. Include evidence.]

### 2.2 Who Has This Problem
[User segment from the organization's ICP tiers, with size estimate]
[Device context: Mobile-first or Desktop-first?]

### 2.3 Current Alternatives
[How do users solve this today? Why is that insufficient?]

### 2.4 Evidence Base
| Source | Finding | Date |
|--------|---------|------|
| User Research | [Quote or insight] | [Date] |
| Customer Feedback | [Pattern from the field] | [Date] |
| Analytics | [Metric showing problem] | [Date] |

### 2.5 Business-Model Insight
[If the business model describes a cross-line loop: how does this relate to the other line?
Otherwise omit.]

## 3. Solution Overview

### 3.1 Proposed Solution
[High-level description]

### 3.2 User Stories (MoSCoW Prioritized)
| Priority | As a... | I want to... | So that... |
|----------|---------|--------------|------------|
| MUST | [Persona] | [Action] | [Outcome] |
| SHOULD | [Persona] | [Action] | [Outcome] |
| COULD | [Persona] | [Action] | [Outcome] |

### 3.3 Out of Scope (WON'T)
[Explicitly state what we are NOT building in this iteration]

## 4. Success Metrics

### 4.1 North Star Metric
- **Metric:** [Name]
- **Current:** [Baseline]
- **Target:** [Goal]
- **Timeframe:** [When to measure]

### 4.2 Supporting Metrics
| Metric | Current | Target | Why It Matters |
|--------|---------|--------|----------------|
| [Name] | [Value] | [Goal] | [Rationale] |

### 4.3 Guardrail Metrics
[Metrics that should NOT get worse: e.g., load time, error rate]

## 5. Technical Requirements

### 5.1 Functional Requirements
[Numbered list of must-have functionality]

### 5.2 Non-Functional Requirements
- **Performance**: [e.g., response time <500ms]
- **Security**: [Data encryption, auth requirements]
- **Accessibility**: WCAG AA minimum
- **Device**: [Mobile-first/Desktop-first per the organization's positioning]

### 5.3 Testing Requirements
- Unit tests: Required before PR
- Integration tests: Required before merge
- E2E tests: Required before release

### 5.4 Technical Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Plan] |

## 6. Design Requirements

### 6.1 Design System Reference
- Brand: see the brand guidelines skill (brand tokens are the organization's decisions)
- Components: the design-system component library
- Device: [Mobile-first/Desktop-first]

### 6.2 Key UX Considerations
[Critical user flows, accessibility needs]

## 7. Cross-Functional Input

### 7.1 Design Review
- [ ] UX designer consulted on UX approach
- [ ] Designs linked

### 7.2 Engineering Review
- [ ] Frontend/backend engineer consulted on technical feasibility
- [ ] Architecture decisions documented

### 7.3 Business-Model Review
- [ ] Cross-line implications considered (if the business model has them)
- [ ] Other-line opportunity noted

## 8. Timeline & Milestones

| Milestone | Target | Owner |
|-----------|--------|-------|
| PRD Approved | [Date] | PM |
| Design Complete | [Date] | Design |
| Development Complete | [Date] | Eng |
| Testing Complete | [Date] | QA |
| Launch | [Date] | PM |

## 9. Stage-Gate Decision

**Next Review Date:** [Date]

| Option | Criteria | Recommendation |
|--------|----------|----------------|
| PROCEED | [What must be true] | |
| PIVOT | [What would trigger] | |
| PAUSE | [What would trigger] | |
```

---

## MoSCoW Prioritization Template

```markdown
## Feature Prioritization: [Release Name]

**Product**: [name + code from the product taxonomy]
**Stage**: [stage from the lifecycle stages]
**Date**: [YYYY-MM-DD]

### MUST HAVE (60% of capacity)
| ID | Feature | Rationale | Evidence |
|----|---------|-----------|----------|
| [CODE]-001 | [Feature] | [Why it's essential] | [Data/research] |

### SHOULD HAVE (20% of capacity)
| ID | Feature | Rationale | Trade-off |
|----|---------|-----------|-----------|
| [CODE]-002 | [Feature] | [Why it matters] | [What we lose if cut] |

### COULD HAVE (20% buffer)
| ID | Feature | If Time Allows | Effort |
|----|---------|----------------|--------|
| [CODE]-003 | [Feature] | [Benefit] | [Size] |

### WON'T HAVE (This Release)
| ID | Feature | Why Not Now | Future Consideration |
|----|---------|-------------|---------------------|
| [CODE]-004 | [Feature] | [Reason] | [When to revisit] |
```

---

## Stakeholder / Investor Update Template

```markdown
## [Product] Monthly Update - [Month Year]

### Headline (30 seconds)
[One sentence: Biggest win + biggest challenge this month]

### Progress Snapshot

| Metric | Last Month | This Month | Trend |
|--------|------------|------------|-------|
| [North Star] | [Value] | [Value] | [+/-] |
| [Secondary 1] | [Value] | [Value] | [+/-] |
| [Secondary 2] | [Value] | [Value] | [+/-] |

### Lifecycle Stage
- **Current**: [Stage from the lifecycle stages]
- **Stage Gate**: [Date] -- [PROCEED/PIVOT/PAUSE expected]

### Key Milestones

| Milestone | Status | Notes |
|-----------|--------|-------|
| [Milestone 1] | [Done/In Progress/Blocked] | [Brief note] |
| [Milestone 2] | [Done/In Progress/Blocked] | [Brief note] |

### Business-Model Insights
[What we learned from one business line that informs the other — if the model has a loop]

### Ask
[What do you need from stakeholders? (Nothing is a valid answer)]

### Next Month Focus
[Top 3 priorities]
```

---

## PRD Review Checklist

```
Product Context:
- [ ] Product code assigned (from the product taxonomy)
- [ ] Lifecycle stage specified (from the lifecycle stages)
- [ ] Device strategy correct (per the organization's positioning)

Prioritization:
- [ ] MoSCoW prioritization complete
- [ ] Every MUST-have has evidence
- [ ] Won't-have items explicitly listed

Business Model:
- [ ] Cross-line angle documented (if the business model has one)
- [ ] Customer pain points considered
- [ ] Other-line opportunity noted

Cross-Functional:
- [ ] UX designer consulted
- [ ] Engineering consulted
- [ ] Architecture decisions documented

Quality:
- [ ] Success metrics defined (North Star + supporting)
- [ ] Guardrail metrics identified
- [ ] Testing requirements specified
- [ ] Technical risks assessed
```

---

## Stage-Gate Review Checklist

```
- [ ] Which stage are we in? (from the lifecycle stages)
- [ ] What evidence do we have?
- [ ] What's the recommendation: PROCEED / PIVOT / PAUSE?
- [ ] What must be true to proceed?
- [ ] What would trigger a pivot?
- [ ] What would trigger a pause?
- [ ] Next review date set?
```

---

## MoSCoW Quick Decision Checklist

```
For each feature, ask:
- [ ] MUST: Will users abandon without this?
- [ ] SHOULD: Does this significantly improve experience?
- [ ] COULD: Is this a nice enhancement?
- [ ] WON'T: Why are we saying no (for now)?

Validation:
- [ ] Evidence supports the classification?
- [ ] MUST items total < 60% of capacity?
- [ ] WON'T items explicitly documented?
```
