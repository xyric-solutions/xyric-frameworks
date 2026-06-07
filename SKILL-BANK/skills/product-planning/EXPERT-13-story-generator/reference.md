# Story Generator (EXPERT-13) — Reference

Detailed step-by-step instructions, patterns, and examples. Load on demand during a
breakdown. Where stories and tasks live, the filename conventions, and the story-linking
field are decided per organization (see [`ADAPT.md`](ADAPT.md)); the methodology below
(INVEST, MoSCoW, BDD) is universal and brand-independent.

---

## The workspace decisions this skill consumes

These are the organization-specific values the skill resolves at use time (decided per
[`ADAPT.md`](ADAPT.md), gathered via the Workspace & Conventions Intake in `forms.md`):

| Decision | Meaning |
|----------|---------|
| Product folder root | How each product's folder is located, e.g. a `{root}/{product}` path |
| Planning/context file | Per-product planning/context file to update after generation |
| Template locations | Where the story + Epic-index templates live |
| Story folder | Sub-folder that holds stories, e.g. `stories/` |
| Story filename pattern | e.g. `S<Epic>-<Seq>-<slug>.md` |
| Epic-index filename pattern | e.g. `Epic-<NN>-Stories-Index.md` |
| Task folder | Sub-folder that holds implementation tasks |
| Task filename pattern | e.g. `<prefix>-<NNN>-<slug>.md` |
| Story-linking field | YAML field a task uses to reference its parent story/stories |
| Product taxonomy | List of products and lifecycle stage — resolve the product from an Epic ref |

Resolve every concrete path and convention from these decisions at use time. If a value is
not yet decided, treat it as unanswered (ask via the intake in `forms.md`, or fall back to a
labeled placeholder).

---

## Phase 0: Research & Context Gathering

**Purpose:** build unified context that informs ALL subsequent phases.

### Step 1: Identify Product & Epic

The user provides an Epic number, path, or product name. Resolve the product folder from
the organization's product taxonomy + product folder root, then locate the Epic PRD.

```
"Generate stories for Epic 03" -> identify the product folder and Epic-03 PRD
```

### Step 2: Read Epic PRD (Primary Input)

Extract:
- All Features (F[X.Y]) with descriptions
- Success metrics and acceptance criteria
- Dependencies and MVP status
- Error-handling requirements

### Step 3: Gather Supporting Context (If Available)

| Source | What to Extract | Why It Matters |
|--------|-----------------|----------------|
| Existing stories | Template patterns, story structure | Ensures consistency |
| Planning/context file | Global decisions, prior learnings | Avoids repeating mistakes |
| Vision/PRD docs | Product success metrics | Stories align to product goals |

**Note:** Do not block on missing files. Use what is available.

### Step 4: Create Unified Epic Analysis

```markdown
## Epic Analysis: E[XX] - [Name]

### From Epic PRD
**Features:** [N] total
- F[X.1]: [Name] - [Scope + complexity]
- F[X.2]: [Name] - [Scope + complexity]

**Success Metrics:** [From PRD - what must be measurable]
**Personas:** [Who benefits from this Epic]
**Dependencies:** [Cross-Epic and external]

### From Product Context (If Found)
**Global Decisions:** [From the planning/context file]
**Template Patterns:** [From existing stories]
**Product Goals:** [From Vision]

### Story Generation Guidance
**Recommended Story Count:** [Based on feature complexity]
**Key Constraints:** [Must be addressed in stories]
**Open Questions:** [Need user input in Phase 1]
```

**CRITICAL:** This unified analysis is the ONLY context used in Phase 1 and Phase 2. No
re-reading of full documents downstream.

---

## Assumption Challenge (Light) — between Phase 0 and Phase 1

Run a **light** challenge (question-why only; skip the alternatives and stress-test
phases):

| Challenge phase | Applied |
|-----------------|---------|
| A: Question Why | Yes |
| B: Alternatives | No (light intensity) |
| C: Stress Test | No (light intensity) |

**What to challenge:**
- Priority assignments: "Why is this feature P0 vs P1?"
- Story granularity: "Why split/combine these stories this way?"
- Scope boundaries: "Should this story include X, or is that separate?"

**Skip when:** the user requests a bypass ("skip challenge"); revising (not newly breaking
down) stories; priorities already validated at the Epic-PRD level.

---

## Phase 1: Questions & User Input

**INPUT:** the Epic Analysis from Phase 0 (not the raw PRD). Present the unified summary,
then ask the 9 tailored questions.

### Question Framework (9 Questions)

**STRATEGIC**
- **Q1 Priority Validation** — present features with current priorities; ask about MoSCoW
  adjustments and any explicit "Won't Have" for MVP.
- **Q2 Scope Boundaries** — list MVP-Core features; ask which to explicitly EXCLUDE from
  MVP scope (mark post-MVP, not delete).
- **Q3 Story Granularity** — present features with complexity; ask Granular (1–3 day),
  Larger (5–7 day), or Mixed.

**TECHNICAL**
- **Q4 Tech-Stack Constraints** — list technical dependencies; ask about selected APIs,
  framework preferences, architectural patterns.
- **Q5 Integration Priority** — list integrations; ask which are MVP-critical vs
  deferrable.

**UX**
- **Q6 Feature Variants** (skip if none) — ask about variants/modes and which gets more
  detail.
- **Q7 Error-Handling Depth** — list defined error scenarios; ask Basic, Comprehensive, or
  Enterprise-grade.

**TIMELINE**
- **Q8 Implementation Phasing** — suggest Foundation / Core Experience / Enhancement; ask
  for agreement or adjustment.
