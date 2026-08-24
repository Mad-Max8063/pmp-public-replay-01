# Human-authored requirements

Human authority: Matías Maximiliano Bernal / Max Devs Solutions

Implement:

```python
normalize_status(value: str) -> str
```

Required behavior:

1. Trim outer whitespace and compare input case-insensitively with Unicode
   `casefold()` semantics.
2. Treat every run of whitespace, underscores, or hyphens as one word
   separator before alias matching.
3. Return `"todo"` for `todo`, `to do`, or `pending`.
4. Return `"in-progress"` for `in progress`, `inprogress`, `doing`, or `wip`.
5. Return `"done"` for `done`, `complete`, or `completed`.
6. Raise `ValueError` for empty or unsupported input with the exact message
   `unsupported status: <repr of original value>`.
7. Use only the Python standard library.

Acceptance boundary:

- `test_normalize_status.py` is human-authored and must not be modified.
- ChatGPT records decisions but does not implement the function.
- Codex implements the function and records actual test evidence.
- A fresh ChatGPT verifier reconstructs the result from Git and CI.
