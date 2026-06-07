# Vision Generator — Reference

Detailed phase-by-phase instructions, context-source loading, brainstorm integration,
and quality standards. All paths and portfolio categories are organization decisions (see
[`ADAPT.md`](ADAPT.md)); the methodology and diagram standards below are universal.

---

## Organization-specific values this skill operates on

Decide these once (see [`ADAPT.md`](ADAPT.md)) and confirm them at use time:

- **Product folder location** — per-product folder pattern (where the vision is written)
- **Progress/tracking file** — planning/progress tracker filename
- **Template location** — where doc templates live (incl. any vision template)
- **Naming convention** — filename convention for the vision file
- **Business model** — one-line model (context only)
- **Portfolio / lifecycle model** — categories or stage names for strategic fit
- **Product / org name + one-liner** — used throughout the vision
- **Audience** — primary / secondary user segments, differentiators, key messages

Use these concrete values at use time. If one is undecided, treat it as unanswered (ask via the
intake in `forms.md`, or fall back to a labeled placeholder and a neutral local path).

---

## Required Context Sources

Before generating a vision document, gather context from available sources. Paths are
relative to the consuming workspace (your product folders and siblings).

| Priority | Source | Where | Extract |
|----------|--------|-------|---------|
| **Critical** | Brainstorm artifact | this product's folder | Pre-validated ideas, challenged assumptions |
| Critical | User Input | (provided by user) | Product idea, notes, brainstorm |
| High | Existing vision docs | other product folders | Template patterns, structure |
| High | Product folder | this product's folder | Existing product context |
| Medium | Company/org context | the org's company docs (if any) | Mission, values |
| Medium | Related products | sibling product folders | Cross-product synergies |
| Low | Frameworks/methodologies | the org's frameworks folder (if any) | Methodologies to apply |

**Key Principle:** User input is the PRIMARY input. Existing documents provide template
patterns and context but should never constrain the new vision's uniqueness.

### Template & Context Loading

**Template reference:** read the vision document template from your organization's template
folder (look for a vision / Product-Vision template). It defines required sections, structure,
and format. Always reference it during Phase 2 (Generation). If none is configured, use the
Required Sections list in `forms.md`.

**Product context (if available):** load product-specific context from the product's
`context/` subfolder when present:

| File | Usage | Required |
|------|-------|----------|
| product-identity | Verify alignment if updating an existing product | Optional |
| personas | Reference existing personas if available | Optional |
| pillars | Understand product domain structure | Optional |

**Note:** For new products, context files will not exist yet. The vision document is
typically the first document created, so context loading is optional.

### Missing Context Handling

**New Product:**
1. Proceed without context files (this is expected)
2. After the vision is created, recommend creating context files for downstream documents

