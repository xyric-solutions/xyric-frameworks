# EXPERT-11: UX/UI Designer — Reference

Deep expertise, patterns, and detailed methodology. Load on demand when working on design
tasks. Brand specifics (palette, typography, logo) are decided per organization (see
[`ADAPT.md`](ADAPT.md)); the structural patterns below are universal and brand-independent.

---

## The brand & audience inputs

These are the concrete values this skill operates on, decided per organization:

```yaml
brand:
  palette:
    primary:  { name, hex, usage }
    accent:   { name, hex, usage }     # often "use sparingly"
    light:    { name, hex, usage }     # surfaces / backgrounds
    dark:     { name, hex, usage }     # grounding / type
    semantic: { success, warning, error, info }
  typography:
    display: { font, usage }           # headlines
    mono:    { font, usage }           # technical / labels / data / code
    accent:  { font, usage }           # optional
  logo:    { dir, files[], clear_space, min_size }
  voice:   { tagline, attributes[], avoid[] }
  accessibility: { primary_target, semantic_target }

audience:
  segments: []         # who you design for — device, literacy, connectivity context
  key_messages: []     # what each screen must communicate
```

Resolve every concrete value at use time from the organization's brand and audience
decisions. If a value isn't decided, treat it as unanswered — ask via the intake in
`forms.md`, or fall back to a labeled `PLACEHOLDER`. Never invent a hex, font, or target
audience.

---

## Design token structure (fill values from the brand)

Build a token set so designs reference semantics, never raw values. The keys below are a
standard, brand-agnostic structure; each value is resolved from the organization's brand.

```jsonc
{
  "colors": {
    "brand": {
      "primary":  "/* brand primary hex */",
      "accent":   "/* brand accent hex  */",
      "light":    "/* brand light base hex   */",
      "dark":     "/* brand dark base hex    */"
    },
    "semantic": {
      "success":  "/* semantic success */",
      "warning":  "/* semantic warning */",
      "error":    "/* semantic error   */",
      "info":     "/* semantic info    */"
    },
    "background": { "light": "/* light base */", "dark": "/* dark base */", "surface": "#ffffff" },
    "text":       { "primary": "/* dark base */", "secondary": "/* accent */", "inverse": "/* light base */" },
    "border":     { "default": "/* neutral 200 */", "strong": "/* accent */" },
    "dataViz":    [ "/* primary→accent progression: 5–6 steps from the primary to the accent */" ]
  },
  "spacing": { "0":"0","1":"4px","2":"8px","3":"12px","4":"16px","5":"20px","6":"24px","8":"32px","10":"40px","12":"48px" },
  "typography": {
    "fontFamily": {
      "heading": "/* brand display/headline font */, system-ui, sans-serif",
      "body":    "/* brand body/mono font or clean system stack */, system-ui, sans-serif",
      "code":    "/* brand mono font */, ui-monospace, monospace"
    },
    "fontSize":   { "xs":"12px","sm":"14px","base":"16px","lg":"18px","xl":"20px","2xl":"24px","3xl":"30px","4xl":"36px" },
    "fontWeight": { "regular":"400","medium":"500","semibold":"600","bold":"700" }
  },
  "borderRadius": { "sm":"4px","md":"8px","lg":"12px","full":"9999px" },
  "shadow": {
    "sm":"0 1px 2px 0 rgb(0 0 0 / 0.05)",
    "md":"0 4px 6px -1px rgb(0 0 0 / 0.1)",
    "lg":"0 10px 15px -3px rgb(0 0 0 / 0.1)",
    "xl":"0 20px 25px -5px rgb(0 0 0 / 0.1)"
  }
}
```

### Color contrast verification (do this for the brand's actual hexes)

Before approving any combination, compute its ratio and record the result:

| Combination | Required | Verify against |
|-------------|----------|----------------|
| Body text on its background | ≥ 4.5:1 | WCAG AA normal text |
| Large/display text on its background | ≥ 3:1 | WCAG AA large text |
| UI component / focus indicator vs. adjacent color | ≥ 3:1 | WCAG 2.1 non-text contrast |

Keep a contrast matrix per project listing each palette pairing and its measured ratio.
Mid-tone accents often pass only for large text — reserve the dark base for body copy.

### Logo usage rules

Use the variants and rules from the organization's logo definition:

- Files come from the logo asset set — a light-on-dark variant and a dark-on-light variant.
- **Clear space**: per the brand's clear-space rule (e.g. padding equal to the wordmark's cap height).
- **Minimum size**: per the brand's minimum-size rule (default 32px height digital, 0.5" print).
- **Background contrast**: light mark on dark surfaces, dark mark on light surfaces.
- **No modifications**: never rotate, skew, distort, recolor, or add effects to the mark.

---

## Mobile-first design patterns

For conversational, messaging-led, and consumer-mobile products.

### Mobile layout example

```
+------------------------+
| <- Header          [=] |  <- 56px height, sticky
+------------------------+
|                        |
|   +----------------+   |
|   |    Content     |   |  <- Card with 16px margin
|   +----------------+   |
|                        |
|   +----------------+   |
|   |    Content     |   |
|   +----------------+   |
|                        |
+------------------------+
| [Primary Action]       |  <- 44px+ height, full width
+------------------------+
```

### Touch targets
- Minimum 44×44px (WCAG AAA target size)
- Comfortable spacing between tappable elements
- Thumb-zone-friendly placement

### Constrained-context considerations (check the organization's target segments for which apply)

When the audience uses low-end devices, slow or intermittent networks, or operates outdoors:

- Low bandwidth: skeleton loading, progressive image loading, data-saver modes
- Offline states explicitly designed
- Diverse device capabilities — don't assume the latest OS or hardware
- Multi-language support where the audience is multilingual; icons supplement text
- High contrast for outdoor visibility
- One-handed operation

