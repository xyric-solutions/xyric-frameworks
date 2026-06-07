# Contributing

Thanks for improving Xyric Frameworks. The goal is a practical public library that people and AI agents can use without carrying private assumptions into their own projects.

## What Belongs Here

- Portable skills that teach a method, workflow, or role.
- Instructions for adapting a skill to a team, brand, workflow, or project.
- Portable reference documents for reusable standards, decision guides, and technology choices.
- Creative reference indexes and contribution patterns.
- Workflow material that helps teams run AI-assisted work more reliably.

## What Does Not Belong Here

- Client names, private proposals, secrets, personal data, or internal-only paths.
- Profiles, personal setup folders, or central org configuration systems.
- Large binary assets committed to git.
- Skills that only work for one private company or one private repo.

## Adding Or Updating A Skill

1. Add the skill under `SKILL-BANK/skills/<domain>/<skill-id>-<slug>/`.
2. Include `SKILL.md`.
3. Include `ADAPT.md` when the skill needs brand, audience, workflow, policy, or project-specific choices.
4. Keep optional deep material in `forms.md` or `reference.md`.
5. Update `SKILL-BANK/registry.yaml` and `SKILL-BANK/REGISTRY.md`.
6. Run:

```bash
python3 SKILL-BANK/tools/leak-gate.py --strict SKILL-BANK/skills
SKILL-BANK/tools/skill-bank list
```

## Skill Quality Bar

A good public skill:

- Says when to use it and when not to use it.
- Keeps methodology separate from organization-specific content.
- Avoids placeholders in normal output unless it clearly labels a generic draft.
- Explains what to adapt instead of inventing missing context.
- Can be copied into Claude or Codex without needing the rest of this repo.

## Creative References

Use `CREATIVES/creatives-index.template.yaml` as the shape. Every reference should include:

- title
- type
- source URL or source note
- license or usage status
- attribution
- tags
- why it is useful
- usage notes

Store heavy files in Google Drive or another asset store and reference them from the index.

## Workflow Changes

ForgeFlow is vendored under `WORKFLOW/forgeflow/`. When updating it:

1. Prefer syncing from the upstream ForgeFlow repo.
2. Update `WORKFLOW/FORGEFLOW-SOURCE.md` with the source commit.
3. Preserve the self-contained folder assumptions unless there is a deliberate versioned change.
4. Run the portability check before opening a PR.

## Pull Request Checklist

- [ ] No secrets, private paths, private clients, or personal data.
- [ ] `SKILL-BANK/registry.yaml` matches skill folders.
- [ ] `SKILL-BANK/tools/skill-bank list` works.
- [ ] Leak gate passes for skill changes.
- [ ] Heavy creative assets are not committed to git.
- [ ] Docs explain what changed and why.
