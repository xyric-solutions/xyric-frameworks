# Story Spec Generator — Reference Guide

Deep patterns, step-by-step instructions, and examples. Document locations and filename
shapes are organization-specific (see [`ADAPT.md`](ADAPT.md)); the spec methodology below
is platform-neutral.

---

## Phase 0: Research & Context Gathering (Detailed)

### Step 1: Identify Target Story

The user specifies which story to spec:
- Story ID: formatted per your story ID convention (e.g., epic.feature.sequence → S01.01.01)
- Story title: from the stories document

### Step 2: Extract from Stories Document

Find the target story and extract:
- Story title and description
- User story format (As a… I want… so that…)
- Acceptance criteria
- Dependencies
- Priority and size

### Step 3: Extract from Epic PRD

For the parent feature:
- Feature description
- Success metrics
- Error scenarios
- Integration points

### Step 4: Gather Technical Context

Read the design system and existing specs:
- UI component patterns
- API conventions
- Data-model patterns
- State-management approach

### Step 5: Create Story Technical Context

```markdown
## Story Technical Context: [Story ID]

### Story Summary
**ID:** S[XX.YY.ZZ]
**Title:** [Title]
**Epic/Feature:** E[XX]/F[X.Y]
**Priority:** P[X]
**Size:** [S/M/L/XL]

### User Story
As a [persona], I want to [action] so that [benefit].

### Acceptance Criteria (from Story)
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Technical Context
**Related Feature:** F[X.Y] - [Feature Name]
**Error Scenarios:** [From Epic PRD]
**Integration Points:** [From Epic PRD]

### Existing Patterns
**UI Components:** [From design system]
**API Style:** [REST/GraphQL/tRPC]
**Data Store:** [Database type]
**State Management:** [Redux/Zustand/Context/etc.]

### Technical Decisions Needed
- [Decision 1]: [Options]
- [Decision 2]: [Options]
- [Decision 3]: [Options]
```

---

## Phase 1: Questions & User Input (Detailed)

### Question Framework

The question framework is hypothesis-driven (align with your Business Insights / question
framework skill if you have one):
- **Hypothesis questions**: validate technical assumptions
- **Constraint discovery**: identify technical limitations
- **Integration validation**: verify integration assumptions

### Q1. API Design (Architecture)

```markdown
This story requires API endpoints for:
[List inferred operations based on story]

Questions:
a) API Style preference:
   - REST (resource-based)
   - GraphQL (flexible queries)
   - tRPC (TypeScript-native)
   - Other: [specify]

b) Authentication approach:
   - JWT tokens
   - Session-based
   - API keys
   - OAuth 2.0
   - Combination: [specify]

c) Endpoint structure for this story:
   - [Proposed endpoint 1]: [Purpose]
   - [Proposed endpoint 2]: [Purpose]
   Does this structure look right?

d) Rate limiting needs:
   - No rate limiting
   - Standard rate limiting
   - Aggressive rate limiting (sensitive operation)
```

### Q2. Data Model (Architecture)

```markdown
This story likely involves these entities:
[List inferred entities based on story]

Questions:
a) Does this story create new database entities?
   - Yes: [List new entities]
   - No: Uses existing entities only

b) Schema changes needed?
   - New tables: [List]
   - New columns on existing tables: [List]
   - No schema changes

c) Data relationships:
   - [Entity A] -> [Entity B]: [Relationship type]
   Does this match your mental model?

d) Data retention considerations:
   - Soft delete vs. hard delete
   - Audit logging requirements
   - GDPR/data privacy needs
```

### Q3. UI Components (UI/UX)

```markdown
Based on the story, these UI elements are needed:
[List inferred UI elements]

Questions:
a) Component breakdown:
   - [Component 1]: [Purpose]
   - [Component 2]: [Purpose]
   Does this component structure make sense?

b) State management:
   - Local component state only
   - Global state (Redux/Zustand/Context)
   - Server state (React Query/SWR)
   - Combination: [specify]

c) Existing components to reuse:
   - [List from design system if available]

d) New components needed:
   - [List any new components]
```

### Q4. User Flows & States (UI/UX)

