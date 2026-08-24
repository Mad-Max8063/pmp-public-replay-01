"""Status normalization task for the PMP public replay."""

import re


_SEPARATOR_RUN = re.compile(r"[\s_-]+")
_CANONICAL_STATUSES = {
    "todo": "todo",
    "to do": "todo",
    "pending": "todo",
    "in progress": "in-progress",
    "inprogress": "in-progress",
    "doing": "in-progress",
    "wip": "in-progress",
    "done": "done",
    "complete": "done",
    "completed": "done",
}


def normalize_status(value: str) -> str:
    """Return the canonical status specified by the human authority."""

    normalized = _SEPARATOR_RUN.sub(" ", value.strip().casefold()).strip()
    try:
        return _CANONICAL_STATUSES[normalized]
    except KeyError:
        raise ValueError(f"unsupported status: {value!r}") from None
