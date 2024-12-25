"""Advent Of Code."""

from functools import cache

import aoc

NUMERIC = {
    "7": 0,
    "8": 1,
    "9": 2,
    "4": 1j,
    "5": 1 + 1j,
    "6": 2 + 1j,
    "1": 2j,
    "2": 1 + 2j,
    "3": 2 + 2j,
    " ": 3j,
    "0": 1 + 3j,
    "A": 2 + 3j,
}
DIRECTIONAL = {
    " ": 0,
    "^": 1,
    "A": 2,
    "<": 1j,
    "v": 1 + 1j,
    ">": 2 + 1j,
}

codes = aoc.input_readlines()


def get_keypad(start: str, end: str) -> dict[str, complex]:
    """Get keypad based on start and end."""
    if start in NUMERIC and end in NUMERIC:
        return NUMERIC
    return DIRECTIONAL


@cache
def path(start: str, end: str) -> str:
    """Get most straighforward path."""
    keypad = get_keypad(start, end)
    d = keypad[end] - keypad[start]
    dy = int(d.imag)
    dx = int(d.real)
    yy = ("^" * -dy) + ("v" * dy)
    xx = ("<" * -dx) + (">" * dx)

    bad = keypad[" "] - keypad[start]
    prefer_yy_first = (dx > 0 or bad == dx) and bad != dy * 1j
    return (yy + xx if prefer_yy_first else xx + yy) + "A"


@cache
def length(code: str, depth: int) -> int:
    """Calculate length of code."""
    if depth == 0:
        return len(code)
    return sum(length(path(code[i - 1], code[i]), depth - 1) for i in range(len(code)))


# Part 1
complexities = sum(int(code.replace("A", "")) * length(code, 3) for code in codes)
aoc.check_part1(complexities, 176870)

# Part 2
complexities = sum(int(code.replace("A", "")) * length(code, 26) for code in codes)
aoc.check_part1(complexities, 223902935165512)
