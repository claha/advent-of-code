"""Advent of Code."""

from pathlib import Path
from typing import Any


def input_read() -> str:
    """Read and return the input."""
    with Path.open("input") as f:
        return f.read().strip()


def input_readlines() -> list[str]:
    """Read and return the input lines."""
    return input_read().split("\n")


def test_read() -> str:
    """Read and return the test."""
    with Path.open("test") as f:
        return f.read().strip()


def test_readlines() -> list[str]:
    """Read and return the test lines."""
    return test_read().split("\n")


def check_part1(answer: Any, expected: Any) -> None:  # noqa: ANN401
    """Print and check answer against expected."""
    print("Part 1:", answer)  # noqa: T201
    assert answer == expected  # noqa: S101


def check_part2(answer: Any, expected: Any) -> None:  # noqa: ANN401
    """Print and check answer against expected."""
    print("Part 2:", answer)  # noqa: T201
    assert answer == expected  # noqa: S101
