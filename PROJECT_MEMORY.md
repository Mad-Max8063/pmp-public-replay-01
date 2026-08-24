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
- Last actor: `Human authority`

## Current state

- [VERIFIED] `TASK.md` contains the human-authored requirements for
  `normalize_status(value: str) -> str`.
- [VERIFIED] `test_normalize_status.py` contains seven executable acceptance
  tests and is locked against agent modification.
- [VERIFIED] `normalize_status.py` is intentionally unimplemented and the
  acceptance suite currently fails with `NotImplementedError`.
- [VERIFIED] `python verify_replay.py` recognizes this repository as a valid
  baseline rather than claiming the task is complete.
- [VERIFIED] No ChatGPT decision evidence, Codex session, or final ChatGPT
  verification evidence exists in this baseline.
- [DOCUMENTED] PMP Core `0.2.1` was adopted from public commit
  `365e48c7b8480f339b622b1f22eb30c8f93a6da8`.

## Active decisions

1. A fresh ChatGPT session must translate `TASK.md` into canonical active
   decisions before implementation begins.
2. The first ChatGPT stage is documentation-only; Codex owns implementation.
3. A separate fresh ChatGPT session owns final reconstruction and verification.
4. Every replay stage must be represented by one focused, reviewable commit.

## Constraints

- Do not paste prior conversation context into either agent session.
- Do not modify implementation or tests during either ChatGPT stage.
- Do not modify tests, `TASK.md`, the verifier, workflow, or provenance during
  the Codex stage.
- Do not weaken, replace, or bypass the human-authored acceptance tests.
- Use only the Python standard library.
- Do not store secrets, tokens, private repository data, or conversation text.

## Priorities

1. Record the human requirements as canonical active decisions.
2. Produce a context-free handoff to a fresh Codex session.
3. Preserve exact commit and CI evidence for independent reconstruction.

## Next action

`Fresh ChatGPT session: using only this repository, read AGENTS.md, PROJECT_MEMORY.md, and TASK.md; record the human requirements as active decisions in PROJECT_MEMORY.md; create evidence/01-chatgpt-decision.md; set Last actor to ChatGPT; leave one exact implementation action for Codex; commit exactly those two paths atomically and push main. Do not implement code, modify tests, or claim the acceptance suite passes.`

## Evidence

- `TASK.md`
- `test_normalize_status.py`
- `PMP_SOURCE.md`
- `python scripts/validate_memory.py PROJECT_MEMORY.md`
- `python verify_replay.py` -> `REPLAY STAGE VERIFIED: baseline`
- direct acceptance-test execution fails at baseline by design

## Update rules

- Read this file before significant work.
- Update it only when current state, a decision, a constraint, a priority, or
  the next action changes.
- Keep historical implementation detail in `.project-memory/sessions/`.
- Never store secrets, credentials, tokens, private keys, `.env` values,
  private conversation text, or unnecessary personal data.
- Use `[VERIFIED]`, `[DOCUMENTED]`, and `[ASSUMED]` exactly as defined by PMP.
- Resolve conflicts using the source precedence in `AGENTS.md`.
