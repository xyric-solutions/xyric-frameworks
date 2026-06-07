# Frontend Design — Reference

Extended reference for distinctive frontend work. The aesthetic-direction menu,
anti-slop checklist, and accessibility floors are universal. The optional brand-token
mapping uses the organization's brand decisions (see [`ADAPT.md`](ADAPT.md)) and is used
only when branded output is wanted.

---

## Aesthetic direction menu

Pick ONE and commit. The strength of a design is in the commitment, not the count of
effects.

| Direction | Signals | Type | Color | Motion |
|-----------|---------|------|-------|--------|
| Brutally minimal | Whitespace, restraint | One refined sans | 2–3 colors, high contrast | Subtle, precise |
| Maximalist | Density, layering, collage | Display + body clash | Saturated, many accents | Energetic, busy |
| Retro-futuristic | Chrome, scanlines, neon | Geometric / techno | Dark + electric accents | Glows, flicker |
| Editorial / magazine | Strong grid, big headlines | Serif display + clean body | Ink + one spot color | Reveal on scroll |
| Brutalist / raw | Visible structure, borders | Monospace / system grotesque | Stark, unstyled feel | Hard, snappy |
| Organic / natural | Curves, grain, warmth | Humanist serif/sans | Earthy, muted | Soft easing |
| Luxury / refined | Generous space, fine rules | Elegant serif | Deep neutrals + metallic | Slow, deliberate |
| Playful / toy-like | Rounded shapes, bounce | Friendly rounded sans | Bright, candy | Springy, bouncy |
| Art deco / geometric | Symmetry, gold lines | Geometric display | Black/gold/jewel tones | Staged entrances |
| Soft / pastel | Low contrast, gentle | Light-weight sans | Desaturated tints | Gentle fades |

The list inspires — design one true to the direction rather than copying a row verbatim.

---

## Optional brand-token mapping

Use this only when an organization's brand is decided **and** branded output is wanted.
Otherwise choose fresh, context-specific fonts and colors per the aesthetic direction
above. The brand inputs this maps from are listed in [`ADAPT.md`](ADAPT.md):

```yaml
brand:
  palette:
    primary: { name, hex, usage }
    accent:  { name, hex, usage }     # honor any "use sparingly" note
    light:   { name, hex, usage }
    dark:    { name, hex, usage }
    semantic: { success, warning, error, info }
  typography:
    display: { font, usage }          # headlines / display
    mono:    { font, usage }          # labels / data / technical
    accent:  { font, usage }          # optional, rare moments
  voice:
    avoid: []                         # off-limits colors/fonts/clichés to respect
  accessibility: { primary_target, semantic_target }
```

Token mapping into CSS variables (fill values from the organization's brand decisions,
not from here):

```css
:root {
  --color-primary: /* brand primary hex */ ;
  --color-accent:  /* brand accent hex  — use sparingly if flagged */ ;
  --color-light:   /* brand light-base hex */ ;
  --color-dark:    /* brand dark-base hex */ ;
  --font-display:  /* brand display font */, system-ui, sans-serif;
  --font-body:     /* brand body/mono font or a refined fallback */, system-ui, sans-serif;
}
```

If a value is not decided, treat it as unanswered: ask for it, or design brand-neutrally
and label the result a GENERIC DRAFT. Never invent brand values.

---

## Anti-slop checklist

Run before shipping. Each unchecked box is a tell of generic AI output.

- [ ] Display font is distinctive — not Inter, Roboto, Arial, or a bare system font
- [ ] No purple-gradient-on-white (or other cliché) color scheme by default
- [ ] Palette has a clear dominant color with sharp, intentional accents (not 6 even pastels)
- [ ] Layout breaks the predictable centered-card pattern where the direction calls for it
- [ ] At least one memorable, signature detail (the "one thing someone remembers")
- [ ] Backgrounds have atmosphere/texture/depth, not just a flat fill
- [ ] Motion is concentrated in high-impact moments, not scattered noise
- [ ] Implementation complexity matches the vision (maximalist → elaborate; minimal → precise)
- [ ] The result does not look like the last design generated — themes/fonts/aesthetic varied
- [ ] Every spacing, weight, and radius value is intentional and consistent

---

## Accessibility floors (universal — not brand-specific)

| Standard | Requirement |
|----------|-------------|
| Primary text contrast | WCAG AA 4.5:1 (or the brand's stated contrast target; AAA where stated) |
| Large text (≥24px or ≥19px bold) | WCAG AA 3:1 minimum |
| Color not sole indicator | Pair color with text, icon, or pattern (states, charts, errors) |
| Focus states | Visible keyboard focus on all interactive elements |
| Motion | Honor `prefers-reduced-motion`; never gate content behind animation |
| Readable type | Minimum ~14px body, ~12px captions |
| Alt text | Meaningful images get descriptive alt text; decorative images get empty alt |

A bold aesthetic and accessibility are not in tension — bake contrast, focus, and
reduced-motion handling into the design from the start.

---

## Implementation notes

| Stack | Motion approach | Notes |
|-------|-----------------|-------|
| Plain HTML/CSS | CSS animations/transitions, `@keyframes`, `animation-delay` for staggered reveals | Prefer CSS-only; no JS dependency for effects |
| React | A motion library (e.g. Motion) when available; CSS otherwise | Keep components functional and production-grade |
| Vue / others | Framework transitions + CSS | Same craft bar applies |

Use CSS custom properties for all color, type, spacing, and radius tokens so the
aesthetic stays cohesive and is trivial to retheme (including swapping in brand tokens).

> When branded output is used, its values come from the organization's brand decisions
> (see [`ADAPT.md`](ADAPT.md)). This file stays portable across organizations — only the
> brand values change.
