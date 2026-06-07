---
name: Epic PRD Generator
description: Expand one epic outline into a detailed Epic PRD — full feature specs, persona-driven user stories, BDD (Given/When/Then) acceptance criteria, error scenarios, success metrics, and architecture-decision flags. Use when detailing a single epic into an implementation-ready PRD before story breakdown; do not use to generate all epic outlines at once (that is the epic generator's job) or to write code. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Epic PRD Generator (EXPERT-23)

Transform a single epic outline into a detailed Epic PRD with full feature
specifications, BDD acceptance criteria, error-handling scenarios, and architecture
decision (ADR) flags. This skill is the **method** — a 4-phase workflow that details
exactly ONE epic per invocation. The specifics it operates on — your repository paths,
output locations, and filename conventions — are decided per organization. See
[`ADAPT.md`](ADAPT.md) for what to decide before using this for a given organization.

When those specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** with neutral `PLACEHOLDER` paths (e.g.
`<products-root>/<product>/`, `<epic-prd-dir>/`, `<progress-file>`) and list what's
missing. Never invent the organization's folder layout, output paths, or filename
conventions.

**Core Philosophy**: Epic PRDs bridge high-level requirements and implementation. They
provide the detailed feature specifications that story generation requires, ensuring every
feature is fully specified before development begins.

## Workspace inputs (resolve these first)

Before researching or writing any Epic PRD, resolve every input path (epic outline, master
PRD, existing epic PRDs) and every output path (Epic PRD file, progress file, stories
index) from your organization's decided workspace conventions — never hardcode them. These
are the values listed in [`ADAPT.md`](ADAPT.md): your products root, progress file,
template locations, naming conventions, and the epic-PRD / stories sub-paths.

If those values are not yet decided, produce a clearly-labeled **GENERIC DRAFT** using
neutral `PLACEHOLDER` paths and list what's missing — do not guess.

## When to Activate

### Trigger Phrases
- "Create Epic PRD for E[XX]"
- "Generate detailed Epic [Name]"
- "Epic PRD for [epic name]"
- "Expand Epic [XX] into PRD"
- "Detail Epic [XX] features"
- "Create epic-PRD document for [epic]"

### Related Roles

| Role | Integration |
|------|-------------|
| **Epic generator** | Epic outline → Epic PRD (upstream) |
| **Story generator** | Epic PRD → stories (downstream) |
| **Master PRD author** | Master PRD context (feature details, personas) |
| **Software architect** | Architecture decisions, ADR creation |
| **Business-insights analyst** | Feature analysis question framework |
| **Product manager** | Feature prioritization |

## Required Context Sources

Resolve each path from your decided workspace conventions — the patterns below are
placeholders, not literals.

| Priority | Source | Path (resolve from your conventions) | Extract |
|----------|--------|--------------------------------------|---------|
| Critical | Epic Overview | `<products-root>/<product>/<epic-overview-file>` | Epic outline, features |
| Critical | Master PRD | `<products-root>/<product>/<prd-file>` | Feature details, personas |
| High | Existing Epic PRDs | `<products-root>/<product>/<epic-prd-dir>/*` | Template patterns |
| Medium | Vision Document | `<products-root>/<product>/<vision-file>` | Strategic context |
| Medium | Progress file | `<products-root>/<product>/<progress-file>` | Session context |
| Low | Design docs | `<products-root>/<product>/<design-dir>/*` | UI/UX patterns |

**Key Principle:** The epic outline is the PRIMARY input. The Epic PRD expands each feature
with full specifications. Do not invent features not in the outline.

## Generator vs Individual Skill

| Scope | Output |
|-------|--------|
| **Epic generator** — creates ALL epic outlines in one pass | Epic Overview Document |
| **This skill** — creates ONE detailed Epic PRD per invocation | One Epic PRD file in `<epic-prd-dir>` |

## Epic PRD Philosophy

1. **Features Fully Specified** — Each feature has user-story format, quantified success
   metrics, testable acceptance criteria, documented error scenarios.
2. **Persona-Driven** — User story for each feature: "As a [persona], I want…".
3. **Testable Criteria** — BDD format (Given/When/Then). Each criterion independently
   verifiable.
4. **Error Handling Required** — Every feature has error scenarios with user-facing messages
   and recovery paths.
5. **Dependencies Explicit** — Feature dependencies documented. Cross-epic dependencies clear.
6. **MoSCoW Tagged** — Every feature has a priority (P0–P3). MVP status clear.

## BDD Acceptance Criteria Format

All acceptance criteria MUST use BDD format (universal — independent of any organization):

```markdown
**Given** [initial context or precondition]
**When** [action or event occurs]
**Then** [expected outcome or behavior]
```

Structure acceptance criteria into categories:
- **Core Functionality:** Happy-path behaviors
- **User Experience:** UX-specific criteria
- **Edge Cases:** Boundary and edge-case handling
- **Performance:** Response-time and load criteria

## ADR Flagging

Flag ADRs for epic-wide architecture patterns, cross-feature design decisions, technology
choices, and integration patterns. Hand off significant decisions to a software architect:

```markdown
| Decision | Choice | ADR Required | Owner |
|----------|--------|--------------|-------|
| [Decision topic] | [Selected approach] | Yes / No | Software architect |
```

## Four-Phase Workflow Overview

```
Phase 0: RESEARCH (Automated)
  -> Read Epic Overview for target epic outline
  -> Read Master PRD for feature details
  -> Read existing Epic PRDs for patterns
  -> OUTPUT: Epic Context Summary (~250 words)

Phase 1: ANALYSIS & QUESTIONS
  -> Present epic context, show features to detail
  -> Ask 4 tailored clarification questions (Q1-Q4)
  -> WAIT FOR USER INPUT

Phase 2: GENERATION (Sequential)
  -> Apply user decisions, flag ADR decisions
  -> FOR EACH FEATURE: description, user story, BDD criteria, error scenarios, metrics
  -> OUTPUT: Complete Epic PRD with BDD Criteria + ADR Flags

Phase 3: VALIDATION (Blocking)
  -> Feature Coverage, BDD Format, ADR Check, Error Scenarios, Metrics
  -> IF ANY FAIL -> Return to Phase 2

Phase 4: OUTPUT & TRACKING
  -> Write the Epic PRD to <epic-prd-dir> using your naming convention
  -> Update the progress file, emit the story-generation handoff hook
```

**For detailed step-by-step instructions, see:** [`reference.md`](reference.md)
**For output templates and checklists, see:** [`forms.md`](forms.md)

## Anti-Patterns

1. **Generate without the epic outline** — Always read the Epic Overview first. Features
   must match the outline list.
2. **Skip acceptance criteria** — Every feature needs testable BDD criteria. Validation
   blocks on missing criteria.
3. **Use vague error messages** — Error scenarios must be specific. User messages must be
   helpful.
4. **Generate all epics at once** — This skill is ONE epic at a time. The epic generator
   produces all epic outlines.
5. **Add new features** — Only specify features from the Epic Overview. Do not invent new
   features.
6. **Skip dependencies** — Feature dependencies must be explicit. Cross-epic dependencies
   documented.

## Sub-Skills

Focused sub-skills available for targeted activation and Agent Teams:

| Sub-Skill | Focus |
|-----------|-------|
| [EPIC-PRD-FEATURES](sub-skills/EPIC-PRD-FEATURES.md) | Feature definitions, user flows, screen specs |
| [EPIC-PRD-BDD](sub-skills/EPIC-PRD-BDD.md) | Given/When/Then scenarios, edge cases, error paths |

Use the parent skill for full-scope work; use a sub-skill for focused team compositions.

## Output Summary

| File | Location (resolve from your conventions) | Typical Length |
|------|------------------------------------------|----------------|
| Epic PRD | `<products-root>/<product>/<epic-prd-dir>/<epic-prd-filename>` | 300–600 lines |

> All paths, output locations, and filename conventions are decided per organization — see
> [`ADAPT.md`](ADAPT.md). This skill stays portable: only those decisions change.
