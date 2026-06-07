# Product Manager — Reference

Deep expertise, patterns, and detailed methodology. Load on demand when working on product
management tasks. Product, lifecycle, audience, and path specifics are the organization's
decisions (see [`ADAPT.md`](ADAPT.md)); the methodology below is generic.

---

## Cross-Line Business Model (Detailed)

Consider the organization's business model. Some organizations run two or more business lines
that feed each other — for example a services/client line whose engagements surface product
opportunities, or one line that funds another. If the model describes such a loop, apply the
pipeline and review below. If the model is a single straightforward line, skip this section
entirely.

### Field Line → Product Pipeline (when the model has one)

```
CUSTOMER / CLIENT ENGAGEMENT
      |
      v
Pain Point Identified -> Document, tag as a product candidate
      |
      v
Pattern Recognition -> 3+ customers with same pain? Escalate to product review
      |
      v
Product Candidate -> Evaluate against product roadmap, MoSCoW prioritize
      |
      v
Feature Backlog -> Enter the lifecycle at the first stage, assign a product code
```

### Service-to-Product Mapping (generic pattern)

| Field signal | Typical customer pain | Product opportunity |
|--------------|-----------------------|---------------------|
| Repeated bespoke build | "We rebuild this every time" | Productize as a reusable feature |
| Manual / spreadsheet workflow | "Everything lives in spreadsheets" | Self-service tool in a product |
| Data quality complaints | "Our data is dirty" | Data-quality capability |
| Support overwhelmed | "We can't keep up with questions" | Self-serve / assistant capability |
| Information hard to find | "We can't find anything" | Search / knowledge capability |
| Repeated manual process | "We do this by hand every week" | Automation capability |

Map each row to a real product code from the organization's product taxonomy at use time — do
not hardcode product names here.

### Cross-Line Review Questions

Before any product decision (when the model has a cross-line loop), ask:
1. **Did this originate from the other business line?** Document the source.
2. **Would this help other customers?** Potential offering.
3. **Does building this improve the other line?** Skills/asset transfer.
4. **Can we validate with current customers?** Real-world testing.

---

## Product Relationships

Take the product set and their relationships from the organization's product taxonomy. Sketch
the dependency graph at use time — which product is foundational, which extend it, which are
specialized. Example shape (fill nodes from the taxonomy):

```
                  [Moonshot / flagship]
                          |
                     Foundation
                          v
                    [Core platform]
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    [Extension]     [Platform]      [Specialized]
```

Do not hardcode any specific product name in this graph — resolve them from the taxonomy.

---

## AI-Native Development (Detailed)

### How AI Assists at Each Stage

| Stage | AI Role | Human Role |
|-------|---------|------------|
| **Vision-type** | Market research, competitor analysis | Strategic direction, problem selection |
| **Feasibility-type** | Technical research, architecture options | Feasibility judgment, resource decisions |
| **Design-type** | PRD drafting, user story generation | Validation, prioritization, stakeholder input |
| **Development-type** | Code generation, test writing | Code review, architecture decisions |
| **Launch-type** | Documentation, release notes | Go/no-go decisions, user communication |

Map "type" rows to the actual stage names in the organization's lifecycle stages.

### AI Guardrails (Skills as Quality Gates)

```
PRD QUALITY GATE
├── Product manager reviews structure and completeness
├── Evidence base verified (not AI-generated assumptions)
├── MoSCoW applied with rationale
└── Cross-functional input documented

DESIGN QUALITY GATE
├── UX designer reviews design decisions
├── Brand compliance checked (brand guidelines skill)
├── Accessibility requirements met (WCAG AA)
└── Device strategy appropriate

DEVELOPMENT QUALITY GATE
├── Engineering reviews technical approach
├── Testing requirements specified
├── No technical debt accepted
└── Documentation requirements clear
```

---

## Stakeholder Management

### Stakeholder Matrix (small team)

