# Xyric Frameworks

Reusable AI work assets for teams and individuals who want better starting points without inheriting someone else's whole operating system.

## Start Here

If you are new to this repo or sharing it with a teammate, read [`START-HERE.md`](START-HERE.md) first. It explains what to use, what to install, how to install selected skills, and how to adopt ForgeFlow in another project.

This repo is intentionally simple:

| Folder | Use it for |
|--------|------------|
| `SKILL-BANK/` | Copy selected skills into Claude or Codex when they are useful for your project. |
| `REFERENCES/` | Read reusable decision guides such as the Xyric tech stack before choosing tools. |
| `CREATIVES/` | Track design inspiration, references, assets, and examples through a lightweight index. Store heavy files in Drive or another asset store. |
| `WORKFLOW/` | Adopt ForgeFlow, a reusable workflow for serious AI-assisted work. |

## Quick Start

Browse before installing anything:

```bash
SKILL-BANK/tools/skill-bank list
```

Install one skill into Claude:

```bash
SKILL-BANK/tools/skill-bank install MKT-03 --target claude --repo /path/to/your-project
```

Install one skill into Codex:

```bash
SKILL-BANK/tools/skill-bank install EXPERT-11 --target codex --repo /path/to/your-project
```

Use ForgeFlow in a project:

```bash
cp -R WORKFLOW/forgeflow /path/to/your-project/framework
cd /path/to/your-project
cp -R framework/starter/. .
```

Then follow `framework/START-HERE.md`.

Use the tech stack reference:

```text
REFERENCES/technology/Xyric-Tech-Stack.md
```

For team onboarding, fuller install notes, and troubleshooting, use [`START-HERE.md`](START-HERE.md).

## How To Think About This Repo

Do not pull everything. Pick the smallest set of skills or workflow pieces that help the current project.

Skills have three adaptation tiers:

| Tier | Meaning |
|------|---------|
| `generic` | Use as-is. |
| `optional-adapt` | Works neutrally, but can improve with project context. |
| `needs-adapt` | Read `ADAPT.md` before tailored use. |

`ADAPT.md` is not a profile system. It is a short note that tells you what your team needs to decide if you want the skill to reflect your brand, workflow, audience, or standards.

## Contributing

See `CONTRIBUTING.md`. The short version:

- Add or update reusable skills only when they are portable.
- Keep private company, client, and personal material out of public skills.
- Store creative files outside git when they are large or licensed assets.
- Improve ForgeFlow through `WORKFLOW/forgeflow` only when the change should travel as part of the method.

## License

MIT. Use it, fork it, adapt it, and improve it.
