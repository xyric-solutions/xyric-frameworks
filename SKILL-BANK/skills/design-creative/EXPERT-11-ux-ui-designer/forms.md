# EXPERT-11: UX/UI Designer — Forms & Checklists

Ready-to-use intake, templates, checklists, and output formats. Brand and audience
specifics are decided per organization (see [`ADAPT.md`](ADAPT.md)); this file never
hardcodes them.

---

## Design Context Intake (the questionnaire for adapting this skill)

Use this when the brand or audience for a surface isn't yet decided. Ask as one numbered
list and **WAIT** for answers; then record them wherever your team keeps brand and audience
decisions. Ask only what's missing.

**Brand tokens:**
1. **Primary color** — name + hex (and where it's used)?
2. **Accent color** — name + hex; use sparingly?
3. **Light base and dark base** — two hexes (surfaces vs. grounding/type)?
4. **Semantic colors** — success / warning / error / info hexes (or use defaults)?
5. **Typefaces** — display/headline font; body/technical/mono font; optional accent font?
6. **Logo** — where the files live, and light-on-dark vs. dark-on-light variants?
7. **Clear space & minimum size** — logo padding rule and smallest allowed size?
8. **Accessibility floor** — minimum contrast target (default WCAG AA 4.5:1)?

**Audience & device context:**
9. **Target users** — who are the primary segments? (device type, connectivity, literacy)?
10. **Device strategy** — mobile-first, desktop-first, or responsive-equal, and why?
11. **Constrained contexts** — low-end devices, slow networks, outdoor use, multilingual?
12. **Brand context for this surface** — branded, brand-free (creative freedom), or
    third-party/client brand?

---

## User Research Plan Template

```markdown
# User Research Plan: [Topic]

## Product Context
**Product:** [name / surface]
**Device Strategy:** [Mobile-first / Desktop-first / Responsive equal]

## Research Goals
**Primary Question:** [Main thing we need to learn]
**Secondary Questions:**
1. [Question 2]
2. [Question 3]

## Methodology
**Method:** [Interviews / Usability Testing / Surveys]
**Why this method:** [Rationale]

## Participants
**Target Users:** [Segment from the organization's ICP / target audience]
**Sample Size:** [Number] participants
**Recruiting Criteria:**
- Must have: [Required characteristics]
- Exclude: [Disqualifying factors]

## Session Structure (60 min)
- 0-5 min: Welcome, consent
- 5-15 min: Background questions
- 15-45 min: Main activity
- 45-55 min: Follow-up
- 55-60 min: Thank you

## Success Criteria
We'll have learned enough when we can:
- [Specific outcome 1]
- [Specific outcome 2]
```

---

## Usability Testing Script Template

```markdown
# Usability Test Script: [Feature Name]

## Pre-Test (5 min)

**Welcome:**
"Thank you for joining. We're testing [product/feature], not you. There are no wrong
answers. Think aloud as you work."

**Device Note:**
[If mobile product: "We'll be testing on a mobile device today."]
[If dashboard: "We'll be testing on desktop."]

## Tasks (30-40 min)

### Task 1: [Task Name]
**Scenario:** "[Realistic scenario in the user's own words]"

**Success Criteria:**
- [ ] User completes task without assistance
- [ ] Time: < [X] minutes
- [ ] Confidence rating: > 3/5

**Observe for:**
- Where do they look first?
- What do they tap/click?
- Where do they hesitate?

**Follow-up Questions:**
- How easy was that? (1-5 scale)
- What, if anything, was confusing?

## Post-Test (10 min)
- What was your overall impression?
- How does this compare to [competitor/current solution]?
- On a scale of 1-10, how likely are you to use this?
```

---

## Design Brief Template

```markdown
## Design Brief
**Date:** [YYYY-MM-DD]   **Requested by:** [Name]
**Surface:** [Mobile screen / Dashboard / Landing / Internal tool]
**Device strategy:** [Mobile-first / Desktop-first / Responsive equal]

### Concept
[1-2 sentences describing the design idea and the user goal it serves]

### Color direction (from the brand)
- Background: [light base / dark base]
- Text: [dark base / light base inverse]
- Accent: [accent color — sparingly]

### Typography (from the brand)
- Display: [display/headline font]    Body: [body/mono font]

### States to design
- [ ] Default  - [ ] Hover  - [ ] Focus  - [ ] Active  - [ ] Disabled
- [ ] Loading  - [ ] Error  - [ ] Empty

### Brand context
[Branded (apply the organization's brand tokens) / Brand-free (creative freedom) / Client brand]

### Checklist
- [ ] Tokens only  - [ ] All states  - [ ] Contrast met  - [ ] Touch targets  - [ ] Alt text
```

---

## Dev Mode Handoff Checklist

```
- [ ] All components use the organization's design tokens (not hardcoded values)
- [ ] Responsive breakpoints specified (mobile, tablet, desktop)
- [ ] All interactive states documented (default, hover, focus, active, disabled)
- [ ] Spacing annotated in 8pt grid units
- [ ] Typography uses defined text styles (display/body/mono from the brand)
- [ ] Colors use semantic tokens (e.g. "error", not "red")
- [ ] Accessibility annotations included (ARIA labels, alt text)
- [ ] Edge cases designed (empty states, errors, loading, overflow)
- [ ] Developer notes added for complex interactions
- [ ] Assets exported at 1x, 2x, 3x (or SVG)
- [ ] Component mapping clear (which design-system component to use)
```

---

## Accessibility Checklist (All Products)

### Perceivable
```
- [ ] All images have meaningful alt text (or empty for decorative)
- [ ] Color is not the only way to convey information
- [ ] Sufficient color contrast (4.5:1 minimum for text)
- [ ] Text can resize to 200% without loss of functionality
```

### Operable
```
- [ ] All functionality available via keyboard
- [ ] No keyboard traps
- [ ] Focus indicators visible and clear
- [ ] Touch targets minimum 44x44px (mobile products)
- [ ] Skip links for repetitive navigation
```

### Understandable
```
- [ ] Language of page declared
- [ ] Form labels associated with inputs
- [ ] Error messages clear and specific
- [ ] Consistent navigation across pages
```

### Robust
```
- [ ] Valid HTML markup
- [ ] ARIA used correctly (when HTML semantics are insufficient)
- [ ] Name, role, value available for all UI components
```

---

## Design QA Checklist (Before Handoff to Frontend)

```
### Quality Standards
- [ ] All designs use the organization's design tokens (not hardcoded)
- [ ] Product device strategy correct (mobile/desktop)
- [ ] Brand colors applied correctly (or creative freedom noted for brand-free surfaces)
- [ ] Cross-role review obtained if needed

### Design Completeness
- [ ] All screens/states designed (default, hover, focus, active, disabled, loading, error, empty)
- [ ] Responsive breakpoints defined
- [ ] All interactive elements specified
- [ ] Edge cases designed (long text, no data, many items)

### Accessibility (WCAG AA)
- [ ] Color contrast checked (4.5:1 minimum)
- [ ] Touch targets >= 44x44px (mobile products)
- [ ] Focus states visible
- [ ] Alt text provided for images
- [ ] ARIA labels specified for icon buttons
- [ ] Form labels associated with inputs

### Dev Mode
- [ ] Annotations added
- [ ] Assets exported (SVG preferred)
- [ ] Responsive behavior documented
- [ ] Developer notes for complex interactions
- [ ] Component mapping clear
```

---

## Constrained-Context Design Checklist

```
For products whose audience (per the organization's target segments) uses low-end devices,
limited connectivity, or operates in challenging physical conditions:

### Device Diversity
- [ ] Works on low-end devices
- [ ] Adapts to varying screen sizes
- [ ] Doesn't require the latest OS versions

### Connectivity
- [ ] Skeleton loading for slow networks
- [ ] Offline states designed
- [ ] Data-efficient images
- [ ] Progressive loading

### Language & Literacy
- [ ] Multi-language support planned where the audience is multilingual
- [ ] Simple, clear language
- [ ] Icons supplement text
- [ ] Voice input/output considered where literacy varies

### Physical Context
- [ ] Outdoor visibility (high contrast)
- [ ] One-handed operation
- [ ] Large touch targets (44px+)
```

---

## Component Documentation Template

```markdown
# Component: [Component Name]

## Overview
[One sentence describing the component's purpose]

## Variants
- **[Variant 1]:** [Description] — uses [token]
- **[Variant 2]:** [Description] — uses [token]

## Anatomy
- Padding: [Values]
- Height: [Mobile] / [Desktop]
- Icons: [Optional/Required, position]

## States
- Default
- Hover
- Focus
- Active
- Disabled
- Loading
- Error

## Accessibility
- Touch target: [Size]
- Keyboard: [Key bindings]
- Focus indicator: [Style]
- Screen reader: [Announcements]

## Usage Guidelines
### Do
- [Guideline 1]
- [Guideline 2]

### Don't
- [Anti-pattern 1]
- [Anti-pattern 2]

## Design Link
[Link to the design-system component library]

## Frontend Integration
Handoff via Dev Mode with:
- Token references (not hex values)
- All states documented
- Responsive behavior specified
```

---

## Platform sizing (universal — not brand-specific)

| Asset | Size |
|-------|------|
| LinkedIn post image | 1200 × 627 px |
| LinkedIn carousel slide | 1080 × 1080 px |
| X (Twitter) post image | 1200 × 675 px |
| Instagram feed post | 1080 × 1080 px |
| Instagram reel / story | 1080 × 1920 px |
| App icon (source) | 1024 × 1024 px |
| Favicon | 32 × 32 px / 16 × 16 px |
