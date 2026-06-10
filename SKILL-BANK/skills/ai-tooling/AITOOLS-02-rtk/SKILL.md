---
name: RTK (Rust Token Killer)
description: CLI proxy binary that intercepts Bash tool calls (git, npm, cargo, pytest, docker, etc.) and compresses their output before it reaches the LLM context — 60–90% token reduction. Zero-config after install; transparent to the agent. Use on every machine where Claude Code runs.
tier: ready
status: ready
origin: community — rtk-ai/rtk
install-url: https://github.com/rtk-ai/rtk
---

# RTK — Rust Token Killer

Single Rust binary that sits between Claude Code's Bash tool and the shell. When the agent runs `git status`, RTK intercepts, filters, deduplicates, and truncates the output before Claude sees it — 60–90% fewer tokens per command, <10ms overhead.

## Philosophy

A Claude Code session's largest token sink is usually command output: `git diff`, `npm test`, `cargo build`. These commands produce verbose output designed for human terminals, not for LLMs. RTK applies four strategies per command type — smart filtering, grouping, truncation, deduplication — returning a compact version that still conveys all actionable information.

RTK works at the Bash layer, not the Claude layer. The agent doesn't need to know RTK exists; it just receives smaller inputs.

## When to Use

Install on every developer machine that runs Claude Code. This is a zero-configuration persistent improvement — not a situational skill. There is no slash command; savings happen automatically on every session.

Explicitly call `rtk <command>` when you want RTK filtering outside the auto-hook:
- `rtk git diff`
- `rtk read file.rs -l aggressive`
- `rtk grep "pattern" .`

## Install (Global — once per machine)

```bash
# macOS
brew install rtk
rtk init -g          # wires PreToolUse hook into Claude Code settings.json

# Linux / macOS (no Homebrew)
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
rtk init -g
```

Restart Claude Code after `rtk init -g`.

## Verify

```bash
rtk --version        # e.g. rtk 0.42.3
rtk gain             # shows cumulative token savings stats
```

In Claude Code, run any `git status` via the Bash tool — RTK intercepts transparently.

## Token Savings (30-min Session Estimates)

| Command | Standard | RTK | Savings |
|---------|----------|-----|---------|
| `git status` (10×) | 3,000 | 600 | −80% |
| `git diff` (5×) | 10,000 | 2,500 | −75% |
| `npm test` (5×) | 25,000 | 2,500 | −90% |
| `grep/rg` (8×) | 16,000 | 3,200 | −80% |
| `cat/read` (20×) | 40,000 | 12,000 | −70% |
| **Total** | **~118,000** | **~23,900** | **−80%** |

## Important Scope Note

RTK only intercepts **Bash tool calls**. Claude Code's built-in `Read`, `Grep`, and `Glob` tools bypass the hook. For those workflows, use shell equivalents (`cat`, `rg`, `find`) or call `rtk read` / `rtk grep` / `rtk find` directly.

## Uninstall

```bash
rtk init -g --uninstall
brew uninstall rtk
```

## Notes

- Works alongside Caveman (AITOOLS-01) — different layers (input vs. output tokens).
- Config lives at `~/Library/Application Support/rtk/config.toml` (macOS).
- Telemetry is disabled by default; opt-in via `rtk telemetry enable`.
