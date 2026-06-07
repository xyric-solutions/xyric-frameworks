---
name: PRD Generator
description: Transform a Product Vision Document into an actionable Product Requirements Document — features, personas, acceptance criteria, MoSCoW scope, success metrics, and epic breakdown. Use when turning a finished vision into specific, testable requirements; do not use to set new strategic direction (that is the vision skill) or to design technical architecture (that is downstream). To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# PRD Generator (EXPERT-21)

Transform a finished Product Vision Document into a comprehensive Product Requirements
Document (PRD): defined features, user personas, success metrics, MoSCoW scope, and an epic
breakdown. This skill is the **method** — the workflow, the section template, the validation
gates. The specifics it operates on — your audience segments, product taxonomy, lifecycle
stage, and where vision/PRD files live — are decided per organization. See
[`ADAPT.md`](ADAPT.md) for what to decide before using this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a clearly-labeled
**GENERIC DRAFT** with neutral `PLACEHOLDER` values (e.g. `<product>`, `<persona>`, generic
file paths) and list what's missing. Never invent the target audience, product name, pricing,
or internal file paths.

**Core Philosophy**: The PRD bridges vision and execution. It turns the "what" and "why"
from the vision into the "what specifically" — detailed requirements, personas, features,
and success criteria that guide development. It inherits strategic direction; it never
invents new strategic goals.

## When to Activate

### Trigger Phrases
- "Create a PRD from [vision document]"
- "Generate PRD for [product]"
- "Product requirements from vision"
- "Transform vision into PRD"
- "PRD for [product name]"
- "Vision to PRD for [product]"
- "Create requirements document"

### Related Skills

| Skill | Integration |
|-------|-------------|
| **Vision Generator** | Vision → PRD transformation (upstream) |
| **Tech Architecture Generator** | PRD → Architecture transformation (downstream) |
| **Epic Generator** | Architecture → Epics (receives downstream) |
| **Product Manager** | Strategic alignment, MoSCoW, lifecycle stage |
| **Software Architect** | Technical feasibility validation |
| **UX/UI Designer** | User-experience alignment |
| **Hypothesis / research skill** | Competitive-analysis framing |

### Workflow Position

```
Vision Generator --> PRD Generator --> Tech Architecture Generator --> Epic Generator
```

- **Input**: the product's Vision Document (in your product folder)
- **Output**: the product's Product Requirements Document (in your product folder, named per
  your filename convention)
- **Typical Length**: 800–1200 lines, 15+ required sections

## PRD Philosophy (house principles)

1. **PRD translates vision to requirements** — inherits strategic direction; defines specific
   features and acceptance criteria; does NOT introduce new strategic goals.
2. **Features must be testable** — each feature has acceptance criteria; success metrics are
   quantified; no vague requirements.
3. **Personas drive prioritization** — user personas derive from your audience segments;
   each feature maps to persona needs; MoSCoW is based on persona impact.
4. **Epic structure enables development** — logical grouping of features; clear dependencies;
   MVP vs Future scope defined.
5. **100% vision coverage** — every vision objective mapped to features; every value
   proposition addressed; no gaps.
6. **Interactive refinement** — questions clarify priorities and scope; user input drives MVP
   decisions; collaborative building.
7. **Product-agnostic template** — works for any product type; adapts to industry context; no
   hardcoded assumptions.

## Core Workflow (4-Phase)

```
Phase 0: RESEARCH (Automated)
  Locate Vision Document -> Extract objectives, segments, constraints
  Read PRD template/patterns from your workspace -> Generate Vision Analysis Summary (~400 words)

        |
        v  (Invoke the Assumption Challenge between Phase 0 and Phase 1)
        |
Phase 1: ANALYSIS & QUESTIONS (Interactive)
  Present Vision Analysis summary to user
  Ask 7 tailored clarification questions (Scope x3, Personas x2, Requirements x2)
  === WAIT FOR USER INPUT ===

        |
        v
Phase 2: GENERATION (Sequential)
  Apply user decisions -> Generate 15 sections sequentially
  Cross-reference with Vision -> Build Vision Coverage Matrix
  Generate Mermaid diagrams for visual documentation

        |
        v
Phase 3: VALIDATION (Blocking)
  Vision Coverage: All objectives mapped       (block if fail)
  Persona Coverage: All personas have features (block if fail)
  Section Coverage: All required sections present (block if fail)
  Completeness: No TBD or placeholder text     (block if fail)
  If ANY check fails -> return to Phase 2, fix, re-validate

        |
        v
Phase 4: OUTPUT & TRACKING
  Write the PRD file (path/name per your convention)
  Update the progress file with session details
  Include pipeline hooks for the architecture skill
```

For detailed step-by-step instructions for each phase, see [`reference.md`](reference.md).
For the PRD output template and validation checklists, see [`forms.md`](forms.md).

## Required Context Sources

Resolve all paths from your own workspace conventions — never hardcode a literal folder name.

| Priority | Source | Where | Extract |
|----------|--------|-------|---------|
| Critical | Vision Document | the product folder (the `*Vision*` file) | Strategic foundation |
| High | Existing PRDs | other product folders | Template patterns |
| High | PRD template | your template location | Section structure |
| High | Existing Epic PRDs | the product's epic-PRD folder | Epic structure patterns |
| Medium | Progress file | the per-product progress file | Session context |
| Medium | Company context | the org's company-docs root | Company standards |
| Low | Design docs | the product's design folder | UI/UX context |

Also load product-specific context (product-identity, personas, pillars, constraints,
design-decisions) from the product's context folder when available. If a personas context
exists, use it as the starting point for the Personas section — enrich, don't replace.

## Anti-Patterns

1. **Generate without a Vision Document** — always read the Vision first; the PRD must align
   with the established vision.
2. **Invent new strategic goals** — the PRD implements vision goals; it does not create new
   strategic direction.
3. **Skip user questions** — MVP scope needs user input; prioritization decisions require
   confirmation.
4. **Use generic personas** — personas must be specific to this product and derive from
   your audience segments; no copy-paste generic templates.
5. **Leave gaps in coverage** — every vision objective needs features; validation ensures
   100% coverage.
6. **Include implementation details** — the PRD defines WHAT, not HOW; technical details
   belong in Epic PRDs and the architecture document.

## Sub-Skills

Focused sub-skills for targeted activation and team compositions:

| Sub-Skill | Focus |
|-----------|-------|
| [PRD-PERSONA](sub-skills/PRD-PERSONA.md) | Persona creation, goal alignment, user segmentation |
| [PRD-FEATURES](sub-skills/PRD-FEATURES.md) | Feature specs, acceptance criteria, MoSCoW |

Use the parent skill for full-scope work; use a sub-skill for focused team compositions.

## Next Steps

- For full phase-by-phase methodology, question frameworks, competitive-analysis approach,
  and integration details, see [`reference.md`](reference.md).
- For the PRD output template, quality checklists, and the activation checklist, see
  [`forms.md`](forms.md).

> Audience, taxonomy, and path values are decided per organization (see [`ADAPT.md`](ADAPT.md)).
> This skill stays portable — only the adaptation values change.
