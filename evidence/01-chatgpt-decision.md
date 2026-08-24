# ChatGPT decision evidence — PMP Public Replay 01

Stage: `chatgpt-decision`
Actor: `ChatGPT`
Date: `2026-08-24`
Verified starting `main`: `69573d2350327400d4c894ffd253beb10644174a`

## Inputs used

This decision stage used only the repository instructions and human-authored
requirements in:

- `AGENTS.md`
- `PROJECT_MEMORY.md`
- `TASK.md`

## Canonical decisions

The human requirements for `normalize_status(value: str) -> str` are resolved
into the following implementation contract for Codex:

1. Preserve the original `value` unchanged for error reporting.
2. For matching, trim outer whitespace and apply Unicode `casefold()`.
3. Collapse each run of whitespace, `_`, or `-` into one word separator before
   alias matching.
4. Return `"todo"` for `todo`, `to do`, or `pending`.
5. Return `"in-progress"` for `in progress`, `inprogress`, `doing`, or `wip`.
6. Return `"done"` for `done`, `complete`, or `completed`.
7. For empty or unsupported input, raise `ValueError` with exactly
   `unsupported status: <repr of original value>`.
8. Use only the Python standard library.
9. Treat `test_normalize_status.py` as the immutable human-authored acceptance
   boundary; do not modify, weaken, replace, or bypass it.

## Stage boundary

This ChatGPT stage is documentation-only. `normalize_status.py` was not
implemented, `test_normalize_status.py` was not modified, and no claim is made
that the seven acceptance tests pass. Actual implementation and executable test
evidence belong to the Codex stage.

Files authorized for this commit are exactly:

- `PROJECT_MEMORY.md`
- `evidence/01-chatgpt-decision.md`

## Exact next action

`Codex: using only this repository and the active decisions in PROJECT_MEMORY.md, implement only normalize_status.py; do not modify test_normalize_status.py, TASK.md, existing evidence, verify_replay.py, the workflow, AGENTS.md, or PMP_SOURCE.md; run python -m unittest -v test_normalize_status.py and python verify_replay.py; update PROJECT_MEMORY.md with only verified results; create exactly one .project-memory/sessions/YYYY-MM-DD-codex-normalize-status.md record; set Last actor to Codex; leave one exact next action for a Fresh ChatGPT verifier; commit exactly normalize_status.py, PROJECT_MEMORY.md, and that one session file atomically and push main.`
