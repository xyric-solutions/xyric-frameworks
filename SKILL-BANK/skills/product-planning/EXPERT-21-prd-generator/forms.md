# PRD Generator — Forms & Checklists

The PRD output template, quality checklists, activation checklist, and section-by-section
validation criteria. Load on demand during PRD generation. Audience, taxonomy, and file
paths are decided per organization (see [`ADAPT.md`](ADAPT.md)); this file never hardcodes them.

---

## PRD Context Intake (the questionnaire for adapting this skill)

This is the questionnaire for the per-organization values this skill consumes (see
[`ADAPT.md`](ADAPT.md)). Ask as one numbered list and **WAIT** for answers; record the answers
wherever your team keeps product decisions (a working brief or your forked copy). Ask only
what's not already decided.

**Audience & messaging:**
1. **Target segments** — who are the primary user/customer segments? (one line each)
2. **Primary segment** — which segment is most important to serve first?
3. **Key messages** — the 5–9 messages each persona/feature must reinforce?
4. **Differentiators** — what makes this product different from alternatives?

**Business model & taxonomy:**
5. **Lifecycle stage** — what stage is this product in (e.g. design/planning, development)?
6. **Product taxonomy** — product code/name, or service line, this PRD belongs to?
7. **Monetization** — monetized at MVP, or "not monetized yet"?

**Workspace & paths:**
8. **Vision/PRD location** — where do product folders live, and what is the vision filename
   pattern?
9. **PRD output name** — the filename convention for the requirements document?
10. **Progress file** — the per-product status file to update?
11. **Template location** — where do PRD/section templates live?

---

## PRD Output Template

