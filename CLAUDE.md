# CLAUDE.md

This repo is a public library of reusable AI work assets. It is not a product repo and it should not be copied into a project wholesale unless the user explicitly wants that.

## How To Use This Repo

1. Choose the smallest relevant subset.
2. For skills, read the selected skill's `SKILL.md`.
3. For references, read only the document needed for the current decision.
4. Read `ADAPT.md` only for selected skills that need project-specific context.
5. Do not invent brand, workflow, client, audience, or policy details.
6. Do not create profiles, central org schemas, or personal setup layers.
7. Treat creative references as inspiration with attribution, not as assets to copy blindly.
8. Treat `WORKFLOW/forgeflow/` as a self-contained method. If adopting it, copy it into the target project as `framework/`.

## Skill Selection

Use `SKILL-BANK/tools/skill-bank list` before installing skills. Install one or a small set:

```bash
SKILL-BANK/tools/skill-bank install EXPERT-11 --target claude --repo /path/to/project
```

Tiers:

- `generic`: use as-is.
- `optional-adapt`: works neutral; can be tailored.
- `needs-adapt`: read `ADAPT.md` before tailored use.

## Contribution Checks

After skill changes:

```bash
python3 SKILL-BANK/tools/leak-gate.py --strict SKILL-BANK/skills
SKILL-BANK/tools/skill-bank list
```
