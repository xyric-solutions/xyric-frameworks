# Brainstormer — Forms & Checklists

Loaded on demand for the brainstorm-document output template, the org-context intake, quality
checklists, and the activation checklist. Organization-specific context (business model,
lifecycle stages, portfolio, audience, paths) is decided per organization — see
[`ADAPT.md`](ADAPT.md); this file never hardcodes it.

---

## Org Context Intake (the questionnaire for adapting this skill)

Ask only what's not yet decided, as one numbered list, and **WAIT** for answers; then record
them wherever your team keeps these decisions (or bake them into your forked copy). These
sharpen classification, portfolio gap analysis, and lifecycle placement. If the user declines,
produce a GENERIC DRAFT and flag those notes as placeholders.

1. **Business model** — one line: how does the organization make money and where does this
   idea fit?
2. **Offering types** — do you classify offerings as products vs. client services, or some
   other taxonomy?
3. **Existing portfolio** — what offerings already exist (name + lifecycle stage), so I can
   check this idea for overlap?
4. **Lifecycle stages** — do you use custom stage names, or the default (Vision, Feasibility,
   Design & Planning, Development, Launch & Growth)?
5. **Core differentiating capability** — what does your organization uniquely enable (e.g. an
   AI-native capability) that should be one of the three expansion lenses?
6. **Audience / ICP** — who are the target customer segments this idea would serve?
7. **Where offerings live** — the root folder pattern for an offering's docs, and the
   brainstorm/vision file names?

---

## Output Format: brainstorm document

The vision-ready marker is an HTML comment placed at the top of the document. Use the literal
form `<!-- VISION_READY: CODE -->` and replace `CODE` with the offering's short code (you ask
the user for it, or derive it from the organization/offering name). Replace every `[...]`
bracket with real content at write time.

### Document structure

```markdown
# [Product Name] - Brainstorm Document

<!-- VISION_READY: CODE -->

> **Status**: Ready for Vision Generator
> **Brainstorm Date**: [date]
> **Participants**: [user], Brainstormer skill

---

## Executive Snapshot

| Element | Summary |
|---------|---------|
| **One-liner** | [25 words max: What is this?] |
| **Problem** | [25 words: What problem does it solve?] |
| **Solution** | [25 words: How does it solve it?] |
| **Primary User** | [Specific persona in one phrase] |
| **Unique Value** | [What makes this different?] |

---

## Raw Ideas Inventory

### Problem Space
- [Captured problem 1]
- [Captured problem 2]

### Solution Ideas
- [Captured feature/approach 1]
- [Captured feature/approach 2]

### Technical Direction
- [Captured tech approach]

### Inspirations
- [Captured references]

---

## Challenged Assumptions

### WHY: Existence & Purpose
**Q**: [Question asked]
**A**: [User's response]
**Insight**: [What we learned]

### WHO: Users & Stakeholders
**Q**: [Question asked]
**A**: [User's response]
**Insight**: [What we learned]

### WHAT: Scope & Definition
**Q**: [Question asked]
**A**: [User's response]
**Insight**: [What we learned]

### HOW: Feasibility & Mechanism
**Q**: [Question asked]
**A**: [User's response]
**Insight**: [What we learned]

### WHAT-IF: Risks & Failure Modes
**Q**: [Question asked]
**A**: [User's response]
**Insight**: [What we learned]

---

## Resolved Tensions

### Tension 1: [Title]
- **Conflict**: [A vs B]
- **Resolution**: [Decision made]
- **Rationale**: [Why this choice]

### Defined Terms
| Term | Definition |
|------|------------|
| [Vague term 1] | [Specific meaning in this context] |
| [Vague term 2] | [Specific meaning in this context] |

---

## User Clarity

### Primary Persona
- **Who**: [Specific description]
- **Frustration**: [Core pain point]
- **Goal**: [What they want to achieve]
- **Context**: [When/where they experience the problem]

### Anti-Persona (NOT our user)
- **Who**: [Who this is NOT for]
- **Why Not**: [What makes them different]

---

## Problem Clarity

### Problem Statement
[Clear, specific problem statement]

### Evidence
- **Type 1**: [Evidence source and finding]
- **Type 2**: [Evidence source and finding]

### Why Existing Solutions Fail
| Solution | Why It Fails |
|----------|--------------|
| [Alternative 1] | [Limitation] |
| [Alternative 2] | [Limitation] |

---

## Solution Clarity

### Core Capabilities (Must Have)
1. [Capability 1] - [why it's essential]
2. [Capability 2] - [why it's essential]
3. [Capability 3] - [why it's essential]

### Out of Scope (Explicit Exclusions)
- [Exclusion 1] - [why excluded]
- [Exclusion 2] - [why excluded]

### Nice to Have (Future)
- [Future capability 1]
- [Future capability 2]

---

## Technical Approach Clarity

### High-Level Approach
[Brief description of technical direction]

### Key Technical Decisions
- [Decision 1]: [Choice made and why]
- [Decision 2]: [Choice made and why]

### Technical Risks
- [Risk 1]: [Mitigation approach]
- [Risk 2]: [Mitigation approach]

---

## Risk Registry

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Approach] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Approach] |
| [Risk 3] | High/Med/Low | High/Med/Low | [Approach] |

---

## Open Questions (For Vision Phase)

| Question | Why It Matters | Owner |
|----------|----------------|-------|
| [Question 1] | [Impact on vision] | Vision Generator |
| [Question 2] | [Impact on vision] | Vision Generator |

---

## Vision Generator Handoff

### Readiness Checklist
- [x] Problem statement clear and specific
- [x] Primary user defined with specifics
- [x] Solution concept bounded and clear
- [x] No unresolved contradictions
- [x] Explicit exclusions listed

### Key Context for Vision Generator
- **Offering Code**: [CODE]
- **Classification**: [Product / Client Service — per the organization's business model]
- **Lifecycle Stage**: [organization's custom stages or generic default]
- **Primary Focus**: [What Vision should emphasize]
- **Watch Out For**: [Potential traps or sensitive areas]

### Recommended Vision Approach
[Any guidance for the Vision Generator based on brainstorm insights]

---

*Brainstorm Document | Generated by the Brainstormer skill | [date]*
*Ready for the Vision Generator*
```

