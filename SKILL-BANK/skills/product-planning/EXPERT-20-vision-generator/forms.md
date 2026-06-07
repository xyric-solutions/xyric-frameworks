# Vision Generator — Forms & Checklists

Ready-to-use intake, templates, and quality checklists. Output location, naming, portfolio
categories, and audience context are organization decisions (see [`ADAPT.md`](ADAPT.md));
this file never hardcodes them.

---

## Vision Context Intake (the questionnaire for adapting this skill)

This is the questionnaire that captures the organization-specific values this skill operates
on. Ask only what's missing, as one numbered list, and **WAIT** for answers; then record them
wherever your team keeps product decisions (a brief, a settings file, or your forked copy).

**Workspace / paths:**
1. **Where do product folders live**, and what is the per-product path pattern?
2. **What is the vision file named**, and the broader filename convention?
3. **Which file tracks planning progress** for a product?
4. **Where do document templates live** (incl. any vision template)?

**Business / portfolio:**
5. **What is this organization or product?** (name, one-liner)
6. **What are the portfolio categories or lifecycle stages** used for strategic fit?
   (e.g. flagship / core / exploratory / supporting)
7. **One-line business model** (for context only; the vision excludes monetization detail)

**Positioning / audience:**
8. **Who are the primary and secondary user segments?**
9. **What differentiators or key messages** should the vision stay consistent with?

---

## Vision Document Template Reference

> **Template location:** read it from your organization's template folder (look for a vision /
> Product-Vision template). The full template with all section details is maintained by the
> consuming organization. Read it during Phase 2 (Generation) for the complete structure.
>
> If no template is configured, fall back to the **Required Sections** structure below.

## Required Sections (10 Sections + Risks)

1. **Executive Summary** — Vision, problem, solution, differentiators, goal
2. **Mission Statement** — Mission, core purpose (user-focused)
3. **Vision Statement** — Expanded vision with 4 components
4. **Product Objectives** — 4–6 objectives with product-focused Key Results
5. **User Value Propositions** — 3+ user types with benefits and frustrations
6. **Product Architecture** — Overview, modules, AI/automation capabilities
7. **Product Principles** — 7 principles in "X Over Y" format
8. **Product Quality Metrics** — UX, product performance, technology
9. **Target Users** — 3–5 user personas with context
10. **Inspiration Sources** — What to learn from others (NOT competitive analysis)
11. **Risks & Mitigation** — 8–12 product-focused risks

### What NOT to Include
- Revenue models / TAM / unit economics
- Go-to-market strategy
- Business KPIs (CAC, LTV, market share)
- Competitive market analysis for positioning

## Output Format

Embed the downstream pipeline hook in the vision document — a `PRD_READY` marker carrying
the product code, e.g.:

```markdown
<!-- PRD_READY: <product-code> -->
```

### Output Structure

- **File:** the product's vision file (in your product folder, using your filename convention)
- **Typical Length:** 600–1000 lines (streamlined to 10 sections)
- **Sections:** 10 required sections + Risks
- **Focus:** Product concept (60%), Problem/Solution (30%), Strategic intent (10%)

---

## Quality Checklist

### Section Completeness Check (10 Sections)

- [ ] 1. Executive Summary (vision, problem, solution, differentiators, goal)
- [ ] 2. Mission Statement (mission, core purpose — user-focused)
- [ ] 3. Vision Statement (expanded vision, 4 components)
- [ ] 4. Product Objectives (4–6 objectives with product-focused KRs)
- [ ] 5. User Value Propositions (3+ user types with benefits and frustrations)
- [ ] 6. Product Architecture (overview, modules, AI/automation capabilities)
- [ ] 7. Product Principles (7 principles in "X Over Y" format)
- [ ] 8. Product Quality Metrics (UX, product performance, technology)
- [ ] 9. Target Users (3–5 user personas with context)
- [ ] 10. Inspiration Sources (what to learn from others — NOT competitive analysis)
- [ ] Risks & Mitigation (8–12 product-focused risks)

### Quality Standards Check

