---
name: Story Generator
description: Break product Epics into well-defined user stories with BDD (Given/When/Then) acceptance criteria, INVEST sizing, 100% feature-coverage validation, and a blocking quality gate. Use when decomposing an Epic or Epic PRD into stories, building a coverage matrix, or validating story completeness; do not use for writing the Epic PRD itself (that is upstream) or for breaking stories into implementation tasks (that is downstream). To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Story Generator (EXPERT-13)

Break down product Epics into comprehensive, well-defined user stories using an
interactive multi-phase workflow that guarantees consistent quality and 100% Epic
coverage. This skill is the **method** — research, questioning, generation, validation,
output. The specifics it operates on — where stories and tasks are written, the filename
conventions, the story-linking field, and the product taxonomy — are decided per
organization. See [`ADAPT.md`](ADAPT.md) for what to decide before using this for a given
organization.

**Core philosophy:** Stories define **WHAT** needs to be done, not **HOW** to implement
it. All stories combined must achieve 100% Epic coverage with no gaps.

When the workspace specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** (write stories to a neutral `stories/` folder with a
`PLACEHOLDER` naming pattern) and list what is missing. Never invent an organization's real
folder layout, naming scheme, or linking field.

The methodology below (INVEST, MoSCoW, BDD Given/When/Then, the 4-phase workflow) is
universal and stays the same for any product.

## When to Activate

### Trigger phrases
- "Break down Epic [X]"
- "Generate stories for Epic [X]"
- "Epic to stories" / "Epic → Story breakdown"
- "Story breakdown for [Epic name]"
- "Create user stories from [Epic]"

### Related skills

| Skill | Integration |
|-------|-------------|
| **EXPERT-10** (Product Manager) | MoSCoW prioritization, PRD structure, lifecycle alignment |
| **EXPERT-03** (Software Architect) | Technical feasibility, modularity, scalability |
| **BI-02** (Question Framework) | Breaking requirements into testable hypotheses |
| **DEV-02** (Test Generator) | Acceptance-criteria patterns, test-case thinking |
| **EXPERT-04** (QA Engineer) | TDD/BDD story structure |

## Required Context Sources

The Epic PRD is the **primary** input. Other sources provide supporting context but must
never block story generation. Resolve all paths relative to the product folder root.

| Priority | Source | Where | Extract |
|----------|--------|-------|---------|
| Critical | Epic PRD | Epic-PRD folder for the product | Feature definitions (F[X.Y]), MVP status |
| Critical | Existing stories | the product's story folder | Template patterns, structure |
| High | Product Requirements doc | product root | Success metrics |
| High | Planning/context file | the per-product planning/context file | Global decisions, prior learnings |
| Medium | Vision docs | product root | Strategic alignment |
| Medium | Cross-Epic PRDs | Epic-PRD folder | Dependencies |
| Low | Design docs | the product's design folder | UI/UX context |

### Product context (if present)

Many products keep a `context/` folder. Load what exists:

| File | Usage | Required |
|------|-------|----------|
| `personas.md` | Accurate persona names in stories | Recommended |
| `terminology.md` | Consistent vocabulary | Recommended |
| `pillars.md` | Domain context | Optional |
| `design-decisions.md` | Respect existing decisions | Optional |

**Missing context handling:** Notify the user which file is absent, proceed using the Epic
PRD as primary reference, and use generic persona references if `personas.md` is
unavailable. If `terminology.md` exists, use it to keep product vocabulary consistent.

## Story Philosophy

1. **Stories define WHAT, not HOW** — describe what must be accomplished and the user
   value; implementation is deferred to task breakdown.
2. **100% Epic coverage** — all stories combined = complete Epic implementation, no gaps.
   Verify with a Feature → Story coverage matrix.
3. **Flexible sizing (not equal chunks)** — story size follows natural scope. Some stories
   are larger, some smaller; story count varies by Epic complexity. Split on cognitive
   load, not arbitrary rules.
4. **User-adaptive flexibility** — combine feature variants by default; split only when
   complexity demands separate stories. Embed error handling unless substantial.
5. **Evidence-based splitting** — split when cognitive load is too high, when distinct
   personas have fundamentally different needs, or when error handling deserves dedicated
   focus. Never split arbitrarily by variant.
6. **Sensible ordering** — sequence stories so implementation makes sequential sense
   (foundation before dependents).
7. **Product-agnostic design** — no hardcoded product patterns. Use the organization's real
   structure, naming, and terminology (decided per ADAPT.md); the skill works for ANY
   product's Epics.

## Four-Phase Interactive Workflow

```
Phase 0: RESEARCH (Automated)
  → Identify product (from the organization's product taxonomy) and Epic PRD
  → Gather context from the product folder; read existing stories
  → Check the planning/context file for global decisions
  → Extract Epic PRD features, personas, dependencies; classify complexity (Simple/Medium/Complex)
  → OUTPUT: Epic Analysis Summary (~500 words) — the ONLY context used downstream

Phase 1: ANALYSIS & QUESTIONS
  → Present the compressed Epic summary (not the full PRD) and context findings
  → Ask the 9 tailored clarification questions (Q1–Q9, with Epic context baked in)
  → ═══ WAIT FOR USER INPUT ═══

Phase 2: STORY GENERATION (Sequential)
  → Apply user decisions to the story breakdown
  → FOR EACH FEATURE: generate story/stories from the template, check overlap with prior
    stories, update the running dependency graph, add to the coverage matrix
  → OUTPUT: stories + dependency diagram + coverage matrix

Phase 3: VALIDATION (Blocking)
  → Coverage, Duplicate, Template, DAG checks (block if fail)
  → BDD / Quantified-metrics / Edge-case / Open-question quality checks
  → IF ANY CRITICAL CHECK FAILS → return to Phase 2, fix, re-validate

Phase 4: OUTPUT & TRACKING
  → Write individual story files into the story folder using the story filename pattern
  → Write the Epic index using the Epic-index filename pattern
  → Update the planning/context file with the session
  → Emit pipeline hooks for the downstream task-generation skill
```

