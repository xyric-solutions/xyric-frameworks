# Brand Guidelines — Forms & Checklists

Ready-to-use intake, checklists, and templates. The brand specifics are decided per
organization (see [`ADAPT.md`](ADAPT.md)); this file never hardcodes them.

---

## Brand Intake (the questionnaire for adapting this skill)

Ask as one numbered list and **WAIT** for answers; then record them wherever your team
keeps brand decisions. Ask only what's missing.

1. **Primary color** — name + hex (and where it's used)?
2. **Accent color** — name + hex; use sparingly?
3. **Light base and dark base** — two hexes (surfaces; grounding/type)?
4. **Semantic colors** — success / warning / error / info hexes (or use defaults)?
5. **Typefaces** — display/headline font; technical/mono font; optional accent font?
6. **Logo** — where the files live (folder/Drive), and light-on-dark vs dark-on-light variants?
7. **Clear space & minimum size** — logo padding rule and smallest allowed size?
8. **Tagline & wordmark** — exact strings, including punctuation?
9. **Descriptor / positioning line** — one line (optional)?
10. **Off-limits** — colors, fonts, or clichés to avoid?
11. **Accessibility floor** — minimum contrast target (default WCAG AA 4.5:1)?

---

## Brand Compliance Checklist

Use before publishing any designed asset. "Brand X" = your organization's brand values.

### Colors
- [ ] Uses only the brand palette for brand expression
- [ ] No off-palette colors introduced
- [ ] Sufficient text/background contrast (especially on strong primary/accent fills)
- [ ] Semantic colors used correctly for UI state

### Typography
- [ ] Display/headings use the brand display font (or approved fallback)
- [ ] Labels/data use the brand mono font
- [ ] Accent font used sparingly (if defined)
- [ ] Weight hierarchy consistent; minimum sizes met (≈14px body, 12px caption)

### Logo
- [ ] Correct variant for background (light on dark, dark on light)
- [ ] Clear space maintained; minimum size met
- [ ] No distortion, rotation, recolor, or effects
- [ ] Placement subtle (default bottom-right) unless brief says otherwise

### Tagline / messaging
- [ ] Tagline matches the brand exactly (including punctuation)
- [ ] Wordmark used only as logo text
- [ ] Descriptor (if used) matches the brand
- [ ] Nothing from the `voice.avoid` list present

### Design quality & accessibility
- [ ] Text on visuals under ~10 words per line; one idea per asset
- [ ] Real photos, or brand-consistent typography/structural motifs (not generic stock)
- [ ] Primary text meets the contrast target; color not the sole meaning indicator
- [ ] Alt text written; correct platform dimensions used

---

## Design Brief Template

```markdown
## Design Brief
**Date**: [YYYY-MM-DD]   **Requested by**: [Name]
**Platform**: [LinkedIn / X / Instagram / Multi]   **Format**: [Post / Carousel / Banner / End card / Story]
**Dimensions**: [e.g., 1080 × 1080 px]

### Concept
[1-2 sentences describing the visual idea]

### Text on visual
[Exact words — under ~10 words per line]

### Color direction
- Background: [profile primary / dark base]
- Text: [profile light base]
- Accent: [profile accent — sparingly]

### Logo
- Position: [Bottom-right / Other]    Variant: [Light bg / Dark bg]

### Style notes
[Mood, references, what to avoid — pull from voice.attributes / voice.avoid]

### Brand checklist
- [ ] Palette only  - [ ] Logo correct  - [ ] Tagline (if applicable)  - [ ] Dimensions  - [ ] Contrast met
```

### Quick one-liner brief
```
DESIGN BRIEF: [Format] | "[Key text]" | [Style/mood] | [Color direction from profile]
```

---

## Color Quick-Copy Card (fill from your brand palette)

```css
:root {
  /* fill from your brand palette */
  --brand-primary:   /* primary hex */ ;
  --brand-accent:    /* accent hex */ ;
  --brand-light:     /* light base hex */ ;
  --brand-dark:      /* dark base hex */ ;
  --brand-success:   /* semantic success */ ;
  --brand-warning:   /* semantic warning */ ;
  --brand-error:     /* semantic error */ ;
}
```