```markdown
# [Product Name] — PRODUCT REQUIREMENTS DOCUMENT
**[Tagline from Vision]**

---

## DOCUMENT INFORMATION

| Attribute | Value |
|-----------|-------|
| **Product** | [Product Name] |
| **Version** | 1.0 |
| **Status** | Draft / Review / Approved |
| **Owner** | [Product Owner] |
| **Last Updated** | [Date] |
| **Vision Document** | [Link to Vision] |

---

## EXECUTIVE SUMMARY

### Product Definition
[Product Name] is [brief description — 2-3 sentences inheriting from Vision].

### Core Value Proposition
[Primary value proposition from Vision — 1-2 sentences]

### Key Differentiators
1. [Differentiator 1 from Vision / your differentiators]
2. [Differentiator 2]
3. [Differentiator 3]
4. [Differentiator 4]

### MVP Scope Overview
**In Scope (MVP v1.0):**
- [Feature area 1]
- [Feature area 2]
- [Feature area 3]

**Out of Scope (Post-MVP):**
- [Future feature 1]
- [Future feature 2]

---

## PRODUCT VISION & QUALITY METRICS

> **Note:** Business metrics (revenue, market share, CAC/LTV) are handled in separate
> business planning documents. This section focuses on product quality and user success.

### North Star Metric
**[Primary product success metric]**: [Target value]

### Product Quality Metrics Dashboard

| Category | Metric | MVP Target | Ultimate Target | Measurement |
|----------|--------|------------|-----------------|-------------|
| User Adoption | [Metric] | [Target] | [Vision target] | [How measured] |
| Engagement | [Metric] | [Target] | [Vision target] | [How measured] |
| Retention | [Metric] | [Target] | [Vision target] | [How measured] |
| Performance | [Metric] | [Target] | [Vision target] | [How measured] |
| Satisfaction | [Metric] | [Target] | [Vision target] | [How measured] |
| Quality | [Metric] | [Target] | [Vision target] | [How measured] |
| Accessibility | [Metric] | [Target] | [Vision target] | [How measured] |
| Reliability | [Metric] | [Target] | [Vision target] | [How measured] |

---

## CORE DESIGN PRINCIPLES

### Principle 1: [Name]
**"[Principle statement]"**

**Application:**
- [How this applies to product decisions]
- [Example of this principle in action]
- [What this means for features]

### Principle 2: [Name]
...

### Principle 3: [Name]
...

[3-5 principles that guide all product decisions]

---

## USER PERSONAS

> Derive personas from your audience segments; enrich existing persona context, don't replace it.

### P1: [Persona Name] (Primary)

**Demographics:**
- **Age**: [Range]
- **Role**: [Job title/role]
- **Technical Proficiency**: [Low/Medium/High]
- **Location**: [Geographic context]

**Background:**
[2-3 sentences describing this persona]

**Goals:**
- [Goal 1]
- [Goal 2]
- [Goal 3]

**Pain Points:**
- "[Pain point 1 — in their words]"
- "[Pain point 2 — in their words]"
- "[Pain point 3 — in their words]"

**Success Story:**
"[Quote describing what success looks like for this persona]"

**Feature Priorities:**
| Priority | Features |
|----------|----------|
| Must Have | [Features this persona needs] |
| Should Have | [Features that help] |
| Could Have | [Nice to have] |

---

### P2: [Persona Name]
...

### P3: [Persona Name]
...

### P4: [Persona Name]
...

### P5: [Persona Name]
...

---

## EPIC OVERVIEW MAP

### Visual Hierarchy

[Generate Mermaid flowchart TB diagram showing epic layers and dependencies]

### Epic Summary Table

| Epic | Name | Focus | Features | Priority | MVP Status | Dependencies |
|------|------|-------|----------|----------|------------|--------------|
| E01 | [Name] | [Focus area] | [Count] | P0 | Core | None |
| E02 | [Name] | [Focus area] | [Count] | P0 | Core | E01 |
| E03 | [Name] | [Focus area] | [Count] | P1 | MVP | E01, E02 |
| E04 | [Name] | [Focus area] | [Count] | P1 | MVP | E01 |
| E05 | [Name] | [Focus area] | [Count] | P2 | Enhanced | E01-E04 |
| ... | ... | ... | ... | ... | ... | ... |

### Epic Descriptions

#### E01: [Epic Name]
**Goal:** [What this epic achieves]
**Scope:** [What's included]
**Key Features:**
- F1.1: [Feature name]
- F1.2: [Feature name]
- F1.3: [Feature name]

**Personas Served:** P1, P2
**Dependencies:** None (foundation epic)
**MVP Status:** Core

---

#### E02: [Epic Name]
...

[Continue for all epics]

---

## MVP vs FUTURE SCOPE MATRIX

### Feature Scope by Epic

| Epic | Feature | MVP v1.0 | v1.1 | v2.0 | Future |
|------|---------|----------|------|------|--------|
| E01 | F1.1 | yes | | | |
| E01 | F1.2 | yes | | | |
| E01 | F1.3 | | yes | | |
| E02 | F2.1 | yes | | | |
| E02 | F2.2 | yes | | | |
| E02 | F2.3 | | | yes | |
| ... | ... | ... | ... | ... | ... |

### MVP Definition
**MVP v1.0 includes:**
- Epic 1: [All/Partial] features
- Epic 2: [All/Partial] features
- Epic 3: [All/Partial] features

**MVP v1.0 excludes:**
- Epic 5+: All features
- Advanced features from Epics 1-4

---

## SUCCESS CRITERIA CHECKLIST

### Epic 1: [Name]
- [ ] [Success criterion 1 — testable]
- [ ] [Success criterion 2 — testable]
- [ ] [Success criterion 3 — testable]

### Epic 2: [Name]
- [ ] [Success criterion 1 — testable]
- [ ] [Success criterion 2 — testable]
- [ ] [Success criterion 3 — testable]

### MVP Launch Criteria
- [ ] All P0 features complete and tested
- [ ] Performance targets met ([specific metrics])
- [ ] Security audit passed
- [ ] Accessibility compliance verified (WCAG [level])
- [ ] User acceptance testing completed
- [ ] Documentation complete

---

## FEATURE TEMPLATE REFERENCE

All features in Epic PRDs follow this standard format:

### F[Epic].[Seq]: [Feature Name]

**Priority:** P0/P1/P2/P3
**MVP Status:** Core / MVP / Enhanced / Future
**Personas:** P1, P2

**Description:**
[1-2 paragraph description of the feature]

**User Story:**
As a [persona], I want to [action] so that [benefit].

**Success Metrics:**
| Metric | Target |
|--------|--------|
| [Metric 1] | [Value] |
| [Metric 2] | [Value] |

**Acceptance Criteria:**
- [ ] [Criterion 1 — testable]
- [ ] [Criterion 2 — testable]
- [ ] [Criterion 3 — testable]

**Error Scenarios:**
| Scenario | Handling |
|----------|----------|
| [Error 1] | [Response] |
| [Error 2] | [Response] |

**Dependencies:**
- F[X.Y]: [Dependency description]

---

## CROSS-REFERENCE INDEX

### Vision to PRD Mapping

| Vision Section | PRD Section | Notes |
|----------------|-------------|-------|
| Strategic Objective 1 | Epic 1 | [Coverage notes] |
| Strategic Objective 2 | Epic 2, 3 | [Coverage notes] |
| Value Prop - Segment 1 | Persona P1 | [Coverage notes] |
| Value Prop - Segment 2 | Persona P2 | [Coverage notes] |

### PRD to Epic PRD Mapping

| PRD Epic | Epic PRD Document | Status |
|----------|-------------------|--------|
| E01 | [epic-PRD file for E01] | [Status] |
| E02 | [epic-PRD file for E02] | [Status] |
| ... | ... | ... |

---

## COMPETITIVE ANALYSIS (INSPIRATION FOCUS)

> **Purpose:** Learn from existing solutions. Don't reinvent the wheel. This is NOT market
> positioning analysis.

### What We Can Learn From Others

**[Category 1: Direct Alternatives]**

| Solution | What They Do Well | Patterns to Adopt | Our Differentiation |
|----------|-------------------|-------------------|---------------------|
| [Solution A] | [Strength] | [Pattern to learn] | [How we're different] |
| [Solution B] | [Strength] | [Pattern to learn] | [How we're different] |

**[Category 2: Adjacent Products]**

| Solution | What They Do Well | Patterns to Adopt | Our Differentiation |
|----------|-------------------|-------------------|---------------------|
| [Solution C] | [Strength] | [Pattern to learn] | [How we're different] |
| [Solution D] | [Strength] | [Pattern to learn] | [How we're different] |

### Best Practices to Adopt

| Practice | Source | Implementation |
|----------|--------|----------------|
| [Practice 1] | Industry standard | [How we'll implement] |
| [Practice 2] | From [Solution A] | [How we'll implement] |
| [Practice 3] | UX best practice | [How we'll implement] |

### Where Others Fall Short (Our Opportunity)

| Gap | Why Existing Solutions Fail | Our Approach |
|-----|----------------------------|--------------|
| [Gap 1] | [Why they fail] | [How we solve it] |
| [Gap 2] | [Why they fail] | [How we solve it] |
| [Gap 3] | [Why they fail] | [How we solve it] |

### Design Inspiration

| Element | Inspiration Source | Application |
|---------|-------------------|-------------|
| [UI Pattern] | [Source] | [How we'll use it] |
| [UX Flow] | [Source] | [How we'll use it] |
| [Feature approach] | [Source] | [How we'll use it] |

---

## ERROR HANDLING & EDGE CASES

### Global Error Handling Patterns

| Error Type | User Message | System Action | Logging |
|------------|--------------|---------------|---------|
| Network failure | "Connection lost. Retrying..." | Auto-retry 3x | Error + context |
| Auth expired | "Please sign in again" | Redirect to login | Info |
| Invalid input | "[Specific validation message]" | Highlight field | Debug |
| Server error | "Something went wrong. We're on it." | Send alert | Error + stack |
| Rate limited | "Too many requests. Try again in [X]" | Backoff | Warning |

### Edge Cases by Epic

**Epic 1: [Name]**
| Scenario | Handling |
|----------|----------|
| [Edge case 1] | [How handled] |
| [Edge case 2] | [How handled] |

**Epic 2: [Name]**
...

---

## ACCESSIBILITY REQUIREMENTS

### Compliance Target
**WCAG 2.1 Level AA** (or as specified)

### Core Requirements

| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Color Contrast | 4.5:1 minimum | Design system tokens |
| Keyboard Navigation | Full keyboard support | Tab order, focus indicators |
| Screen Reader | ARIA labels | Semantic HTML, ARIA |
| Text Scaling | Up to 200% | Responsive typography |
| Motion | Reduced motion option | `prefers-reduced-motion` |
| Touch Targets | 44x44px minimum | Button sizing standards |

### Testing Requirements
- [ ] Automated accessibility testing (axe, WAVE)
- [ ] Screen reader testing (VoiceOver, NVDA)
- [ ] Keyboard-only navigation testing
- [ ] Color contrast verification
- [ ] Mobile accessibility testing

---

## ACCOUNT MANAGEMENT

### Account Types

| Type | Access | Features | Limits |
|------|--------|----------|--------|
| Free | Basic | [Features] | [Limits] |
| Premium | Full | [Features] | [Limits] |
| Enterprise | Custom | [Features] | [Limits] |

### Account Lifecycle

[Generate Mermaid stateDiagram-v2 showing: SignUp -> Active -> Upgraded/Churned/Downgraded]

### Data Retention
- Active accounts: [Policy]
- Inactive accounts: [Policy]
- Deleted accounts: [Policy]

---

## AI SAFETY BOUNDARIES

*[Include this section if the product has AI capabilities]*

### AI Principles
1. **Transparency**: [How AI decisions are explained]
2. **Human Control**: [When human override is available]
3. **Safety First**: [What AI must never do]

### Prohibited AI Actions
- [ ] [Prohibited action 1]
- [ ] [Prohibited action 2]
- [ ] [Prohibited action 3]

### Crisis Detection & Escalation
*[If applicable — e.g., healthcare, mental health]*

| Signal | Detection | Response |
|--------|-----------|----------|
| [Crisis type 1] | [How detected] | [Escalation path] |
| [Crisis type 2] | [How detected] | [Escalation path] |

### AI Disclaimers
- [Disclaimer 1 — when shown]
- [Disclaimer 2 — when shown]

---

## DATA MANAGEMENT

### Data Classification

| Data Type | Classification | Encryption | Retention |
|-----------|----------------|------------|-----------|
| User PII | Sensitive | AES-256 | Account lifetime |
| Usage Data | Internal | AES-256 | [Period] |
| Analytics | Aggregated | TLS | [Period] |
| AI Training | [Policy] | [Policy] | [Policy] |

### Data Sources

| Source | Data Type | Integration | Frequency |
|--------|-----------|-------------|-----------|
| [Source 1] | [Type] | [API/Import] | [Real-time/Daily] |
| [Source 2] | [Type] | [API/Import] | [Real-time/Daily] |

### Privacy Compliance
- [ ] GDPR compliance (EU users)
- [ ] CCPA compliance (California users)
- [ ] [Industry-specific]: [Requirement]

### Data Export
- User data export: [Format, method]
- Bulk export: [Enterprise only]

---

## DOCUMENT GOVERNANCE

### Review Schedule
- **Weekly**: Feature prioritization adjustments
- **Monthly**: Epic progress review
- **Quarterly**: Full PRD alignment with Vision

### Change Control
| Change Type | Approval Required | Process |
|-------------|-------------------|---------|
| Minor (typos, clarification) | None | Direct edit |
| Feature scope | Product Owner | Review meeting |
| Epic scope | Product + Engineering | Change request |
| Strategic (MVP change) | Leadership | Vision alignment review |

### Related Documents
| Document | Location | Status |
|----------|----------|--------|
| Vision Document | [Link] | Approved |
| Epic PRDs | [epic-PRD folder] | [Status] |
| Design System | [design folder] | [Status] |
| Stories | [stories folder] | [Status] |

---

**PRD Established:** [Date]
**Next Review:** [Date]
**PRD Owner:** [Name/Role]

---

*[Product Name] Product Requirements Document v1.0 | [Date]*

<!-- ARCHITECTURE_READY: [product-code] -->
```

