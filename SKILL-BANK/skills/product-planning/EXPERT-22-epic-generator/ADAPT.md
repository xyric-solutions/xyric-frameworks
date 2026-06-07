# Adapting Epic Generator

**What this skill does:** breaks a finished Master PRD into a complete set of epic outlines
(one Epic Overview document) with 100% feature coverage, MoSCoW distribution,
hypothesis-driven scoping, and dependency complexity scoring.

This skill is generic methodology — the four-phase workflow, MoSCoW enforcement, and
complexity scoring are universal. To use it for your organization, decide the values below
and either keep them in your generation brief at use time, or bake them into your forked
copy of `SKILL.md`. Until they're decided, the skill emits a labeled GENERIC DRAFT with
neutral `PLACEHOLDER` paths rather than inventing your folder layout or filenames.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Products root** — parent path + per-product folder pattern (e.g. a `{product}` folder under a top-level products directory) | Concrete paths & vocabulary; Required Context Sources | Everything else resolves relative to this. |
| **Master PRD filename** — what the PRD is called inside a product folder | Concrete paths & vocabulary; Required Context Sources | Primary input; epics must cover its features. |
| **Technical Architecture filename** — that doc's name (if your pipeline has one) | Concrete paths & vocabulary; Required Context Sources | Optional if no architecture step. |
| **Vision doc filename** — strategic-alignment input | Required Context Sources | Optional. |
| **Epic subfolder** — where detailed Epic PRDs live + example files | Concrete paths & vocabulary; Required Context Sources | Used for template patterns and as output dir downstream. |
| **Epic Overview output filename** — the file this skill writes | Concrete paths & vocabulary; Output Summary | The single deliverable. |
| **Progress file** — per-product session/progress-tracking file | Concrete paths & vocabulary; Required Context Sources; Phase 4 | Updated after generation. |
| **Epic-PRD template location** — where doc templates live | Concrete paths & vocabulary; Four-Phase Workflow | Referenced for downstream epic-PRD format. |
| **Naming / ID conventions** — epic ID format (e.g. `E01`), feature ID format (e.g. `F1.1`), filename casing | Concrete paths & vocabulary; Required Context Sources | Drives feature extraction and file naming. |
| **Lifecycle / MVP stage labels** — your stage vocabulary | Epic Philosophy; MoSCoW; Phase 1 Q3 | Fallback: Core / MVP / Enhanced / Future. |
| **Product taxonomy** — product codes/names the Epic Overview header should reflect | Output document header (forms.md template) | Optional context for the header. |

## How to gather these

The numbered **Epic Generation Context Intake** in [`forms.md`](forms.md) is the
questionnaire for all of the above — ask it once, record the answers wherever your team
keeps project/pipeline decisions.

## Platform-independent (do not change)

The following are universal methodology, not organization-specific — they work as-is for
any team:

- The four-phase workflow, MoSCoW 60/20/20 targets, and dependency complexity formula in
  `SKILL.md`.
- The activation checklist, quality checklist, validation criteria, and output document
  templates in [`forms.md`](forms.md).
- The step-by-step phase instructions, question framework, assumption-challenge pass, and
  hypothesis examples in [`reference.md`](reference.md).
