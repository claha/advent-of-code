"""Advent Of Code."""

import aoc

stones = list(map(int, aoc.input_read().split(" ")))
dp = {}


def split_stone(stone: int) -> tuple[int, int]:
    """Split a stone in half."""
    digits = len(str(stone))
    factor = 10 ** (digits // 2)
    return stone // factor, stone % factor


def prog(stone: int, blink: int) -> int:
    """Do the dynamic programming."""
    digits = len(str(stone))
    key = (stone, blink)
    if key in dp:
        return dp[key]
    if blink == 0:
        return 1
    if blink == 1:
        if stone == 0:
            return 1
        if digits % 2 == 0:
            return 2
        return 1
    if stone == 0:
        dp[key] = prog(1, blink - 1)
    elif digits % 2 == 0:
        stone1, stone2 = split_stone(stone)
        dp[key] = prog(stone1, blink - 1) + prog(stone2, blink - 1)
    else:
        dp[key] = prog(stone * 2024, blink - 1)
    return dp[key]


# Part 1
count = sum([prog(stone, 25) for stone in stones])
aoc.check_part1(count, 199986)

# Part 2
count = sum([prog(stone, 75) for stone in stones])
aoc.check_part2(count, 236804088748754)
