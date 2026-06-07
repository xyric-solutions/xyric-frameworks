# Brainstormer — Reference

Loaded on demand for detailed phase instructions, the hard-questions framework, contradiction
detection, and the Vision Generator handoff. The questioning method is universal;
organization-specific context (business model, lifecycle stages, portfolio, paths) is decided
per organization — see [`ADAPT.md`](ADAPT.md).

---

## Phase 0: INTAKE (Capture & Parse)

**Purpose**: Transform raw, unstructured input into an organized inventory.

### Step 1: Accept any format

The user provides the idea in any format:
- Brief: "I want to build an app that helps people save money"
- Detailed: a multi-paragraph brain dump with scattered thoughts
- Mixed: notes, inspirations, competitor mentions, feature ideas

### Step 2: Parse into categories

| Category | What to Extract |
|----------|-----------------|
| **Problem Space** | Pain points mentioned, problems to solve |
| **Solution Ideas** | Features, approaches, mechanisms |
| **Target Users** | Who was mentioned (explicit or implied) |
| **Technical Hints** | Technology mentions, platform, constraints |
| **Scope Signals** | What's in, what's out, ambition level |
| **Inspirations** | Competitors, analogies, references |

### Step 3: Create the Raw Ideas Inventory

```markdown
## Raw Ideas Inventory: [Product Name]

### Problem Space
- [Extracted problem 1]
- [Extracted problem 2]
- [Gap/unclear]: [What's missing]

### Solution Ideas
- [Feature/approach 1]
- [Feature/approach 2]
- [Potential conflict]: [X vs Y]

### Target Users
- [User type mentioned]
- [Implicit user]: [inferred from context]
- [Missing]: Specific persona details

### Technical Direction
- [Tech mentioned]
- [Platform implied]
- [Complexity flag]: [area of concern]

### Scope Signals
- [In scope]: [what's clearly included]
- [Ambiguous]: [unclear boundaries]
- [Red flag]: [scope creep indicators like "everything"]

### Inspirations & Analogies
- [Competitor/product mentioned]
- [Analogy used]
```

### Step 4: Flag issues for Phase 1

Identify:
- Vague terms needing definition
- Potential contradictions
- Missing critical elements (no user? no problem?)
- Scope creep signals
- Portfolio overlap with the organization's existing offerings (its product taxonomy /
  service lines) (when the portfolio is not yet known: ask the user for their portfolio, or defer)

**Output**: Present the inventory to the user with flagged issues.

---

## Phase 1: HARD QUESTIONS (Challenge + Expand)

**Purpose**: Challenge assumptions AND expand thinking through Socratic questioning.

**The Brainstormer difference**: Unlike pure challenge frameworks, the Brainstormer ADDS to
the user's thinking. Each question category includes:
1. **Core Challenges** — surface what's unstated
2. **Expansion Prompts** — contribute patterns and perspectives
3. **Specificity Demands** — force concrete details

### Step 1: Present inventory for validation

```markdown
### Inventory Validation

I've parsed your input into the following inventory. Before we dive into questions,
please confirm this captures your thinking:

[Show Raw Ideas Inventory]

**Quick validation:**
- Did I miss any key ideas?
- Did I miscategorize anything?
- Any immediate corrections?
```

### Step 2: Apply the Hard Questions Framework (below)

Walk through all 5 categories, adapting to the specific idea.

### Step 3: WAIT for user input

Blocking step. Do not proceed to Phase 2 until the user has responded to all categories.

### Step 4: Optional follow-ups

If responses are still vague or raise new questions, ask targeted follow-ups before proceeding.

**Output**: a Challenged Assumptions Matrix showing the question asked, the user's response,
remaining ambiguities, and contradictions identified.

---

## Phase 2: CLARIFICATION (Resolve Tensions)

**Purpose**: Resolve contradictions and define vague terms.

### Step 1: Present tensions

```markdown
### Tensions to Resolve

Based on your answers, I've identified these areas needing clarification:

**Contradiction 1: [Title]**
- You mentioned: "[Statement A]"
- But also: "[Statement B]"
- These seem to conflict because: [Explanation]

**Vague Term 1: [Term]**
- You used "[term]" in context of [where]
- This could mean: [Interpretation A], [Interpretation B], or [Interpretation C]
- Which is closest to your intent?

**Missing Element 1: [What's Missing]**
- Your brainstorm doesn't address [element]
- This matters because [why]
- Options: [A], [B], or [explicitly out of scope]
```

