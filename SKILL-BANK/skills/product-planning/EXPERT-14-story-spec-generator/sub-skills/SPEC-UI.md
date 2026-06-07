---
name: SPEC-UI
parent: EXPERT-14
description: Generate UI component specifications from user stories — hierarchy, props, state, responsive behavior.
version: "1.0"
domain: UI component design and interaction specifications
---

# UI Component Specs (SPEC-UI)

> Sub-skill of [Story Spec Generator (EXPERT-14)](../SKILL.md)

## Focus Area

Transforms user story acceptance criteria into detailed UI component specifications. Covers component hierarchy, props/state definitions, wireframe descriptions, responsive behavior across viewports, and interaction state management. Does NOT cover API endpoint design or database schema — defer those to SPEC-API and SPEC-DATA respectively.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Component Hierarchy | Tree structure, composition patterns, reuse identification |
| Props & State | TypeScript interfaces, local vs global state, server state integration |
| Interaction States | Loading, error, empty, success — complete state matrix per component |
| Responsive Behavior | Desktop (1440px), tablet (768px), mobile (375px) layout adaptation |
| Design System Alignment | Reuse existing components, tokens, and patterns from the product design docs |

## Methodology

### Priority Order
1. Read the product design system FIRST — reuse before creating new components
2. Map acceptance criteria to visual elements and user interactions
3. Define the component tree top-down, then detail each component bottom-up
4. Every component must handle all four states: loading, error, empty, success

### Workflow
1. Review the product design-system docs (your design area)
2. Build component hierarchy tree from page down to atomic elements
3. Define TypeScript prop interfaces and state hooks for each component
4. Document interaction states and user event handlers
5. Specify responsive behavior at three viewports (1440px, 768px, 375px)

## Key Patterns

**Design System First**: Check the product design system before specifying new components. Reuse ensures visual consistency and reduces implementation effort.

**Four-State Completeness**: Every data-driven component specifies what it renders in loading, error, empty, and success states. No component should show a blank screen for any data condition.

**Props as Contract**: Component props are the interface between parent and child. Define them as TypeScript interfaces with clear types, optionality, and descriptions. Props drive testability.

**Event Flow Documentation**: Document trigger (user action), handler (function), and effect (state change, API call, navigation) for every interactive element.

**Responsive by Default**: Specify layout at three breakpoints. Mobile-first: start with 375px, then expand. Stack on mobile, grid on desktop.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Components without state definitions | Define all four states (loading, error, empty, success) |
| New components when design system has existing ones | Audit design system first, extend before creating |
| Props typed as `any` or `object` | Explicit TypeScript interfaces for all props |
| Desktop-only specs | Specify responsive behavior at 1440px, 768px, 375px |

## Quality Gates

| Gate | Target |
|------|--------|
| AC visual coverage | Every acceptance criterion mapped to a component |
| State completeness | All components handle loading, error, empty, success |
| Design system reuse | Existing components referenced before creating new ones |
| Responsive coverage | Layout specified for desktop, tablet, and mobile |

## Deep Reference

For detailed patterns and code examples in this domain:
- Parent skill: `../SKILL.md` (full tech-spec philosophy, cross-skill integration)
- Reference sections: `../reference.md` → Q3: UI Components, Q4: User Flows & States
- Checklists: `../forms.md` → Section 5: UI Components, Component hierarchy

## Team Integration

This sub-skill is designed for use in:
- **Product Development Team** — as the UI specification specialist
- Pairs well with: SPEC-API (endpoint responses shape component data needs), SPEC-DATA (validation rules inform form behavior)
