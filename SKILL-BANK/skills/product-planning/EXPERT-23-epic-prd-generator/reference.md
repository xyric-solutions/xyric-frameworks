# Epic PRD Generator — Reference

Detailed step-by-step instructions, patterns, examples, and integration details. All
input/output paths resolve from your organization's decided workspace conventions (see
[`ADAPT.md`](ADAPT.md)); the path patterns shown here are placeholders, not literals. The
BDD and feature-spec methodology below is universal.

---

## Workspace conventions to resolve

These are the values you decide once for your organization (see `ADAPT.md`):

- **products root** — parent path for product folders
- **progress file** — session-continuity file per product
- **template locations** — where doc templates live (epic outline, master PRD, etc.)
- **naming conventions** — ID/casing/separator rules (epic `E[XX]`, feature `F[X.Y]`, etc.)
- epic-PRD-specific sub-paths: epic overview file, master PRD file, epic PRD directory,
  epic PRD filename pattern, stories index

Resolve every concrete path at use time. If a value is not yet decided, treat it as
unanswered (ask via the Workspace Intake in [`forms.md`](forms.md), or fall back to a
labeled placeholder).

---

## Phase 0: Research & Context Gathering

**Purpose:** Extract the epic outline and gather context for full specification.

### Step 1: Identify Target Epic

User specifies which epic to detail:
- Epic ID: E[XX] (e.g., E01, E05)
- Epic Name: [From the Epic Overview]

### Step 2: Extract from Epic Overview

Read the Epic Overview (`<products-root>/<product>/<epic-overview-file>`), find the target
epic, and extract:
- Epic statement and goal
- Feature list (F[X.Y] IDs)
- Personas served
- Dependencies
- MVP status
- Success criteria

### Step 3: Extract from Master PRD

Read the Master PRD (`<products-root>/<product>/<prd-file>`). For each feature in the epic:
- Feature name and priority
- Initial description (if any)
- Persona mapping
- MVP status

### Step 4: Gather Template Patterns

Read existing Epic PRDs (`<products-root>/<product>/<epic-prd-dir>/*`) to extract:
- Feature specification format
- Acceptance criteria patterns
- Error scenario templates
- Success metric patterns

### Step 5: Create Epic Context Summary

```markdown
## Epic Context: E[XX] - [Epic Name]

### Epic Overview
**Statement:** [From Epic Overview]
**Goal:** [From Epic Overview]
**MVP Status:** [Core/MVP/Enhanced/Future]

### Features to Specify
| Feature | Name | Priority | MVP |
|---------|------|----------|-----|
| F[X.1] | [Name] | P[X] | [Status] |
| F[X.2] | [Name] | P[X] | [Status] |

### Personas Served
- **Primary:** P[X] - [Name]
- **Secondary:** P[Y], P[Z]

### Dependencies
- **Upstream:** [Epic dependencies]
- **Feature-level:** [Any feature dependencies]

### Success Criteria (from Epic Overview)
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Gaps Requiring Clarification
- [Gap 1]: Feature scope unclear
- [Gap 2]: Acceptance criteria needed
```

---

## Phase 1: Questions & User Input

**INPUT:** Epic Context Summary from Phase 0

Present the Epic Context Summary, then ask 4 tailored questions.

### Question Framework (4 Questions)

**FEATURE SCOPE (2 Questions)**

**Q1. Feature Detail Level**
- Present all features with current detail level (Brief/None)
- Ask: Any features needing special attention? Simpler features? Complex edge cases?
- Estimate acceptance criteria per feature: Standard (3-5), Complex (6-10), Simple (2-3)

**Q2. Feature Scope Clarification**
- For each feature needing clarification: What should it INCLUDE? EXCLUDE? Specific behaviors?

**USER EXPERIENCE (1 Question)**

**Q3. Error Handling & Edge Cases**
- Ask about error message style (technical vs friendly), key error scenarios to document,
  recovery expectations (auto-retry, save state, clear recovery path)

**ACCEPTANCE CRITERIA (1 Question)**

**Q4. Success Criteria & Metrics**
- Ask which metrics matter most (engagement, performance, quality, business KPIs)
- Ask about SLAs or performance requirements (response times, availability, throughput)

---

## Assumption Challenge Integration

Apply an assumption-challenge pass between Phase 0 (Research) and Phase 1 (Questions),
surfacing the underlying assumption and a credible alternative before committing.

| Challenge Phase | Applied | Trigger |
|-----------------|---------|---------|
| A: Question Why | Yes | User specifies feature scope / acceptance criteria |
| B: Alternatives | Yes | Feature boundaries, acceptance criteria depth |
| C: Stress Test | No | (Medium intensity — skip Phase C) |

**What to Challenge:**
- Feature scope: "Is this feature doing too much or too little?"
- Acceptance criteria: "Are these criteria testable and complete?"
- Error handling: "What edge cases are missing?"
- Dependencies: "Are the feature dependencies correctly identified?"

**Skip Challenge When:**
- User explicitly requests bypass ("skip challenge")
- Feature specifications already validated
- User provides detailed acceptance criteria upfront

