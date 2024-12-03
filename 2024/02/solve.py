"""Advent Of Code."""

import aoc

data = [list(map(int, line.split())) for line in aoc.input_readlines()]


def is_safe(record: list[int]) -> bool:
    """Check if a record is safe or not."""
    safe_diff_range = [1, 2, 3]
    diff = [record[i + 1] - record[i] for i in range(len(record) - 1)]
    if any(d > 0 for d in diff) and any(d < 0 for d in diff):
        return False
    diff = list(map(abs, diff))
    return all(d in safe_diff_range for d in diff)


# Part 1
safe = 0
for record in data:
    safe += int(is_safe(record))

aoc.check_part1(safe, 379)

# Part 2
for record in data:
    if is_safe(record):
        continue
    for i in range(len(record)):
        record_mod = record[:]
        record_mod.pop(i)
        if is_safe(record_mod):
            safe += 1
            break

aoc.check_part2(safe, 430)
