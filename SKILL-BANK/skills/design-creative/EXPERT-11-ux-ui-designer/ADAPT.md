# Adapting UX/UI Designer

**What this skill does:** designs and reviews interfaces, flows, design systems, and
accessibility, applying one organization's visual identity and audience context to the work.

This skill is generic methodology — it never hardcodes a specific brand or audience. To use
it for your organization, decide the values below and either keep them in your design brief
at use time, or bake them into your forked copy of `SKILL.md`. Until they're decided, the
skill emits a labeled GENERIC DRAFT (neutral placeholders, system fonts, 44px targets)
rather than inventing a brand or a target audience.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Palette** — primary, accent, light base, dark base (name + hex each) | Priority Order, Design context, Core Workflow | Note if the accent is "use sparingly". Drives the design tokens. |
| **Semantic colors** — success / warning / error / info | Accessibility, Core Workflow | Defaults are fine if you have none. |
| **Typefaces** — display/headline font, mono/technical font, optional accent font | Core Workflow | State a system-font fallback. |
| **Logo** — asset location, light-on-dark vs. dark-on-light variants | Design context, Cross-Skill Integration | See `reference.md` for usage rules. |
| **Clear space & minimum size** — logo padding rule + smallest allowed size | Cross-Skill Integration | Defaults: 32px digital / 0.5in print. |
| **Contrast target** — minimum ratio (default WCAG AA 4.5:1) | Accessibility, Success Criteria | Raise to AAA where required. |
| **Target users / ICP segments** — primary segments and their device, connectivity, literacy context | Core Workflow, device-strategy table | Drives research recruiting and constrained-context design. |
| **Key messages** — what each screen must communicate | Core Workflow | Optional; shapes content hierarchy. |
| **Device strategy** — mobile-first, desktop-first, or responsive-equal | Product-appropriate device strategy | Pick from product context, not habit. |
| **Constrained contexts** — low-end devices, slow networks, outdoor use, multilingual | Accessibility, Key Anti-Patterns | Determines which inclusive-design patterns apply. |

## How to gather these

The numbered **Design Context Intake** in [`forms.md`](forms.md) is the questionnaire for all
of the above — ask it once, record the answers wherever your team keeps brand and audience
decisions (a design brief, a fork of `SKILL.md`, or your own design-system docs).

## Platform-independent (do not change)

`forms.md` checklists (accessibility, design QA, dev-mode handoff, constrained-context),
template formats, and platform sizing — and `reference.md` token structure, layout patterns,
and WCAG thresholds — are universal facts. They work as-is for any organization; only the
concrete color/font/logo/audience values plug into them.