---

## Phase 2: Epic PRD Generation

### Step 1: Apply User Decisions

| Decision | Impact on Features |
|----------|--------------------|
| Detail level | Depth of specification |
| Scope clarifications | Feature boundaries |
| Error handling | Error scenario tables |
| Success criteria | Metric targets |

### Step 2: Generate Features (Sequential)

For each feature, sequentially:
1. Write the feature description (2-3 paragraphs)
2. Create the user story (As a… I want… so that…)
3. Define success metrics (table with targets)
4. Write BDD acceptance criteria (Given/When/Then)
5. Document error scenarios (table with messages, actions, recovery)
6. Flag ADR decisions if applicable
7. Note dependencies

### Feature Specification Structure

```markdown
### F[X.Y]: [Feature Name]

**Priority:** P[X]
**MVP Status:** Core / MVP / Enhanced / Future
**Personas:** P[X] (Primary), P[Y], P[Z] (Secondary)

**Description:**
[2-3 paragraphs describing the feature in detail]

**User Story:**
As a [persona name], I want to [action/capability] so that [benefit/value].

**Success Metrics:**
| Metric | Target | Measurement |
|--------|--------|-------------|
| [Metric 1] | [Target] | [How measured] |

**Acceptance Criteria (BDD Format):**

*Core Functionality:*
- **Given** [context], **When** [action], **Then** [outcome]

*User Experience:*
- **Given** [context], **When** [action], **Then** [outcome]

*Edge Cases:*
- **Given** [edge case context], **When** [action], **Then** [graceful handling]

*Performance:*
- **Given** [load condition], **When** [action], **Then** [response within target]

**Error Scenarios:**
| Scenario | User Message | System Action | Recovery |
|----------|--------------|---------------|----------|
| Network timeout | "Connection lost…" | Retry 3x | Retry button |
| Invalid input | "[Field] is invalid…" | Highlight field | Clear guidance |

**Dependencies:**
- **Prerequisite Features:** None / F[X.Y]
- **Cross-Epic:** E[YY] - [Reason]
```

---

## Phase 3: Validation (Blocking)

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Feature Coverage** | All epic features specified | Add missing features |
| **BDD Format** | All criteria use Given/When/Then | Convert to BDD format |
| **ADR Flagging** | Significant decisions flagged | Add ADR flags |
| **Acceptance Criteria** | Every feature has 3+ criteria | Add criteria |
| **Error Scenarios** | Every feature has error table | Add scenarios |
| **Success Metrics** | Every feature has metrics | Add metrics |

### Quality Checks (Warning → Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **User Story** | Proper format (As a… I want… so that…) | Reformat |
| **BDD Completeness** | Given/When/Then all present | Complete BDD |
| **Metric Quantification** | Targets are numbers | Add targets |
| **Dependency Clarity** | Dependencies specified | Document |

---

## Phase 4: Output & Tracking

### Step 1: Write the Epic PRD File
Create the file in the epic-PRD directory using your filename convention:
`<products-root>/<product>/<epic-prd-dir>/<epic-prd-filename>`

The filename convention comes from your decided naming conventions (an `Epic-XX-Name` style
pattern is typical — prefix, epic number, and a hyphenated name, e.g. an "Epic 01:
Onboarding" file). Resolve the exact pattern from your conventions.

### Step 2: Update the Progress File
Append to `<products-root>/<product>/<progress-file>`:
- Session timestamp
- Epic: E[XX] - [Name]
- Features specified: [count]
- Ready for story generation

### Step 3: Emit the Story-Generation Hook
Include a handoff hook for the story generator:
- Epic ID and feature list
- Format: `<!-- STORY_READY: E[XX] -->`

---

## Integration Details

### Upstream Roles

| Role | Integration |
|------|-------------|
| **Epic generator** | Input: epic outline with statement, goal, feature list, personas |
| **Master PRD author** | Reference: feature details, personas, success metrics |

### Role Invocations (During PRD Generation)

| Phase | Role | Purpose |
|-------|------|---------|
| **Questions** | Business-insights analyst | Feature analysis question framework |
| **Generation** | Software architect | Epic-level and feature-level ADR decisions |

### Downstream Roles

| Role | Integration |
|------|-------------|
| **Story generator** | Output: full Epic PRD with BDD criteria for story breakdown |
| | Handoff: `<!-- STORY_READY: E[XX] -->` |
| | Stories inherit the BDD acceptance-criteria format |

### Invocation Pattern

```
Epic PRD Generator produces the Epic PRD
    |
    +-- Questions Phase -> apply the business-insights feature-analysis framework
    |
    +-- Generation Phase
    |   +-- Flag epic-level ADR decisions
    |   +-- Hand significant decisions to the software architect
    |   +-- Generate BDD acceptance criteria
    |   +-- Flag feature-level ADRs
    |
    +-- Output Phase -> handoff to the story generator for story generation
```

> All paths and output locations are decided per organization (see [`ADAPT.md`](ADAPT.md)).
> This file stays portable across organizations — only those decisions change.
