"""Advent Of Code."""

import aoc

lines = aoc.input_read().split("\n\n")
locks = [block.split("\n") for block in lines if block.startswith("#")]
keys = [block.split("\n") for block in lines if block.startswith(".")]
ROWS = len(locks[0])
COLS = len(locks[0][0])


def get_heights(schematic: list[str], *, is_lock: bool) -> list[int]:
    """Convert a schematic into a list of heights."""
    heights = []
    rows = range(ROWS) if is_lock else range(ROWS - 1, -1, -1)
    for col in range(COLS):
        height = sum(1 for row in rows if schematic[row][col] == "#")
        heights.append(height)

    return heights


# Part 1
count = 0

for lock in locks:
    lock_heights = get_heights(lock, is_lock=True)
    for key in keys:
        key_heights = get_heights(key, is_lock=False)
        if all(
            lock_height + key_height <= ROWS
            for lock_height, key_height in zip(lock_heights, key_heights)
        ):
            count += 1

aoc.check_part1(count, 3057)