**Step-by-step detail:** [`reference.md`](reference.md). **Output templates & checklists:**
[`forms.md`](forms.md).

### Assumption challenge (light)

Between Phase 0 (Research) and Phase 1 (Questions), run a **light** assumption challenge
(question-why only):

- Priority assignments: "Why is this feature P0 vs P1?"
- Story granularity: "Why split/combine these stories this way?"
- Scope boundaries: "Should this story include X, or is that separate?"

**Skip** the challenge when the user requests a bypass, when revising (not newly breaking
down) stories, or when priorities were already validated at the Epic-PRD level.

### The 9 clarification questions (Phase 1)

Questions must include Epic context — never generic. Full tailored wording is in
[`reference.md`](reference.md) and [`forms.md`](forms.md).

| Group | Q | Asks |
|-------|---|------|
| Strategic | Q1 Priority Validation | Adjust any MoSCoW priorities? Anything explicitly "Won't Have" for MVP? |
| Strategic | Q2 Scope Boundaries | Any MVP-Core features to explicitly exclude (mark post-MVP)? |
| Strategic | Q3 Story Granularity | Granular (1–3 day), Larger (5–7 day), or Mixed? |
| Technical | Q4 Tech-Stack Constraints | Selected APIs, framework preferences, architectural patterns? |
| Technical | Q5 Integration Priority | Which integrations are MVP-critical vs deferrable? |
| UX | Q6 Feature Variants | Variants/modes present? Which gets more detail? (skip if none) |
| UX | Q7 Error-Handling Depth | Basic, Comprehensive, or Enterprise-grade? |
| Timeline | Q8 Implementation Phasing | Agree with Foundation / Core / Enhancement phasing? |
| Timeline | Q9 External Dependencies | Any blockers affecting sequencing? Missing dependencies? |

## Validation Gate (Phase 3)

**Critical checks (block if any fail → return to Phase 2):**

| Check | Criteria | Action if fail |
|-------|----------|----------------|
| Coverage | Every feature has ≥1 story | Add missing stories |
| Duplicate | No overlapping story scopes | Merge or differentiate |
| Template | All required template sections present | Add missing sections |
| DAG | Dependencies are acyclic | Fix circular dependencies |

**Quality checks (warning → block if more than 3 fail):**

| Check | Criteria |
|-------|----------|
| BDD format | Acceptance criteria in Given/When/Then |
| Quantified metrics | Success metrics are numeric |
| Edge cases | Error scenarios addressed |
| Open questions | Deferred decisions documented |

## Output (Phase 4)

| File | Where | Description |
|------|-------|-------------|
| Story files | the story folder + the story filename pattern | One file per story |
| Epic index | the story folder + the Epic-index filename pattern | Navigation hub: index table, dependency diagram, coverage matrix, phases, quick links |

Each story file carries YAML frontmatter (`type`, `id`, `title`, `epic`, `feature`,
`product`, `priority`, `status`) and the full story body from the organization's story
template. The Epic index emits the **pipeline hooks** the downstream task-generation skill
consumes: the story-ID list with file paths, identified technical dependencies, and
priority ordering. When that downstream skill writes task files, each task links back to its
story via the organization's story-linking field — this linkage is what keeps work
traceable; tasks without it are orphaned.

## Anti-Patterns

| Anti-Pattern | Better Way |
|--------------|------------|
| Auto-generate without questions | Always ask the 9 clarification questions; user input ensures alignment |
| Split feature variants arbitrarily | Combine variants by default; split only when substantially different |
| Prescribe HOW in stories | Stories define WHAT; implementation is for task breakdown |
| Skip coverage verification | Always build the Feature → Story matrix; verify 100% before completing |
| Generic questions | Bake Epic context into every question; show understanding of the features |
| Ignore error handling | Embed error scenarios; separate only when complexity warrants |
| Re-read full docs in Phase 1/2 | Use only the Phase 0 Epic Analysis Summary downstream |
| Hardcode folders / naming | Use the organization's decided paths and conventions (see ADAPT.md) |

## Sub-Skills

Focused sub-skills for targeted activation and team compositions:

| Sub-Skill | Focus | Agent stub |
|-----------|-------|------------|
| [STORY-DECOMPOSE](sub-skills/STORY-DECOMPOSE.md) | Feature→Story grouping, sizing, INVEST criteria, dependency mapping | `story-decompose` |
| [STORY-VALIDATE](sub-skills/STORY-VALIDATE.md) | Coverage matrix, dependency verification, persona mapping, gap analysis | `story-validate` |

Use the parent skill for full-scope work; use a sub-skill for focused team compositions.

## Cross-Skill Integration

| Role | Connection |
|------|------------|
| Product manager | MoSCoW prioritization, lifecycle alignment, value validation |
| Software architect | Technical feasibility, integration dependencies, architectural concerns |
| Question-framework skill | Acceptance criteria as testable hypotheses, measurable metrics |
| Test-generator / QA | Test cases from acceptance criteria, BDD Given/When/Then, Definition of Done |
| Task-generation skill (downstream) | Consumes the pipeline hooks; links each task to its story |

> All paths, naming, and product context are decided per organization (see
> [`ADAPT.md`](ADAPT.md)). This skill stays portable across organizations — only those
> decisions change.
