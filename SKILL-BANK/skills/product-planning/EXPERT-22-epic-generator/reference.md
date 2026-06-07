# Epic Generator — Reference

Detailed step-by-step instructions, patterns, examples, and integration details.
Repository paths, filenames, templates, and lifecycle vocabulary are decided per
organization (see [`ADAPT.md`](ADAPT.md)); the workflow and scoring patterns below are
universal and org-independent.

---

## Concrete inputs the skill needs

The skill resolves these from your organization's adaptation decisions at use time:

- **Products root** — where product folders live (e.g. `<root>/<product>`).
- **Progress file** — per-product progress-tracking filename.
- **Template location** — where doc templates live (epic-PRD template included).
- **Naming conventions** — epic ID (E01), feature ID (F1.1), filename casing.
- **Product taxonomy** — list of `{ code, name, stage }` for the header/context.
- **Lifecycle stages** — stage labels; fallback: Core / MVP / Enhanced / Future.

Resolve every concrete path and filename from these decisions at use time. If something is
undecided, fall back to a labeled `PLACEHOLDER` path. Never invent the organization's
folder layout, document filenames, or template location.

---

## Phase 0: Research & Context Gathering

**Purpose:** Extract all features from the PRD and identify existing epic structure.

### Step 1: Locate the Master PRD

Look inside your products-root path/`<product>`/ for the PRD using your naming
convention. Common patterns to try:
- the canonical PRD filename from your naming conventions
- a `PRD`-named file
- any `*PRD*` file in the product folder

### Step 2: Extract Features from the PRD

Parse all features using your naming convention:
- Feature ID: `F[Epic].[Sequence]` (e.g. F1.1, F2.3)
- Feature name
- Priority (P0–P3)
- MVP / lifecycle status (from your lifecycle stage labels; default Core / MVP / Enhanced / Future)
- Personas served

### Step 3: Extract Existing Epic Structure

If the PRD has an Epic Overview Map section:
- Extract proposed epic names
- Extract proposed feature assignments
- Extract proposed dependencies

### Step 4: Create the PRD Feature Inventory

```markdown
## PRD Feature Inventory: [Product Name]

### Feature Count Summary
| Category | Count |
|----------|-------|
| Total Features | [X] |
| P0 (Critical) | [X] |
| P1 (High) | [X] |
| P2 (Medium) | [X] |
| P3 (Low) | [X] |
| MVP Features | [X] |
| Post-MVP Features | [X] |

### Features by Proposed Epic

**E01: [Name from PRD]**
- F1.1: [Feature name] - P[X] - [MVP Status]
- F1.2: [Feature name] - P[X] - [MVP Status]

**E02: [Name from PRD]**
- F2.1: [Feature name] - P[X] - [MVP Status]

[Continue for all proposed epics]

### Unassigned Features (if any)
- [Feature] - needs epic assignment

### Persona Coverage
| Persona | Features | Epics |
|---------|----------|-------|
| P1 | [Count] | E01, E02, ... |
| P2 | [Count] | E01, E03, ... |

### Dependency Hints
- [Dependency observation 1]
- [Dependency observation 2]
```

---

## Phase 1: Questions & User Input

**INPUT:** PRD Feature Inventory from Phase 0

Present the inventory summary, then ask 5 tailored questions.

### Question Framework (5 Questions)

**STRUCTURE (2 Questions)**

**Q1. Epic Grouping Validation**
- Present identified epic groupings with feature counts
- Ask: Does the structure make sense? Any epics to combine/split/rename? Features to move?

**Q2. Dependency Mapping**
- Present proposed dependency order with diagram
- Ask: Does the dependency order match the plan? Missing dependencies? Foundation epic? Parallel opportunities?

**SCOPE (2 Questions)**

**Q3. MVP Epic Scope**
- Present MVP Core / MVP Enhanced / Post-MVP classification (use your lifecycle stage labels)
- Ask: Is the MVP/Post-MVP split correct? MUST-HAVE epics for launch? NICE-TO-HAVE? Defer?

**Q4. Epic Sizing**
- Present current epic sizes with feature counts
- Ask: Any too large (should split)? Too small (should combine)? Target: 4-8 features per epic

**PRIORITY (1 Question)**

**Q5. Development Priority**
- Present suggested development order by sprint phases
- Ask: Does the order make sense? Earlier priorities needed? Can anything wait longer?

---

## Assumption Challenge Integration

Run an **assumption-challenge pass** between Phase 0 (Research) and Phase 1 (Questions).

| Challenge Phase | Applied | Trigger |
|-----------------|---------|---------|
| A: Question Why | Yes | User validates epic structure/groupings |
| B: Alternatives | Yes | Epic boundaries, dependency ordering |
| C: Stress Test | No | (Medium intensity — skip Phase C) |

