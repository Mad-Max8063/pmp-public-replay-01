# PMP public replay instructions

This repository uses PMP Core `0.2.1`.

Canonical memory: repository-root `PROJECT_MEMORY.md`

Before acting, read `PROJECT_MEMORY.md`, `TASK.md`, and the exact next action.
Use only this repository and the current short human prompt. Do not import
context from another repository or conversation.

## Phase contract

- If the next action names **Fresh ChatGPT session**, translate the requirements
  in `TASK.md` into canonical active decisions. Modify only
  `PROJECT_MEMORY.md` and a new `evidence/01-chatgpt-decision.md`. Do not modify
  code, tests, `TASK.md`, the verifier, workflow, or protocol provenance. Do
  not claim the acceptance tests pass. Commit those two paths atomically and
  push only when the next action explicitly authorizes it.
- If the next action names **Codex**, implement only `normalize_status.py` from
  the active decisions. Do not modify tests, `TASK.md`, existing evidence, the
  verifier, workflow, or protocol provenance. Run
  `python -m unittest -v test_normalize_status.py` and
  `python verify_replay.py`; update `PROJECT_MEMORY.md`; create exactly one
  `.project-memory/sessions/YYYY-MM-DD-codex-normalize-status.md`; then commit
  the three allowed paths atomically and push only when authorized.
- If the next action names **Fresh ChatGPT verifier**, reconstruct the handoff
  from repository history and exact CI evidence. Modify only
  `PROJECT_MEMORY.md` and a new `evidence/03-chatgpt-verification.md`. Do not
  modify implementation, tests, `TASK.md`, existing evidence, sessions, the
  verifier, workflow, or provenance. Commit those two paths atomically and
  push only when the next action explicitly authorizes it.
- If the next action names **Human authority**, stop after reporting the
  verified repository state. Do not make changes.

Source precedence: latest authorized human instruction -> current verified
evidence -> `PROJECT_MEMORY.md` -> specialized documentation -> session history
-> private model memory.

Never store secrets, credentials, `.env` values, private conversation text, or
unnecessary personal data.
