# Skill Bank

Reusable skills for Claude and Codex. Each skill is a portable folder with a `SKILL.md` file and optional supporting docs.

The bank is intentionally not a profile system. People should copy only the skills that help their current work, then adapt those copies to their own project.

## Browse

```bash
SKILL-BANK/tools/skill-bank list
```

## Install Into Claude

```bash
SKILL-BANK/tools/skill-bank install MKT-03 --target claude --repo /path/to/project
```

This copies the selected skill to:

```text
/path/to/project/.claude/skills/
```

## Install Into Codex

```bash
SKILL-BANK/tools/skill-bank install EXPERT-11 --target codex --repo /path/to/project
```

This copies the selected skill to:

```text
/path/to/project/.agents/skills/
```

## Adaptation Tiers

| Tier | Meaning |
|------|---------|
| `generic` | Use as-is. |
| `optional-adapt` | Works neutral out of the box; `ADAPT.md` notes optional enrichment. |
| `needs-adapt` | Read `ADAPT.md` before tailored use. |

If a skill needs context and you do not have it, produce a clearly labeled generic draft instead of inventing specifics.

## Folder Layout

```text
SKILL-BANK/
├── README.md
├── REGISTRY.md
├── registry.yaml
├── skills/
│   └── <domain>/<skill-id>-<slug>/
│       ├── SKILL.md
│       ├── ADAPT.md
│       ├── forms.md
│       └── reference.md
└── tools/
    ├── skill-bank
    └── leak-gate.py
```

## Contribution Checks

```bash
python3 SKILL-BANK/tools/leak-gate.py --strict SKILL-BANK/skills
SKILL-BANK/tools/skill-bank list
```