### Step 2: Propose resolution options

For each tension, provide 2–3 concrete options:

```markdown
**Contradiction 1 Resolution Options:**

A) Prioritize [Statement A]: This means [implication]
B) Prioritize [Statement B]: This means [implication]
C) Context-dependent: [A] for [context], [B] for [other context]

Which approach fits your vision?
```

### Step 3: WAIT for user decisions

Blocking step. Capture the user's decision on each tension.

### Step 4: Document resolutions

For each resolved tension: what was the conflict, what was decided, and why.

**Output**: a Resolved Positions Document.

---

## Phase 3: SYNTHESIS (Generate the brainstorm document)

**Purpose**: Combine all inputs into a structured brainstorm document.

### Step 1: Map content to template

| Source | Maps To |
|--------|---------|
| Raw Ideas Inventory | "Raw Ideas Inventory" section |
| Phase 1 Q&A | "Challenged Assumptions" section |
| Phase 2 Resolutions | "Resolved Tensions" section |
| User clarity | "User Clarity", "Problem Clarity", "Solution Clarity" |
| Risk questions | "Risk Registry" section |
| Open items | "Open Questions" section |

### Step 2: Generate each section

Follow the Output Format (see `forms.md`) and generate each section sequentially, ensuring
consistency.

### Step 3: Cross-reference check

- Does the Executive Snapshot align with the detailed sections?
- Are all inventory items accounted for?
- Do resolved tensions appear in the appropriate sections?

**Output**: a complete brainstorm-document draft.

---

## Phase 4: VALIDATION (Blocking)

**Purpose**: Quality gate ensuring the brainstorm is ready for the Vision Generator.

### Critical checks (block if fail)

| Check | Criteria | If Fail |
|-------|----------|---------|
| **Problem Clarity** | Problem statement is specific, not generic | Return to Phase 1, WHY questions |
| **User Clarity** | Primary user defined with specifics | Return to Phase 1, WHO questions |
| **Solution Clarity** | Solution concept is bounded and clear | Return to Phase 1, WHAT questions |
| **Contradiction-Free** | No unresolved contradictions remain | Return to Phase 2 |
| **Scope Bounded** | Explicit exclusions listed | Return to Phase 1, WHAT questions |

### Quality checks (warning if >3 fail)

| Check | Criteria | If Fail |
|-------|----------|---------|
| **Evidence Present** | At least 2 types of evidence for the problem | Note in Open Questions |
| **Risks Identified** | At least 3 risks documented | Add Risk Registry items |
| **Technical Direction** | High-level approach stated | Note in Open Questions |
| **Anti-Persona** | Who is NOT the user is defined | Add to User Clarity |
| **Session Logged** | Brainstorm session captured | Add to document |

### Validation output

```markdown
## Validation Results

### Critical Checks
- [x] Problem Clarity: PASS - [summary]
- [x] User Clarity: PASS - [summary]
- [x] Solution Clarity: PASS - [summary]
- [x] Contradiction-Free: PASS - [summary]
- [x] Scope Bounded: PASS - [summary]

### Quality Checks
- [x] Evidence Present: PASS
- [x] Risks Identified: PASS (4 risks)
- [ ] Technical Direction: WARNING - flagged for Vision phase
- [x] Anti-Persona: PASS
- [x] Session Logged: PASS

**Result**: READY FOR VISION GENERATOR
```

