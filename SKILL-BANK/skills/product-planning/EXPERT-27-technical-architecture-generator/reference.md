# Technical Architecture Generator — Reference

Detailed step-by-step instructions, question framework, generation patterns, and integration
protocols. The default stack and all read/write paths are organization-specific decisions (see
[`ADAPT.md`](ADAPT.md)): `{products_root}` is your parent folder for product docs, `{progress_file}`
your per-product progress filename, the template location is your reusable-template folder, and
`{product}` is the current product slug.

---

## Phase 0: Research and Context Gathering

**Purpose**: Extract all relevant information from the PRD and establish technical context before
asking the user any questions.

### Step 1: Locate PRD Document

Search for the PRD in order, under `{products_root}/{product}/`:
1. `Product-Requirements-Document.md`
2. `PRD.md`

If no PRD is found, invoke the Escape Hatch (see SKILL.md, Cross-Expert Integration). Do not
proceed with architecture generation without a PRD.

### Step 2: Extract from PRD Document

| Section | What to Extract |
|---------|-----------------|
| Executive Summary | Product description, scope, constraints |
| Epic Overview | Epic structure, dependencies, features per epic |
| Success Metrics | Performance targets, scale requirements |
| Personas | User types, access patterns, concurrent user estimates |
| Accessibility | Compliance requirements (WCAG level) |
| AI/ML Safety | AI capabilities, boundaries, model requirements (if applicable) |
| Data Management | Data types, privacy requirements, retention |
| Special Requirements | Security, compliance, integrations |

### Step 3: Extract from Vision Document

| Section | What to Extract |
|---------|-----------------|
| Product Architecture | High-level components, key capabilities |
| Product Principles | Guiding principles that constrain architecture |
| Quality Metrics | Performance targets, reliability goals |

### Step 4: Research Existing Patterns

Research reference architectures for:
- Similar product types (health apps, AI platforms, marketplaces, etc.)
- Technology patterns relevant to requirements (real-time, event-driven, batch processing)
- Scale characteristics matching the target (user volume, data volume, request frequency)
- Other products in the same portfolio that solved similar problems — reuse beats reinvention

### Step 5: Assess PRD Completeness

Before proceeding, check that the PRD provides:
- [ ] Named epics with feature descriptions
- [ ] Success metrics with quantifiable targets
- [ ] User personas with access patterns
- [ ] Integration requirements
- [ ] Compliance and security constraints

For any missing item, flag it as a gap. If more than two critical items are missing, recommend
returning to the PRD Generator before continuing.

### Step 6: Create PRD Analysis Summary

Generate a structured analysis (~500 words). Use your organization's lifecycle stage names
(defaults: Vision / Feasibility / Design & Planning / Development / Launch & Growth):

```markdown
## PRD Analysis: [Product Name]

### Product Context
**Product:** [Name and brief description]
**Type:** [Web App / Mobile App / Platform / API / etc.]
**Target Scale:** [Users, requests, data volume]
**Target Platforms:** [Web, iOS, Android, Desktop]
**Lifecycle Stage:** [from your organization's lifecycle stages]

### Epic Structure Extracted
| Epic | Name | Key Features | Technical Implications |
|------|------|--------------|------------------------|
| E01 | [Name] | [Features] | [Implications] |
| E02 | [Name] | [Features] | [Implications] |

### Component-Epic Alignment (Initial Assessment)
[Preliminary mapping of which epics might share components, where boundaries seem natural, and
where coupling risks exist]

### Technical Requirements
**From PRD:**
- Performance: [Targets from success metrics]
- Security: [Requirements from special requirements]
- Compliance: [GDPR, HIPAA, etc.]
- Accessibility: [WCAG level]

**From Vision:**
- Capabilities: [List from Product Architecture]
- Integrations: [Required integrations]
- Principles: [Relevant product principles]

### Constraints Identified
- Budget: [If mentioned]
- Timeline: [MVP timeline]
- Team: [Size, expertise if known]
- Technology: [Any mandated technologies]

### Default Stack Assessment
[Note where the organization's default stack covers requirements and where deviations may be
needed]

### Decision Points Requiring Input
- [Decision 1]: [Options identified]
- [Decision 2]: [Options identified]

### PRD Gaps Identified
- [Gap 1]: [What is missing and why it matters for architecture]
```

---

## Phase 1: Questions and User Input

**Input**: PRD Analysis from Phase 0.
**Output**: User decisions that drive architecture generation.

Present the PRD Analysis summary to the user, then ask 6 tailored questions organized in three
pairs.

### Question Framework (6 Questions)

**Architecture Foundation (2 Questions)**

**Q1. Architecture Pattern**
- Present the analysis of epic structure and technical characteristics
- Recommend Modular Monolith (default) with evidence for why it fits
- If evidence exists for microservices, present the case
- Ask: team size, independent deployment needs, different runtimes needed, scale projections that
  differ by module

