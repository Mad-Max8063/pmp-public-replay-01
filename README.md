# PMP Public Replay 01

This repository is a disposable, public, evidence-oriented replay of a
ChatGPT -> Codex -> ChatGPT handoff using Project Memory Protocol (PMP).

## Current stage

The repository begins at a deliberately incomplete baseline:

- the human requirements and acceptance tests are present;
- `normalize_status.py` is intentionally unimplemented;
- no ChatGPT decision evidence or Codex session exists;
- the stage-aware verifier confirms that this is a valid baseline.

The incomplete implementation is not a failed release. It is the controlled
starting state for the replay.

## Protocol source

The replay adopts PMP Core `0.2.1` from
[`Mad-Max8063/project-memory-protocol-public`](https://github.com/Mad-Max8063/project-memory-protocol-public)
at commit `365e48c7b8480f339b622b1f22eb30c8f93a6da8`.

See [PMP_SOURCE.md](PMP_SOURCE.md) for the provenance boundary.

## Replay stages

1. **Baseline:** human requirements, locked tests, and an unimplemented function.
2. **ChatGPT decision:** a fresh ChatGPT session records canonical decisions without coding.
3. **Codex implementation:** a fresh Codex session implements only the recorded decision.
4. **ChatGPT verification:** another fresh ChatGPT session reconstructs and verifies the handoff.

Each stage must be represented by one focused commit on `main`. Agents must
use only repository context and the short stage prompt supplied by the human
operator. Prior conversations must not be pasted into a fresh session.

## Verify the current stage

```bash
python scripts/validate_memory.py PROJECT_MEMORY.md
python verify_replay.py
```

At the initial commit, the second command prints:

```text
REPLAY STAGE VERIFIED: baseline
```

Running the acceptance tests directly at baseline is expected to fail with
`NotImplementedError`. After the Codex stage, all seven tests must pass.

## Evidence boundaries

This replay can prove that repository state, commits, tests, and CI support a
context-free operational handoff. It cannot prove hidden model identity,
session freshness, or which internal reasoning process an agent used.

## License

MIT. See [LICENSE](LICENSE).
