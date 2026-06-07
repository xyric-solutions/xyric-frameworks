# Adapting Story Spec Generator

**What this skill does:** turns a single user story into a complete technical specification
(API contracts, data models, UI components, security, testing, performance) and flags
architecture decisions for review.

This skill is generic methodology — the spec frameworks, question flow, and validation gates
are universal. What is organization-specific is *where* documents live and *how* files and IDs
are named. Decide the values below and either keep them in your working brief at use time, or
bake them into your forked copy of `SKILL.md`. Until they're decided, the skill emits a labeled
GENERIC DRAFT (with `PLACEHOLDER` paths and IDs) rather than inventing a folder layout.

## What to decide for your organization

| Decide | Used in `SKILL.md` under | Notes |
|--------|--------------------------|-------|
| **Products root** — parent path/pattern for per-product documents | Required Context Sources; Phase 4: Output & Tracking; Output | e.g. one subfolder per product. |
| **Doc areas** — folders for stories, epic PRDs, design system, specs, and master requirements doc | Required Context Sources | These are the read sources Phase 0 gathers from. |
| **Planning/status file** — the per-product file you update with architecture decisions and milestones | Required Context Sources; Four-Phase Workflow (Phase 4) | e.g. a progress/status document. |
| **Story ID convention** — how story IDs are formatted | Required Context Sources; Output | e.g. epic.feature.sequence → `S01.01.01`. |
| **Spec filename convention** — how the generated spec file is named | Four-Phase Workflow (Phase 4); Output | e.g. a per-story `Story-[ID]-Spec` document. |
| **Pipeline hook** — the marker that signals downstream tooling the story is ready for tasks | Output | e.g. `<!-- TASKS_READY: [Story ID] -->`. |

## How to gather these

The numbered **Workspace Intake** in [`forms.md`](forms.md) is the questionnaire for all of the
above — ask it once, record the answers wherever your team keeps workspace/naming decisions.

## Platform-independent (do not change)

The Technical Specification template, Quality Checklist, and Activation Checklist in
[`forms.md`](forms.md); the question frameworks, generation steps, and validation gates in
[`reference.md`](reference.md); and the sub-skills (`SPEC-API`, `SPEC-DATA`, `SPEC-UI`) are all
platform-neutral methodology. The 10 spec sections, error-code tables, and responsive viewport
sizes (1440px / 768px / 375px) work as-is for any organization.
