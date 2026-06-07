---
name: Presentation System
description: Build, review, and adapt on-brand presentation decks — pitch decks, proposals, strategy decks, operating reviews, product narratives, and reusable templates — applying an organization's color/type system and positioning. Use when a deck must look on-brand and argue a point; do not use for plain slide mechanics with no brand or narrative. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Presentation System

A method for making presentation decks that look on-brand and make an argument. This
skill is the **deck-craft**; the specifics it operates on — the actual palette, type, logo,
tagline, and positioning — are an organization's brand and message, not part of the skill.
See [`ADAPT.md`](ADAPT.md) for what to decide before using this for a given organization.
Pairs naturally with a PPTX/file-mechanics skill (for building the file) and a
brand-guidelines skill (for visual identity rules).

When the brand and positioning specifics are not yet decided, **do not invent them** —
produce a clearly-labeled **GENERIC DRAFT** with obviously-neutral placeholders (system
fonts, `#000000`/`#FFFFFF`) marked `PLACEHOLDER`, and list what's missing. **Never invent**
brand colors, fonts, taglines, logos, or positioning claims.

## Core rules

- **Lead with tension, then prove it.** Open on the problem the audience feels (the gap
  between what they have and what they need), then earn the resolution. Don't open with a
  feature tour.
- **One claim + one proof object per slide.** Every content slide states a single claim and
  backs it with exactly one proof object: a chart, table, process diagram, architecture map,
  quote, benchmark, or decision log. No claim without proof; no proof without a claim.
- **Use the brand's color system.** Express the deck only in the brand palette. Use the accent
  color sparingly — for labels, key words, focal boxes, and next-step emphasis — never as
  decorative filler.
- **Use the brand's type system.** Headlines/display use the brand display font; labels and
  data use the technical/mono font. Keep a consistent weight hierarchy.
- **Use a consistent structural visual device.** Pick one structural motif the brand defines
  (e.g. a grid, a connected-node diagram, a stepped band) to show structure, connection, and
  decision paths — and reuse it. The device must encode a real relationship; decorative
  versions are chrome and should be cut.
- **One idea per visual.** No long paragraphs; text on a slide stays scannable in seconds.
- **State the implication.** Every table or chart says what decision it drives — not just
  what the data is.
- **Use the brand's wordmark and tagline exactly** (including punctuation). Reserve the
  tagline for the sign-off / close; never paraphrase it.

## Workflow

1. **Classify the deck** — proposal, strategy, operating review, product/platform narrative,
   workshop, or reusable template. Each has a different rhythm.
2. **Pick layouts from a template, don't invent.** Map each slide's job to an existing layout
   recipe (see [`reference.md`](reference.md) → Layout Selection) before designing anything new.
3. **Write the claim spine first.** Fill the Claim Spine table in [`forms.md`](forms.md): one
   row per slide, each with its narrative role, its single claim, and its single proof object.
   The spine is the deck; layout comes after.
4. **Build or edit the file** using a PPTX/file-mechanics skill. Apply the brand palette and
   type system.
5. **Reuse template layouts** before creating new ones, so the deck stays coherent.
6. **Render a contact sheet** (all slides as thumbnails) and inspect at thumbnail scale.
7. **Fix text fit, contrast, hierarchy, and proof-object clarity** before delivery. Run the
   Presentation QA checklist in [`forms.md`](forms.md).

## Anti-patterns

- Generic blue-gray SaaS palettes and soft pastel "tech" gradients (use the brand palette).
- Accent-color boxes that decorate rather than signal importance.
- Repeating the same left-title / right-card layout across most of the deck.
- Network/node graphics that look structural but encode no real relationship.
- Stock office photos, handshake imagery, generic-robot "AI" cliches.
- Tables or charts with no stated decision implication.
- Long display headlines that wrap into awkward word fragments.
- Fabricated client evidence; generated imagery only for abstract atmosphere, never as proof.

## Deliverable standard

A finished deck should feel high-contrast, precise, and usable in a live room. At
contact-sheet size, the sequence should show **distinct slide rhythms** (not one repeated
template). At full size, every slide should carry a **claim, a proof, and a next
implication**. The whole deck should look unmistakably like the organization's brand, not
generic.
