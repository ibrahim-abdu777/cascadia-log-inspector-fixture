"""Utilities for inspecting simple newline-delimited logs."""

from collections import Counter


def count_levels(lines: list[str]) -> dict[str, int]:
    """Count recognized log levels at the start of each non-empty line."""
    counts: Counter[str] = Counter()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        level = stripped.split(maxsplit=1)[0].upper()
        if level in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
            counts[level] += 1
    return dict(counts)