**What to challenge:**
- Epic groupings: "Why group these features together?"
- Epic boundaries: "Should this feature be in Epic X or Epic Y?"
- Dependency order: "What if Epic Y was prioritized before Epic X?"
- Scope per epic: "Is this epic too large/small to be manageable?"

**Skip the challenge when:**
- User explicitly requests bypass ("skip challenge")
- Epic structure already validated in a prior session
- User provides detailed grouping rationale upfront

---

## Phase 2: Epic Generation

### Step 1: Apply User Decisions

| Decision | Impact on Epics |
|----------|-----------------|
| Grouping validation | Final epic names, feature assignments |
| Dependency mapping | Epic dependency diagram |
| MVP scope | Epic MVP/lifecycle status tags |
| Epic sizing | Split or combine decisions |
| Development priority | Epic ordering |

### Step 2: Generate Epics (Sequential)

For each epic, sequentially:
1. Define epic name and goal
2. List all assigned features
3. Map personas served
4. Define dependencies
5. Set MVP / lifecycle status
6. Calculate MoSCoW distribution
7. Define hypothesis
8. Calculate complexity score
9. Add to coverage matrix

### Step 3: Build Coverage Matrix

```markdown
| Feature | Feature Name | Epic | Status |
|---------|--------------|------|--------|
| F1.1 | [Name] | E01 | Assigned |
| F1.2 | [Name] | E01 | Assigned |
| F2.1 | [Name] | E02 | Assigned |
| **Total** | **[X] features** | | **100%** |
```

---

## Phase 3: Validation (Blocking)

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Coverage** | 100% of PRD features assigned | Assign missing features |
| **Uniqueness** | No feature in multiple epics | Remove duplicates |
| **No Circular Dependencies** | Dependency graph is acyclic | Resolve cycles |
| **Persona Coverage** | Every persona has features | Add features/adjust |

### Quality Checks (Warning -> Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Epic Sizing** | 4-12 features per epic | Consider split/merge |
| **Dependency Depth** | Max 3 levels deep | Restructure if needed |
| **MVP Balance** | At least 50% MVP | Review priorities |
| **Description Quality** | All epics have goals | Add descriptions |
| **MoSCoW Distribution** | ~60/20/20 (±15%) per epic | Rebalance priorities |
| **Hypothesis Defined** | Each epic has hypothesis | Add validation hypothesis |
| **Complexity Scored** | All epics have complexity score | Calculate scores |

---

## Phase 4: Output & Tracking

### Step 1: Write the Epic Overview File
Create the epic-overview file in your products-root path/`<product>`/ using the
epic-overview filename from your naming conventions.

### Step 2: Update the Progress File
Update your per-product progress file with:
- Session timestamp, product name
- Epic Overview created
- Epic count, feature count, coverage percentage

### Step 3: Output Pipeline Hooks
For each epic, include a hook for the downstream epic-PRD generator:
- Epic ID and name, feature list
- Format: `<!-- EPIC_PRD_READY: E[XX] -->`

---

## Integration Details

Map these roles onto the consuming team's own pipeline.

### Upstream: PRD Generator
- Input: Master PRD (often via a technical-architecture step)
- Inherits: Features, personas, epic structure hints
- Coverage: 100% of PRD features

### Upstream: Technical-Architecture Generator
- Input: Technical Architecture Document (immediate upstream)
- Inherits: System design, component mapping, ADRs
- Epic–component alignment: each epic maps to architecture components

### Downstream: Epic-PRD Generator
- Output: epic outlines for detailed breakdown
- Handoff: `<!-- EPIC_PRD_READY: E[XX] -->`

### Downstream: Story Generator
- Epic PRDs feed into story generation
- Stories are generated per Epic PRD

---

## Hypothesis Examples by Epic Type

| Epic Type | Hypothesis Example |
|-----------|-------------------|
| Foundation | "Users can successfully onboard in <5 min with minimal friction" |
| Core Feature | "Feature X solves problem Y better than existing alternatives" |
| Integration | "Users will combine features A+B to achieve outcome C" |
| Enhancement | "Advanced users will adopt capability X" |

---

## Template & Context Loading

### Template Reference
Read the epic-PRD template from your configured template location.

### Product Context
Load from the product's context folder under your products-root path/`<product>`/.

| File | Usage | Required |
|------|-------|----------|
| product identity | Verify alignment with product identity | Recommended |
| personas | Map features to personas accurately | Recommended |
| pillars | Understand epic domain context | Recommended |
| design decisions | Respect existing architecture decisions | Optional |
| constraints | Factor in known constraints | Optional |

### Missing Context Handling
If context files are missing:
1. Notify the user: "Context file `<filename>` not found for `<product>`"
2. Proceed using PRD content as the primary reference
3. Recommend creating context files for consistent downstream generation

---

> All paths, filenames, templates, and lifecycle vocabulary come from your organization's
> adaptation decisions (see [`ADAPT.md`](ADAPT.md)). This file stays portable across
> organizations — only those values change.
