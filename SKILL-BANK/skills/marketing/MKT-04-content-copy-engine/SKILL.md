---
name: Content Copy Engine
description: Generates ready-to-post social copy, profile copy, and design briefs from a library of copy templates, with a mandatory human-voice check, a LinkedIn growth/hook system, and a founder-authenticity gate. Use when writing post captions, threads, founder posts, or bios; do not use for long-form articles, ad creative production, or generic copy with no brand/audience context. To use it for a specific organization, see ADAPT.md.
tier: needs-adapt
adapt: ADAPT.md
status: ready
origin: community-template
---

# Content Copy Engine

The workhorse skill for daily content execution. It turns a topic and a raw draft
into ready-to-post copy by selecting a copy template, fitting the story into it,
writing a design brief, and validating every piece through a human-voice check
before output. This skill is the **method** — the templates, hooks, gates, and
workflow. The specifics it operates on — the organization's actual voice,
positioning, key messages, content pillars, accounts, and founders — are decided per
organization. See [`ADAPT.md`](ADAPT.md) for what to decide before using this for a
given organization.

When those specifics are not yet decided, **do not invent them** — produce a
clearly-labeled **GENERIC DRAFT** with neutral, obviously-non-brand `PLACEHOLDER`
values for any account name, message, pillar, palette, or founder voice, and list
what is missing. **Never invent** the organization's key messages, content pillars,
brand palette, taglines, or a founder's personal story.

## When to Activate

**Triggers**:
- "Write a post about [topic]"
- "Generate content for [day/platform]"
- "Create a caption for [format]"
- "Write copy using template [#]"
- "Generate a design brief for [post]"
- "Write profile copy for [account]"
- Any content-generation task for one of the organization's accounts/founders
- Ready-to-post copy for a content tracker — run this skill's full workflow
  (IDENTIFY → SELECT → GENERATE → DESIGN → VALIDATE → TARGET), then file the final
  copy wherever your content output lives (your content folder / active channels)

**Related skills** (compose where present): a brand-voice skill for voice alignment,
a founder-brand skill for founder-specific voice, a content-strategy skill for
diversity checks, an ICP/positioning skill for tier targeting, and per-platform
formatting skills (LinkedIn / X / Instagram rules).

## Strategy inputs to load on activation

| Input | Source | What to pull |
|-------|--------|--------------|
| **Copy templates** | The org's copy playbook (or [`reference.md`](reference.md) starter library) | Full template structures + examples, Quick Template Picker, Human Check, dead-words list, "what makes copy sound human" rules |
| **Positioning & messages** | The organization's positioning (promise, key messages, differentiators, ICP tiers) | ICP tiers, value pillars, key messages, one-liners |
| **Content plan** | The org's content pillars / channels + GTM/plan docs | Today's topic, format, and pillar assignment per account |
| **Founder schedule** | The list of founder accounts + each founder's plan | A founder's daily content (raw draft = source; shape into a template) |

## Content Generation Workflow

```
1. IDENTIFY  → Which account? (org / one of the founder accounts)
              → Which platform? (LinkedIn / X / Instagram / profile copy)
              → What's the topic/format? (from the content plan or user request)

2. SELECT    → Map the requested format to a template number via the Quick Template
              Picker (e.g. Vulnerable Story → Template 8)
              → Load that template's full structure (the body with placeholders)
              → Template defines the skeleton; the plan/raw draft provides the story

3. GENERATE  → Fit the raw story INTO the template structure — adapt the template,
              never fill-in-the-blank
              → Keep the template's flow (e.g. Template 8: achievement + hardest →
              When I had → And honestly? → So here's what I did → Three things I
              know → That's it)
              → Apply human-voice rules: specific details, casual connectors, short
              sentences, one imperfect moment
              → If the account is a founder (or the post introduces a founder), apply
              the Founder Personal Touch Protocol below before finalizing
              → Length: 800–1,500 chars LinkedIn story, 200–280 chars X

4. DESIGN    → Write a 1–2 line design brief (see Design Brief Format)
              → For vulnerable/story posts: often "No graphic — text-only"

5. VALIDATE  → Run the Human Check (mandatory). If any check fails, rewrite first.

6. TARGET    → ICP tier (from the org's ICP tiers) + value pillar (from positioning /
              content pillars)
```

