# PMP Public Replay 01 — Project Memory

> Canonical operational memory for a public blind handoff replay.
> Protocol: PMP `0.2.1`
> Canonical path: `PROJECT_MEMORY.md`

## Identity

- Project: `PMP Public Replay 01`
- Repository: `https://github.com/Mad-Max8063/pmp-public-replay-01`
- Human authority: `Matías Maximiliano Bernal / Max Devs Solutions`
- Default branch: `main`
- Last updated: `2026-08-24`
- Last actor: `ChatGPT`

## Current state

- [VERIFIED] `main` was confirmed at baseline
  `69573d2350327400d4c894ffd253beb10644174a` before this ChatGPT stage.
- [VERIFIED] `TASK.md` contains the human-authored requirements for
  `normalize_status(value: str) -> str`.
- [VERIFIED] `test_normalize_status.py` contains seven executable acceptance
  tests and is locked against agent modification.
- [VERIFIED] `normalize_status.py` remains intentionally unimplemented at this
  stage; ChatGPT did not implement it or claim the acceptance suite passes.
- [VERIFIED] The human requirements have been translated into canonical active
  decisions below and recorded in `evidence/01-chatgpt-decision.md`.
- [DOCUMENTED] PMP Core `0.2.1` was adopted from public commit
  `365e48c7b8480f339b622b1f22eb30c8f93a6da8`.

## Active decisions

1. `normalize_status(value: str) -> str` must preserve the original `value`
   unchanged for any error message, while normalization for matching begins by
   trimming outer whitespace and comparing with Unicode `casefold()` semantics.
2. Before alias matching, every run of whitespace, underscores, or hyphens is
   treated as a single word separator.
3. The canonical result `"todo"` is returned for normalized aliases `todo`,
   `to do`, and `pending`.
4. The canonical result `"in-progress"` is returned for normalized aliases
   `in progress`, `inprogress`, `doing`, and `wip`.
5. The canonical result `"done"` is returned for normalized aliases `done`,
   `complete`, and `completed`.
6. Empty or unsupported input must raise `ValueError` with exactly
   `unsupported status: <repr of original value>`.
7. The implementation must use only the Python standard library.
8. `test_normalize_status.py` is the immutable human-authored acceptance
   boundary; Codex must not modify or bypass it.
9. ChatGPT's decision stage is documentation-only. Codex owns implementation
   and actual test execution/evidence. A separate fresh ChatGPT verifier owns
   final reconstruction from Git and CI.
10. Every replay stage must remain one focused, reviewable atomic commit within
    its phase contract.

## Constraints

- Do not paste prior conversation context into either agent session.
- Do not modify implementation or tests during either ChatGPT stage.
- Codex may modify only `normalize_status.py`, `PROJECT_MEMORY.md`, and exactly
  one `.project-memory/sessions/YYYY-MM-DD-codex-normalize-status.md` session
  record during its stage.
- Codex must not modify tests, `TASK.md`, existing evidence, `verify_replay.py`,
  the workflow, `AGENTS.md`, or `PMP_SOURCE.md`.
- Do not weaken, replace, or bypass the human-authored acceptance tests.
- Use only the Python standard library.

## Priorities

1. Hand the canonical decisions to a fresh Codex session without relying on
   hidden or conversational context.
2. Have Codex implement only `normalize_status.py` and record actual execution
   evidence for the acceptance suite and replay verifier.
3. Preserve exact commit and CI evidence for independent ChatGPT verification.

## Next action

`Codex: using only this repository and the active decisions in PROJECT_MEMORY.md, implement only normalize_status.py; do not modify test_normalize_status.py, TASK.md, existing evidence, verify_replay.py, the workflow, AGENTS.md, or PMP_SOURCE.md; run python -m unittest -v test_normalize_status.py and python verify_replay.py; update PROJECT_MEMORY.md with only verified results; create exactly one .project-memory/sessions/YYYY-MM-DD-codex-normalize-status.md record; set Last actor to Codex; leave one exact next action for a Fresh ChatGPT verifier; commit exactly normalize_status.py, PROJECT_MEMORY.md, and that one session file atomically and push main.`

## Evidence

- baseline commit `69573d2350327400d4c894ffd253beb10644174a`
- `TASK.md`
- `test_normalize_status.py`
- `PMP_SOURCE.md`
- `evidence/01-chatgpt-decision.md`
- decision-stage CI for the ChatGPT commit must validate stage
  `chatgpt-decision`; acceptance completion is not asserted at this stage

## Update rules

- Read this file before significant work.
- Update it only when current state, a decision, a constraint, a priority, or
  the next action changes.
- Keep historical implementation detail in `.project-memory/sessions/`.
- Use `[VERIFIED]`, `[DOCUMENTED]`, and `[ASSUMED]` exactly as defined by PMP.
- Resolve conflicts using the source precedence in `AGENTS.md`.
