# Technical Architecture Generator — Forms & Templates

Output templates, quality checklists, activation checklists, and validation criteria. The default
stack and all read/write paths are organization-specific decisions (see [`ADAPT.md`](ADAPT.md));
this file never hardcodes them.

---

## Architecture Context Intake (the adaptation questionnaire)

These are the decisions to make before using this skill for an organization. Ask as one numbered
list and **WAIT** for answers; then record them wherever your team keeps these decisions (your
design brief, or your forked copy of `SKILL.md`). Ask only what's missing.

1. **Default / standard tech stack** — the org's go-to stack for new products (frontend, backend,
   client/server state, database, deployment target)? (If there is no standard, say so — the skill
   will choose per-product and record it in an ADR.)
2. **Portfolio model** — one line on how products relate (e.g. many products sharing a developer
   pool, single product, agency/client work)? This sets the bar for stack coherence.
3. **Lifecycle stages** — the named stages a product passes through, if different from the defaults
   (Vision → Feasibility → Design & Planning → Development → Launch & Growth)?
4. **Products root** — the folder pattern where product docs live (e.g. a products directory with a
   sub-folder per product)?
5. **Progress file name** — the per-product session/progress doc filename?
6. **Naming conventions** — filename conventions for architecture, ADRs, and milestones?
7. **Template location** — where reusable doc templates (e.g. an architecture template) live, if
   any?

---

## Activation Checklist

When this skill is activated (`{products_root}` and the progress file are your organization's
decided values — see ADAPT.md):

**Phase 0: Research**
1. [ ] Locate the PRD Document for the product
2. [ ] Extract epics, features, constraints, integrations
3. [ ] Read the Vision Document for strategic context
4. [ ] Research existing patterns for similar systems
5. [ ] Generate PRD Analysis Summary (~500 words)

**Phase 1: Analysis**
6. [ ] Present PRD Analysis to user
7. [ ] Ask 6 tailored architecture questions
8. [ ] **WAIT for user responses**
9. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
10. [ ] Apply user decisions to architecture structure
11. [ ] Invoke a Software Architect skill for ADR creation
12. [ ] Generate 12 sections sequentially
13. [ ] Build Epic-Component Mapping Matrix

**Phase 3: Validation (Blocking)**
14. [ ] Verify all 12 sections complete
15. [ ] Verify 100% PRD epic coverage
16. [ ] Verify all major decisions have ADRs
17. [ ] If fails → return to Phase 2 and fix

**Phase 4: Output**
18. [ ] Write `Technical-Architecture.md` under the product folder (your products root)
19. [ ] Write ADRs to the product's `adrs/` folder
20. [ ] Update the progress file (your per-product progress filename)
21. [ ] Include pipeline hooks for the Epic Generator
22. [ ] Present completion summary

---

## Quality Checklist

### Section Completeness Check
- [ ] Executive Summary (system overview, key decisions)
- [ ] System Architecture Overview (components, layers, diagram)
- [ ] Technology Stack Selection (frontend, backend, database, infra)
- [ ] Component Architecture (module structure, boundaries)
- [ ] API Design Patterns (style, contracts, versioning)
- [ ] Data Architecture (models, storage, caching)
- [ ] Security Architecture (auth, authz, compliance)
- [ ] Infrastructure Requirements (cloud, deployment, scaling)
- [ ] Integration Points (external APIs, third-party services)
- [ ] Architecture Decision Records (ADR index + details)
- [ ] Epic-Component Mapping (PRD alignment)
- [ ] Technical Constraints & Trade-offs

### PRD Alignment Check
- [ ] Every PRD epic has component mapping
- [ ] Every PRD constraint addressed
- [ ] Every PRD integration point covered
- [ ] Security requirements from PRD implemented
- [ ] Performance targets from PRD achievable

### Quality Standards Check
- [ ] All technology choices have rationale
- [ ] All ADRs have alternatives evaluated
- [ ] No placeholder text (TBD, [fill in], etc.)
- [ ] Diagrams included for key architectures
- [ ] Modular Monolith First principle applied or justified

---

## PRD Analysis Summary Template

```markdown
## PRD Analysis: [Product Name]

### Product Context
**Product:** [Name and brief description]
**Type:** [Web App / Mobile App / Platform / API / etc.]
**Target Scale:** [Users, requests, data volume]
**Target Platforms:** [Web, iOS, Android, Desktop]

### Epic Structure Extracted
| Epic | Name | Key Features | Technical Implications |
|------|------|--------------|------------------------|
| E01 | [Name] | [Features] | [Implications] |
| E02 | [Name] | [Features] | [Implications] |

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

### Decision Points Requiring Input
- [Decision 1]: [Options identified]
- [Decision 2]: [Options identified]
```

---

## Epic-Component Mapping Matrix Template

```markdown
| PRD Epic | Components | APIs | Data Models | ADRs |
|----------|------------|------|-------------|------|
| E01 | [Components] | [APIs] | [Models] | [ADRs] |
| E02 | [Components] | [APIs] | [Models] | [ADRs] |
| **Coverage** | 100% | | | |
```

---

## Validation Criteria

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Epic Coverage** | Every PRD epic has component mapping | Add missing mappings |
| **ADR Coverage** | Major decisions have ADRs | Create missing ADRs |
| **Section Coverage** | All 12 required sections present | Add missing sections |
| **PRD Alignment** | No conflicts with PRD constraints | Resolve conflicts |
| **Completeness** | No TBD or placeholder content | Fill in gaps |

### Quality Checks (Warning if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Technology Rationale** | Each tech choice has justification | Add rationale |
| **API Contracts** | Key APIs defined | Add API definitions |
| **Data Models** | Core entities documented | Add data models |
| **Security Coverage** | Auth/authz defined | Add security details |