---

## Quality Checklist

### Section Completeness Check
- [ ] Document Information (metadata table)
- [ ] Executive Summary (definition, value prop, differentiators, MVP scope)
- [ ] Product Vision & Quality Metrics (north star, 8+ product metrics — NO revenue)
- [ ] Core Design Principles (3-5 principles with applications)
- [ ] User Personas (5 personas with full template)
- [ ] Epic Overview Map (visual, table, descriptions)
- [ ] MVP vs Future Scope Matrix (feature-level scope)
- [ ] Success Criteria Checklist (by epic, launch criteria)
- [ ] Feature Template Reference (standard format)
- [ ] Cross-Reference Index (Vision to PRD, PRD to Epics)
- [ ] Competitive Analysis (INSPIRATION focus — learn from others, NOT market positioning)
- [ ] Error Handling & Edge Cases (patterns, by epic)
- [ ] Accessibility Requirements (WCAG target, requirements, testing)
- [ ] Account Management (types, lifecycle, retention)
- [ ] AI Safety Boundaries (if applicable)
- [ ] Data Management (classification, sources, privacy)
- [ ] Document Governance (schedule, change control)

### Vision Alignment Check
- [ ] Every strategic objective mapped to epic/features
- [ ] Every value proposition addressed
- [ ] Every persona segment has features
- [ ] Success metrics aligned with vision targets
- [ ] Constraints and scope respected
- [ ] Differentiators reflected in features