- [ ] All metrics are quantified (numbers, percentages, targets)
- [ ] All differentiators are product/technology focused (not business focused)
- [ ] Inspiration Sources focuses on learning (not market positioning)
- [ ] Risks have specific mitigation strategies
- [ ] Principles follow "X Over Y" format with application
- [ ] No placeholder text (TBD, [fill in], etc.)
- [ ] Consistent product name throughout (the org's product/org name)
- [ ] NO business metrics (revenue, CAC, LTV, market share)
- [ ] NO go-to-market or revenue model content

### Consistency Check

- [ ] Vision statement aligns with product objectives
- [ ] Value propositions address user frustrations
- [ ] Architecture supports stated differentiators
- [ ] Risks address product assumptions
- [ ] Metrics measure product quality (not business success)
- [ ] Strategic fit matches the org's portfolio / lifecycle model

### Visual Documentation Check

- [ ] Product Evolution Timeline present (after Vision Statement)
- [ ] Objective Dependencies Map present (if 4+ objectives)
- [ ] Value Proposition Flow present (after Core Value Proposition)
- [ ] Stakeholder Influence Matrix present (if 3+ stakeholder types)
- [ ] Risk Landscape Visualization present (after Risk Mitigation)
- [ ] All diagrams use a consistent color scheme
- [ ] All Mermaid syntax renders correctly (valid syntax)
- [ ] Diagrams enhance understanding (not just decoration)

---

## Activation Checklist

When this skill is activated, follow these steps:

### Phase 0: Research

1. [ ] **Confirm the organization's decided values** (product folder, naming, progress file,
   portfolio model, product name, audience) — ask the Vision Context Intake if any are unknown
2. [ ] **Check for a brainstorm artifact** in the product folder with a `VISION_READY` marker containing the product code
3. [ ] **Set mode:** "With Brainstorm" or "Without Brainstorm" (Legacy)
4. [ ] Parse input (brainstorm artifact OR user input depending on mode)
5. [ ] Identify product type, users, technology approach
6. [ ] Gather context from existing documents
7. [ ] Generate Input Analysis Summary (~300 words)

### Phase 1: Analysis

*If With Brainstorm Mode:*

8. [ ] Present Brainstorm Summary (extracted from the brainstorm artifact)
9. [ ] Ask **4 reduced questions** (vision expansion, positioning, architecture, metrics)
10. [ ] **WAIT for user responses**

*If Without Brainstorm (Legacy) Mode:*

8. [ ] Present Input Analysis to user
9. [ ] Ask **7 tailored clarification questions** (NO business questions)
10. [ ] **WAIT for user responses**
11. [ ] (Optional) Ask follow-up questions if needed

### Phase 2: Generation

12. [ ] Apply user decisions to vision structure
13. [ ] Generate 10 sections sequentially
14. [ ] Cross-reference for consistency
15. [ ] Verify NO business content included

### Phase 3: Validation (Blocking)

16. [ ] Verify all 10 sections complete
17. [ ] Check no contradictions
18. [ ] Check no placeholder content
19. [ ] Check NO business content (revenue, TAM, go-to-market)
20. [ ] If fails → return to Phase 2 and fix

### Phase 4: Output

21. [ ] Write the vision file to your product folder, using your filename convention
22. [ ] Update the progress/tracking file
23. [ ] Include pipeline hooks for the downstream PRD step (`PRD_READY` marker)
24. [ ] Present completion summary

---

## Input Analysis Template

Use this template during Phase 0 to present the context summary:

```markdown
## Input Analysis: [Product Name]

### Extracted from User Input
**Product Concept:** [Brief description]
**Problem Statement:** [What problem are we solving]
**Target Market:** [Who are the users]
**Technology Approach:** [What tech/approach mentioned]
**Revenue Model:** [If mentioned, or "Not specified" — not used in the vision]
**Competitive Context:** [Any competitors mentioned]

### Inferred from Context
**Product Type:** [B2B SaaS / B2C App / Platform / Service / etc.]
**Industry:** [Healthcare / Finance / Education / etc.]
**Portfolio Fit:** [Standalone / Extends an existing product / Related to another — framed via the org's portfolio model]

### Gaps Requiring Clarification
- [Gap 1]: [What's missing]
- [Gap 2]: [What's unclear]
- [Gap 3]: [Decision needed]

### Template Patterns (From Existing Visions, if any)
**Typical Length:** [e.g. 600–1000 lines]
**Section Structure:** [10 sections + Risks]
**Depth Examples:** [Reference to any prior vision docs in your product folders]
```

## Brainstorm Summary Template

Use this template when entering "With Brainstorm" mode:

```markdown
## Brainstorm Summary: [Product Name]

**From the upstream brainstorm session:**
- **One-liner:** [From Executive Snapshot]
- **Problem:** [From Problem Clarity]
- **Primary User:** [From User Clarity]
- **Core Capabilities:** [From Solution Clarity]
- **Key Risks:** [From Risk Registry]

**Challenged & Validated:**
- [X] Problem statement validated
- [X] User defined (persona + anti-persona)
- [X] Scope bounded (must-have + exclusions)
- [X] No unresolved contradictions

**Ready for Vision expansion.**
```
