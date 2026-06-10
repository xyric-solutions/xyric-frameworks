---
name: Caveman
description: Claude Code plugin that compresses agent output by ~75% using terse fragment-style responses. Cuts output token cost without sacrificing technical accuracy. Install once globally; auto-activates every session via hook. Use when API costs or context window pressure is high.
tier: ready
status: ready
origin: community — JuliusBrussee/caveman
install-url: https://github.com/JuliusBrussee/caveman
---

# Caveman

Output token compression plugin for Claude Code. Makes the agent respond in dense, no-filler fragments — same technical content, ~75% fewer tokens. "Brain still big. Mouth small."

## Philosophy

LLM output tokens cost money and burn context window space. Most agent verbosity is filler: preambles, restatements, hedge words, transitional phrases. Caveman strips them without removing code, paths, URLs, or technical judgement. The result reads like a senior engineer's Slack message, not a formal writeup.

## When to Activate

**Triggers** (agent detects automatically after install):
- `/caveman` — activate (levels: `lite`, `full` [default], `ultra`, `wenyan`)
- `/caveman-commit` — write conventional commit messages ≤50 chars
- `/caveman-review` — one-line PR comments
- `/caveman-stats` — show session token savings
- `/caveman-compress <file>` — rewrite a memory file (CLAUDE.md, etc.) into caveman-speak (~46% smaller)

Auto-activates on session start via Claude Code hook after installation. No manual trigger needed.

## Install (Global — once per machine)

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

Restart Claude Code after install. The session-start hook activates caveman-speak automatically from message one.

## Verify

```bash
cat ~/.claude/.caveman-active   # should output: full
```

Open Claude Code, type `/caveman`. Response should be terse fragments.

## Levels

| Level | Behaviour |
|-------|-----------|
| `lite` | Drop filler words only |
| `full` | Default caveman mode — fragments, no articles |
| `ultra` | Telegraphic — maximum compression |
| `wenyan` | Classical Chinese prose (shortest of all) |

## Token Savings (Benchmarks)

Average **65% output reduction** across 10 real tasks (range 22–87%). Source: `benchmarks/` in the repo.

## Uninstall

```bash
npx -y github:JuliusBrussee/caveman -- --uninstall
```

## Notes

- Does not affect code blocks, paths, or URLs — those are preserved verbatim.
- `/caveman-compress` on CLAUDE.md or project memory files saves ~46% on every future session start (input token reduction).
- Works alongside RTK (AITOOLS-02) and Supermemory (AITOOLS-03) — different layers.
