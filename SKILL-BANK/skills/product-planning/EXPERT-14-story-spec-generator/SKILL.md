---
name: Story Spec Generator
description: Turn a user story into a complete technical specification — API contracts, data models, UI components, security, testing, performance — and flag architecture decisions for review. Use when a story is ready to be specced for engineering; do not use to write the story itself (that is upstream) or to break work into tasks (that is downstream). To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Story Spec Generator (EXPERT-14)

Transform a single **user story** into a detailed **technical specification** that
gives a team everything it needs for task breakdown. This skill bridges product
requirements and engineering implementation. It is the **method** — the spec frameworks,
question flow, and validation gates.

**Core philosophy:** a technical spec translates a user-facing story into an
engineering-ready design. It defines APIs, data models, UI components, and integration
patterns — the **HOW** — without changing the story's **WHAT**.

- **Type:** Individual (one story at a time)
- **Flags:** Architecture Decision Records (ADRs) for review

The specifics this skill operates on — where stories, specs, and planning files live, and
how files and IDs are named — are decided per organization. See [`ADAPT.md`](ADAPT.md) for
what to decide before using this for a given organization. When those specifics are not yet
decided, **do not invent them** — produce a clearly-labeled **GENERIC DRAFT** with a neutral
`PLACEHOLDER` output path and `PLACEHOLDER` story/spec IDs, and list what's missing. The spec
**content** below is portable and needs no adaptation.

## When to Activate

### Trigger Phrases
- "Create tech spec for story [ID]"
- "Generate technical specification for [story]"
- "Story spec for [story ID]"
- "Technical design for [story]"
- "Spec out story [ID]"

### Related Skills

| Skill | Integration |
|-------|-------------|
| Story Generator | Story → Tech Spec (upstream) |
| Task Generator | Tech Spec → Tasks (downstream) |
| Software Architect | Architecture patterns, ADR creation |
| Business Insights / question framework | Hypothesis-driven question alignment |
| Engineers (frontend / backend / full-stack) | Implementation guidance |

### Workflow Position

```
Story Generator → [Story Spec Generator] → Task Generator → Implementation Guide
                   ^^^^^^^^^^^^^^^^^^^^^^
                   YOU ARE HERE
```

## Required Context Sources

The locations below are illustrative roles, not literal paths — use your organization's
document roots, planning file, and naming conventions (see [`ADAPT.md`](ADAPT.md)).

| Priority | Source | Where | Extract |
|----------|--------|-------|---------|
| Critical | Story file | your stories area | Target story |
| High | Epic PRD | your epic-PRD area | Feature context |
| High | Design system | your design area | UI patterns |
| Medium | Master PRD | your product requirements doc | Technical reqs |
| Medium | Planning/status file | your planning/status file | Architecture decisions |
| Low | Existing specs | your specs area | Reusable patterns |

**Key principle:** the user story is the PRIMARY input. The tech spec defines HOW to
implement without changing WHAT the story requires.

## Tech Spec Philosophy

1. **Spec defines HOW, not WHAT** — the story owns user-facing behavior; the spec owns the technical approach
2. **API-first design** — define contracts before implementation; schemas explicit; error codes documented
3. **Data-model clarity** — entities and relationships defined; schema changes documented; migration path considered
4. **UI component breakdown** — component hierarchy; state-management approach; event flows documented
5. **Testability built-in** — test strategy per layer; test-data requirements; coverage expectations
6. **Security by design** — auth/authz requirements; data protection; input-validation rules
7. **Performance considered** — response-time targets; resource limits; optimization opportunities

## Four-Phase Workflow (Overview)

### Phase 0: Research (automated)
1. Locate the story, read the Epic PRD, gather design-system patterns
2. Identify technical questions and decisions
3. OUTPUT: Story Technical Context (~300 words)

