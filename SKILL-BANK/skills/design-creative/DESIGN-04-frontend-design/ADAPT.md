# Adapting Frontend Design

**What this skill does:** creates distinctive, production-grade frontend interfaces with a
clear aesthetic point-of-view, optionally applying an organization's brand when on-brand
output is wanted.

This skill is generic methodology and **brand-neutral by default** — most of the time it
should pick fresh, context-specific fonts and colors rather than reuse fixed tokens. You
only need the values below when you want **on-brand** output. Keep them in your design
brief at use time, or bake them into your forked copy of `SKILL.md` and `reference.md`.
Until they're decided, the skill designs brand-neutrally or emits a labeled GENERIC DRAFT
rather than inventing a brand.

## What to decide for your organization

These are only needed when branded output is wanted; for one-off or exploratory work,
skip them entirely.

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Palette** — primary, accent, light base, dark base (name + hex each) | Brand inputs, Color & Theme | Note if the accent is "use sparingly". Maps to `--color-*` CSS vars in `reference.md`. |
| **Semantic colors** — success / warning / error / info | Color & Theme | For UI state only; defaults are fine if you have none. |
| **Typefaces** — display/headline font, body (or mono/technical) font, optional accent font | Typography | Maps to `--font-display` / `--font-body`. State a system-font fallback. |
| **Voice "avoid" list** — off-limits colors, fonts, clichés | Frontend Aesthetics Guidelines | Honored on top of the universal anti-slop rules. |
| **Logo** — asset location and which variant fits light vs dark backgrounds | Brand inputs | Used only if a logo is placed on the artifact. |
| **Contrast target** — minimum ratio (default WCAG AA 4.5:1) | Reference → Accessibility floors | Raise to AAA where required. |

## How to gather these

This skill has no dedicated intake form. The brand values above come from the
organization's existing brand decisions — the same inputs the Brand Guidelines skill's
intake collects. Capture them once and record them wherever your team keeps brand
decisions, or pass them inline in your design brief.

## Platform-independent (do not change)

The following in `reference.md` are universal craft and platform facts — they need no
adaptation:

- **Aesthetic-direction menu** — the ten directions and their signals.
- **Anti-slop checklist** — generic-AI-output tells to avoid.
- **Accessibility floors** — WCAG contrast, focus, reduced-motion, type-size, alt-text rules.
- **Implementation notes** — per-stack motion approach and CSS-custom-property guidance.
