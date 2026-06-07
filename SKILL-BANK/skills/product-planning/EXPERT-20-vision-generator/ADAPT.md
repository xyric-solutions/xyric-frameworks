# Adapting Vision Generator

**What this skill does:** turns a product idea (brief notes or a structured brainstorm) into
a comprehensive Vision Document through a 4-phase interactive workflow — defining WHAT we're
building, WHY it matters, and WHO it serves, while deliberately excluding business/monetization
content.

This skill is generic methodology — it never hardcodes where files go, what the product is
called, or how the organization frames strategic fit. To use it for your organization, decide
the values below and either keep them in your working brief at use time, or bake them into your
forked copy of `SKILL.md`, `forms.md`, and `reference.md`. Until they're decided, the skill
emits a labeled GENERIC DRAFT (neutral local path + `PLACEHOLDER` markers) rather than inventing
them.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Product folder location** — parent path + per-product folder pattern | Output; Two Entry Modes; Mode Detection | Where the vision file is written, e.g. a folder per product under a shared parent. |
| **Vision filename + naming convention** — what the vision file is called and the broader filename rule | Output | e.g. a `Product-Vision.md` file. |
| **Progress/tracking file** — the per-product planning-continuity file to update | 4-Phase Workflow (Phase 4) | a per-product session-continuity log. |
| **Template location** — where doc templates live (incl. any vision template) | Output (via `forms.md`/`reference.md`) | Falls back to the Required Sections list in `forms.md` if none. |
| **Portfolio / lifecycle model** — categories or lifecycle stages used for strategic fit | Vision Philosophy; Anti-Patterns | e.g. flagship / core / exploratory / supporting. |
| **Product / org name + one-liner** — the name used consistently throughout the vision | Output; Anti-Patterns | Drives the "consistent product name" quality check. |
| **Business model (one line)** — context only | NOT in Scope | Vision excludes monetization detail; captured for framing only. |
| **Audience / ICP tiers** — primary and secondary user segments | Vision Philosophy (WHO it serves) | Cross-checked in Phase 1 user questions. |
| **Differentiators / key messages** — what the vision should stay consistent with | Vision Philosophy; Consistency checks | — |

## How to gather these

The **Vision Context Intake** in [`forms.md`](forms.md) is the questionnaire for all of the
above — ask it once at the start of a vision engagement, and record the answers wherever your
team keeps product decisions (a brief, a settings file, or directly in your fork).

## Platform-independent (do not change)

These are method/structure facts that work as-is for any organization:

- `forms.md` — the Required Sections list (10 + Risks), quality/consistency/visual checklists,
  the activation checklist, and the Input Analysis / Brainstorm Summary templates.
- `reference.md` — the 4-phase instructions, brainstorm→vision section mapping, validation
  gates, assumption-challenge structure, and the universal Mermaid diagram color scheme
  (generic Material-style swatches, not a brand palette).