**Updating an Existing Product Vision:**
1. Check for existing context files
2. Ensure updates align with the established product identity (the org's product name)
3. Note any conflicts in the output

---

## Phase 0: Research & Context Gathering (Detailed)

**Purpose:** Build unified context from user input and existing documents.

### Step 0: Brainstorm Detection

Before parsing user input, check for a structured brainstorm artifact:

```
1. Check: does a brainstorm artifact exist in this product's folder?
2. If YES: check for a VISION_READY marker containing the product code
3. If MARKER FOUND:
   - Set MODE = "With Brainstorm"
   - Extract structured content (see mapping table below)
   - Skip to Step 1b (Brainstorm Extraction)
4. If NO MARKER:
   - Warn: "A brainstorm exists but isn't marked ready. Complete the brainstorm step first?"
5. If NO FILE:
   - Set MODE = "Without Brainstorm" (Legacy)
   - Continue to Step 1a (User Input Parsing)
```

### Step 1a: Parse User Input (Legacy Mode)

User provides the product idea in any format:
- Brief: "I want to build an AI tutoring platform"
- Detailed: a multi-page brainstorm document
- Mixed: rough notes with some research

Extract from user input:
- Product name (or suggest one)
- Core problem being solved
- Target market/users
- Technology approach
- Revenue model hints (captured for context only; excluded from the vision)
- Competitive landscape mentions

### Step 1b: Extract from Brainstorm (With Brainstorm Mode)

When a brainstorm artifact exists and is marked ready:

| Extract | Brainstorm section |
|---------|--------------------|
| Product name | Executive Snapshot → One-liner |
| Problem statement | Problem Clarity → Problem Statement |
| Primary user | User Clarity → Primary Persona |
| Anti-persona | User Clarity → Anti-Persona |
| Core capabilities | Solution Clarity → Must Have |
| Exclusions | Solution Clarity → Out of Scope |
| Tech approach | Technical Approach Clarity |
| Risks | Risk Registry |
| Defined terms | Resolved Tensions → Defined Terms |

**Advantage:** all content is pre-validated through the upstream brainstorm challenge process.

### Brainstorm → Vision Section Mapping

| Brainstorm section | Maps to vision section |
|--------------------|------------------------|
| Executive Snapshot | Executive Summary seed |
| User Clarity (Primary Persona) | Target Users foundation |
| Problem Clarity | Problem statement, evidence |
| Solution Clarity | Core capabilities, differentiators |
| Technical Approach Clarity | Product Architecture hints |
| Risk Registry | Risks & Mitigation foundation |

### Step 2: Gather Supporting Context

Check for these and extract relevant patterns:

| Source | What to Extract | Why It Matters |
|--------|-----------------|----------------|
| Existing vision docs | Section structure, depth level | Ensures consistency |
| Company/org docs | Mission, values, portfolio | Strategic alignment |
| Related products | Synergies, cross-references | Ecosystem fit |

### Step 3: Create Input Analysis Summary

Combine ALL context into one summary (see the Input Analysis Template in `forms.md`).

---

## Phase 1: Questions & User Input (Detailed)

**INPUT:** Input Analysis from Phase 0

**Mode-Dependent Flow:**
- **With Brainstorm Mode:** present the brainstorm summary, ask 4 reduced questions
- **Without Brainstorm (Legacy) Mode:** present the input analysis, ask 7 full questions

---

### With Brainstorm Mode (4 Questions)

**Step 1: Present the Brainstorm Summary** (see template in `forms.md`).

**Step 2: Reduced Questions (4 Questions)**

Since the brainstorm has pre-validated core content, focus on VISION-SPECIFIC expansion.

**Q1. Vision Expansion**
```markdown
The brainstorm establishes your product as:
"[One-liner from brainstorm]"

For the long-term VISION:
a) How do you see this product evolving over time?
b) What's the ultimate form this product could take?
c) What capabilities would a mature version have that v1 won't?
d) Is there platform potential? (Other products building on this?)
```

**Q2. Strategic Positioning**
```markdown
Questions about strategic fit:
a) Where does this fit in the organization's portfolio?
   (Offer the org's portfolio / lifecycle categories —
    e.g. flagship bet / core product / exploratory / supporting)
b) Why is this a priority NOW? What's changed?
c) What resources are you prepared to commit?
d) What would success look like in 1 year? 3 years?
```

**Q3. Architecture Depth**
```markdown
The brainstorm mentions this technical approach:
"[From Technical Approach Clarity]"

For vision-level architecture:
a) What are the major system components you envision?
b) What's the core technology that makes this possible?
c) Any technology bets or dependencies to call out?
d) Build vs. buy decisions at a high level?
```

**Q4. Quality Metrics**
```markdown
What product quality metrics matter most?
a) User Experience: time to value? ease of use / learning curve?
b) Performance: speed requirements? scale expectations?
c) Reliability: uptime requirements? error tolerance?
d) Which 3 metrics would you never compromise on?
```

---

### Without Brainstorm Mode (7 Questions — Legacy)

**Step 1: Present Analysis to User** — show the unified Input Analysis summary.

**Step 2: Tailored Questions**

**Critical:** questions must reference the user's specific input, not be generic.

> **Note:** Business questions (revenue model, go-to-market) are intentionally excluded.
> Vision documents focus on product concept, not monetization.

**PRODUCT CONCEPT (3 Questions — PRIMARY)**

**Q1. Problem Space**
```markdown
Based on your input, the core problem appears to be:
"[Extracted problem statement]"

a) Is this problem statement accurate? What would you refine?
b) How severe is this problem? (Minor inconvenience → Critical pain point)
c) What evidence do you have that this problem exists? (Experience, research, interviews)
d) Why do existing solutions fail to solve this adequately?
```

**Q2. Target Users**
```markdown
Target users appear to be:
"[Extracted target users — cross-check the org's primary/secondary segments]"

a) Who is the PRIMARY user? (Most important to serve well)
b) Who are SECONDARY users? (Also benefit from the product)
c) What does a day in the life of your primary user look like?
d) What are their top 3 frustrations with current solutions?
```

**Q3. Solution Approach**
```markdown
The product concept appears to be:
"[Extracted solution description]"

a) What are the 3–5 core capabilities this product MUST have?
b) What makes this approach unique? (Why choose this over alternatives?)
c) What will users be able to do that they couldn't do before?
d) What's the "aha moment" when users understand the value?
```

**TECHNOLOGY (2 Questions — SECONDARY)**

**Q4. Technology Approach**
```markdown
Based on your input, the technology approach seems to involve:
"[Extracted tech mentions]"

a) What core technology enables this product? (AI/ML, Platform, API, etc.)
b) Build vs. Buy: what should be built in-house vs. leveraged from existing tools?
c) Any specific technology constraints or preferences?
d) What makes this technically feasible now? (Why couldn't this exist 5 years ago?)
```

**Q5. Integration & Ecosystem**
```markdown
a) How does this product fit into the organization's portfolio?
   (Use the org's portfolio categories —
    e.g. standalone / extension of an existing product / synergistic / flagship)
b) What integrations are essential? (APIs, platforms, services)
c) If AI/ML is involved:
   - What data is needed? How will it be acquired?
   - What's the AI doing? (Predictions, automation, insights, generation)
   - Human-in-the-loop requirements? (Full automation vs. AI-assisted)
```

**CONSTRAINTS (2 Questions — TERTIARY)**

**Q6. Resource Constraints**
```markdown
What constraints should the vision acknowledge?
a) Team constraints: team size (current/planned); key skills available or needed
b) Scope constraints: what's explicitly OUT of scope? Features to exclude? Timeline expectations?
c) Context to know: industry regulations? past attempts at this?
```

**Q7. Risks & Product Assumptions**
```markdown
What keeps you up at night about this product?
a) Biggest product risks: technology / adoption / competition / complexity / other
b) What could kill this product? [Top concern]
c) What assumptions must be true for success? [Critical assumptions]
```

---

## Phase 2: Vision Generation (Detailed)

**INPUTS:** Input Analysis (Phase 0) + User Answers (Phase 1). No re-reading of full
documents — all context comes from the Phase 0 summary.

### Step 1: Apply User Decisions

Map user answers to vision sections:

| Decision | Impact on Vision |
|----------|------------------|
| Problem validation | Problem statement, evidence |
| Timeline & ambition | Vision statement, strategic objectives |
| Strategic positioning | Product differentiation, portfolio fit |
| Technology approach | Product architecture, principles |
| Risks | Risks & mitigation section |
| Constraints | Scope, timeline, governance |

> Note: revenue-model answers (if any) are captured for context only and do NOT produce a
> business-model section — the vision excludes monetization content.

### Step 2: Generate Sections (Sequential)

For each section, in order:
1. Reference user input and answers
2. Generate section content using the template
3. Cross-reference with previous sections
4. Ensure consistency and coherence

**Why sequential:** context preserved across sections, consistency maintained, no
contradictions, quality verified in real time.

### Step 3: Generate Visual Documentation

During Phase 2, generate these Mermaid diagrams:

| Diagram | Mermaid Type | Section | When to Generate |
|---------|--------------|---------|------------------|
| Product Evolution Timeline | `timeline` | Vision Statement | Always |
| Objective Dependencies Map | `flowchart TD` | Strategic Objectives | If 4+ objectives |
| Value Proposition Flow | `flowchart LR` | Core Value Proposition | Always |
| Stakeholder Influence Matrix | `quadrantChart` | Stakeholder Alignment | If 3+ stakeholders |
| Risk Landscape | `flowchart LR` | Risk Mitigation | Always |

**Generation instructions:**
1. **Timeline**: extract phases from the Vision Statement; use 3 phases minimum (Foundation → Growth → Platform)
2. **Dependencies**: identify objective relationships from Key Results; show the critical path to the goal
3. **Value Flow**: map user pain points → product capabilities → user benefits
4. **Stakeholder Matrix**: position stakeholders by influence (Y) and interest (X)
5. **Risk Landscape**: categorize risks by impact (High/Medium); connect to mitigations

**Diagram standards (universal Mermaid color scheme):**
```
- Light blue (#e3f2fd): Process steps, inputs, foundations
- Light yellow (#fff9c4): Warnings, decisions, medium priority
- Light green (#c8e6c9): Success, outputs, benefits
- Light red (#ffcdd2): Risks, errors, pain points
```
> These four are generic Material-style diagram swatches for readability — they are NOT a
> brand palette. If the org defines a brand palette, you may substitute it.

---

## Phase 3: Validation (Detailed)

**Purpose:** quality gate — must pass ALL checks before output.

### Critical Checks (Block if Fail)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Section Coverage** | All 10 required sections present | Add missing sections |
| **Consistency** | No contradictions between sections | Resolve conflicts |
| **Completeness** | No TBD, placeholder, or empty content | Fill in gaps |
| **Specificity** | Metrics quantified, names specific | Add concrete details |
| **No Business Content** | No revenue model, TAM/SAM, go-to-market | Remove business content |

### Quality Checks (Warning → Block if >3)

| Check | Criteria | Action if Fail |
|-------|----------|----------------|
| **Differentiators** | Product/tech advantage stated (not business) | Reframe as product-focused |
| **Risks** | At least 8 product risks identified | Add more risks |
| **Principles** | 7 product principles defined | Add principles |
| **Users** | At least 3 user personas | Add personas |
| **Focus Hierarchy** | 60% product, 30% problem, 10% strategy | Rebalance content |

### Validation Output
- All checks pass → proceed to Phase 4
- Any critical check fails → return to Phase 2

---

## Phase 4: Output & Tracking (Detailed)

### Step 1: Write the Vision File

Create the vision file in your product folder, using your filename convention. If the product
folder does not exist:
- Create the product folder
- Write the vision document as its first file

### Step 2: Update the Progress/Tracking File

Append a session entry to your progress/tracking file:
- Session timestamp
- Product name (the org's product name)
- Vision document created
- Key decisions made
- Open questions for the PRD phase

### Step 3: Output Pipeline Hooks

Include in the vision document for downstream consumption:
- Product code (for the PRD step)
- Strategic objectives summary
- Key constraints identified
- Format: a `PRD_READY` marker containing the product code

---

## Assumption-Challenge Integration (Detailed)

Run the **assumption-challenge pass** between Phase 0 (Research) and Phase 1 (Questions).

| Challenge Phase | Applied | Trigger |
|-----------------|---------|---------|
| A: Question Why | Yes | User provides a problem statement or product idea |
| B: Alternatives | Yes | Market assumptions, product positioning |
| C: Stress Test | Yes | Before finalizing vision direction |

**Challenge intensity:** Full (A + B + C)

**What to challenge:**
- Problem framing: "Is this the right problem to solve?"
- Target market: "Are these the right users to focus on?"
- Solution approach: "Why this approach vs. alternatives?"
- Uniqueness claims: "What evidence supports this differentiation?"

**Workflow update:**
```
Phase 0: Research → Assumption Challenge → Phase 1: Questions → Phase 2: Generate → Phase 3: Validate
```

**Skip the challenge when:**
- The user explicitly requests a bypass ("skip challenge")
- It's a vision revision (not new creation) with minor updates
- The user provides comprehensive rationale upfront

> If the organization defines a dedicated assumption-challenge skill/method, invoke it here;
> otherwise apply the A/B/C structure above inline.

---

## Integration with Other Roles

### PRD generation step
- Output: the vision document
- Handoff: a `PRD_READY` marker containing the product code
- PRD inherits: vision, objectives, personas, constraints

### Product management
- Alignment: strategic objectives, MoSCoW readiness
- Lifecycle: vision is the first lifecycle stage
- Review: PRD structure compatibility

### Software architecture
- Validation: technical feasibility of the architecture
- Input: technology approach, constraints
- Review: architecture-section accuracy

---

## Example: Vision Questions (Tailored)

A worked illustration (the AI tutoring platform is a generic example, not a real product):

```markdown
Based on your input, the core problem appears to be:
"Students struggle to get personalized tutoring at affordable prices, while traditional
tutoring doesn't scale and is limited by geography."

Target market appears to be:
"K-12 and college students globally, particularly in underserved regions."

Questions:
a) Is this problem statement accurate? What would you refine?
b) How severe is this problem?
   - A majority of students report needing more personalized help
   - Conventional one-to-one tutoring is costly per hour
   - Rural / emerging-market students often have no access
c) What evidence do you have?
   - Personal experience with tutoring challenges
   - Market research on EdTech adoption
   - Interviews with students/parents
d) Market size estimate? (cite a source or qualify as "estimated")
   - Reference the broader EdTech market and the online-tutoring segment
```
