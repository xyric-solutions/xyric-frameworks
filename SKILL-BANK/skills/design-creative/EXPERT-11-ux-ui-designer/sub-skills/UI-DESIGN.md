---
name: UI-DESIGN
parent: EXPERT-11
description: Design systems, component patterns, interaction design, prototyping, responsive layouts, and visual hierarchy
version: "1.0"
domain: Visual & Interaction Design
---

# Visual & Interaction Design (UI-DESIGN)

> Sub-skill of [UX/UI Designer (EXPERT-11)](../SKILL.md)

## Focus Area

Specializes in translating requirements into visual interfaces: design systems, component
patterns, interaction design, prototyping, responsive layouts, and visual hierarchy. Owns
the "how it looks and behaves" layer. It does NOT cover user research/discovery
(UX-RESEARCH) or accessibility auditing (UX-A11Y), though accessibility foundations are
built into every design decision.

Visual tokens (palette, typography, logo) are decided per organization — see the parent's
[`ADAPT.md`](../ADAPT.md); ask via the parent's Design Context Intake if not yet decided.
Never hardcode hex or fonts.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Design Systems | Component libraries, design tokens, Figma libraries, token-based theming |
| Interaction Design | User flows, micro-interactions, state management (default/hover/focus/active/disabled/loading/error/empty) |
| Visual Hierarchy | Typography scale, color theory, spacing systems (8pt grid), information density |
| Prototyping | High-fidelity prototypes, interactive flows, Dev Mode handoff |
| Responsive Layouts | Mobile-first vs. desktop-first strategy, breakpoint behavior, adaptive patterns |

## Methodology

### Priority Order
1. **Design tokens over hardcoded values** — never use raw hex; always reference the organization's semantic tokens
2. **All states designed** — a component is incomplete without its 8 states documented
3. **Brand context awareness** — apply the organization's brand tokens where a brand is defined; creative freedom on brand-free surfaces; client brand for client work
4. **Product-dependent device strategy** — conversational/consumer = mobile-first, dashboards = desktop-first

### Workflow
1. **Review requirements** — PRD with the product manager; understand acceptance criteria and device strategy
2. **Wireframe (low-fi)** — layout and flow focus; stakeholder validation before polish
3. **High-fidelity design** — apply design tokens, design ALL states, use the component library
4. **Prototype and iterate** — interactive prototypes; incorporate usability-testing feedback
5. **Dev Mode handoff** — annotations, exported assets, developer notes, component mapping to the frontend engineer

## Key Patterns

**Design-token architecture**: Colors (brand/semantic/background/text/border/dataViz),
spacing (4-48px on an 8pt grid), typography (display/body/mono from the brand), border
radius (4-12px + full), shadow (sm-xl). All values resolve from the organization's brand — never hardcode.

**Mobile layout**: 56px sticky header, 16px card margins, 44px+ full-width primary action
at the bottom. Thumb-zone friendly, skeleton loading, one-handed operation.

**Dashboard layout**: Top nav, collapsible sidebar, KPI cards row, main + secondary charts,
sortable data table. Pair with a data-viz skill for chart selection.

**Component docs**: Overview, variants with tokens, anatomy, all 8 states, accessibility
notes, do/don't guidelines, design link.

**Creative freedom**: On brand-free surfaces (a new product with no brand yet), pursue a
bold, distinctive aesthetic and avoid generic "AI slop" defaults.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Hardcoded hex values in designs | Use the organization's semantic design tokens |
| Missing states (only the "happy path") | Design all 8 states: default, hover, focus, active, disabled, loading, error, empty |
| Pixel-perfect polish before validation | Test low-fi wireframes first, polish after stakeholder validation |
| Wrong brand context | Branded = brand tokens, brand-free = creative freedom, client = client brand |
| Desktop layout for mobile-first products | Follow the product-dependent device-strategy table |

## Quality Gates

| Gate | Target |
|------|--------|
| Design token usage | 100% — zero hardcoded values |
| State completeness | All 8 states designed per interactive component |
| Dev handoff quality | < 2 clarifications per handoff, < 3 issues per design QA |
| Brand consistency | Correct context applied (branded / brand-free / client) |

## Deep Reference

- Parent: `../SKILL.md` | Reference: `../reference.md` → Tokens, Mobile, Desktop, Visual, Components, Design-System Library
- Checklists: `../forms.md` → Dev Handoff, Design QA, Component Template

## Team Integration

- **Product Design / Frontend Implementation** teams — as lead visual designer
- Pairs with: UX-RESEARCH (insights), UX-A11Y (accessibility), frontend engineer (handoff), creative-direction skill (aesthetics)
