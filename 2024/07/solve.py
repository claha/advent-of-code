"""Advent Of Code."""

import aoc

eqs = [list(map(int, line.replace(":", "").split())) for line in aoc.input_readlines()]


def is_possible(eq: list[int], *, concat: bool = False) -> bool:
    """Check if equations is possible to satisfy."""
    if len(eq) == 2:  # noqa: PLR2004
        return eq[0] == eq[1]
    if eq[0] == 0:
        return False
    add = is_possible([eq[0] - eq[-1]] + eq[1:-1], concat)
    mul = False
    if eq[0] % eq[-1] == 0:
        mul = is_possible([eq[0] // eq[-1]] + eq[1:-1], concat)
    con = False
    if concat:
        digits = len(str(eq[-1]))
        factor = 10**digits
        if eq[0] % factor == eq[-1]:
            con = is_possible([eq[0] // factor] + eq[1:-1], concat)
    return add or mul or con


# Part 1
t = 0
for eq in eqs:
    if is_possible(eq):
        t += eq[0]
aoc.check_part1(t, 5837374519342)


# Part 2
t = 0
for eq in eqs:
    if is_possible(eq, concat=True):
        t += eq[0]
aoc.check_part2(t, 492383931650959)
