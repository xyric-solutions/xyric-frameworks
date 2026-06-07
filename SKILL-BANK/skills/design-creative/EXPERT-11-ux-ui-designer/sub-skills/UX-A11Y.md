---
name: UX-A11Y
parent: EXPERT-11
description: WCAG compliance from a design perspective, inclusive design patterns, contrast requirements, keyboard navigation design
version: "1.0"
domain: Accessibility Design
---

# Accessibility Design (UX-A11Y)

> Sub-skill of [UX/UI Designer (EXPERT-11)](../SKILL.md)

## Focus Area

Specializes in designing for accessibility from the ground up: WCAG 2.1 AA compliance at
the design layer, inclusive design patterns, contrast verification, keyboard-navigation
design, and inclusivity for constrained contexts. Owns accessibility as a design
foundation, not an afterthought. It does NOT cover frontend accessibility implementation or
general visual design (UI-DESIGN), but provides the design specifications that
implementation follows.

Contrast verification uses the organization's actual palette and its contrast target
(default WCAG AA 4.5:1); ask via the parent's intake if not yet decided. See the parent's
[`ADAPT.md`](../ADAPT.md).

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| WCAG Compliance | 2.1 AA minimum from design phase: contrast ratios, text resizing, non-color information |
| Inclusive Design | Constrained contexts (low-end devices, outdoor visibility, multilingual), diverse abilities |
| Keyboard Navigation | Focus-order design, skip links, keyboard-trap prevention, focus-indicator specs |
| Touch Accessibility | 44x44px minimum targets, comfortable spacing, thumb-zone placement |
| Screen Reader Design | ARIA-label specs, meaningful alt-text guidance, announcement patterns |

## Methodology

### Priority Order
1. **Accessibility from day one** — baked into wireframes, not bolted on after visual design
2. **WCAG AA is the floor, not the ceiling** — exceed minimum requirements where feasible
3. **Constrained contexts amplify accessibility needs** — low-end devices, outdoor glare, literacy variation
4. **Design specifications drive implementation** — every accessibility requirement must be explicit in handoff

### Workflow
1. **Audit requirements** — review the PRD and wireframes for accessibility implications
2. **Define accessibility specs** — contrast ratios, touch targets, focus order, ARIA labels per component
3. **Verify contrast** — check all color combinations against WCAG thresholds (4.5:1 text, 3:1 large text, 3:1 UI components)
4. **Design keyboard flow** — tab order, focus indicators, skip links, no traps
5. **Handoff to implementation** — accessibility annotations in the design file; coordinate with the frontend engineer for code-level compliance

## Key Patterns

**Contrast matrix**: Build a matrix of every palette pairing from the brand and its
measured ratio. Reserve the dark base for body copy; mid-tone accents often pass only for
large text. Verify every new combination before approving it.

**POUR in design**: Perceivable (alt text, non-color info, 200% resize). Operable
(keyboard-accessible, no traps, 44px+ targets). Understandable (labels, clear errors,
consistent nav). Robust (ARIA specs, semantic-HTML preferences).

**Constrained contexts**: Outdoor visibility via high contrast. Multilingual support with
icons where the audience is multilingual. Voice I/O for literacy variation. One-handed
mobile with large targets.

**Focus indicators**: A visible outline (≈2px, the brand accent color) with ≥3:1
contrast, visible on both light and dark surfaces. Keyboard-only (`:focus-visible`).

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Accessibility as a final checklist | Build it into wireframes from the start |
| Relying on color alone for status/errors | Combine color with icons, text labels, or patterns |
| Mid-tone text on light backgrounds | Mid-tones may pass only for large text — use the dark base for body text |
| Missing focus indicators | Specify a visible focus outline for all interactive elements |
| Generic alt text ("image", "icon") | Meaningful descriptions, or empty alt for decorative images |

## Quality Gates

| Gate | Target |
|------|--------|
| Contrast compliance | All text combinations meet WCAG AA (4.5:1 normal, 3:1 large) |
| Touch targets | 100% of interactive elements >= 44x44px on mobile products |
| Keyboard navigability | All functionality accessible via keyboard, zero traps |
| Lighthouse accessibility | Score > 90 on all pages |
| Screen reader annotations | ARIA labels specified for all icon buttons and non-text controls |

## Deep Reference

- Parent: `../SKILL.md` (WCAG section) | Reference: `../reference.md` → Contrast Verification, Touch Targets, Constrained-Context
- Checklists: `../forms.md` → Accessibility Checklist, Constrained-Context Checklist

## Team Integration

- **Design Review / Product Quality** teams — as accessibility auditor
- Pairs with: UI-DESIGN (compliance review), UX-RESEARCH (inclusive methods), frontend engineer (implementation handoff)