### Phase 1: Analysis & Questions
4. Present story + technical context to the user
5. Ask 5 tailored technical questions (Architecture ×2, UI/UX ×2, Technical ×1)
6. **WAIT FOR USER INPUT** (blocking)
7. Optional follow-up questions

### Phase 2: Generation (sequential)
8. Apply user decisions to the technical approach
9. Identify architecture patterns (invoke the Software Architect skill)
10. Flag ADR decisions; generate API contracts, data models, UI components
11. OUTPUT: complete Technical Specification with ADR flags

### Phase 3: Validation (blocking)
12. Story coverage, section check, architecture alignment, design-system refs
13. Completeness (no TBD), consistency (API/Data/UI aligned)
14. IF ANY CHECK FAILS → return to Phase 2, fix, re-validate

### Phase 4: Output & Tracking
15. Write the spec to your specs area, named per your spec filename convention
16. Update your planning/status file; emit pipeline hook for the Task Generator

> Detailed step-by-step instructions, question frameworks, and generation patterns: [`reference.md`](reference.md).
> Output templates and quality checklists: [`forms.md`](forms.md).

## Architecture Alignment

### Pattern Selection (invoke the Software Architect skill)

| Pattern Category | Examples | When to Apply |
|------------------|----------|---------------|
| Data patterns | Repository, CQRS, Event Sourcing | Data-heavy stories |
| API patterns | REST, GraphQL, BFF | API design decisions |
| UI patterns | Container/Presenter, Compound Components | Complex UI |
| Integration patterns | Saga, Circuit Breaker, Retry | External integrations |

### ADR Flagging

**When to flag for ADR:**
- New architectural pattern introduced
- Deviation from established patterns
- Cross-cutting concerns (auth, logging, caching)
- Technology choices with long-term implications

**ADR flag format:**
```markdown
**ADR Required:** [Decision Topic]
- **Impact:** High | Medium | Low
- **Scope:** Story | Epic | Product
- **Action:** Invoke the Software Architect skill for ADR creation
```

## Assumption Challenge

Between Phase 0 and Phase 1, surface the key assumptions at **medium intensity**:
- **A: Question why** — architecture patterns, technology choices
- **B: Alternatives** — API design, data-model choices

**Skip when:** the user requests a bypass, you are following an established pattern, or
the decisions already live in approved ADRs.

## Sub-Skills

Focused sub-skills for targeted activation and Agent Teams:

| Sub-Skill | Focus | Agent Stub |
|-----------|-------|------------|
| [SPEC-API](sub-skills/SPEC-API.md) | API contracts, endpoints, error codes | `spec-api` |
| [SPEC-DATA](sub-skills/SPEC-DATA.md) | Entity relationships, schema, migrations | `spec-data` |
| [SPEC-UI](sub-skills/SPEC-UI.md) | Component breakdown, props/state, responsive | `spec-ui` |

Use the parent skill for full-scope work; use a sub-skill for focused team compositions
(e.g., three specs generated in parallel).

## Anti-Patterns

1. **Generate without the story** — always read the story first; the spec must address every acceptance criterion
2. **Change story requirements** — the spec defines HOW, not WHAT; never modify acceptance criteria
3. **Skip the security section** — every spec needs security considerations
4. **Leave decisions unresolved** — capture open decisions with a recommendation
5. **Forget the testing strategy** — every spec needs a test approach with coverage expectations
6. **Ignore performance** — response-time targets required; resource limits considered

## Output

- **File:** your specs area, named per your spec filename convention (e.g., a `Story-[ID]-Spec` document)
- **Typical length:** 400–700 lines per story
- **Quality bar:** every acceptance criterion addressed; all 10 sections present
- **Pipeline hook:** an HTML comment marking the story ready for tasks (e.g., `<!-- TASKS_READY: [Story ID] -->`)

> All locations and filename shapes are organization-specific — see [`ADAPT.md`](ADAPT.md).
> This skill stays portable across organizations; only the adapted values change.
