---
name: Frontend Design
description: Create distinctive, production-grade frontend interfaces with high design quality and a clear aesthetic point-of-view. Use when building or styling web components, pages, landing pages, dashboards, posters, artifacts, or applications (HTML/CSS/JS, React, Vue), and when the goal is polished UI that avoids generic AI aesthetics. Brand-neutral by default. To use it for a specific organization, see ADAPT.md.
tier: optional-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Frontend Design

Guide the creation of distinctive, production-grade frontend interfaces that avoid
generic "AI slop" aesthetics. Implement real, working code with exceptional attention
to aesthetic detail and creative, intentional choices.

The user provides frontend requirements: a component, page, application, or interface
to build. They may include context about the purpose, audience, or technical
constraints.

## Brand inputs (optional — only when branded output is wanted)

This skill works **brand-neutrally by default** — its whole point is to make a
distinctive, context-specific aesthetic choice, which usually means picking fresh,
unexpected fonts and colors rather than reusing fixed brand tokens. This skill is the
**method**; the brand specifics it can optionally operate on are decided per organization
— see [`ADAPT.md`](ADAPT.md).

- If the user wants **on-brand** output and the organization's brand tokens (palette,
  typography, logo, voice) are available, use them as the starting palette/type system,
  then still execute with the craft described below.
- If no brand is supplied, or the user wants a one-off / exploratory look, design
  brand-neutrally. Ask **only** if it's unclear whether brand consistency matters here.
- Never invent an organization's brand colors, fonts, or tagline. If asked for
  "on-brand" work and the tokens are not yet decided, ask for them or clearly label the
  result a **GENERIC DRAFT** and list what's missing.

Everything below is the method, and applies whether or not a brand is in play.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:

- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic,
  organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw,
  art deco/geometric, soft/pastel, industrial/utilitarian, and more. Use these for
  inspiration but design one that is true to the chosen direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What is the one thing someone
  will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold
maximalism and refined minimalism both work — the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:

- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:

- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid
  generic fonts like Arial and Inter; opt instead for distinctive, characterful choices
  that elevate the aesthetic. Pair a distinctive display font with a refined body font.
  (If branded output is wanted, the brand's display and body fonts are the starting point.)
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency.
  Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
  (If branded output is wanted, draw from the brand palette and honor any "use sparingly"
  note on the accent.)
- **Motion**: Use animation for effects and micro-interactions. Prefer CSS-only
  solutions for plain HTML; use a motion library for React when available. Focus on
  high-impact moments — one well-orchestrated page load with staggered reveals
  (animation-delay) creates more delight than scattered micro-interactions. Use
  scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow.
  Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting
  to solid colors. Add contextual effects and textures that match the overall aesthetic:
  gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic
  shadows, decorative borders, custom cursors, grain overlays.

NEVER use generic AI-generated aesthetics: overused font families (Inter, Roboto, Arial,
system fonts), cliched color schemes (particularly purple gradients on white
backgrounds), predictable layouts and component patterns, and cookie-cutter design that
lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the
context. No two designs should be the same. Vary between light and dark themes,
different fonts, different aesthetics. NEVER converge on common defaults (Space Grotesk,
for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist
designs need elaborate code with extensive animation and effects. Minimalist or refined
designs need restraint, precision, and careful attention to spacing, typography, and
subtle detail. Elegance comes from executing the vision well.

Remember: you are capable of extraordinary creative work. Don't hold back — show what
can truly be created when thinking outside the box and committing fully to a distinctive
vision.

## Reference

Aesthetic-direction menu, the optional brand-token mapping, an anti-slop checklist, and
accessibility floors are in [`reference.md`](reference.md). The brand tokens (when used)
come from the organization's brand decisions (see [`ADAPT.md`](ADAPT.md)); the platform
and accessibility facts there are universal and brand-independent.
