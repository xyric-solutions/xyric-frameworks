# Changelog

All notable changes to Forgeflow are recorded here. Versioning follows [SemVer](https://semver.org): **MAJOR** = a breaking change to the method or the artifact layout · **MINOR** = new capabilities/sections · **PATCH** = fixes and clarifications. A project records the version that seeded it (see `VERSION`) so its build is traceable to a method.

## 1.2.0 — 2026-06-07

Existing-project adoption upgrade: Forgeflow now handles mature repos that already have project-specific Claude/Codex guidance, and adds explicit upgrade, verification, memory, domain-review, and docs-drift mechanics.

### Added
- `starter/runbooks/adopt-existing-project.md`, `/adopt-existing-project`, and `forgeflow-adopt-existing-project` for merging Forgeflow into mature projects without overwriting existing root `AGENTS.md` / `CLAUDE.md`.
- `starter/runbooks/upgrade-framework.md`, `/upgrade-framework`, and `forgeflow-upgrade-framework` for comparing versions, preserving project-local truth, and migrating framework/starter/template improvements.
- `templates/verification-matrix.md` with change-type rows for backend/API, frontend/UI, DB migration, docs/framework, AI/data provenance, auth/security, and health/safety.
- Optional domain reviewer packs under `templates/teams/packs/`.

### Changed
- Memory schema now includes `risk_level` and `critical_invariant` conventions for facts future agents must not violate.
- Docs audit guidance now requires active docs, archived docs, and the tie-breaker source, with stronger checks for dated plans/logs being mistaken for live truth.
- Verification runbook now starts from the verification matrix and records manual-review lens, evidence location, and stop-condition status.
- `START-HERE.md`, `README.md`, and team docs now reference the new workflows, matrix, and packs.
- `verify/portability-check.mjs` now includes the new shipped workflows, checks `START-HERE.md` coverage, and scans shipped starter files for placeholders from activated project roots.

## 1.1.0 — 2026-06-07

Dual-harness operations upgrade: Forgeflow now ships useful foundations for both Claude Code and Codex, and the operational artifacts force stronger handoffs, ledgers, verification, and multi-agent review.

### Added
- `starter/AGENTS.md` for Codex repo guidance.
- Codex-native repo skills under `starter/.agents/skills/`, including `research-first` and `forgeflow-*` workflow wrappers.
- Shared `starter/runbooks/` for onboarding, handoff, start-handoff, start-batch, close-batch, docs audit, story planning, work-item creation, and verification.
- Claude command wrappers for the new operational workflows.
- `templates/deferred-decisions.md` and `templates/accepted-improvements.md`.

### Changed
- Canonical handoff path is now `plans/next-session-handoff.md`; `.claude/plans/next-session-handoff.md` is legacy fallback only.
- Handoff, progress, findings, memory, lane, and team templates now require owner, blocked work, next action, closure condition, verification evidence, drift/waiver status, dirty-worktree cautions, and one exact next slice.
- Capability docs now distinguish Claude `.claude/*` from Codex `AGENTS.md`, `.agents/skills/*`, `.codex/hooks.json`, `.codex/config.toml`, and `.codex-plugin/plugin.json`.
- `verify/portability-check.mjs` now checks required dual-harness files, runbooks, handoff sections, stale handoff path references, and placeholders.

## 1.0.1 — 2026-06-04

First **public release**, named **Forgeflow**. Shareability pass — no method changes.

### Changed
- Named the framework **Forgeflow** (was the working title "Production Framework") throughout.
- Moved the internal meta-docs to `docs/meta/` (`IMPLEMENTATION-PROMPT.md`, `REVIEW-AND-RECOMMENDATIONS.md`) and sanitized all machine-specific paths to `<PROJECT_ROOT>` / `<USER_HOME>`.
- Renamed the starter workspace file to the generic `project.code-workspace`.
- `README.md`: on-ramp updated for the standalone-repo flow (`git clone … framework`) and a "For teams" section added.

### Added
- `LICENSE` (MIT), `CONTRIBUTING.md`, and a `.gitignore`.

## 1.0.0 — 2026-05-31

First **portable, self-contained** release. The framework now travels as one folder and activates itself in a fresh project with no dependency on the origin repo's memories, plans, or external `~/.claude/` files.

### Added
- **`starter/` working payload** — copy its contents into a new project's root to activate:
  - `research-first` skill (move A0, generalized from the Balencia `research-first-workflow`).
  - `/handoff` + `/start-handoff` commands (the survivability loop), de-user-pathed to a repo-relative `.claude/plans/next-session-handoff.md` path at the time; newer projects use canonical `plans/next-session-handoff.md`.
  - `/onboard` command — walks the §C1 on-ramp interactively (workspace map → research → founding brief → equip → domain models → ledgers → batch plan).
  - Self-activating `starter/CLAUDE.md` (imports `@memory/MEMORY.md`).
  - Committed `memory/` scaffold — `MEMORY.md` index + frontmatter schema + the `[[name]]` linking convention + four worked example facts.
- **`framework/CLAUDE.md`** — orients an agent that opens the framework folder itself.
- **`START-HERE.md`** — one-screen router + full file-map.
- **`VERSION` + `CHANGELOG.md`** — provenance for a seeded project.
- **`verify/portability-check.mjs`** — dogfoods the verify discipline: scans a project for dangling references the framework names, a missing `CLAUDE.md`, or unfilled placeholders. Exit 0/1. Expanded in 1.1.0 for dual-harness checks.
- `FRAMEWORK.md`: new *"What this folder assumes, ships, and expects you to build"* section.

### Changed
- `FRAMEWORK.md`: repointed the dangling `~/.claude/...`, `/handoff`, and `research-first-workflow` references to the shipped `starter/` copies; labeled Part B's real paths illustrative; updated the §C11.7 memory note and the §C11.1 capability table to the committed-`memory/` + `@import` pattern.
- `README.md`: on-ramp updated to the single-copy `cp -r framework <project>/` + activate + `/onboard` flow.

### Notes
- Model: **copy-the-folder, self-contained** (not a plugin). A deferred plugin-packaging appendix remains optional — see `FRAMEWORK.md` §C11.6.
- The blank `templates/` are unchanged in purpose: they stay scaffolds for building *new* artifacts; `starter/` holds the *working* files. Keep the two separate.

---

_Baseline (pre-1.0.0): the `FRAMEWORK.md` guide + `templates/` were extracted from the Balencia build but referenced capabilities that lived outside the folder. See `docs/meta/REVIEW-AND-RECOMMENDATIONS.md` for the audit that motivated 1.0.0._
