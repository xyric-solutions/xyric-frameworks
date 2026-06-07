# START HERE

The **Forgeflow** — a reusable, domain-agnostic method for getting high-quality output from AI models on serious work, plus the working tools to run it. Pick your situation:

| You are… | Do this |
|----------|---------|
| **Starting a new project** | `cp -r framework <project>/`, then from the project root `cp -R framework/starter/. .` to activate the payload, then run **`/onboard`** in Claude or `forgeflow-onboard` in Codex. It writes `CLAUDE.md`, `AGENTS.md`, the founding brief, capability layer, ledgers, and first handoff. |
| **Adopting an existing project** | Copy in `framework/`, activate only missing starter pieces, then run **`/adopt-existing-project`** in Claude or `forgeflow-adopt-existing-project` in Codex. It merges Forgeflow into existing `AGENTS.md` / `CLAUDE.md` and preserves local commands, gotchas, auth, DB, test, and lane rules. |
| **Upgrading Forgeflow** | Run **`/upgrade-framework`** in Claude or `forgeflow-upgrade-framework` in Codex. It compares `framework/VERSION` to upstream, migrates framework/starter/template improvements, and preserves project-local memory, plans, ledgers, and root guidance. |
| **Returning to a project** | Run **`/start-handoff`** in Claude or use `forgeflow-start-handoff` in Codex — both resume from `plans/next-session-handoff.md`. (No handoff? Read `memory/MEMORY.md` and the latest commits.) |
| **Wanting to learn the method** | Read **`FRAMEWORK.md` Part A** (the 8 moves + 13 principles). Skim Part B (the Balencia case study) for a worked example; keep Part C as the working reference. |
| **Building a capability** (skill/command/team/hook/MCP) | Use the blank scaffolds in **`templates/capabilities/`** and the build loop in `FRAMEWORK.md` §C11. |
| **Mid-session, need to stop** | Run **`/handoff`** in Claude or use `forgeflow-handoff` in Codex to distill state into `plans/next-session-handoff.md`, then clear/start fresh. |

> **The model:** the framework is *copy-the-folder, self-contained.* One folder carries the guide, the blank templates, a working starter payload, and a self-check. See `FRAMEWORK.md` → *"What this folder assumes, ships, and expects you to build."*

## The spine (say it out loud)
**Ground → Capture → Equip → Reference → Plan & Slice → Build → Verify → Persist.**
Large undivided tasks break; small, gated, ledgered slices compound — and the tools you build once make every future task start higher.

## File map — every file and when to use it

| Path | What it is | Reach for it when |
|------|------------|-------------------|
| `FRAMEWORK.md` | The master guide: Part A (method) · Part B (Balencia case study) · Part C (mechanics, §C1 on-ramp, §C11 capability engineering). | You want the *why* and the *how* — the canonical reference. |
| `README.md` | Quickstart: the spine, the on-ramp commands, the eight non-negotiables. | You want the short version. |
| `START-HERE.md` | This file — one-screen router + file map. | You just opened the folder. |
| `CLAUDE.md` / `AGENTS.md` | Orient agents that open **the framework folder itself** (vs. a project using it). | Claude and Codex auto-load their respective guidance. |
| `VERSION` | The framework version that seeded a project. | Recording or checking provenance. |
| `CHANGELOG.md` | What changed between framework versions. | Upgrading; auditing what method produced a build. |
| `templates/` | **Blank** `<PLACEHOLDER>` scaffolds for every artifact (`CLAUDE.md`, `AGENTS.md`, founding brief, ledgers, rubric, teams, verify scripts…). | Standing up a new artifact in your project — fill a *copy*, never the template. |
| `templates/capabilities/` | Blank dual-harness syntax for the Equip layer (`SKILL.md`, Claude command, Codex skill notes, hooks, MCP, plugin). | Building a *new* skill/command/subagent/hook/MCP/plugin. |
| `templates/verification-matrix.md` | Blank matrix mapping change types to deterministic gates, manual review lens, evidence, and stop conditions. | Choosing the right verify gates for backend/API, frontend/UI, DB, docs/framework, AI/data provenance, auth/security, or health/safety work. |
| `templates/teams/` | The six generic reviewer-persona briefs plus optional domain packs under `templates/teams/packs/`. | Setting up your verify lane (A6). |
| `starter/` | The **working** payload — copy its contents to your project root to activate. | New project on-ramp (the `cp -R framework/starter/. .` step). |
| `starter/CLAUDE.md` | Self-activating project root: tells a fresh session to read the method and run `/onboard`; imports `@memory/MEMORY.md`. | Becomes your project's root `CLAUDE.md`. |
| `starter/AGENTS.md` | Codex project guidance: reads memory, handoff, source hierarchy, progress, and lane rules before work. | Becomes your project's root `AGENTS.md`. |
| `starter/.claude/skills/research-first/SKILL.md` | The **A0 grounding skill** (Query→Execute→Synthesize→Apply, source rubric). | Any strategic/architectural decision. |
| `starter/.agents/skills/` | Codex-native `research-first` and `forgeflow-*` workflow skills: `onboard`, `adopt-existing-project`, `upgrade-framework`, `handoff`, `start-handoff`, `start-batch`, `close-batch`, `audit-docs`, `plan-story`, `create-work-items`, and `verify`. | Running Forgeflow in Codex. |
| `starter/.claude/commands/` | Claude command wrappers for `onboard`, `adopt-existing-project`, `upgrade-framework`, handoff, batch, docs audit, story planning, work-item creation, and verify. | Running Forgeflow in Claude. |
| `starter/runbooks/` | Canonical workflow instructions shared by Claude commands and Codex skills for `onboard`, `adopt-existing-project`, `upgrade-framework`, `handoff`, `start-handoff`, `start-batch`, `close-batch`, `audit-docs`, `plan-story`, `create-work-items`, and `verify`. | Auditing or extending any workflow. |
| `starter/memory/` | Committed memory scaffold: `MEMORY.md` index + frontmatter schema, critical-invariant convention, and four worked examples. | Persisting durable facts that travel with the repo. |
| `verify/portability-check.mjs` | Self-check: scans a project for required Claude/Codex files, runbooks, handoff sections, stale handoff paths, and unfilled placeholders. | Before trusting a copy; after `/onboard`; in CI. |

## The eight non-negotiables
1. One self-contained **founding brief** before producing anything.
2. **Declare which source wins** when two disagree.
3. **Slice the work** — never "do it all at once."
4. **Gate everything** — automated checks + multi-role review; nothing is done on assertion.
5. **Plan-then-apply** for anything hard to reverse.
6. **Persist state** in git + metadata + ledgers/handoffs/memory — never only in chat.
7. **Truth is the deliverable** — never inflate a grade to show progress.
8. **Build your tooling** — on the 3rd repetition (or when a proven practice is missing), turn it into a skill/command/team.