### Quality Standards Check
- [ ] All metrics are quantified (numbers, percentages, targets)
- [ ] All features have MoSCoW priority tags
- [ ] All epics have dependency mapping
- [ ] No placeholder text (TBD, [fill in], etc.)
- [ ] Consistent product name throughout
- [ ] Consistent persona references (P1-P5)

### Visual Documentation Check
- [ ] System Architecture diagram in Epic Overview Map section
- [ ] User Journey Map for primary persona (P1) included
- [ ] Feature Priority Matrix if 8+ features defined
- [ ] Error Recovery Decision Tree in Error Handling section
- [ ] Account Lifecycle state diagram in Account Management section
- [ ] Data Flow Architecture if multi-source data integration
- [ ] AI Agent Interaction diagram if AI product
- [ ] All diagrams use a consistent color scheme (blue/yellow/green/red)
- [ ] All Mermaid syntax renders correctly

---

## Activation Checklist

When this skill is activated:

**Phase 0: Research**
1. [ ] Confirm the per-organization values (audience, taxonomy, paths) — see `ADAPT.md`
2. [ ] Locate the Vision Document for the product (in the product folder)
3. [ ] Extract strategic objectives, segments, constraints
4. [ ] Read the PRD template / existing PRDs for patterns
5. [ ] Load product context files (if available)
6. [ ] Generate Vision Analysis Summary (~400 words)

