# Content Copy Engine — Reference

Extended reference: the starter copy-template library, the LinkedIn growth playbook,
before/after transformation patterns, and design-brief patterns by format.

All examples below use **neutral placeholder content** to show structure only. At use
time, replace the placeholder topic, message, and palette with your organization's
decided brand inputs — voice, key messages, content pillars, and palette (see
[`ADAPT.md`](ADAPT.md)). If the organization keeps its own copy playbook, load that as
the source of truth and use this file as a fallback library.

---

## The brand inputs this skill operates on

The skill draws on these decided inputs (see [`ADAPT.md`](ADAPT.md) for how to gather
them):

- **Voice** — tagline, voice attributes, words to avoid.
- **Palette** — primary / accent / light / dark (for design briefs).
- **Positioning** — brand promise; key messages (one is the signature theme);
  differentiators / value pillars; ICP tiers (name + description, no pricing).
- **Content** — 3–5 content pillars; active channels; founder accounts
  (name, angle, voice per founder).

Resolve every concrete topic, message, pillar, account, and color from these decided
inputs. Never embed a specific org's message or example as if it were universal.

---

## LinkedIn Growth Playbook

### 4 pillars for inbound (no hard selling)

1. **Positioning**: who you help + the problem + delivery model (from the brand
   promise and differentiators).
2. **Content trust bar**: content fills know/like/trust over time.
3. **Say what only you can say**: personal insights, lived stories, client-specific
   proof.
4. **Repel to attract**: filter wrong-fit people out early.

### Hook rules that increase distribution

- First line: short and hard-hitting (target ≤ 59 chars).
- Add one keyword signal in the hook (drawn from the org's key messages / content
  pillars).
- Use one of 4 starts:
  - Result claim: "Every week, we…"
  - Contrarian: "Unpopular opinion…"
  - Costly mistake: "Most teams still…"
  - Reality check: "What looks like growth is…"

### CTA endings (comment-first)

Use one clear prompt at the end:

- "Agree or disagree?"
- "Comment 1/2/3 and I will share what to fix first."
- "What is your biggest blocker right now?"
- "Comment 'FRAMEWORK' and I will send the breakdown."

### Warm-message prompt (post-engagers only)

```text
Hey [Name] — are you here mainly for the content, or are you currently solving [core problem] as well?
```

Use only with warm signals: commenter, profile viewer, follower, accepted connection.
The `[core problem]` is the pain in the brand promise / the targeted ICP tier.

---

## Starter copy-template library (structures only)

Use these skeletons when the org has no playbook of its own. Each shows the flow; fill
the specifics from the decided brand inputs and the raw draft. (Numbering matches the
Quick Template Picker.)

| # | Name | Skeleton |
|---|------|----------|
| 1 | Question Hook | Provocative question → tension → your take → comment CTA |
| 3 | Origin / Credibility | Where you started → a turning point → what you do now |
| 5 | Hard vs Simple | "X is supposed to be HARD" → what everyone says → "Actually it's simple" → real steps → reframe |
| 6 | Contrarian | "Unpopular opinion:" → the claim → why the common view is wrong → proof |
| 7 | Proof / Result | Concrete result → how you got it → the principle behind it |
| 8 | Achievement That Almost Didn't Happen | Hook (achievement + hardest) → "When I had" (bullets) → "And honestly?" → "So here's what I actually did" (bullets) → "Three things I know for sure now" (bullets) → "That's it. No hack." |
| 9 | Old Way vs New Way | "The old way:" (bullets) → "The new way:" (bullets) → the shift in one line |
| 10 | Educational / How-To | The problem → the steps (numbered) → the payoff |
| 11 | Framework | Name the framework → its parts → when to use it |
| 12 | Poll / Engagement | Set up two options → ask which → say you'll share results |
| 13 | Case Snapshot | Situation → what changed → measurable outcome |
| 14 | Myth Buster | "X lies the [industry] won't tell you" → each myth → the truth |
| 15 | Listicle | "N things about [topic]" → one line each → CTA |

> Example — Template 5 skeleton, filled with a **placeholder** topic:
>
> ```
> [TOPIC] is supposed to be HARD.
>
> Everyone tells you to:
> → [common advice 1]
> → [common advice 2]
> → [buy an expensive tool]
>
> Nah. It's actually pretty simple:
> → Answer this: "[the one question that matters]"
> → Connect the [inputs] that feed that answer
> → Automate the rest. Move on.
>
> [TOPIC] isn't hard. We've just been overcomplicating it.
> ```
>
> Replace `[TOPIC]` with one of the org's key messages / content pillars.

---

## Before/After transformation patterns

### Founder intro: generic AI tone → personal human tone