```markdown
The story involves these user states:
[List inferred states: loading, error, success, empty, etc.]

Questions:
a) Loading states:
   - Skeleton loaders / Spinners / Progressive loading / Optimistic updates

b) Error display:
   - Inline errors / Toast notifications / Modal dialogs / Banner alerts

c) Empty states:
   - Helpful guidance / Call to action / Illustration/graphic

d) Success feedback:
   - Toast confirmation / Visual indicator / Redirect behavior
```

### Q5. Testing & Performance (Technical)

```markdown
Questions:
a) Testing priority for this story:
   - Unit tests: [High/Medium/Low]
   - Integration tests: [High/Medium/Low]
   - E2E tests: [High/Medium/Low]

b) Test data requirements:
   - Mock data sufficient / Seed data needed / Production-like data needed

c) Performance targets:
   - API response time: [Xms target]
   - UI render time: [Xms target]

d) Special technical considerations:
   - Offline support? Real-time updates? File upload/download? Third-party integrations?
```

---

## Phase 2: Tech Spec Generation (Detailed)

### Step 1: Apply User Decisions

| Decision | Impact on Spec |
|----------|----------------|
| API style | API contracts section |
| Auth approach | Security section |
| Data model | Data models section |
| Components | UI components section |
| Testing priority | Testing strategy section |

### Step 2: Generate Sections (Sequential)

Generate each section in order (dependency chain):
1. Story Reference
2. Technical Overview
3. API Contracts
4. Data Models
5. UI Components
6. Integration Points
7. Security Requirements
8. Testing Strategy
9. Performance Requirements
10. Open Technical Decisions

**Why sequential:** API → Data → UI dependency chain. Consistency is maintained.
Cross-references stay accurate.

### Design System Reference

Link to the design system for UI stories:
- Component patterns to reuse
- Design tokens (colors, spacing, typography)
- Interaction patterns
- Accessibility standards

---

## Phase 3: Validation (Detailed)

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| Story Coverage | Every acceptance criterion addressed | Map criteria to spec |
| Section Coverage | All required sections present | Add missing sections |
| Architecture Alignment | Patterns identified, ADRs flagged | Invoke the Software Architect skill |
| Design System Reference | UI components linked to design docs | Add references |
| Completeness | No TBD or placeholder content | Fill in gaps |
| Consistency | API/Data/UI aligned | Resolve conflicts |

### Quality Checks (Warning; Block if >3 fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| API Completeness | All endpoints have schemas | Add schemas |
| Data Clarity | All entities have fields | Define fields |
| ADR Documentation | Significant decisions flagged | Add ADR flag |
| Test Coverage | Test strategy defined | Add strategy |
| Security | Auth/authz documented | Add security |

---

## Integration Patterns

### Upstream: Story Generator
- Input: a user story with acceptance criteria, dependencies, and priority

### Skill Invocations During Spec Generation

| Phase | Skill | Purpose |
|-------|-------|---------|
| Questions | Business Insights / question framework | Hypothesis-driven question framework |
| Generation | Software Architect | Architecture patterns, ADR creation |

### Downstream: Task Generator
- Output: the tech spec, for test-driven task breakdown
- Handoff: a pipeline hook marking the story ready for tasks (e.g., `<!-- TASKS_READY: [Story ID] -->`)
- Tasks are generated from the tech spec's sections

### Invocation Flow

```
Story Spec Generator produces the tech spec
    |
    +-- Questions Phase
    |   +-- Apply the hypothesis-driven question framework
    |
    +-- Generation Phase
    |   +-- Identify architecture patterns
    |   +-- Invoke the Software Architect skill for ADR decisions
    |   +-- Reference the design system for UI
    |
    +-- Output Phase
        +-- Hand off to the Task Generator for task breakdown
```

---

## Workspace values to resolve

This skill operates on a few organization-specific values:

- **Products root** — root folder pattern for per-product docs
- **Planning/status file** — per-product planning/status filename to update
- **Naming conventions** — story ID, spec filename, and output-path conventions

Resolve every concrete location and filename from your organization's decisions at use time
(see [`ADAPT.md`](ADAPT.md)). If a value is undecided, treat it as unanswered (ask the
Workspace Intake in [`forms.md`](forms.md), or fall back to a clearly-labeled `PLACEHOLDER`
path and emit the spec in chat).

---

*Reference | Story Spec Generator | community template*