## LinkedIn Growth Engine (mandatory for growth posts)

For LinkedIn growth-oriented content (lead gen, authority, inbound), apply this
4-part system:

1. **Positioning first**: state who you help, what problem you solve, and how you
   deliver — pull these from the organization's brand promise and differentiators.
2. **Content as magnet**: prioritize proof posts and lead-magnet posts over generic
   tips.
3. **Warm messaging only**: convert from post engagement, profile views, followers,
   and connection requests. Avoid cold-pitch behavior.
4. **Repel to attract**: use a clear POV so wrong-fit people self-filter out.

### Hook Rules (non-negotiable for LinkedIn)

- First line should be short and punchy (target ≤ 59 characters).
- Include one high-intent keyword early — pull candidate keywords from the
  organization's key messages and content pillars (e.g. the org's domain terms,
  roles, or outcomes), not a fixed list.
- Open with one of these: hard claim, sharp contradiction, costly mistake, or
  concrete result.

### CTA Rules (comment-first default)

Every LinkedIn post must end with a specific engagement CTA. Default to comments:

- "Agree or disagree?"
- "Comment 1/2/3 and I will share what to fix first."
- "What is your biggest blocker right now?"

Do not ship a final draft without an explicit CTA line.

## Founder Personal Touch Protocol (mandatory)

Apply this whenever the post is for one of the founder accounts, or when an org post
introduces a founder:

1. **Start from a real human note first**: capture 2–4 lines from founder input
   (voice note, chat lines, bullets, or memory) before drafting.
2. **Use first-hand perspective**: include at least one line that sounds lived —
   e.g. "I've seen…", "One thing I learned…", "What stood out to me…".
3. **Anchor one concrete detail**: name, moment, context, year, or specific behavior
   (not generic praise).
4. **Avoid polished corporate praise**: no generic "visionary leader" lines unless
   backed by a specific example.
5. **Humanize sentence rhythm**: keep one slightly imperfect or conversational
   sentence; do not over-sanitize.
6. **Run the Founder Authenticity Gate**: if any gate item fails, rewrite first.

### Founder Authenticity Gate (pass/fail)

- [ ] Sounds like a person who knows the founder personally, not a brand intern
- [ ] Includes one specific lived detail (moment/behavior/lesson)
- [ ] Uses natural language (no AI-buzzword polish)
- [ ] Could be said in a real conversation without sounding scripted
- [ ] Each founder's distinct voice is preserved (use the founder's voice note)

### Template Mapping (requested format → copy template)