---

## Required Context Sources

Before beginning a brainstorm session, understand what context is available. Use the
organization's product-folder location for any path references — do not hardcode folder names.

| Priority | Source | Where to look | Extract |
|----------|--------|---------------|---------|
| Critical | User Input | (provided by user) | Raw idea, notes, thoughts, inspirations |
| High | Organization Context | org name / business model; org-level docs | Mission, values, existing portfolio |
| Medium | Related Offerings | existing vision docs in the product-folder location | Synergies, patterns, positioning |
| Low | Existing Brainstorms | prior brainstorm docs in the product-folder location | Template patterns, depth examples |

**Key principle:** User input is PRIMARY. The skill's contribution is to expand and challenge
that input, not replace it with generic thinking.

## Template & Context Loading

### Template reference
If the organization maintains a brainstorm-document template (at its template location), use
it. Otherwise use the output format defined above.

### Offering context (if available)
If brainstorming for an existing offering folder (in the product-folder location), check for
an existing vision document (to align with) and any context files (personas, constraints,
identity). For brand-new offerings, these will not exist — the brainstorm document is often
the first artifact created.

---

## Quality Checklist

### Section completeness
- [ ] Executive Snapshot complete (one-liner, problem, solution)
- [ ] Raw Ideas Inventory captures all user input
- [ ] All 5 Hard Question categories addressed
- [ ] Resolved Tensions section documents all decisions
- [ ] User Clarity includes primary AND anti-persona
- [ ] Problem Clarity includes evidence
- [ ] Solution Clarity includes explicit exclusions
- [ ] Risk Registry has at least 3 entries
- [ ] Open Questions flagged for Vision phase
- [ ] Handoff section complete with readiness checklist

### Quality standards
- [ ] No vague terms remain undefined
- [ ] No contradictions remain unresolved
- [ ] All inventory items appear somewhere in the final document
- [ ] Executive Snapshot aligns with detailed sections
- [ ] Vision-ready marker present with offering code

### Consistency check
- [ ] Primary user consistent across sections
- [ ] Problem statement consistent across sections
- [ ] Solution scope consistent with exclusions
- [ ] Risks align with HOW and WHAT-IF responses

---

## Activation Checklist

When this skill is activated:

**Phase 0: Intake**
1. [ ] Accept the user's raw idea / brainstorm input
2. [ ] Parse into categories (Problem, Solution, Users, Tech, Scope)
3. [ ] Create the Raw Ideas Inventory
4. [ ] Flag vague terms, contradictions, gaps
5. [ ] Present inventory for user validation

**Phase 1: Hard Questions**
6. [ ] User confirms inventory accuracy
7. [ ] Apply WHY questions (challenge + expand)
8. [ ] Apply WHO questions (challenge + expand)
9. [ ] Apply WHAT questions (challenge + expand)
10. [ ] Apply HOW questions (challenge + expand)
11. [ ] Apply WHAT-IF questions (challenge + expand)
12. [ ] **WAIT for user responses**
13. [ ] Optional follow-ups on unclear answers

**Phase 2: Clarification**
14. [ ] Present identified contradictions
15. [ ] Present vague terms needing definition
16. [ ] Propose resolution options for each
17. [ ] **WAIT for user decisions**
18. [ ] Document all resolutions

**Phase 3: Synthesis**
19. [ ] Generate Executive Snapshot
20. [ ] Compile Challenged Assumptions
21. [ ] Document Resolved Tensions
22. [ ] Write User Clarity section
23. [ ] Write Problem Clarity section
24. [ ] Write Solution Clarity section
25. [ ] Write Technical Approach section
26. [ ] Compile Risk Registry
27. [ ] List Open Questions
28. [ ] Complete Handoff section

**Phase 4: Validation**
29. [ ] Run Critical Checks (block if fail)
30. [ ] Run Quality Checks (warn if >3 fail)
31. [ ] If any critical fails -> return to the appropriate phase
32. [ ] Write the brainstorm document to the offering folder (the organization's product-folder location)
33. [ ] Confirm the vision-ready marker is present
34. [ ] Present the completion summary to the user

---

*Brainstormer Forms | Templates and checklists loaded on demand*