**Phase 1: Analysis**
7. [ ] Invoke the Assumption Challenge (unless bypassed)
8. [ ] Present Vision Analysis to user
9. [ ] Ask 7 tailored clarification questions
10. [ ] **WAIT for user responses**
11. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
12. [ ] Apply user decisions to PRD structure
13. [ ] Generate 15 sections sequentially using the template above
14. [ ] Cross-reference with Vision objectives
15. [ ] Generate Mermaid diagrams for visual documentation
16. [ ] Build Vision Coverage Matrix

**Phase 3: Validation (Blocking)**
17. [ ] Verify all required sections complete
18. [ ] Verify 100% Vision objective coverage
19. [ ] Verify all personas have features
20. [ ] Verify no placeholder text remains
21. [ ] If fails: return to Phase 2 and fix

**Phase 4: Output**
22. [ ] Write the PRD file (path/name per your convention)
23. [ ] Update the per-product progress file
24. [ ] Include pipeline hooks for the architecture skill
25. [ ] Present completion summary

---

## Section-by-Section Validation Criteria

| # | Section | Required Elements | Fail Condition |
|---|---------|-------------------|----------------|
| 1 | Document Information | Product, Version, Status, Owner, Date, Vision link | Missing any field |
| 2 | Executive Summary | Definition, value prop, differentiators (4+), MVP scope | Fewer than 4 differentiators |
| 3 | Product Vision & Metrics | North star metric, 8+ metrics table | Fewer than 8 metrics or unquantified targets |
| 4 | Core Design Principles | 3-5 principles with application bullets | Fewer than 3 principles |
| 5 | User Personas | 5 personas with demographics, goals, pain points, feature priorities | Fewer than 5 or missing template fields |
| 6 | Epic Overview Map | Visual diagram, summary table, per-epic descriptions | Missing visual or descriptions |
| 7 | MVP vs Future Scope | Feature-level matrix across versions | Missing version columns |
| 8 | Success Criteria | Per-epic checklists, MVP launch criteria | Missing launch criteria |
| 9 | Feature Template | Standard format documented | Missing format specification |
| 10 | Cross-Reference Index | Vision-to-PRD mapping, PRD-to-Epic mapping | Missing either mapping table |
| 11 | Competitive Analysis | 4+ solutions, best practices, gaps | Fewer than 4 solutions or missing inspiration framing |
| 12 | Error Handling | Global patterns table, per-epic edge cases | Missing global patterns |
| 13 | Accessibility | WCAG target, 6+ requirements, testing checklist | Missing WCAG target |
| 14 | Account Management | Types table, lifecycle diagram, retention policies | Missing lifecycle |
| 15 | AI Safety Boundaries | Principles, prohibited actions, escalation (if AI product) | Missing if product has AI |
| 16 | Data Management | Classification, sources, privacy checklist | Missing classification |
| 17 | Document Governance | Review schedule, change control table, related docs | Missing change control |
