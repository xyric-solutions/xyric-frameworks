---
name: Epic Generator
description: Break a Master PRD into a complete set of epic outlines with 100% feature coverage, MoSCoW distribution, hypothesis-driven scoping, and dependency complexity scoring. Use when turning a finished PRD into an Epic Overview before detailed Epic PRDs are written; do not use to write a single detailed Epic PRD (that is the Epic-PRD generator's job) or to scope work with no PRD. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Epic Generator

Transform a Master PRD into a comprehensive set of **epic outlines**, ensuring 100%
feature coverage with no gaps. This skill generates ALL epics at once, producing a single
Epic Overview document that becomes the foundation for detailed Epic PRD generation
downstream. It is the **method** — the four-phase workflow, MoSCoW enforcement, and
complexity scoring. The specifics it operates on — where product folders live, what the
PRD and output files are called, the ID/naming conventions, and the lifecycle vocabulary —
are decided per organization. See [`ADAPT.md`](ADAPT.md) for what to decide before using
this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** with neutral `PLACEHOLDER` paths (e.g.
`<products_root>/<product>/<prd_file>`) and default filenames, and list what's missing.
Never invent the organization's folder layout, the PRD's actual filename, the
epic-overview output path, the progress-tracking file, or the epic-PRD template location.

**Core philosophy**: Epics are logical groupings of features that can be developed
together. The generator ensures every PRD feature is captured exactly once, dependencies
are explicit and acyclic, and the development path is well-defined.

## Concrete paths & vocabulary the skill needs

Resolve every concrete path and filename from your organization's decisions at use time
(see [`ADAPT.md`](ADAPT.md)). The skill needs:

| What the skill needs | Where it comes from |
|----------------------|---------------------|
| Where products live | your products-root path (e.g. `<root>/<product>/`) |
| The Master PRD file | products-root + your PRD filename convention |
| The Technical Architecture file | products-root + that doc's name |
| Existing epic-PRD examples / output dir | products-root + your epic subfolder name |
| The Epic Overview output file | products-root + your epic-overview filename |
| Progress-tracking file | your per-product progress file |
| Epic-PRD template | your template location |
| Filename / ID conventions (E01, F1.1) | your naming conventions |
| MVP / lifecycle stage names | your lifecycle stage labels (fallback: Core / MVP / Enhanced / Future) |

## When to Activate

### Trigger Phrases
- "Generate epics from PRD"
- "Break PRD into epics"
- "Create epic outlines for [product]"
- "Epic breakdown for [product]"
- "PRD to Epics for [product]"
- "Generate all epics"

### Pipeline Position

This skill sits between requirements and detailed epic specs. Adapt the role names to the
consuming team's own pipeline:

| Pipeline role | Integration |
|---------------|-------------|
| **PRD generator** | PRD → (Technical Architecture) → Epics (upstream) |
| **Technical-architecture generator** | Architecture → Epics (immediate upstream) |
| **Epic-PRD generator** | Epic outline → detailed Epic PRD (downstream) |
| **Story generator** | Epic PRD → Stories (downstream) |
| **Product manager** | Strategic alignment, prioritization |
| **Hypothesis-question framework** | Epic scoping questions, validation hypotheses |

## Required Context Sources

All paths resolve from your products-root path and your naming conventions — never
hardcode a literal folder.

| Priority | Source | Where to look | Extract |
|----------|--------|---------------|---------|
| Critical | Master PRD | products-root/`<product>`/ + PRD filename | Features, personas, epic hints |
| Critical | Technical Architecture | products-root/`<product>`/ + arch doc name | System design, ADRs, components |
| High | Vision Document | products-root/`<product>`/ + vision doc name | Strategic alignment |
| High | Existing Epic PRDs | products-root/**/ + epic subfolder | Template patterns |
| Medium | Progress file | your per-product progress file | Session context |
| Low | Existing Stories | products-root/`<product>`/ + stories subfolder | Story patterns |

**Key principle:** Master PRD and Technical Architecture are the PRIMARY inputs. Every
feature in the PRD must map to exactly one epic.

## Generator vs. Individual Epic-PRD Skill

| Skill | Scope | Output |
|-------|-------|--------|
| **This skill** | Creates ALL epic outlines in one pass | Epic Overview document |
| **Epic-PRD generator** | Creates ONE detailed Epic PRD per invocation | Full Epic PRD document |

## Epic Philosophy

1. **100% coverage required** — every PRD feature maps to exactly one epic. No gaps.
2. **Natural groupings** — epics group related features. Size by scope, not arbitrary limits.
3. **Clear dependencies** — epic dependencies explicitly mapped. No circular dependencies.
4. **MVP alignment** — each epic tagged by lifecycle stage (your stage labels;
   default Core / MVP / Enhanced / Future). MVP scope clearly defined.
5. **Persona coverage** — each epic serves specific personas. No persona left without features.
6. **Testable boundaries** — epic completion is measurable with success criteria.
7. **MoSCoW distribution** — each epic tracks MUST / SHOULD / COULD features and enforces
   the target distribution below.

## MoSCoW Distribution

| Priority | Target | Description |
|----------|--------|-------------|
| **MUST** | ~60% | Critical features, epic fails without these |
| **SHOULD** | ~20% | Important features, significant value |
| **COULD** | ~20% | Nice-to-have, can defer if needed |

**Validation rules:**
- Epics with >80% MUST features: flag as high-risk (no flexibility)
- Epics with <40% MUST features: flag as potentially de-scoped
- Acceptable variance: ±15% from the 60/20/20 target

## Hypothesis-Driven Epic Scoping

Each epic validates a product hypothesis:

```markdown
**Hypothesis:** [What we believe to be true]
**Validation:** [How this epic validates the hypothesis]
**Key Questions:** [From the team's hypothesis-question framework]
```

## Dependency Complexity Scoring

```
Complexity Score = (Upstream Dependencies × 2) + (Downstream Dependents × 1) + (Cross-Epic Integrations × 3)
```

| Score | Level | Implication |
|-------|-------|-------------|
| 0–2 | Low | Can develop independently |
| 3–5 | Medium | Standard dependencies, manageable |
| 6–8 | High | Complex coordination required |
| 9+ | Critical | High risk, needs careful sequencing |

## Four-Phase Workflow Overview

```
Phase 0: RESEARCH (Automated)
  -> Locate Master PRD, extract features (F[X.Y] pattern)
  -> Extract epic structure, read existing Epic PRDs
  -> OUTPUT: PRD Feature Inventory (~300 words)

Phase 1: ANALYSIS & QUESTIONS
  -> Present feature inventory, propose epic groupings
  -> Ask 5 tailored clarification questions (Q1-Q5)
  -> WAIT FOR USER INPUT

Phase 2: GENERATION (Sequential)
  -> Apply user decisions, generate epics sequentially
  -> Build coverage matrix and dependency diagram
  -> OUTPUT: Epic Overview Document + Coverage Matrix

Phase 3: VALIDATION (Blocking)
  -> Coverage, Uniqueness, Circular Dependency, Persona checks
  -> IF ANY FAIL -> Return to Phase 2

Phase 4: OUTPUT & TRACKING
  -> Write the Epic Overview file, update the progress file
  -> Pipeline hooks for the epic-PRD generator
```

**Template reference:** the epic-PRD template at your configured template location.

**For detailed step-by-step instructions, see** [`reference.md`](reference.md).
**For output templates and checklists, see** [`forms.md`](forms.md).

## Anti-Patterns

1. **Generate without a PRD** — always read the PRD first. Epics must cover PRD features.
2. **Leave features unassigned** — every feature belongs to exactly one epic. Validation blocks on gaps.
3. **Create overlapping epics** — features cannot live in multiple epics. Clear boundaries required.
4. **Ignore dependencies** — dependencies must be explicit. Development order follows them.
5. **Skip validation** — 100% coverage is required. Blocking validation enforces this.
6. **Generate detailed feature specs** — this skill creates OUTLINES only. The epic-PRD
   generator creates detailed Epic PRDs.

## Output Summary

| File | Location | Typical Length |
|------|----------|---------------|
| Epic Overview | products-root/`<product>`/ + your epic-overview filename | 400–800 lines |

> All paths, filenames, templates, and lifecycle vocabulary come from your organization's
> adaptation decisions (see [`ADAPT.md`](ADAPT.md)). This skill stays portable across
> organizations — only those values change.

*4-Phase PRD → Epic Overview Generator | MoSCoW Distribution | Hypothesis-Driven | Complexity Scoring*
