# Start Here

Use this guide when you are sharing Xyric Frameworks with a teammate or setting it up in another project.

This repo is a library of reusable AI work assets. It is not something to install wholesale into every project. Pick the smallest useful piece, copy or install that piece, and adapt only when the skill or framework asks for project context.

## What Is In This Repo

| Folder | Use it when | What you do |
|--------|-------------|-------------|
| `SKILL-BANK/` | You want a reusable AI skill for Claude or Codex. | Browse the list, then install selected skill IDs into a target project. |
| `REFERENCES/` | You need a reusable decision guide, standard, or tech-stack reference. | Read only the matching reference and apply its default or approved choices. |
| `WORKFLOW/` | You want a workflow system for planning, verification, handoff, and repeatable AI-assisted work. | Copy `WORKFLOW/forgeflow` into a target project as `framework/`. |
| `CREATIVES/` | You want a lightweight way to track design references, inspiration, assets, and usage notes. | Copy the index template or follow the folder model. |

## What To Install

Choose by need:

| Need | Install or copy |
|------|-----------------|
| A specific writing, planning, design, research, or operations capability | One or more selected skills from `SKILL-BANK/skills/`. |
| A default tool choice or technology decision | A selected document from `REFERENCES/`, such as `REFERENCES/technology/Xyric-Tech-Stack.md`. |
| A repeatable project workflow for AI agents and humans | `WORKFLOW/forgeflow` copied as `framework/` in the target project. |
| A creative reference library | `CREATIVES/creatives-index.template.yaml` copied into your project or workspace. |
| Everything in this repo | Do not do this by default. Browse first and select what helps the current project. |

## Prerequisites

No package manager install is required for normal use.

You only need:

- `bash`, `cp`, and standard shell tools for copying and installing assets.
- `python3` only when running contribution checks such as the leak gate.
- Claude or Codex if you want installed skills to be available to those agents.
- `git` if you are contributing changes back to this repo.

## Browse Available Skills

From the root of this repo:

```bash
SKILL-BANK/tools/skill-bank list
```

Read the output and choose the specific skill IDs you need, such as `MKT-03` or `EXPERT-11`.

Avoid category installs unless the project truly needs a full domain. The installer refuses `all` installs on purpose.

## Install Skills Into A Project

Install one skill into Claude:

```bash
SKILL-BANK/tools/skill-bank install MKT-03 --target claude --repo /path/to/your-project
```

That copies the selected skill to:

```text
/path/to/your-project/.claude/skills/
```

Install one skill into Codex:

```bash
SKILL-BANK/tools/skill-bank install EXPERT-11 --target codex --repo /path/to/your-project
```

That copies the selected skill to:

```text
/path/to/your-project/.agents/skills/
```

If you need to replace an existing installed copy, add `--overwrite`:

```bash
SKILL-BANK/tools/skill-bank install EXPERT-11 --target codex --repo /path/to/your-project --overwrite
```

After installing, open the target project in Claude or Codex and ask for the skill by name or let the agent use it when the task matches. The agent should read the installed `SKILL.md` first. If the skill includes `ADAPT.md`, use it only when project-specific output is needed.

## Adopt ForgeFlow

ForgeFlow is the workflow framework in `WORKFLOW/forgeflow/`. It should travel as a self-contained folder named `framework/` inside the project using it.

For a new project:

```bash
cp -R WORKFLOW/forgeflow /path/to/your-project/framework
cd /path/to/your-project
cp -R framework/starter/. .
```

Then follow:

```text
framework/START-HERE.md
```

For an existing project, copy in `framework/` first, then use the adoption workflow in `framework/START-HERE.md`. Do not overwrite existing project guidance without merging it carefully.

## Use The Creatives Folder

`CREATIVES/` is an index-first reference system. It is best for tracking inspiration, examples, design references, source URLs, license notes, and usage notes.

Start by copying:

```text
CREATIVES/creatives-index.template.yaml
```

Use it to create a project-local `creatives-index.yaml`. Keep heavy files such as screenshots, decks, fonts, and brand assets in Drive or another asset store. Keep attribution and license notes with each reference.

## Adaptation Rules

Skills use three adaptation tiers:

| Tier | Meaning |
|------|---------|
| `generic` | Use as-is. |
| `optional-adapt` | Works neutrally; add project context only when it improves the work. |
| `needs-adapt` | Read `ADAPT.md` before tailored use. Do not invent brand, workflow, audience, client, or policy specifics. |

For team use, the safest pattern is:

1. Install only the skill or workflow you need.
2. Read the asset's own `README.md`, `START-HERE.md`, or `SKILL.md`.
3. Adapt inside the target project, not in the public source copy, unless the improvement is portable.
4. Keep private names, client data, secrets, and personal paths out of this repo.

## Team Sharing Checklist

Before sharing this repo or a copied framework folder with a teammate:

- Point them to this `START-HERE.md` first.
- Tell them which folder they need: `SKILL-BANK/`, `WORKFLOW/`, or `CREATIVES/`.
- Give them the exact skill IDs or workflow command to use.
- Remind them not to install every skill.
- Confirm whether they are using Claude, Codex, or both.
- For ForgeFlow, confirm whether their project is new or existing before they copy starter files.

## Contribution Checks

After skill edits:

```bash
python3 SKILL-BANK/tools/leak-gate.py --strict SKILL-BANK/skills
SKILL-BANK/tools/skill-bank list
```

After registry or installer edits:

```bash
SKILL-BANK/tools/skill-bank list
```

For ForgeFlow changes, read `WORKFLOW/FORGEFLOW-SOURCE.md` and `WORKFLOW/forgeflow/CONTRIBUTING.md` before editing the vendored framework.

## Troubleshooting

If a skill does not install:

- Check that the target project path exists.
- Run `SKILL-BANK/tools/skill-bank list` and verify the skill ID.
- Use a specific ID such as `MKT-03`, not `all`.
- Use `--allow-category` only when intentionally installing a whole domain.

If ForgeFlow feels like too much for a small task, use one selected skill instead. ForgeFlow is for projects that need planning, verification, handoff, and durable workflow memory.

If a teammate is choosing tools for a Xyric software project, start with `REFERENCES/technology/Xyric-Tech-Stack.md`. Any `Decision needed` rows should be resolved before implementation starts.

If a teammate is unsure where to begin, ask what they are trying to do:

- "I need a capability" means start with `SKILL-BANK/`.
- "I need a project workflow" means start with `WORKFLOW/forgeflow/`.
- "I need references or examples" means start with `CREATIVES/`.
