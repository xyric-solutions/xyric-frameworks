# ForgeFlow Source

ForgeFlow is vendored into this repo for convenience.

| Field | Value |
|-------|-------|
| Source repo | `https://github.com/hamza-xyric/forgeflow` |
| Imported commit | `07d8ca2b8d96fbc46208d2f45ae69e54c83e94c0` |
| Imported date | `2026-06-07` |
| Source license | MIT |
| Local path | `WORKFLOW/forgeflow/` |

## Update Process

1. Check the latest upstream ForgeFlow commit.
2. Replace `WORKFLOW/forgeflow/` with the upstream contents.
3. Update this file with the new commit SHA and date.
4. Run:

```bash
node WORKFLOW/forgeflow/verify/portability-check.mjs WORKFLOW/forgeflow/starter
```

5. Review `WORKFLOW/forgeflow/START-HERE.md`, `VERSION`, and `CHANGELOG.md`.
6. Commit the update with a clear source note.
