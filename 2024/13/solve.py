"""Advent Of Code."""

import re

import aoc

machines = aoc.input_read().split("\n\n")
equations = [list(map(int, re.findall(r"\d+", machine))) for machine in machines]


def solve(  # noqa: PLR0913
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    b0: int,
    b1: int,
    *,
    add: bool = False,
) -> int:
    """Solve linear equations."""
    if add:
        b0 += 10000000000000
        b1 += 10000000000000
    det = x0 * y1 - y0 * x1
    a0 = (b0 * y1 - b1 * x1) / det
    a1 = (b1 * x0 - b0 * y0) / det
    if a0 == int(a0) and a1 == int(a1):
        return int(3 * a0 + a1)
    return 0


# Part 1
tokens = sum([solve(*eq) for eq in equations])
aoc.check_part1(tokens, 39748)

# Part 2
tokens = sum([solve(*eq, add=True) for eq in equations])
aoc.check_part2(tokens, 74478585072604)
