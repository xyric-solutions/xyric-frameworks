---
name: Vision Generator
description: Transform a product idea (brief notes or a structured brainstorm) into a comprehensive Vision Document via a 4-phase interactive workflow — defines WHAT we're building, WHY it matters, and WHO it serves, deliberately excluding business/monetization content. Use when creating or updating a product vision; do not use for PRDs, GTM/revenue strategy, or feature specs. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Vision Generator (EXPERT-20)

Transform a product idea — from brief notes to a detailed brainstorm — into a
comprehensive Vision Document. Vision documents establish the **product concept** and
**strategic north star**: they define WHAT we're building, WHY it matters, and WHO it
serves — **not** HOW to monetize it. This skill is the **method**; the specifics it operates
on — where vision files are written and named, the portfolio/lifecycle model used for
strategic fit, the product/org name, and the audience context — are decided per organization.
See [`ADAPT.md`](ADAPT.md) for what to decide before using this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a clearly-labeled
**GENERIC DRAFT**: write the vision to a neutral path (e.g. `./Product-Vision.md`) with
`PLACEHOLDER` markers for any unknown org/portfolio/audience value, and list what's missing.
Never fabricate output paths, portfolio categories, product names, or target audience.

For detailed phase instructions, see [`reference.md`](reference.md). For templates and
checklists, see [`forms.md`](forms.md).

## Purpose

Vision documents are the **entry point of the product pipeline**. They precede the PRD and
seed every downstream artifact (objectives, personas, constraints, architecture hints). A
vision is aspirational yet achievable: a multi-year north star grounded in near-term
execution.

## When to Activate

### Trigger Phrases
- "Create a vision document for [idea]"
- "Generate vision for [product]"
- "Product vision for [concept]"
- "Vision document from my notes"
- "Turn this idea into a vision document"
- "Vision → PRD pipeline for [product]"

### Pipeline position (role-based, not tool-specific)

```
Upstream brainstorming step  (optional)
        |
        v
   brainstorm artifact
        |
        v
>>> Vision Generator (this skill) <<<
        |
        v
  Product Vision document
        |
        v
Downstream PRD step
```

### Related roles

| Role | Integration |
|------|-------------|
| Brainstorming / discovery step | Brainstorm → Vision (upstream input) |
| PRD generation step | Vision → PRD transformation (downstream) |
| Product management | Strategic alignment, MoSCoW readiness, lifecycle staging |
| Software architecture | Technical feasibility validation of the architecture section |
| UX/UI design | User-experience alignment with personas and value props |

## Vision Philosophy

### Core Principles

1. **Product Concept First** — What is it? How does it work? What makes it unique? Skip the business model.
2. **Problem/Solution Focus** — What problem? Who has it? Why do existing solutions fail?
3. **Strategic Intent (Light Touch)** — Long-term product vision and platform potential. NOT revenue, GTM, or business KPIs.
4. **Aspirational Yet Achievable** — A multi-year vision that inspires, grounded in near-term execution.
5. **Product-Agnostic Template** — Works for any product type (B2B, B2C, Platform, Service).
6. **Interactive Refinement** — Multiple question rounds; user input drives depth.
7. **Quality Over Speed** — An excellent 500 lines beats a mediocre 1500. Blocking validation ensures completeness.

### Focus Hierarchy

```
PRODUCT CONCEPT (60%)
  What is it? How does it work? What makes it unique?

PROBLEM & SOLUTION (30%)
  What problem? Who has it? Why existing solutions fail?

STRATEGIC INTENT (10%)
  Long-term product vision, platform potential
```

### NOT in Scope (Business Focus)
- Go-to-Market Strategy / Revenue Model / Business Model
- Market Opportunity / TAM / SAM / SOM / Unit Economics
- Customer Acquisition Strategy
- Competitive Market Analysis for positioning (keep only as "Inspiration Sources")

## 4-Phase Interactive Workflow

```
Phase 0: RESEARCH (Automated)
  Parse input, detect brainstorm, gather context
  Output: Input Analysis Summary (~300 words)
          |
          v
Phase 1: ANALYSIS & QUESTIONS
  Present analysis, ask tailored questions
  With Brainstorm: 4 questions | Without: 7 questions
  === WAIT FOR USER INPUT ===
          |
          v
Phase 2: GENERATION (Sequential)
  Apply user decisions, generate 10 sections sequentially
  Cross-reference for consistency
  Output: Complete Vision Document + Section Coverage Matrix
          |
          v
Phase 3: VALIDATION (Blocking)
  Section check, consistency check, completeness check
  Quality check, no-business-content check
  IF FAIL -> Return to Phase 2, fix, re-validate
          |
          v
Phase 4: OUTPUT & TRACKING
  Write vision file (to your product folder), update the progress/tracking file
  Include pipeline hooks for the downstream PRD step
```

### Assumption-challenge integration

Run an **assumption-challenge pass** between Phase 0 and Phase 1, at full intensity.

Challenge: problem framing, target market, solution approach, and uniqueness claims.

Skip when: the user explicitly requests a bypass, the change is a minor vision revision, or
the user provides comprehensive rationale upfront.

## Two Entry Modes

### Mode 1: With Brainstorm (Recommended)

**Trigger:** a brainstorm artifact exists in the product's folder, marked ready for vision
expansion (e.g. a `VISION_READY` marker containing the product code).

- Phase 0 extracts structured content from the brainstorm artifact
- Phase 1 asks **4 reduced questions** (vision expansion, positioning, architecture, metrics)
- Validated assumptions carry forward from the brainstorm step

### Mode 2: Without Brainstorm (Legacy)

**Trigger:** no brainstorm artifact exists, OR the user explicitly bypasses it.

- Full **7-question** Phase 1 (traditional flow)
- More user interaction required
- Suitable for quick ideas, time-constrained sessions, or vision updates

### Mode Detection

```
Check: does a brainstorm artifact exist in this product's folder?
  YES -> Check for a VISION_READY marker containing the product code
    MARKER FOUND -> "With Brainstorm" mode (4 questions)
    NO MARKER    -> Warn the user; suggest completing the brainstorm step first
  NO  -> "Without Brainstorm" mode (7 questions)
```

## Output

- **File:** the product's vision file, placed in your product folder using your filename
  convention (e.g. a `Product-Vision.md` under the product folder).
- **Length:** 600–1000 lines
- **Sections:** 10 required + Risks
- **Pipeline Hook:** a `PRD_READY` marker containing the product code, for the downstream PRD step.

## Anti-Patterns

1. **Generate without questions** — Always ask clarification questions first.
2. **Use generic content** — Every section must be specific to this product.
3. **Skip validation** — All 10 sections must be complete. Blocking validation is required.
4. **Include implementation details** — Vision defines WHAT and WHY. HOW belongs in the PRD.
5. **Include business content** — No revenue models, TAM, go-to-market, or business KPIs.
6. **Ignore constraints** — Document constraints in the governance section. List out-of-scope items.
7. **Make unsupported claims** — Market sizes need a source or an "estimated" qualifier.

## Next Steps

- For detailed phase-by-phase instructions, see [`reference.md`](reference.md)
- For the vision document template and quality checklists, see [`forms.md`](forms.md)

> All output paths, portfolio categories, naming, and audience context are organization
> decisions — see [`ADAPT.md`](ADAPT.md). This skill stays portable across organizations;
> only those decided values change.