| Role | Who | Communication | Frequency |
|------|-----|---------------|-----------|
| **Decision Makers** | Leadership | Strategy alignment, stage-gates | Weekly sync |
| **Contributors** | Builders / contractors | Task-level updates, blockers | Per sprint |
| **Advisors** | Advisory board | Strategic input | Monthly |
| **Investors** | Current + potential | Progress updates, metrics | Quarterly |

### RACI for a small team

| Decision/Task | Product Lead | Tech Lead | Contributor |
|---------------|:------------:|:---------:|:-----------:|
| Product Vision | **A** | C | I |
| Technical Architecture | C | **A** | R |
| Feature Prioritization | **A** | C | I |
| Sprint Execution | I | C | **R** |
| Stage-Gate Decisions | **A** | **A** | I |
| Customer Communication | **A** | C | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

Adapt the role columns to the organization's actual leadership structure.

---

## MoSCoW Decision Criteria (Detailed)

| Category | Ask This | Evidence Required |
|----------|----------|-------------------|
| **Must** | Will users abandon without this? | User research showing a dealbreaker |
| **Should** | Does this significantly improve experience? | Usage data or feedback pattern |
| **Could** | Is this a nice enhancement? | Occasional requests, not blocking |
| **Won't** | Why are we saying no (for now)? | Resource constraints, strategic focus |

### Evidence-Based Prioritization

Every MUST-have feature requires evidence. Acceptable evidence sources:
- Direct user research (interviews, usability tests)
- Customer feedback patterns (3+ customers with the same pain)
- Analytics data showing user behavior
- Competitive analysis (table-stakes features)
- Regulatory/compliance requirements

---

## Stage-Gate Deep Dive

### Stage Gate Decision Framework

Map each row to a named stage from the organization's lifecycle stages.

| Stage type | Gate Question | Proceed If | Pivot If | Pause If |
|------------|---------------|------------|----------|----------|
| Vision | Is this worth pursuing? | Clear problem + market | Problem unclear, market exists | No market signal |
| Feasibility | Can we build it? | Technically viable + resourced | Tech hard but solvable | Requires capabilities we lack |
| Design | Do we know what to build? | Clear spec + user validation | Spec unclear but direction right | User feedback contradicts thesis |
| Development | Is it working? | Tests pass + metrics tracking | Bugs fixable + on track | Quality compromised |
| Launch | Is it growing? | Retention + growth metrics | Growth levers identified | Market rejection |

### Confidence Indicators

Before the Design-type stage is complete, use confidence indicators:
- **High Confidence**: validated with users, technically feasible, resources available
- **Medium Confidence**: partially validated, some unknowns remain
- **Low Confidence**: assumptions untested, significant unknowns

Never commit dates until the Design-type stage is complete with High Confidence.

---

## Depth Requirements

Every deliverable must include:
- **Product context** — which product (from the taxonomy), which stage
- **Evidence citations** — data source, research date, sample size
- **MoSCoW classification** — clear prioritization with reasoning
- **Business-model angle** — cross-line implications considered (when the business model has them)
- **Success criteria** — measurable, time-bound, achievable

---

## Workspace Integration

Use the organization's decided paths — never hardcode them:
- Product folders live under the organization's products-root path.
- Planning context goes in the organization's progress file; the execution queue in its
  next-steps file.
- Document templates live at the organization's template locations.
- Filenames follow the organization's naming conventions.

If a workspace path is undecided, ask the Product Context Intake question for it (see
[`forms.md`](forms.md)) before writing files, or use a clearly-labeled placeholder path.

---

## References

- **Method (external)**: [MoSCoW Method](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html),
  [Stage-Gate Process](https://www.stage-gate.com/), [Continuous Product Discovery](https://www.producttalk.org/)
- **Companion skills**: UX designer, frontend engineer, software architect, dashboard/data-viz
  skill, brand guidelines skill, assumption-challenge skill
