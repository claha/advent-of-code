"""Advent Of Code."""

from itertools import pairwise

import aoc


def next_secret_number(secret_number: int) -> int:
    """Calculate next secret number."""
    secret_number ^= (secret_number * 64) & 0xFFFFFF
    secret_number ^= (secret_number // 32) & 0xFFFFFF
    return secret_number ^ ((secret_number * 2048) & 0xFFFFFF)


nums = list(map(int, aoc.input_readlines()))


# Part 1
sum_all = 0
for num in nums:
    for _ in range(2000):
        num = next_secret_number(num)  # noqa: PLW2901
    sum_all += num
aoc.check_part1(sum_all, 17612566393)


# Part 2
bananas = {}
for num in nums:
    secret_nums = [num]
    for _ in range(2000):
        num = next_secret_number(num)  # noqa: PLW2901
        secret_nums.append(num)

    diffs = [b % 10 - a % 10 for a, b in pairwise(secret_nums)]
    seen = set()
    for i in range(len(secret_nums) - 4):
        pattern = tuple(diffs[i : i + 4])
        if pattern in seen:
            continue
        if pattern not in bananas:
            bananas[pattern] = 0
        bananas[pattern] += secret_nums[i + 4] % 10
        seen.add(pattern)

max_bananas = max(bananas.values())
aoc.check_part2(max_bananas, 1968)
