# Adapting Epic PRD Generator

**What this skill does:** expands one epic outline into a detailed Epic PRD — feature
specs, persona-driven user stories, BDD acceptance criteria, error scenarios, success
metrics, and ADR flags.

This skill is generic methodology — the 4-phase workflow and the BDD/MoSCoW/feature-spec
structures never change. What changes per organization is *where* the inputs live and
*where* the output is written. To use it for your organization, decide the values below and
either keep them in your generation brief at use time, or bake them into your forked copy of
`SKILL.md`. Until they're decided, the skill emits a labeled GENERIC DRAFT with placeholder
paths rather than inventing your folder layout.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Products root** — parent path for product folders | Workspace inputs, Required Context Sources, Output Summary | the directory under which each product folder lives. |
| **Epic Overview file** — filename/pattern holding epic outlines | Required Context Sources | The PRIMARY input — features come from here. |
| **Master PRD file** — master requirements doc filename | Required Context Sources | Source of feature details and personas. |
| **Existing Epic PRD location** — folder of prior Epic PRDs | Required Context Sources | Used to extract template patterns. |
| **Epic PRD output directory** (`<epic-prd-dir>`) | Workspace inputs, Generator vs Individual, Output Summary | Where the generated Epic PRD is written. |
| **Epic PRD filename convention** (`<epic-prd-filename>`) | Output Summary, Phase 4 | e.g. an `Epic-XX-Name` pattern — prefix + epic number + hyphenated name. |
| **Stories index path** — per-epic stories index | reference.md (Document Governance) | For downstream story-generation governance links. |
| **Progress file** (`<progress-file>`) | Workspace inputs, Required Context Sources, Phase 4 | Session-continuity file updated at the end of a run. |
| **Vision / design locations** (optional) | Required Context Sources | Strategic and UI/UX context, if you keep them. |
| **Naming conventions** — ID/casing/separator rules | Workspace inputs, throughout | Epic `E[XX]`, feature `F[X.Y]`, etc. |

## How to gather these

The numbered **Workspace Intake** in [`forms.md`](forms.md) is the questionnaire for all of
the above — ask it once, record the answers wherever your team keeps workspace decisions
(your generation brief, a fork of `SKILL.md`, or your own conventions doc).

## Platform-independent (do not change)

The following are universal methodology and need no adaptation:

- `forms.md` — Activation Checklist, Quality Checklist, Epic PRD Document Template,
  Validation Criteria.
- `reference.md` — the 4-phase workflow, question framework, BDD/feature-spec structures,
  assumption-challenge integration.
- `sub-skills/EPIC-PRD-FEATURES.md` and `sub-skills/EPIC-PRD-BDD.md` — feature-definition
  and BDD methodology.
- The **BDD Given/When/Then** format and **MoSCoW** priority scheme in `SKILL.md`.
