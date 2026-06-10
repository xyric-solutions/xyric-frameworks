---
name: Supermemory
description: Claude Code plugin for persistent AI memory across sessions. Automatically captures conversation signals and makes them retrievable in future sessions — user preferences, architecture decisions, past work context. Requires Supermemory Pro subscription and API key.
tier: needs-credentials
status: ready
origin: community — supermemoryai/claude-supermemory
install-url: https://github.com/supermemoryai/claude-supermemory
---

# Supermemory

Persistent memory plugin for Claude Code. Captures what matters from each session (decisions, patterns, architecture notes, preferences) and retrieves relevant context automatically in future sessions. Extends Claude's built-in memory (which is project-local and manual) with a searchable, cross-session, cross-project memory store.

## Philosophy

Claude Code's native memory system (`~/.claude/projects/*/memory/`) is manual and local. Supermemory adds a server-backed layer: the agent extracts signals from conversations automatically, stores them with semantic indexing, and surfaces relevant memories at the start of future sessions without prompting. Team memories can be shared across engineers on the same project.

## When to Use

Install on every machine where Claude Code runs (requires Pro subscription). Especially valuable for:
- Long-running projects where context accumulates across many sessions.
- Teams where multiple engineers work on the same codebase — shared project memory reduces onboarding friction.
- Users with strong preferences (tool choices, code style, workflow patterns) they don't want to re-explain.

## Install (Global — once per machine)

**Step 1 — Get an API key:**
Sign up at [app.supermemory.ai](https://app.supermemory.ai) (Pro or above required). Copy your API key (`sm_...`).

**Step 2 — Install the plugin:**
```bash
claude plugin marketplace add supermemoryai/claude-supermemory
claude plugin install claude-supermemory@supermemory-plugins
```

**Step 3 — Set the API key:**
```bash
export SUPERMEMORY_CC_API_KEY="sm_..."
```

Add that export to `~/.zshrc` or `~/.bashrc` so it persists across terminal sessions.

**Step 4 — Restart Claude Code.**

## Commands

| Command | Description |
|---------|-------------|
| `/claude-supermemory:index` | Index the current codebase architecture and patterns into memory |
| `/claude-supermemory:status` | Show auth status and memory stats |
| `/claude-supermemory:session` | Show clickable URL for the current session document |
| `/claude-supermemory:project-config` | Configure per-repo memory settings |
| `/claude-supermemory:logout` | Clear saved credentials |

## How It Works

- **Auto-capture** — At session end, conversations are saved to your Supermemory store.
- **supermemory-search** — Ask Claude about past work; it searches your memory store.
- **supermemory-save** — Explicitly save something: "save this architecture decision."
- **Team memory** — Project knowledge is shared across team members (same API key or team plan).

## Configuration

Global settings at `~/.supermemory-claude/settings.json`:

```json
{
  "maxProfileItems": 5,
  "signalExtraction": true,
  "signalKeywords": ["remember", "architecture", "decision", "bug", "fix"]
}
```

## Success Criteria

- [ ] `SUPERMEMORY_CC_API_KEY` is set and `claude-supermemory:status` shows authenticated
- [ ] First session indexed via `/claude-supermemory:index`
- [ ] Future sessions show relevant past context surfaced automatically

## Notes

- Supermemory Pro or above is required — the free tier does not include the Claude Code plugin.
- Works alongside Caveman (AITOOLS-01) and RTK (AITOOLS-02) — orthogonal concerns (input context richness vs. token cost).
- The MCP endpoint is `https://mcp.supermemory.ai/mcp` — can also be added directly to MCP clients without the plugin.