| Requested format | Template | Structure to use |
|------------------|----------|------------------|
| Vulnerable Story / Founder Journey / "Personal story" | **Template 8** (Achievement That Almost Didn't Happen) | Hook (achievement + hardest) → When I had (→ bullets) → And honestly? → So here's what I actually did (→ bullets) → Three things I know for sure now (→ bullets) → That's it. No hack. |
| Contrarian / Hot Take | #5, #9, #6 | Load from the copy playbook |
| Myth Buster | #14, #5, #9 | Load from the copy playbook |
| Poll / Engagement | #12, #1 | Load from the copy playbook |
| Other | Quick Template Picker | Match content type → template → load structure |

## The Human Check (mandatory)

Before outputting ANY copy, validate against these 6 checks:

| # | Check | If Fail → |
|---|-------|-----------|
| 1 | Read it out loud — does it sound like a real person? | Rewrite with casual connectors, shorter sentences |
| 2 | At least ONE specific detail (name, number, place, year)? | Add a real reference point |
| 3 | Would you send this as a WhatsApp to a smart friend? | Cut the formality, make it direct |
| 4 | At least one imperfect, casual, or raw moment? | Add "Honestly," or an incomplete thought |
| 5 | Does the first line stop the scroll? | Rewrite the hook — punchier, more specific |
| 6 | FREE of dead words? | Kill the dead words (see below) |

## Dead Words (never use in output)

These are universal corporate-cliché killers. Always add the organization's own
words-to-avoid list on top of this baseline.

| Dead Word | Replace With |
|-----------|-------------|
| "Leverage" | "Use" or remove |
| "Unlock" | "Find" / "Build" / "Get" |
| "Game-changer" | Say what actually changed |
| "In today's fast-paced world" | Delete. Start with the point. |
| "Let's dive in" | Delete. Just start. |
| "Synergy" / "Holistic" / "Paradigm" | Normal words |
| "I'm thrilled to announce" | "We just did [thing]" |
| "Excited to share" | Just share it |

## Design Brief Format

Every post that needs a visual gets this brief. Pull palette tokens from the brand
palette — never hardcode hex values or palette names.

```
DESIGN BRIEF: [Visual type] | [Key text/quote] | [Mood/style]
Palette: <brand primary> / <brand accent> / <brand light> / <brand dark>
```

## Brand block (default "who is this org" line)

When content needs a one-line "who we are", build it from the organization's identity
and positioning — do not hardcode it:

```
<org name> — <org descriptor>
<brand promise>
<brand tagline>
```

Short version (for bios, email footers):
```
<org name> | <short descriptor> | <brand tagline>
```

## Quick Template Picker

| Content Type | Best Templates | Platform |
|-------------|---------------|----------|
| Founder Story | #3, #8, #4 | LinkedIn |
| Contrarian / Hot Take | #5, #9, #6 | LinkedIn, X |
| Educational | #10, #15, #11 | LinkedIn |
| Myth Buster | #14, #5, #9 | LinkedIn, X |
| Engagement | #12, #1 | LinkedIn |
| Credibility | #7, #13, #3 | LinkedIn |
| Vulnerability | #8, #3, #12 | LinkedIn |
| Quick X Post | #5, #9, #6 | X |
| Signature theme (org's #1 message) | Use the organization's signature key message as a recurring hook | LinkedIn, X |
| Product Launch / 0-to-Launch | #7 + a "before/after" pattern | LinkedIn |
| Reel Script | No template — conversational, 30s, one point | Instagram |

## Output Format

Every content generation must include:

```markdown
## [Account] — [Platform] — [Date]

### Copy
[The actual post text]

### CTA
[Comment-focused CTA line]

### Design Brief
DESIGN BRIEF: [brief]

### Human Check
- [x] Sounds human: [yes/no + note]
- [x] Specific detail: [what detail]
- [x] WhatsApp test: [pass/fail]
- [x] Imperfect moment: [where]
- [x] Scroll-stopping hook: [first line]
- [x] Dead words: [clean/flagged]

### Targeting
- ICP Tier: [from the org's ICP tiers]
- Value Pillar: [from positioning / content pillars]
```

## Anti-Patterns

| Don't | Do Instead |
|-------|-----------|
| Write post copy without a template | Map format → template (e.g. Vulnerable Story → #8), load structure, fit raw draft into it |
| Fill templates robotically | Adapt structure, keep template flow; use the plan/raw draft for story and specifics |
| Use any dead word | Replace with specific, human alternatives (add the org's words-to-avoid list) |
| Output without the Human Check | Always validate before presenting |
| Write copy that works for "any company" | Make it specific to the org's / founder's real experience (use the decided brand inputs) |
| Write founder intros as polished generic bios | Write founder intros as personal narratives with specific moments |
| Post without a comment CTA | End with a specific comment-focused question or prompt |
| Treat LinkedIn like resume content | Use positioning + proof + CTA to drive inbound conversations |
| Ignore the design brief | Always include one (or "No graphic" when strategy says so) |
| Skip ICP/value targeting | Every post maps to an ICP tier and a value pillar |
| Hardcode key messages, pillars, palette, or a tagline | Resolve them from the decided brand inputs |

> **Full template library, before/after transformations, and design-brief patterns**: load [`reference.md`](reference.md)
> **Intake questions, checklists, and output forms**: load [`forms.md`](forms.md)

> Voice, message, pillar, and palette values are decided per organization (see
> [`ADAPT.md`](ADAPT.md)). This skill stays portable across organizations — only the
> decided inputs change.
