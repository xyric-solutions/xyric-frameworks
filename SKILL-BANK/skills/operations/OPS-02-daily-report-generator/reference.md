# Daily Report Generator — Reference

Deep reference for author normalization and the HTML dashboard. File paths are
organization-specific decisions (see [`ADAPT.md`](ADAPT.md)); the patterns below are
structural and portable.

---

## Workspace inputs this skill consumes

| Input | What it is |
|-------|-----------|
| Progress doc filename | file that records decisions/blockers per area |
| Work-queue filename | file holding the execution queue + item status |
| Areas root | folder glob where those files live, one per project/area |
| Team registry | author/team registry (names, ids, git aliases, emails) |
| Report templates | folder with report templates (optional; inline if absent) |

Decide these per organization (see [`ADAPT.md`](ADAPT.md)). If one is undecided, treat it
as unanswered — fall back to a labeled placeholder / inline generation.

---

## Git author normalization logic

Normalize each raw git author/email against the team registry in four steps, in order.
Stop at the first match.

```
Input: a raw author handle or email from `git log`
       (e.g. "j-doe" or "j.doe@example.com")

1. Check declared git aliases in the team registry
   -> handle "j-doe" listed under member "Jane Doe".git_aliases
   -> Return "Jane Doe"

2. If not found, extract the email username and match registry emails
   -> "j.doe" from "j.doe@example.com"
   -> matches the email recorded for "Jane Doe"
   -> Return "Jane Doe"

3. If still not found, try name-contains
   -> raw name contains a registry member's first/last name
   -> Return that member's canonical name

4. Fallback
   -> Return "<raw-author> (external)"
```

If your team registry is undecided or the file is missing, skip steps 1–3 and tag every
author `(external)`.

---

## HTML dashboard components

| Component | Data source |
|-----------|-------------|
| Metric cards | Commit count, contributors, projects touched, blocked count |
| Team cards | Registry members with commit counts and avatars/initials |
| Progress bars | Milestone completion read from your progress docs |
| Commit table | Full commit list with conventional-commit type badges |
| Blocked alert | Highlighted alert box for blocked queue items |
| Priorities | Tomorrow's focus items from the work queue |

Use your HTML report template when you have one; otherwise generate the dashboard inline
with the same components. Write the result to the gitignored output directory (default
`reports/daily/YYYY-MM-DD.html`) — never commit rendered reports.

---

## Conventional-commit type reference (universal)

These type names are a portable convention, independent of any organization. Parse commit
subjects for them and tally per member.

| Type | Meaning |
|------|---------|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation only |
| refactor | Code change that neither fixes a bug nor adds a feature |
| test | Adding or correcting tests |
| chore | Build process, tooling, or maintenance |

> Workspace inputs are organization-specific decisions (see [`ADAPT.md`](ADAPT.md)). This
> file stays portable across organizations — only those decisions change.