**Q2. Technology Stack**
- Present the organization's default stack as the starting point. If there is no default, say so
  and propose a fit-for-purpose stack to be recorded in an ADR.
- Highlight any requirements that the default stack may not cover
- Ask: technology constraints or mandates, team expertise beyond the default stack, existing
  infrastructure to integrate with, build vs buy preference for specific components

**Integration and Data (2 Questions)**

**Q3. Integration Architecture**
- List all integration points extracted from the PRD
- Categorize: internal (between components), external (third-party APIs), data (import/export)
- Ask: priority per integration (MVP vs later), API style preferences (REST/GraphQL/tRPC),
  real-time requirements, fallback strategies for external dependencies

**Q4. Data Architecture**
- List data requirements from PRD (user data, feature data, training/analytics data)
- Present the default database (from the organization's default stack) with any cases where
  alternatives may apply
- Ask: data residency requirements, retention policies, analytics/reporting needs, data export
  requirements, multi-tenancy approach

**Operations and Security (2 Questions)**

**Q5. Security and Compliance**
- List security requirements from the PRD
- Present an authentication approach based on product type (session/cookie auth for web apps,
  token-based auth for APIs)
- Ask: authentication strategy preferences, authorization model (RBAC, ABAC), security
  certifications needed, API security requirements

**Q6. Infrastructure and Operations**
- List scale and performance requirements from the PRD
- Present the default deployment target (from the organization's default stack)
- Ask: cloud provider constraints, deployment model (single region, multi-region), CI/CD
  requirements, monitoring and observability preferences

### Handling User Responses

- If the user accepts defaults on all questions, proceed with the default stack and recommended
  patterns. Document this in ADRs as "Default stack selected, no deviations required."
- If the user provides partial answers, use defaults for unanswered items and note them as
  assumptions.
- If the user raises concerns not covered by the 6 questions, address them in supplementary ADRs.

---

## Phase 2: Architecture Generation

### Step 1: Apply User Decisions

Map each user decision to the architecture sections it affects:

| Decision Area | Impacts These Sections |
|---------------|------------------------|
| Architecture pattern | System Overview, Component Architecture |
| Technology stack | Technology Stack, ADRs |
| Integration style | API Design, Integration Points |
| Data architecture | Data Architecture, Component Architecture |
| Security approach | Security Architecture, ADRs |
| Infrastructure | Infrastructure, Deployment |

### Step 2: Invoke the Software Architect for ADR Creation

For each significant decision, create an ADR using the Software Architect's ADR format:
- Architecture pattern (Modular Monolith vs alternatives)
- Primary database selection (if deviating from the default stack)
- Frontend framework (if deviating from the default stack)
- Backend framework (if deviating from the default stack)
- Authentication approach
- Any domain-specific technology decisions

**Conflict resolution with the Software Architect**: If the architect recommends an approach that
conflicts with the user's stated preference or the Epic-Component Mapping:
1. Document both perspectives in the ADR's "Considered Options"
2. Evaluate each option against the team parallelism criterion
3. Present the tradeoff to the user: "The architect recommends X because [reason]. The alternative
   Y better supports parallel epic execution because [reason]. Which approach do you prefer?"
4. Record the decision and the rejected alternative

### Step 3: Generate 12 Sections (Sequential)

For each section, in order:
1. Reference the PRD Analysis and user answers
2. Generate section content using the architecture template (your organization's template, if one
   exists)
3. Cross-reference with PRD epics to verify alignment
4. Verify component-epic alignment — flag any component that serves more than 2 epics

**Section Generation Order**:

1. **Executive Summary** — System overview, key architecture decisions, default stack usage
2. **System Architecture Overview** — High-level components, layers, data flow diagram
3. **Technology Stack Selection** — Default stack confirmation or deviation justification
4. **Component Architecture** — Module structure, boundaries, dependency graph
5. **API Design Patterns** — Style, contracts, versioning, error handling
6. **Data Architecture** — Models, storage strategy, caching, migration approach
7. **Security Architecture** — Authentication, authorization, threat model, compliance
8. **Infrastructure Requirements** — Cloud resources, deployment, scaling triggers
9. **Integration Points** — External APIs, third-party services, event flows
10. **Architecture Decision Records** — ADR index with summaries, links to individual ADR files
11. **Epic-Component Mapping** — The primary deliverable: matrix showing epic-to-component alignment
12. **Technical Constraints and Trade-offs** — Limitations, deferred decisions, evolution triggers

### Step 4: Build the Epic-Component Mapping Matrix

This is the most important output. For each PRD epic:

```markdown
| PRD Epic | Components | APIs | Data Models | ADRs | Dependencies |
|----------|------------|------|-------------|------|--------------|
| E01 | [Components] | [APIs] | [Models] | [ADRs] | None |
| E02 | [Components] | [APIs] | [Models] | [ADRs] | E01 (API X) |
| **Coverage** | 100% | | | | |
```

Validation rules for the matrix:
- Every PRD epic must appear as a row
- Every component must appear in at least one epic's row
- Shared components (appearing in 3+ epics) must be flagged with a note explaining the coupling
- Dependencies between epics must be explicit

---

## Phase 3: Validation (Blocking)

Run all quality gates from SKILL.md. The validation is binary: pass or fail.

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Epic Coverage** | Every PRD epic has component mapping | Add missing mappings |
| **ADR Coverage** | Every significant decision has an ADR | Create missing ADRs |
| **Stack Justification** | Default stack or deviation justified | Add ADR or revert |
| **Integration Clarity** | All component interfaces defined | Define missing interfaces |
| **Pipeline Readiness** | Handoff block present | Add the block |
| **Completeness** | No TBD or placeholder content | Fill gaps |

### Quality Checks (Warning if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Technology Rationale** | Each tech choice justified | Add rationale |
| **API Contracts** | Key APIs defined | Add API definitions |
| **Data Models** | Core entities documented | Add data models |
| **Security Coverage** | Auth/authz defined | Add security details |
| **PRD Alignment** | No conflicts with PRD constraints | Resolve or document tradeoff |

If any critical check fails, return to Phase 2 and address the gap before proceeding to output.

---

## Phase 4: Output and Tracking

### Step 1: Write Architecture File

Create `{products_root}/{product}/Technical-Architecture.md` using your organization's architecture
template (a `technical-architecture-template.md` if the org provides one; otherwise follow the
12-section order above).

### Step 2: Write ADRs

Create the folder `{products_root}/{product}/adrs/` if it does not exist.
Create individual files: `ADR-001-[decision-name].md`, `ADR-002-[decision-name].md`, etc.
(follow your organization's naming conventions if they specify an ADR filename pattern).

### Step 3: Update the Progress File

Add a milestone entry to `{products_root}/{product}/{progress_file}` with:
- Session timestamp and product name
- Technical Architecture created (file path)
- ADRs created (list with file paths)
- Key decisions made (summary)
- Open questions for the Epic phase
- Default stack deviations (if any)

### Step 4: Include Pipeline Readiness Block

End the architecture document with:

```markdown
## Pipeline Readiness

**Epic Coverage**: [X/X] PRD epics mapped to components (100%)
**Open ADRs**: [List any ADRs with status "Proposed" that need resolution before epic generation]
**Deferred Decisions**: [List any decisions marked as deferred with <!-- DEFERRED --> markers]
**Shared Components**: [List components that appear in 3+ epics, requiring coordination]

Architecture complete. Ready for the Epic Generator.
```

### Step 5: Output Pipeline Hooks

Include these markers for downstream consumption:
- Component list for the Epic Generator
- Epic-component mapping matrix
- Technical constraints per epic
- Handoff marker: `<!-- EPIC_READY_WITH_ARCHITECTURE: {PRODUCT-CODE} -->`

---

## Integration Protocols

### Upstream Handoff from the PRD Generator

- **Input**: `Product-Requirements-Document.md`
- **Inherits**: Epics, features, constraints, integrations, success metrics
- **Handoff marker received**: `<!-- ARCHITECTURE_READY: {PRODUCT-CODE} -->`
- **Validation**: Confirm PRD has named epics and quantifiable success metrics before proceeding

### Downstream Handoff to the Epic Generator

- **Output**: Technical Architecture with Epic-Component Mapping Matrix
- **Handoff marker sent**: `<!-- EPIC_READY_WITH_ARCHITECTURE: {PRODUCT-CODE} -->`
- **What the Epic Generator consumes**: Component assignments, tech constraints per epic, API
  contracts, dependency chain between epics

### Frontend/Backend Validation Protocol

- **When**: Phase 2, after initial section generation
- **Frontend**: Review Component Architecture (section 4) and API Design (section 5) for frontend
  feasibility
- **Backend**: Review Data Architecture (section 6), API Design (section 5), and Security
  Architecture (section 7)
- **Format**: Each specialist provides a pass/fail with specific concerns
- **Conflict resolution**: If a specialist's recommendation changes the Epic-Component Mapping,
  evaluate whether the change improves or harms team parallelism. Present both options to the user
  with the parallelism tradeoff.

---

## Template and Context Loading

### Template Reference

Read the architecture template from your organization's reusable-template folder (e.g. a
`technical-architecture-template.md`). If none is provided, follow the 12-section order in Phase 2.

### Product Context

Load product-specific context from `{products_root}/{product}/context/`:

| File | Usage | Required |
|------|-------|----------|
| `constraints.md` | Technical constraints, compliance requirements | Recommended |
| `product-identity.md` | Product nature, target platforms, positioning | Optional |
| `personas.md` | User types, access patterns, scale implications | Optional |

### Missing Context Handling

If required context files are missing:
1. Notify user: "Context file `{filename}` not found for {product}"
2. Offer to proceed with the information available from the PRD
3. Document any assumptions in the architecture and flag them in the Pipeline Readiness block
