# Forgeflow

A reusable, **domain-agnostic** method for getting the most out of AI models on serious work — extracted from the Balencia design build, generalized so it works for design, backend, research, content, or infra. It travels as **one self-contained folder**: copy it into a project and it activates itself.

> **The spine:** Ground → Capture → **Equip** → Reference → Plan & Slice → Build → Verify → Persist.
> **The core lesson:** large undivided tasks break; small, gated, ledgered slices compound quality — and the tools you build once (skills, commands, teams) make every future task start at a higher floor.

## What's here

| Path | What it is |
|------|------------|
| `START-HERE.md` | **One-screen router + file map** — read this first. |
| `FRAMEWORK.md` | **The master document.** Part A = the 8-move method (project-agnostic). Part B = the Balencia pipeline (worked case study, illustrative paths). Part C = on-ramp (§C1), **Capability Engineering** (§C11 — build skills/commands/teams/subagents/hooks/MCP), feedback loops, failure-mode playbook, batch-sizing, ownership, quality mechanics. |
| `templates/` | **Blank** copy-paste scaffolds for every artifact the method uses, with `<PLACEHOLDER>` tokens. Build *new* artifacts from these. |
| `templates/capabilities/` | Blank dual-harness syntax for the Equip layer: Claude `.claude/*`, Codex `.agents/*` / `.codex/*`, hooks, MCP, plugins, and the capability build checklist. |
| `templates/verification-matrix.md` | Blank matrix for mapping change types to deterministic gates, manual review lenses, evidence, and stop conditions. |
| `templates/teams/packs/` | Optional domain reviewer packs for backend/API, frontend/product, AI/data provenance, security/privacy, health/safety, and docs/research. |
| `starter/` | **Working** ready-to-drop payload — copy its contents to a new project's root to activate: self-activating `CLAUDE.md` and `AGENTS.md`, Claude commands, Codex skills, shared `runbooks/`, the `research-first` skill, and committed `memory/`. |
| `verify/portability-check.mjs` | Self-check: scans a project for required Claude/Codex starter files, runbooks, missing handoff sections, stale handoff paths, and unfilled placeholders. |
| `CLAUDE.md` / `AGENTS.md` | Orient agents that open the framework folder itself. |
| `docs/meta/` | Internal meta-docs (Forgeflow's own self-review + the implementation prompt that built v1.0.0). Transparency only — not needed to use it. |
| `VERSION` · `CHANGELOG.md` | Which framework version/method seeded a project. |

## How to use it

**New here?** Read `START-HERE.md` — a one-screen router + a map of every file.

**Reading the method:** start with `FRAMEWORK.md` Part A (the 8 moves), skim Part B (how Balencia did it — illustrative), keep Part C open as the working reference.

**Starting a new project (the on-ramp — see `FRAMEWORK.md` §C1):**

```bash
# 1. From your project root, pull Forgeflow in as a `framework/` folder
#    (one unit: guide + templates + starter payload). Clone or copy — either works:
git clone https://github.com/hamza-xyric/forgeflow.git framework
rm -rf framework/.git            # detach from Forgeflow's history; framework/ now lives in YOUR repo

# 2. Activate the working payload at the project root
cp -R framework/starter/. .

# 3. Run the guided on-ramp — it walks §C1 interactively and writes your artifacts:
#    CLAUDE.md + AGENTS.md → research-first findings → FOUNDING-BRIEF →
#    capability gaps → domain models → ledgers → batch plan → first handoff
/onboard

# 4. Sanity-check that nothing the framework names is left dangling
node framework/verify/portability-check.mjs .
```

> All internal paths assume Forgeflow lives at `framework/` in your project — keep that folder name.

**Adopting an existing mature project:** copy `framework/` into the repo, then use `/adopt-existing-project` in Claude or `forgeflow-adopt-existing-project` in Codex. This workflow merges Forgeflow into existing root `AGENTS.md` / `CLAUDE.md` and preserves local commands, gotchas, test patterns, auth conventions, DB rules, and lane rules.

**Upgrading Forgeflow in a project:** use `/upgrade-framework` or `forgeflow-upgrade-framework`. The runbook compares `framework/VERSION` to upstream, lists changed files, preserves project-local `memory/`, `plans/`, ledgers, and root guidance, and migrates only framework/starter/template improvements.

**Returning to a project:** run `/start-handoff` in Claude, or use the `forgeflow-start-handoff` Codex skill. Both resume from `plans/next-session-handoff.md` (legacy `.claude/plans/next-session-handoff.md` is read only as a fallback).

**Per session (the survivability loop — see §C11):** do *one bounded batch* → run the verify gate → update ledgers/progress/memory → write `plans/next-session-handoff.md` → checkpoint → clear or start fresh.

## The non-negotiables

1. **One self-contained founding brief** before producing anything.
2. **Declare which source wins** when two disagree.
3. **Slice the work** — never "do it all at once."
4. **Gate everything** — automated checks + multi-role review; nothing is done on assertion.
5. **Plan-then-apply** for anything hard to reverse.
6. **Persist state** in git + metadata + ledgers/handoffs/memory — never in chat history.
7. **Truth is the deliverable** — never inflate a grade to show progress.
8. **Build your tooling** — on the 3rd repetition (or when a proven practice is missing), turn it into a skill/command/team instead of hand-crafting it again.

## For teams

Forgeflow is a method, not a dependency — there's nothing to `npm install`. To roll it out:

- **Adopt it per project** with the on-ramp above. Keep `framework/` committed in each project so the method (and its version) travels with the code.
- **Use either Claude or Codex** against the same foundation. Claude uses `CLAUDE.md` + `.claude/commands`; Codex uses `AGENTS.md` + `.agents/skills`; both share `runbooks/`, `memory/`, ledgers, and `plans/next-session-handoff.md`.
- **Improve the method itself** by opening a PR against this repo (branch → change → PR). See `CONTRIBUTING.md`. Bumps follow SemVer in `VERSION` + `CHANGELOG.md`, so any project can trace which version seeded it.
- **License:** MIT — use it freely, internally or publicly.

## Making it yours

Everything in `FRAMEWORK.md` that mentions Balencia (SIA, RPG, 60/30/10, specific file keys) is a *swappable instance*. Keep the structure and the gates; replace the nouns. See `FRAMEWORK.md` §C12 for the swap checklist, and *"What this folder assumes, ships, and expects you to build"* for what travels vs. what you build.
