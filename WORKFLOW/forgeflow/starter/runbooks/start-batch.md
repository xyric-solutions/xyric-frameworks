# Forgeflow Runbook: Start Batch

## Required Context

- Founding brief and source hierarchy.
- `_progress.md`, current batch plan, and previous batch closeout.
- Nearest lane `AGENTS.md` and relevant shared canon.
- Open findings, deferred decisions, accepted improvements, blockers, drift, and waivers.

## Steps

1. Confirm active lane, active root, batch ID, batch scope, item list, and session cap.
2. Check prerequisites: required sources exist, blockers are resolved or waived, and the worktree cautions are understood.
3. Create or update the batch file from `framework/templates/batch-template.md`.
4. Record item locators, source links, owners, expected evidence, verify command, and closeout checklist.
5. Mark the batch `in progress` in `_progress.md`.
6. State the first item and the stop condition before implementation or review begins.

## Expected Output

- A concrete batch artifact with real item IDs, locators, owners, evidence targets, verify commands, and closeout criteria.

## Quality Bar

- The batch is small enough to finish and verify in one bounded session.
- Every item traces to an active source, not an archived or superseded doc.
- There is exactly one active next step.

## Persistence / Closeout

- Save the batch artifact and update `_progress.md`.
- Note any unresolved blocker in `findings-ledger.md` or `deferred-decisions.md`.

## Stop Conditions

- Stop if the batch crosses lanes or roots.
- Stop if required sources disagree and the source hierarchy does not resolve the conflict.
- Stop if the batch cannot be verified deterministically.
