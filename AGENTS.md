# AGENTS.md

This repo is a public library of reusable AI work assets. It is not a product repo and it is not a full operating system that should be copied wholesale.

## Core Rules For AI Agents

1. Select only the skills, references, or workflow files that are useful for the current task.
2. Do not bulk-load or install every skill.
3. For a chosen skill:
   - Read `SKILL.md` first.
   - Read `ADAPT.md` only when the skill has one and the project needs tailored output.
   - Load `forms.md` or `reference.md` only when the skill points to them for the task.
4. Respect adaptation tiers:
   - `generic`: use as-is.
   - `optional-adapt`: works neutral; ask for or infer context only when it materially improves the work.
   - `needs-adapt`: do not invent brand, workflow, audience, client, or policy specifics. Use `ADAPT.md`.
5. Treat `CREATIVES/` as inspiration and reference material, not as a license to copy assets or UI exactly.
6. Treat `WORKFLOW/forgeflow/` as a self-contained framework folder. When adopting it into a project, copy it as `framework/` unless the target project deliberately changes the assumptions.
7. Do not create profile systems, central org schemas, or personal configuration layers in this repo.

## Folder Map

| Folder | Agent behavior |
|--------|----------------|
| `SKILL-BANK/` | Search/list first; install selected skills only. |
| `REFERENCES/` | Read only the reference needed for the task. Treat defaults as binding and unresolved decisions as questions, not guesses. |
| `CREATIVES/` | Use indexes and notes to find references. Preserve attribution and usage notes. |
| `WORKFLOW/` | Use ForgeFlow for project workflow adoption, verification, handoff, and capability building. |

## Before Contributing

- Run `python3 SKILL-BANK/tools/leak-gate.py --strict SKILL-BANK/skills` after skill edits.
- Run `SKILL-BANK/tools/skill-bank list` after registry or installer edits.
- Keep docs ASCII unless the source file already uses non-ASCII.
- Keep public docs free of private paths, secrets, client material, and personal data.