### Conversational / messaging-led patterns

For products delivered through a chat or messaging surface:

- Conversational UI patterns and chat-bubble aesthetics
- Quick-reply buttons for guided flows
- Media-message handling (images, documents, voice)

---

## Desktop-first design patterns (dashboards)

### Dashboard layout example

```
+------------------------------------------------------------+
| Logo     Search                    [User] [Settings] [Help] |  <- Top nav
+---------+--------------------------------------------------+
|         |  Page Title                       [Export] [+]    |
| Nav     +--------------------------------------------------+
|         |  +-------+ +-------+ +-------+ +-------+         |
| - Home  |  | KPI 1 | | KPI 2 | | KPI 3 | | KPI 4 |        |  <- Metric cards
| - Dash  |  +-------+ +-------+ +-------+ +-------+         |
| - Data  +-------------------------+------------------------+
| - ...   |      Main Chart         |     Secondary Chart    |  <- Data viz
|         +-------------------------+------------------------+
|         |  Data Table                                      |
+---------+--------------------------------------------------+
```

### Desktop design principles
- Information density: show more data without overwhelming
- Use the dataViz palette (primary→accent progression) for charts; pair with a data-viz
  skill for chart selection and dashboard philosophy
- Hover states for additional info
- Keyboard shortcuts and focus management; tab navigation through data tables
- Sidebar navigation with resizable panels

---

## Visual design patterns

### Empty states

```
+--------------------------------------+
|           [Illustration]              |  <- brand colors
|                                       |
|         No items yet                  |  <- display font, dark text
|                                       |
|   You haven't added any items.        |  <- body font, secondary text
|   Get started by creating your        |
|   first one.                          |
|                                       |
|     [+ Create Item]                   |  <- primary button (brand primary)
+--------------------------------------+
```

### Loading states (skeleton screen)

```
+--------------------------------------+
| ############                          |  <- animated pulse, palette tints
| ####################                  |
|                                       |
| ########          ########            |
+--------------------------------------+
```

For mobile and constrained contexts: show immediately, match the structure of the final
content, minimal animation for low bandwidth.

### Error states

```
+--------------------------------------+
| Email                                 |
| +----------------------------+        |
| | user@invalid               |        |  <- error border (semantic error)
| +----------------------------+        |
| Please enter a valid email address    |  <- error-color text
+--------------------------------------+
```

Error-message guidelines: explain what happened, explain what to do next, helpful (not
blaming) tone, no error codes without explanation, no technical jargon.

---

## Component documentation pattern

```markdown
# Component: Button

## Overview
Buttons trigger actions when clicked. Use buttons for primary actions.

## Variants
- **Primary:**   Main call-to-action — uses the brand primary
- **Secondary:** Alternative actions — uses the brand accent
- **Outline:**   Low-priority actions — primary border on light surface
- **Danger:**    Destructive actions — uses the semantic error color

## Anatomy
- Padding: 16px / 24px
- Height: 44px (mobile), 40px (desktop)
- Icons: optional, leading or trailing

## Accessibility
- Touch target: 44×44px minimum (mobile products)
- Keyboard accessible (Enter / Space to activate)
- Focus indicator: 2px outline, accent color, ≥ 3:1 contrast
- Loading state announced to screen readers

## Usage Guidelines
DO:    one primary action per view, clear labels, primary color for the main action
DON'T: multiple competing primaries, vague labels, error color for non-destructive actions
```

---

## Design-system library organization (Figma)

```
Design System:
├── Cover Page (overview, links, changelog)
├── Foundations
│   ├── Colors (brand palette + semantic + dataViz — from the brand)
│   ├── Typography (display + body + mono — from the brand)
│   ├── Spacing (8pt grid)
│   ├── Elevation (shadow system)
│   ├── Border Radius
│   └── Iconography
├── Components
│   ├── Buttons (primary, secondary, danger)
│   ├── Forms (inputs, selects, checkboxes)
│   ├── Navigation
│   ├── Feedback (alerts, toasts, modals)
│   ├── Data Display (tables, cards, charts)
│   └── Overlays
├── Patterns
│   ├── Mobile Patterns
│   ├── Dashboard Patterns
│   ├── Form Patterns
│   ├── Empty States
│   ├── Error States
│   └── Loading States
├── Templates
│   ├── Mobile App Screens
│   ├── Dashboard Templates
│   ├── Landing Pages
│   └── Internal Tools
└── Documentation
    ├── Getting Started
    ├── Brand Guidelines (link to the brand-guidelines skill / brand docs)
    └── Changelog
```

---

## Accessibility standards (generic)

| Standard | Requirement |
|----------|-------------|
| Primary text contrast | the organization's contrast target (default WCAG AA 4.5:1; AAA where stated) |
| Large text contrast | 3:1 minimum |
| UI / focus indicator contrast | 3:1 minimum |
| Touch targets | 44×44px minimum on mobile |
| Color not sole indicator | Always pair color with text, icon, or pattern |
| Alt text | All meaningful images get descriptive alt text; decorative images get empty alt |
| Readable fonts | Minimum 14px body, 12px captions |

---

## References

- **Within this skill**: sub-skills `UX-RESEARCH`, `UI-DESIGN`, `UX-A11Y`; templates in
  `forms.md`.
- **Companion roles**: product manager (requirements), frontend engineer (handoff),
  data-viz / dashboard skill (charts), brand-guidelines skill (brand token source of truth),
  creative-direction skill (brand-free aesthetics).
- **External**: [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/),
  [Material Design](https://m3.material.io/),
  [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/).
