# Proposal Generator — Reference

Deep reference for proposal construction. Firm specifics (service lines, promise, name)
are decided per organization (see [`ADAPT.md`](ADAPT.md)); the phase methodology and
structural patterns below are generic. **Every price and outcome metric is HUMAN INPUT —
never invent one.**

The firm-specific inputs this skill consumes are: the firm name and exact wordmark, a
one-line descriptor, the promise, the key messages, the differentiators, the business model,
and the service lines (each with a name, a one-line summary, and the client pain it solves).
Resolve every firm value from the firm's decided details at use time; if one isn't decided,
treat it as unanswered (ask via [`forms.md`](forms.md), or fall back to a labeled
`PLACEHOLDER`).

---

## Phase Details (generic methodology)

The four canonical phases below are a reusable journey shape. Map each phase to the
relevant service lines; show outcomes, never service codes. Every investment line is
**HUMAN INPUT**.

### Phase 1: ASSESS (Discovery & Strategy)
**What happens**:
- Deep dive into current state (systems, data, processes, pain points)
- Stakeholder interviews (leadership, operations, technical)
- Current-state audit and opportunity assessment
- Prioritized roadmap creation

**Client deliverable**: Strategic Roadmap
- Current-state assessment
- Prioritized opportunities (quick wins + long-term)
- Recommended journey with investment ranges
- ROI projections (from the client's numbers)

**Investment**: [HUMAN INPUT REQUIRED]
**Timeline**: 1-2 weeks

### Phase 2: FOUNDATION (Build the Base)
**What happens**:
- Stand up or optimize the core platform/infrastructure
- Connect source systems (APIs, databases, tools)
- Baseline quality and clean up
- Automate the pipelines (no more manual exports)

**Client deliverable**: A reliable, centralized foundation
- Core platform with key sources connected
- Automated refresh
- Quality monitoring and alerts
- Documentation and handoff

**Investment**: [HUMAN INPUT REQUIRED]
**Timeline**: 4-8 weeks (depends on number of sources)

### Phase 3: VISIBILITY (Make It Visible)
**What happens**:
- Define success metrics and a metrics hierarchy
- Design and build views/reports
- Enable self-service
- Train the team for adoption

**Client deliverable**: Decision-ready insight
- Executive views (real-time, accessible)
- Department-level views
- Self-service capability
- Training and documentation

**Investment**: [HUMAN INPUT REQUIRED]
**Timeline**: 3-6 weeks

### Phase 4: AUTOMATION (Add Intelligence)
**What happens**:
- Build assistants and automations on the foundation
- Automate repetitive processes and workflows
- Add intelligent integrations
- Optimize and improve continuously

**Client deliverable**: Intelligent, automated operations
- Automation for repetitive tasks
- Assistants for customer/employee support
- Process automation that reduces manual work
- Continuous improvement

**Investment**: [HUMAN INPUT REQUIRED]
**Timeline**: 4-12 weeks (depends on scope)

---

## Pricing Framework (structure only — every figure is HUMAN INPUT)

### Engagement structure

```
INITIAL PROJECT (fixed fee per phase)
ASSESS -> FOUNDATION -> VISIBILITY -> AUTOMATION
[one-time investment for each phase]
                    |
                    v
ONGOING RETAINER (monthly partnership)
- optimization & continuous improvement
- strategic advisory
- new capability development
- priority support
```

### Retainer tiers (reference shape — customize per client, fill prices as HUMAN INPUT)

| Tier | Monthly Investment | Typical Scope |
|------|--------------------|---------------|
| Advisory | $[HUMAN INPUT] | Monthly strategy call, priority support |
| Growth | $[HUMAN INPUT] | Regular touchpoints, ongoing improvements, small enhancements |
| Embedded | $[HUMAN INPUT] | Dedicated capacity, strategic partner, major development |

### ROI framing (compute from the client's own numbers)

Always include an ROI projection, expressed as bracketed placeholders filled from the
client's data — never a carried-over figure:

- **Time savings**: `[hours reclaimed]` × `[loaded hourly cost of affected staff]`
- **Error reduction**: `[cost of errors]` (rework, customer impact) reduced by `[%]`
- **Revenue impact**: faster decisions, better insight, captured opportunities
- **Avoided costs**: hires not needed, systems not purchased
- **Payback**: `[months to recoup investment]`

---

## Pain → Service-Line Mapping (internal use — NEVER shown to the client)

Build this table at runtime from the firm's service lines. Each entry carries the
client-facing pain it solves and a plain-language summary. **There are no numeric codes** —
the proposal speaks in outcomes, this table only helps Claude decide what to include.

| Client pain (their words) | Service line that solves it | Outcome to promise |
|---------------------------|-----------------------------|--------------------|
| The pain that service line solves | The service line's name | The service line's summary framed as a client outcome |

How to use it:
1. Cluster the client's discovery pain into bundles (see SKILL.md).
2. For each pain, match the service line whose client pain fits.
3. Slot the matched work into the right **phase** (FOUNDATION / VISIBILITY / AUTOMATION).
4. In the proposal, describe only the **outcome** — never the service-line name as a
   menu item, and never any internal code.

> If no service lines are decided yet, ask the Proposal Intake (forms.md, Q7) and record
> the answers — including each line's client pain — before drafting.

---

## Best Practices

### Client-centric language
- Use THEIR words from discovery; quote them back ("You told us…").
- Frame everything as solving THEIR problem.
- Outcomes over deliverables.

### Partnership positioning
- "Your partner", not "your vendor".
- Reference the ongoing relationship and long-term value, not just the project.
- Pull the "why us" from the firm's differentiators and key messages.

### Phased approach
- Always start with ASSESS.
- Build trust before proposing big builds.
- Quick wins + long-term transformation.
- Retainer for ongoing value once the foundation exists.

> All firm-specific values are decided per organization (see [`ADAPT.md`](ADAPT.md)). This
> file stays portable across firms — only the decided values change. No price or outcome
> metric is ever invented.
