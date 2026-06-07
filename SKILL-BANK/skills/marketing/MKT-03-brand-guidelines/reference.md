# Brand Guidelines — Reference

Extended reference for brand application. The brand specifics (palette, fonts, logo) are
decided per organization — see [`ADAPT.md`](ADAPT.md). The platform sizes and structural
patterns below are universal and need no adaptation.

---

## Typography application (generic)

| Use | Font | Weight | Size |
|-----|------|--------|------|
| Display / H1–H2 | brand display font | Bold | 24–72px |
| Body | brand mono font or clean system fallback | Regular | 14–18px |
| Technical / labels | brand mono font | Regular/Bold | 10–14px |
| Accent | brand accent font | Regular | Short moments only |

Font stack pattern (fill fonts for your brand):
```css
--font-display: /* display font */, system-ui, sans-serif;
--font-body:    /* mono font */, system-ui, sans-serif;
--font-mono:    /* mono font */, ui-monospace, monospace;
```

---

## Logo usage rules (generic)

| Rule | Detail |
|------|--------|
| Files | light-on-dark and dark-on-light variants |
| Clear space | per the brand's clear-space rule |
| Minimum size | per the brand's minimum (default 32px digital, 0.5" print) |
| On light base | dark mark |
| On primary / dark base | light mark |
| Placement on designs | bottom-right, subtle |

**Don'ts:** rotate/skew, recolor, place on busy backgrounds without overlay, use below
minimum size, add shadows/gradients/glows.

---

## Platform sizing (universal — not brand-specific)

### LinkedIn
| Asset | Size |
|-------|------|
| Post image | 1200 × 627 px |
| Carousel slide | 1080 × 1080 px |
| Company banner | 1584 × 396 px |
| Profile photo | 400 × 400 px |

### X (Twitter)
| Asset | Size |
|-------|------|
| Post image | 1200 × 675 px |
| Header | 1500 × 500 px |
| Profile photo | 400 × 400 px |

### Instagram
| Asset | Size |
|-------|------|
| Feed post | 1080 × 1080 px |
| Reel / Story | 1080 × 1920 px |
| End card | 1080 × 1920 px |

---

## Accessibility standards (generic)

| Standard | Requirement |
|----------|------------|
| Primary text contrast | brand contrast target (default WCAG AA; AAA where stated) |
| Secondary text contrast | WCAG AA (4.5:1) minimum |
| Color not sole indicator | Always pair color with text, icon, or pattern |
| Alt text | All designed assets get descriptive alt text |
| Readable fonts | Minimum 14px body, 12px captions |

---

## Integration with other skills

| Skill | Connection |
|-------|------------|
| Campaign / content skills | Visuals follow this palette and these specs |
| Voice skill | Voice and visuals stay aligned |
| Copy / design-brief skills | Briefs follow these brand standards |
| Presentation / deck skills | Decks use the same brand system |
| Canvas / design-tool skills | Tool tokens come from the brand palette |
