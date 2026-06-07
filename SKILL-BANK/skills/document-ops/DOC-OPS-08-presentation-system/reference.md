# Presentation System — Reference

Extended reference for deck-craft. Brand and positioning specifics come from your
organization's decisions (see [`ADAPT.md`](ADAPT.md)); the layout, source-order, and rhythm
patterns below are universal.

---

## The values the deck binds to

A deck resolves these concrete values at build time:

```text
Brand:
  Palette  — primary, accent (often "use sparingly"), light base (evidence /
             table backgrounds), dark base (authority / type); each with name + hex.
  Type     — display font (headlines), mono font (labels / data).
  Logo     — asset location, file variants, clear-space and minimum-size rules.
  Voice    — exact wordmark and tagline (the tagline closes the deck).

Positioning:
  Promise          — the one value statement.
  Key messages     — the claims the deck must make.
  Differentiators  — why this over the alternative.
```

If a value is not yet decided, treat it as unanswered — ask via the Deck Intake in
[`forms.md`](forms.md), or fall back to a labeled placeholder.

---

## Source order (where the deck's truth comes from)

Resolve in this order; earlier sources win:

1. **Adopted brand & positioning** — the organization's color, type, logo, wordmark,
   tagline, and narrative claims (see `ADAPT.md`): the source of truth.
2. **Template deck** — the organization's reusable starter `.pptx` and its layout guide, if
   one exists. Use its layouts before inventing new ones.
3. **Brand-guidelines skill** — for any visual-identity rule not covered here.
4. **Brand asset folder** — official logo and symbol files.

---

## Layout selection

Map each slide's job to a layout recipe. Numbers are generic slots, not a fixed template —
match them to whatever template deck the organization uses.

| Need | Layout slot |
|---|---:|
| First impression / cover | 1 |
| Narrative spine / agenda | 2 |
| Section / chapter break | 3 |
| Problem reframe | 4 |
| Before / after | 5 |
| Claim plus evidence | 6 |
| Use cases / workstreams | 7 |
| Roadmap / phasing | 8 |
| Architecture / system map | 9 |
| Table / decision log | 10 |
| KPI / chart | 11 |
| Strategic fit | 12 |
| Quote / belief | 13 |
| Close / next step | 14 |

---

## Visual mode system (map to the brand palette)

Use color *mode* to signal the kind of slide. Bind each mode to a palette role — don't
hardcode colors.

| Mode | Built from | Carries |
|------|-----------|---------|
| Dark mode | dark base | Authority, high-stakes claims |
| Primary mode | primary | Platform, workflow, movement |
| Light mode | light base | Evidence, tables, decision logs |
| Accent mode | accent (sparingly) | Quote, close, key moments |

Rules:
- A structural device (grid, nodes) sits **behind** content and never competes with the proof.
- Node clusters / connection graphics are chrome unless they encode a real relationship.

---

## Typography application (generic — fonts from the brand)

| Use | Font | Weight | Size |
|-----|------|--------|------|
| Display / titles | brand display font | Bold | 28–72px |
| Body / claim | brand display font or clean fallback | Regular | 18–28px |
| Labels / data / captions | brand mono font | Regular/Bold | 12–18px |

Keep a consistent weight hierarchy across the deck; minimum ≈14px for any body text on a slide.

---

## Asset hierarchy (what to reach for first)

1. Official logo and symbol assets from the brand's logo folder.
2. Existing template / brand presentation assets.
3. Native editable shapes in the deck tool (preferred over imported images).
4. A single coherent icon family — only when an icon is functional, not decorative.
5. Generated imagery only for abstract atmosphere — **never** to fake client evidence.

---

## Slide rhythm

A good deck reads as a sequence, not a stack of identical templates.

- Alternate visual modes so the contact sheet shows variation.
- Place section breaks to give the audience a breath between arguments.
- End every argument arc on its implication before moving to the next.
- The close restates the core promise and names a concrete next step.

---

## Integration with other skills

| Skill | Connection |
|-------|------------|
| PPTX / file-mechanics skill | Builds and edits the actual `.pptx` |
| Brand-guidelines skill | Source of visual-identity rules (palette, logo, type) |
| Brand-voice skill | Keeps headline and body copy on-tone |
| Data-visualization skill | Designs the proof objects (charts, KPIs) on metric-heavy slides |

> All brand and positioning values come from the organization's adopted decisions (see
> `ADAPT.md`). This file stays portable across organizations — only those values change.
