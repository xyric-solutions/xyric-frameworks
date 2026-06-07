#!/usr/bin/env python3
"""
leak-gate.py — block company/client/personal specifics from entering the skill bank.

Scans EVERY file in a template folder against a deny-list that is part static
(skill-bank/tools/denylist.yaml: brand tokens, product names, service codes) and
part auto-sourced from the surrounding wiki when present (CLIENTS/ directory names
and PROJECTS/team.yaml member names, emails, and git aliases).

  deny  match -> reported and the gate FAILS (exit 1)
  warn  match -> reported only (exit 0), unless --strict (then treated as deny)

Usage:
  python leak-gate.py templates/                 # scan the whole bank
  python leak-gate.py templates/02-marketing/MKT-03-brand-guidelines
  python leak-gate.py --strict templates/        # warns also fail
  python leak-gate.py --list                      # print the resolved deny-list and exit

The script has no hard third-party dependency: it parses denylist.yaml and
team.yaml with light regex, so it works both inside the wiki and after the bank
is lifted into its own repo (where the auto-sources simply won't exist).
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_BANK = os.path.dirname(HERE)

# Files we bother scanning (text only). Everything else is skipped.
TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".sh", ".js",
            ".ts", ".html", ".css", ".csv", ".toml", ".cfg", ".ini", ""}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def find_wiki_root(start):
    """Walk up looking for a dir that has both CLIENTS/ and PROJECTS/team.yaml."""
    d = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(d, "CLIENTS")) and \
           os.path.isfile(os.path.join(d, "PROJECTS", "team.yaml")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def load_denylist():
    """Parse denylist.yaml (deny/warn -> terms/patterns) with light regex."""
    path = os.path.join(HERE, "denylist.yaml")
    deny_terms, deny_pat, warn_terms, warn_pat = [], [], [], []
    if not os.path.isfile(path):
        return deny_terms, deny_pat, warn_terms, warn_pat
    section = subkey = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].rstrip() if not raw.strip().startswith("#") else ""
            if not line.strip():
                continue
            if re.match(r"^(deny|warn):\s*$", line):
                section = line.strip().rstrip(":")
                subkey = None
                continue
            m = re.match(r"^\s{2}(terms|patterns):\s*$", line)
            if m:
                subkey = m.group(1)
                continue
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m and section and subkey:
                val = m.group(1)
                if (val.startswith('"') and val.endswith('"')) or \
                   (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                bucket = {
                    ("deny", "terms"): deny_terms, ("deny", "patterns"): deny_pat,
                    ("warn", "terms"): warn_terms, ("warn", "patterns"): warn_pat,
                }[(section, subkey)]
                bucket.append(val)
    return deny_terms, deny_pat, warn_terms, warn_pat


def autosource_terms(wiki_root):
    """Client names (from CLIENTS/ dir names) + people (from team.yaml)."""
    terms = set()
    if not wiki_root:
        return terms
    clients_dir = os.path.join(wiki_root, "CLIENTS")
    if os.path.isdir(clients_dir):
        for name in os.listdir(clients_dir):
            if name.startswith("CLIENT-"):
                terms.add(name[len("CLIENT-"):].replace("-", " ").strip())
    team = os.path.join(wiki_root, "PROJECTS", "team.yaml")
    if os.path.isfile(team):
        with open(team, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*name:\s*(.+?)\s*$", line)
                if m:
                    full = m.group(1).strip().strip('"').strip("'")
                    terms.add(full)
                    for part in full.split():
                        if len(part) > 3:
                            terms.add(part)          # first/last names too
                m = re.match(r"\s*email:\s*(.+?)\s*$", line)
                if m:
                    terms.add(m.group(1).strip().strip('"').strip("'"))
                m = re.match(r"\s*-\s*([A-Za-z0-9_.+@-]+)\s*$", line)
                if m and "@" in m.group(1):
                    terms.add(m.group(1).strip())
    return {t for t in terms if t}


def compile_term(term):
    """Whole-word, case-insensitive matcher for a plain term."""
    esc = re.escape(term)
    left = r"(?<![\w@])" if term[0].isalnum() else ""
    right = r"(?![\w@])" if term[-1].isalnum() else ""
    return re.compile(left + esc + right, re.IGNORECASE)


def iter_files(target):
    if os.path.isfile(target):
        yield target
        return
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if os.path.splitext(fn)[1].lower() in TEXT_EXT:
                yield os.path.join(root, fn)


def scan(targets, strict=False):
    deny_terms, deny_pat, warn_terms, warn_pat = load_denylist()
    wiki_root = find_wiki_root(targets[0] if targets else ".")
    auto = autosource_terms(wiki_root)
    deny_terms = sorted({t for t in (set(deny_terms) | auto) if t and t.strip()})
    warn_terms = [t for t in warn_terms if t and t.strip()]

    deny_rx = [(t, compile_term(t)) for t in deny_terms] + \
              [(p, re.compile(p, re.IGNORECASE)) for p in deny_pat]
    warn_rx = [(t, compile_term(t)) for t in warn_terms] + \
              [(p, re.compile(p, re.IGNORECASE)) for p in warn_pat]

    deny_hits, warn_hits = [], []
    for target in targets:
        for path in iter_files(target):
            try:
                with open(path, encoding="utf-8", errors="replace") as f:
                    for n, line in enumerate(f, 1):
                        for term, rx in deny_rx:
                            if rx.search(line):
                                deny_hits.append((path, n, term, line.strip()[:120]))
                        for term, rx in warn_rx:
                            if rx.search(line):
                                warn_hits.append((path, n, term, line.strip()[:120]))
            except (OSError, UnicodeError):
                continue

    def show(hits, label):
        if not hits:
            return
        print(f"\n{label} ({len(hits)}):")
        for path, n, term, ctx in hits:
            rel = os.path.relpath(path, SKILL_BANK)
            print(f"  {rel}:{n}  [{term}]  {ctx}")

    print(f"leak-gate: wiki_root={'(none)' if not wiki_root else os.path.relpath(wiki_root, os.getcwd()) if False else wiki_root}")
    print(f"leak-gate: {len(deny_terms)} deny terms ({len(auto)} auto-sourced), scanning {', '.join(targets)}")
    show(deny_hits, "DENY")
    show(warn_hits, "WARN")

    failed = bool(deny_hits) or (strict and bool(warn_hits))
    if failed:
        print(f"\nFAIL: {len(deny_hits)} deny" + (f" + {len(warn_hits)} warn (strict)" if strict else "") + " — not safe for the bank.")
        return 1
    print(f"\nPASS"+ (f" ({len(warn_hits)} warn — review)" if warn_hits else "") + ".")
    return 0


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    strict = "--strict" in sys.argv
    if "--list" in sys.argv:
        deny_terms, deny_pat, warn_terms, warn_pat = load_denylist()
        auto = autosource_terms(find_wiki_root("."))
        print("DENY terms:", sorted(set(deny_terms) | auto))
        print("DENY patterns:", deny_pat)
        print("WARN terms:", warn_terms)
        print("WARN patterns:", warn_pat)
        return 0
    if not args:
        args = [os.path.join(SKILL_BANK, "templates")]
    return scan(args, strict=strict)


if __name__ == "__main__":
    sys.exit(main())