**Before (too generic)** — placeholder:
```
Meet [Founder], Co-Founder of [Org].
They bring strategic vision, leadership, and excellence to our mission.
We're excited to have them driving growth and innovation.
```

**After (personal + human)** — placeholder:
```
Meet [Founder] — my co-founder at [Org].

What I respect most is [one specific, observed behavior].
I've watched them [a concrete moment], keep standards high,
and still make people feel heard.

That's a big part of how we build.
You'll hear more from them directly in the coming weeks.
```

**Why this works**:
- Uses first-hand voice ("I've watched…")
- Adds a specific behavior, not abstract praise
- Sounds like a real person, not a template
- Pulls the founder's angle/voice from the founder accounts

---

### Generic AI output → on-brand (Content Copy Engine applied)

**Before (generic AI output)** — note the dead words:
```
In today's fast-paced business world, leveraging [category] solutions
can unlock tremendous value for your organization. At [Org], we're
excited to share how our cutting-edge capabilities help businesses
transform their operations.
```

**After (skill applied)** — placeholder structure:
```
A client told us last week: "[a vivid, specific quote about their real problem]."

That's the gap. Not a [tool] gap — a [translation/decision] gap.

You don't need another [thing]. You need someone to ask: "[the one
question that reframes the problem]."

We asked that at [a real, un-named situation]. [N] weeks later: [a
specific, measurable change].
```

**What changed**:
- Killed: "fast-paced", "leveraging", "unlock", "excited to share", "cutting-edge"
- Added: a specific client quote, a specific outcome, a story
- Made it about the client's problem, not the org's capabilities

---

### Template-robot → adapted template

**Before (filled in robotically)** — placeholder:
```
I asked 10 [role] one question:
"What's the biggest mistake in [domain]?"
Their answers broke my brain a little.
Here's what came back:
```

**After (adapted with personality)** — placeholder:
```
Last month I asked 10 [role] — [a vivid, specific mix of who they were] —
one question:

"[a sharper, more provocative version of the question]"

The answers weren't what I expected. At all.
```

**What changed**:
- Added specificity to who was asked
- Made the question more provocative
- Added a personal reaction

---

## Design-brief patterns by format

Pull palette tokens from the brand palette; never hardcode hex or palette names.

| Post Format | Design Brief Pattern |
|-------------|---------------------|
| **Contrarian Take** | DESIGN BRIEF: Quote card \| "[the punchy claim]" \| Dark bg, bold light text, logo bottom-right |
| **Myth Buster** | DESIGN BRIEF: Numbered list graphic (3 items) \| "[N lies about [topic]]" \| Clean layout, each myth a block, brand colors |
| **Story Hook** | DESIGN BRIEF: No graphic — text-only post performs better for stories |
| **Poll** | DESIGN BRIEF: No graphic — native LinkedIn/X poll |
| **Carousel** | DESIGN BRIEF: 5 slides \| Slide 1: hook, Slides 2–4: one point per slide, Slide 5: CTA + logo \| Brand colors, clean minimal |
| **Before/After** | DESIGN BRIEF: Split comparison card \| Left: "Before" (muted), Right: "After" (bold brand accent) \| Clean numbers |
| **Reel** | DESIGN BRIEF: 30s vertical video \| Fast cuts, subtitles, trending audio, brand-color overlays \| [Scene description] |
| **BTS Photo** | DESIGN BRIEF: Casual phone shot \| No heavy editing — authenticity > polish |

---

## Copy length reference (universal platform facts)

| Platform | Type | Characters | Notes |
|----------|------|-----------|-------|
| LinkedIn | Story/Thought Leadership | 800–1,500 | Medium. Hook in first 2 lines. White space. |
| LinkedIn | Quick Take | 300–600 | Short. Punchy. One idea. |
| X | Tweet | 200–280 | One shot. Make it count. |
| X | Thread | 3–5 tweets, 200–280 each | First = hook. Last = CTA. |
| Instagram | Caption | 150–300 | Short. The reel talks. |
| Design Brief | — | 1–2 lines | Specific, not vague. |

---

## Integration with other skills & strategy docs

| When you need | Load this |
|--------------|-----------|
| Post topic + content details | The org's GTM/content plan (per account) |
| Copy template | The org's copy playbook, or the starter library above |
| ICP tier + messaging angle | The org's positioning (ICP tiers, key messages) |
| Voice rules | A brand-voice skill + the org's brand voice |
| Format diversity check | A content-strategy skill |
| Founder voice specifics | A founder-brand skill + the founder's voice note |
| Visual standards | A brand-guidelines skill + the brand palette |

> All topic, message, pillar, account, and palette values are decided per organization
> (see [`ADAPT.md`](ADAPT.md)). This file stays portable across organizations — only
> the decided inputs change.
