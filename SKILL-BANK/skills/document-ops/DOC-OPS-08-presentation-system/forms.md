# Presentation System — Forms & Checklists

Ready-to-use intake, claim-spine planner, and QA checklist. Brand and positioning
specifics come from your organization's decisions (see [`ADAPT.md`](ADAPT.md)); this file
never hardcodes them.

---

## Deck Intake (the questionnaire for adapting this skill)

Use this to capture an organization's brand and positioning the first time. Ask as one
numbered list and **WAIT** for answers; then record them wherever your team keeps these
decisions. Ask only what's missing.

**Brand:**
1. **Palette** — primary, accent, light base, dark base (names + hexes); which is used sparingly?
2. **Typefaces** — display/headline font; technical/mono font for labels and data?
3. **Logo / wordmark** — exact wordmark string (incl. punctuation); where the logo files live; light-on-dark vs dark-on-light variants?
4. **Tagline / sign-off** — exact string (incl. punctuation) used to close a deck?
5. **Structural visual device** — is there a signature motif (grid, connected nodes, stepped band) that should recur across slides?

**Positioning:**
6. **Core promise** — the one value statement the deck must land?
7. **The tension to open on** — what gap or pain does the audience feel before you pitch?
8. **Key messages** — 3-7 claims the deck must make?
9. **Differentiators** — what makes this offer different from the obvious alternative?

**Deck context (per deck, not part of the standing brand decisions):**
10. **Deck type** — proposal / strategy / operating review / product narrative / workshop / template?
11. **Audience & decision** — who's in the room and what should they decide afterward?

---

## Claim Spine (fill before designing any slide)

One row per slide. The spine is the deck; layout comes after. Map each slide to a layout
recipe in [`reference.md`](reference.md).

| # | Role | Claim (one sentence) | Proof Object (one) | Layout |
|--:|------|----------------------|--------------------|-------:|
| 1 | Cover | | | 1 |
| 2 | Narrative spine / agenda | | | 2 |
| 3 | Section break | | | 3 |
| 4 | Problem reframe | | | 4 |
| 5 | Before / after | | | 5 |
| … | Claim + evidence | | | 6 |
| … | Close / next step | | | 14 |

Proof object = chart, table, process, architecture, quote, benchmark, or decision log.

---

## Presentation QA Checklist

Use before delivery. "Brand X" = the organization's adopted brand and positioning values.

### Brand fidelity
- [ ] Uses only the brand palette; no off-palette colors
- [ ] Accent color used for emphasis, not filler
- [ ] Display font for headlines, mono font for labels/data (or approved fallbacks)
- [ ] Logo is the correct variant for the background, high-contrast, undistorted
- [ ] Wordmark and tagline match the brand exactly (incl. punctuation)

### Narrative & proof
- [ ] Deck opens on the audience's tension before the solution
- [ ] Each slide has one clear claim and one proof object (or one clear narrative role)
- [ ] Main claim of each slide is readable in ~3 seconds
- [ ] Every table or chart states its decision implication
- [ ] All key messages and differentiators are present
- [ ] Close restates the promise and names a concrete next step

### Craft
- [ ] No awkward word breaks in large headlines
- [ ] One idea per visual; no long paragraphs
- [ ] Structural visual device (if used) encodes a real relationship, not decoration
- [ ] No stock office / handshake / generic-robot / soft-SaaS imagery
- [ ] No fabricated client evidence

### Handoff
- [ ] Contact sheet rendered and inspected at thumbnail scale
- [ ] Contact sheet shows varied slide rhythm, not one repeated template
- [ ] Final file rendered and visually checked before delivery

---

## Copy patterns (structure, not content — fill from your positioning)

A reusable shape for the opening tension and the resolution. Pull the actual words from your
core promise and key messages.

```text
TENSION (open):
  [What they have]  does not equal  [what they need].
  [The artifact they get] tells them what happened.
  [What they actually want] tells them what to do next.

RESOLUTION (your move):
  The gap is [the thing you bridge].
  [The offer] turns [input] into [outcome].

CLOSE (next step):
  Let's validate this with one focused [pilot / phase].
  [Deliverable 1]. [Deliverable 2]. [Success criteria].
```
