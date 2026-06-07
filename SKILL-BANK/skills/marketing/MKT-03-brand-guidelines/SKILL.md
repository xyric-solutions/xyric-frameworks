---
name: Brand Guidelines
description: Apply an organization's brand — colors, typography, logo, tagline, voice — to designed assets, social graphics, decks, and documents, and review work for brand compliance. Use when brand consistency or visual formatting matters; do not use for generic layout with no brand. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Brand Guidelines

Apply one organization's visual identity consistently to any artifact, and check
existing work against it. This skill is the **method**. The specifics it operates on —
the actual palette, fonts, logo, tagline, and voice — are an organization's brand, not
part of the skill. See [`ADAPT.md`](ADAPT.md) for what to decide before using this for a
given organization.

When the brand specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** with obviously-neutral placeholders (e.g. `#000000`,
system fonts) marked `PLACEHOLDER`, and list what's missing.

## Color discipline

- Use **only** the brand palette for brand expression. Flag any off-palette color in a
  review.
- Follow each color's role (primary / accent / light base / dark base). Use the accent
  sparingly if the brand marks it so.
- For data visualization, prefer a primary→accent progression, the dark base for labels,
  and the light base for chart backgrounds. Never rely on color alone to carry meaning.
- Use the brand's semantic colors (success / warning / error / info) only for UI state.

## Typography

- Headlines/display use the brand's display font; labels/data use the mono font;
  optional accent font only for rare moments.
- Keep a consistent weight hierarchy (e.g. H1 heaviest → body regular) and minimum sizes
  (≈14px body, 12px caption). State a system-font fallback when brand fonts may be absent.

## Logo usage

- Pick the variant that contrasts the background (light mark on dark, dark mark on light).
- Honor the brand's clear-space and minimum-size rules. Default placement on designed
  assets: subtle, bottom-right — not dominant.
- Never rotate, skew, recolor, add effects to, or place the logo on a busy background
  without an overlay.

## Tagline & messaging

- Use the brand's tagline exactly as written (including punctuation); never modify,
  abbreviate, or translate it. Use the wordmark only as logo text.
- Use the optional descriptor for About sections / under the tagline when space allows.
- Respect the brand's "avoid" list (off-limits colors, fonts, clichés).

## Design quality

- Text on visuals: keep under ~10 words per line; one idea per asset.
- Prefer real photography; if none, use brand-consistent typography or geometric/structural
  motifs rather than generic stock imagery.
- Match the brand's stated character — don't drift to a generic look.

## Accessibility

- Primary body text: aim for the brand's contrast target (default WCAG AA 4.5:1; AAA where
  stated). Semantic colors meet the same target.
- Color is never the sole indicator of meaning. All designed assets get descriptive alt text.

## Compliance review & platform specs

- Run the **Brand Compliance Checklist** in [`forms.md`](forms.md) before publishing.
- Standard platform dimensions and design-brief templates are in [`reference.md`](reference.md)
  and `forms.md` — those are platform facts, independent of brand.