**If all critical pass**: write the brainstorm document to the offering folder (the
organization's product-folder location) with the vision-ready marker (see `forms.md`).

**If any critical fail**: return to the appropriate phase and re-validate.

---

## Hard Questions Framework

### Category 1: WHY Questions (Existence & Purpose)

**Purpose**: Challenge the fundamental reason for this product to exist.

**Core Challenge Questions**
```
1. "Why does this need to exist?"
2. "What problem is so severe that THIS specific solution is needed?"
3. "Why would anyone care about this?"
4. "Why you? Why now? What's changed that makes this the right time?"
5. "Why can't the existing alternatives solve this?"
```

**Expansion Prompts** (the skill contributes)
```
"Based on your problem statement, I see parallels to [pattern/category].
Products in this space typically exist because of [reasons].
Does any of this resonate, or is your 'why' different?"

"You mentioned [X]. That suggests the core 'why' might be about [deeper need].
Am I reading that correctly?"

"The timing question is interesting. What I know about [domain/technology]:
[relevant context]. Does this inform your timing?"
```

**Specificity Demands**
```
"If I asked 10 random people why this product should exist,
what's the one sentence you'd want them all to say?"
```

---

### Category 2: WHO Questions (Users & Stakeholders)

**Purpose**: Define exactly who this is for — and who it is NOT for.

**Core Challenge Questions**
```
1. "Who exactly will use this? Be specific -- 'everyone' is wrong."
2. "Who is NOT your user? What makes them different?"
3. "Who pays vs. who uses? Are they the same person?"
4. "Who has the problem most severely? Who barely has it?"
5. "Who would be your first 10 users? Can you name them?"
```

**Expansion Prompts** (the skill contributes)
```
"Products in [this space] typically serve personas like:
- [Persona A]: [description]
- [Persona B]: [description]
- [Persona C]: [description]

Which is closest to your target? Or is yours different?"

"You mentioned [characteristic]. That suggests users who [behavior].
Let me expand on what that user typically needs and struggles with..."

"The 'who pays vs. who uses' distinction matters because [reason].
In your case, I'm inferring [X]. Is that right?"
```

> When the organization defines its target audience segments (ICP tiers), anchor the persona
> expansion in those real segments rather than inventing generic ones.

**Specificity Demands**
```
"Describe your primary user in one sentence including:
their role, their biggest frustration, and what they're trying to achieve."
```

---

### Category 3: WHAT Questions (Scope & Definition)

**Purpose**: Define exactly what this is — and what it is not.

**Core Challenge Questions**
```
1. "What exactly does [vague term from inventory] mean to you?"
2. "What is this product NOT? What are the hard boundaries?"
3. "What must it do (P0) vs. what would be nice (P2)?"
4. "What does 'done' look like for version 1?"
5. "What would you cut if you had half the resources?"
```

**Expansion Prompts** (the skill contributes)
```
"When you say '[term]', I can interpret it as:
A) [Interpretation A] - like [example]
B) [Interpretation B] - like [example]
C) [Interpretation C] - like [example]
Which is closest?"

"Based on the problem you described, I'd expect core features like:
- [Feature X] - because [reasoning]
- [Feature Y] - because [reasoning]
Does that match your thinking, or am I off?"

"The boundary between [related concept A] and [related concept B]
is often where products get confused. Where do you draw that line?"
```

**Specificity Demands**
```
"Complete this sentence: 'This product lets [user] do [action]
so they can [outcome], but it does NOT [explicit exclusion].'"
```

---

### Category 4: HOW Questions (Feasibility & Mechanism)

**Purpose**: Understand how this will actually work.

**Core Challenge Questions**
```
1. "How will this actually work? Walk me through a user's journey."
2. "What makes this technically possible -- or hard?"
3. "How will users discover and start using this?"
4. "How is this different from [closest alternative] in practice?"
5. "How will you know if it's working?"
```

**Expansion Prompts** (the skill contributes)
```
"The technical approach you're describing has known patterns:
- [Pattern A]: Used by [examples], works well when [conditions]
- [Pattern B]: Used by [examples], works well when [conditions]
Which aligns with your thinking?"

"I see potential complexity in [area]. Similar products have handled
this by [approach]. Is that applicable here?"

"You mentioned [technology]. Based on what I know, the implications are:
- Enables: [capabilities]
- Constrains: [limitations]
- Requires: [dependencies]
Does that match your understanding?"
```

**Specificity Demands**
```
"Walk me through the exact sequence from the moment a user
first hears about this to the moment they get value. What are the steps?"
```

---

### Category 5: WHAT-IF Questions (Risks & Failure Modes)

**Purpose**: Surface risks and failure scenarios before they are embedded in plans.

**Core Challenge Questions**
```
1. "What if [key assumption from inventory] is wrong?"
2. "What would kill this product?"
3. "What's your nightmare scenario?"
4. "What if a well-funded competitor copies this tomorrow?"
5. "What if your first 100 users hate it?"
```

**Expansion Prompts** (the skill contributes)
```
"Products in this space commonly fail because of:
- [Failure mode 1]: [why it happens]
- [Failure mode 2]: [why it happens]
- [Failure mode 3]: [why it happens]
How does your approach avoid or mitigate these?"

"If [key assumption] is wrong, your fallback options might include:
- [Pivot option A]
- [Pivot option B]
Have you considered these?"

"The [technology/approach] you mentioned has these known risks:
[list]. Which concern you most?"
```

**Specificity Demands**
```
"Name three specific things that could make this fail,
and what you'd do if each happened."
```

---

## Contradiction & Vagueness Detection

### Automatic detection patterns

| Issue Type | Detection Pattern | Example | Action |
|------------|-------------------|---------|--------|
| **Contradiction** | Statement A directly conflicts with Statement B | "Simple and intuitive" vs "Feature-rich with many options" | Surface in Phase 2, require resolution |
| **Vagueness** | Terms without operational definition | "Smart", "AI-powered", "modern", "seamless" | Demand specific definition |
| **Scope Creep** | Unlimited ambition signals | "Everyone", "all users", "everything", "complete solution" | Challenge in Phase 1, bound in Phase 2 |
| **Missing Who** | No clear user definition | Solution described without specific persona | Block until WHO questions answered |
| **Missing Why** | Solution without problem | Features listed without pain points | Block until WHY questions answered |
| **Wishful Thinking** | Unsupported assumptions | "Users will love...", "Obviously...", "Everyone needs..." | Challenge with "How do you know?" |
| **False Precision** | Specific numbers without basis | "Will get 10,000 users in month 1" | Flag as assumption, not fact |
| **Hidden Dependency** | Success requires an unstated factor | "This will work once we have..." | Surface the dependency explicitly |

### Vague Term Dictionary

When these terms appear without definition, demand specificity:

| Vague Term | Demand |
|------------|--------|
| "AI-powered" | What specifically does the AI do? What's the input/output? |
| "Smart" | Smart compared to what? What decision does it make? |
| "Modern" | Modern in what way? UI? Architecture? Approach? |
| "Seamless" | No friction where specifically? What would friction look like? |
| "Easy to use" | Easy for whom? Compared to what? |
| "Scalable" | Scale to what numbers? What's the constraint? |
| "Secure" | Secure against what threats? What compliance? |
| "Fast" | Fast compared to what? What's the target? |

---

## Handoff to the Vision Generator

### Two entry modes for the Vision Generator

**Mode 1: With brainstorm (recommended)**
```
When the Vision Generator receives a document with the vision-ready marker:

1. Read the brainstorm document as the primary context source
2. The research phase is pre-populated from the brainstorm
3. The questions phase is REDUCED:
   - Skip questions already answered in the brainstorm
   - Focus on vision-specific questions (strategy, positioning)
   - Reference brainstorm decisions, don't re-challenge
4. Faster path to a Vision Document
```

**Mode 2: Without brainstorm (legacy)**
```
When no brainstorm document exists:

1. The Vision Generator runs its full workflow
2. All questions are asked
3. More iteration is required
4. Higher risk of embedded contradictions
```

### Handoff protocol

1. The Brainstormer writes the brainstorm document to the offering folder (the organization's
   product-folder location).
2. It includes the vision-ready marker at the top (format in `forms.md`).
3. The user invokes the Vision Generator with the offering context.
4. The Vision Generator detects the marker and enters Mode 1.
5. It references the brainstorm throughout generation.

### What transfers to Vision

| Brainstorm Section | Vision Section |
|--------------------|----------------|
| Executive Snapshot | Executive Summary (seed) |
| User Clarity | Target Users, Value Propositions |
| Problem Clarity | Problem Statement, Market Context |
| Solution Clarity | Product Architecture (foundation) |
| Risk Registry | Risks & Mitigation |
| Open Questions | Questions-phase focus areas |

---

*Brainstormer Reference | Deep expertise loaded on demand*
