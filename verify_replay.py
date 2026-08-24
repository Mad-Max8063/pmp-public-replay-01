#!/usr/bin/env python3
"""Verify the current stage of the public PMP replay."""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TASK_SHA256 = "b96dc90adef240ed3c2734c172142994bcd657b2f70b1f80f608eeca67e8d331"
TEST_SHA256 = "ba1d765ba7b97951cc8de54ca7e54bc5b43b345c7fc46e98d25ec78c1f7026f4"
BASELINE_IMPLEMENTATION_SHA256 = (
    "e92866982637637b4c58735937fe1fadad23019f01639741adf5e3a1361852d5"
)


def normalized_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def nonempty_file(path: Path) -> bool:
    return path.is_file() and bool(path.read_text(encoding="utf-8").strip())


def run_tests() -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", "test_normalize_status.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = result.stdout + result.stderr
    passed = result.returncode == 0 and "Ran 7 tests" in output and "OK" in output
    return passed, output


def main() -> int:
    errors: list[str] = []
    memory_path = ROOT / "PROJECT_MEMORY.md"
    memory = memory_path.read_text(encoding="utf-8")

    memory_check = subprocess.run(
        [sys.executable, "scripts/validate_memory.py", "PROJECT_MEMORY.md"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if memory_check.returncode != 0:
        errors.append("canonical memory failed structural validation")

    if normalized_sha256(ROOT / "TASK.md") != TASK_SHA256:
        errors.append("human-authored TASK.md changed")
    if normalized_sha256(ROOT / "test_normalize_status.py") != TEST_SHA256:
        errors.append("human-authored acceptance tests changed")

    implementation_is_baseline = (
        normalized_sha256(ROOT / "normalize_status.py")
        == BASELINE_IMPLEMENTATION_SHA256
    )
    tests_passed, test_output = run_tests()
    seven_tests_ran = "Ran 7 tests" in test_output
    chatgpt_evidence = ROOT / "evidence" / "01-chatgpt-decision.md"
    final_evidence = ROOT / "evidence" / "03-chatgpt-verification.md"
    session_dir = ROOT / ".project-memory" / "sessions"
    codex_sessions = (
        list(session_dir.glob("*-codex-normalize-status.md"))
        if session_dir.is_dir()
        else []
    )

    actor: str | None = None
    if "Last actor: `Human authority`" in memory:
        actor = "Human authority"
    elif "Last actor: `Codex`" in memory:
        actor = "Codex"
    elif "Last actor: `ChatGPT`" in memory:
        actor = "ChatGPT"
    else:
        errors.append("canonical memory has no recognized Last actor")

    if actor == "Human authority":
        stage = "baseline"
        if not implementation_is_baseline:
            errors.append("baseline implementation changed")
        if tests_passed or not seven_tests_ran or "NotImplementedError" not in test_output:
            errors.append("baseline acceptance suite did not fail as expected")
        if chatgpt_evidence.exists() or final_evidence.exists() or codex_sessions:
            errors.append("baseline contains premature agent evidence")
        if "Fresh ChatGPT session" not in memory:
            errors.append("baseline next action does not name a fresh ChatGPT session")
    elif actor == "ChatGPT" and not final_evidence.exists():
        stage = "chatgpt-decision"
        if not nonempty_file(chatgpt_evidence):
            errors.append("ChatGPT decision evidence is missing or empty")
        if not implementation_is_baseline:
            errors.append("implementation changed during the ChatGPT decision stage")
        if tests_passed or not seven_tests_ran or "NotImplementedError" not in test_output:
            errors.append("decision-stage acceptance suite did not fail as expected")
        if codex_sessions:
            errors.append("decision stage contains a premature Codex session")
        if "Codex" not in memory:
            errors.append("decision-stage next action does not name Codex")
    elif actor == "Codex":
        stage = "codex-implementation"
        if not nonempty_file(chatgpt_evidence):
            errors.append("Codex stage is missing ChatGPT decision evidence")
        if implementation_is_baseline:
            errors.append("Codex stage still has the baseline implementation")
        if not tests_passed:
            errors.append("Codex-stage acceptance suite is not passing")
        if len(codex_sessions) != 1 or not nonempty_file(codex_sessions[0]):
            errors.append("expected exactly one nonempty Codex session record")
        if final_evidence.exists():
            errors.append("Codex stage contains premature final ChatGPT evidence")
        if "Fresh ChatGPT verifier" not in memory:
            errors.append("Codex-stage next action does not name a fresh ChatGPT verifier")
    elif actor == "ChatGPT" and final_evidence.exists():
        stage = "chatgpt-verification"
        if not nonempty_file(chatgpt_evidence):
            errors.append("final stage is missing ChatGPT decision evidence")
        if implementation_is_baseline or not tests_passed:
            errors.append("final-stage implementation evidence is incomplete")
        if len(codex_sessions) != 1 or not nonempty_file(codex_sessions[0]):
            errors.append("final stage requires exactly one Codex session record")
        if not nonempty_file(final_evidence):
            errors.append("final ChatGPT evidence is empty")
        if "Human authority" not in memory:
            errors.append("final-stage next action does not name Human authority")
    else:
        stage = "unknown"

    if errors:
        print("REPLAY STAGE INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"REPLAY STAGE VERIFIED: {stage}")
    print("- TASK.md and acceptance-test hashes are intact")
    print(f"- seven-test suite passing: {tests_passed}")
    print(f"- ChatGPT decision evidence: {chatgpt_evidence.exists()}")
    print(f"- Codex session count: {len(codex_sessions)}")
    print(f"- final ChatGPT evidence: {final_evidence.exists()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