- **Q9 External Dependencies** — list external dependencies with status; ask about blockers
  and any missing dependencies.

---

## Phase 2: Story Generation

### Step 1: Apply User Decisions

| Decision | Impact on Stories |
|----------|-------------------|
| Priority changes | Adjust MoSCoW per story |
| Scope exclusions | Mark as Won't Have |
| Granularity | Determine split strategy |
| Tech constraints | Add to story constraints |
| Integration priority | Sequence dependencies |
| Mode/variant balance | Detail level per variant |
| Error handling | Embed vs separate stories |
| Phasing | Group into sprints/phases |
| External deps | Add to dependencies |

### Step 2: Generate Stories (Sequential)

For each feature, sequentially:
1. Load the feature spec from the Epic Analysis Summary
2. Generate story/stories using the organization's story template
3. Check for overlap with previous stories
4. Update the running dependency graph
5. Add to the Feature → Story coverage matrix

**Why sequential:** context is preserved across features, dependencies build
incrementally, there is no risk of overlapping stories, and coverage is verified in
real time.

---

## Phase 3: Validation (Blocking)

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Coverage** | Every feature has >=1 story | Return to Phase 2, add missing stories |
| **Duplicate** | No overlapping story scopes | Merge or differentiate stories |
| **Template** | All required template sections present | Add missing sections |
| **DAG** | Dependencies are acyclic | Fix circular dependencies |

### Quality Checks (Warning -> Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **BDD Format** | Acceptance criteria in Given/When/Then | Reformat criteria |
| **Quantified Metrics** | Success metrics are numeric | Add specific targets |
| **Edge Cases** | Error scenarios addressed | Document edge cases |
| **Open Questions** | Deferred decisions documented | List open questions |

---

## Phase 4: Output & Tracking

### Step 1: Write Individual Story Files

For each story, write into the story folder using the story filename pattern. Slugs are
lowercase, hyphenated, ≤ 40 chars.

Each file contains the YAML frontmatter (`type: story`, `id`, `title`, `epic`, `feature`,
`product`, `priority`, `status`) and the full story body from the configured template.

### Step 2: Write the Epic Index File

Write into the same story folder using the Epic-index filename pattern.
The index contains: the Story Index table with links, the Dependency Diagram, the Feature →
Story Coverage Matrix, the Implementation Phases, and Quick Links to related docs.

### Step 3: Update the Planning/Context File

Append a session entry to the planning/context file: timestamp, Epic completed, stories
generated (count), files created (list), decisions made (capture for future epics), and
open questions for the next session.

### Step 4: Emit Pipeline Hooks

Include in the Epic index for downstream consumption by the task-generation skill:
- The story-ID list with file paths
- Technical dependencies identified
- Priority ordering for implementation

When the downstream skill creates task files, each task references its parent story via the
organization's story-linking field. This linkage is what keeps the
Vision → PRD → Epic → Story → Task chain traceable; a task without it is orphaned work.

---

## Integration Details

| Skill | Use for |
|-------|---------|
| Product manager (EXPERT-10) | MoSCoW prioritization, lifecycle alignment |
| Software architect (EXPERT-03) | Technical feasibility, architectural concerns |
| Question framework (BI-02) | Acceptance criteria as hypotheses, measurable metrics |
| Test generator (DEV-02) | Test cases from acceptance criteria, edge cases |
| QA engineer (EXPERT-04) | BDD structure, Given/When/Then patterns |

---

## Example: Tailored Questions (generic illustration)

The examples below show the **shape** of tailored questions for a hypothetical messaging-
integration Epic. Replace every feature, integration, and constraint with the actual Epic's
content at run time.

### Q1. Priority Validation (tailored shape)

```markdown
Epic 03 ([Epic name]) has 7 features, all marked MVP Core:

| Feature | Name | Current Priority |
|---------|------|------------------|
| F3.1 | [Account Linking]        | MVP Core |
| F3.2 | [Text-based interaction] | MVP Core |
| F3.3 | [Media analysis]         | MVP Core |
| F3.4 | [Voice processing]       | MVP Core |
| F3.5 | [Proactive notifications]| MVP Core |
| F3.6 | [Quick logging]          | MVP Core |
| F3.7 | [Cross-channel sync]     | MVP Core |

Do you want to adjust any priorities?
- Should [Media analysis] (F3.3) be P0 Must Have or P1 Should Have?
- Is [Voice processing] (F3.4) MVP critical, or could it be post-MVP?
- Could [Proactive notifications] (F3.5) be deferred to a later release?
```

### Q4. Tech-Stack Constraints (tailored shape)

```markdown
Epic 03 has these technical dependencies:
- **[Messaging Business API]**: send / receive / templated messages
- **[SMS / verification provider]**: phone verification codes
- **[AI/ML service]**: media analysis, voice processing, sentiment detection
- **[Object storage]**: media file handling

Are there any technical constraints?
- API tier (standard vs enterprise)?
- Preferred provider for media/voice analysis?
- Storage requirements for media files?
```

---

## INVEST & sizing reminders (universal)

- **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable — every story
  should satisfy all six.
- **MoSCoW**: Must / Should / Could / Won't — maps to P0 / P1 / P2 / P3.
- **BDD acceptance criteria**: `Given <context>, When <action>, Then <outcome>` — cover
  happy path, edge cases, and error states.
- **Sizing**: S (1–2 day), M (3–5 day), L (5–8 day). Flag L stories for possible splitting;
  most stories should be S or M.
