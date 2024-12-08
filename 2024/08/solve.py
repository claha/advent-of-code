"""Advent Of Code."""

import aoc

data = aoc.input_readlines()

ROWS = len(data)
COLS = len(data[0])
antennas = {}

for r in range(ROWS):
    for c in range(COLS):
        obj = data[r][c]
        if obj == ".":
            continue
        if obj not in antennas:
            antennas[obj] = []
        antennas[obj].append((r, c))


def in_range(r: int, c: int) -> bool:
    """Check if (r,c) is in range."""
    return 0 <= r < ROWS and 0 <= c < COLS


# Part 1
nodes = set()
for antenna_group in antennas.values():
    for i in range(len(antenna_group) - 1):
        for j in range(i + 1, len(antenna_group)):
            a1 = antenna_group[i]
            a2 = antenna_group[j]
            dr, dc = a1[0] - a2[0], a1[1] - a2[1]
            if in_range(a1[0] + dr, a1[1] + dc):
                nodes.add((a1[0] + dr, a1[1] + dc))
            if in_range(a1[0] - 2 * dr, a1[1] - 2 * dc):
                nodes.add((a1[0] - 2 * dr, a1[1] - 2 * dc))

aoc.check_part1(len(nodes), 303)


# Part 2
nodes = set()
for antenna_group in antennas.values():
    for i in range(len(antenna_group) - 1):
        for j in range(i + 1, len(antenna_group)):
            a1 = antenna_group[i]
            a2 = antenna_group[j]
            dr, dc = a1[0] - a2[0], a1[1] - a2[1]

            n = 0
            while True:
                if not in_range(a1[0] + n * dr, a1[1] + n * dc):
                    break
                nodes.add((a1[0] + n * dr, a1[1] + n * dc))
                n += 1
            n = 0
            while True:
                if not in_range(a1[0] - n * dr, a1[1] - n * dc):
                    break
                nodes.add((a1[0] - n * dr, a1[1] - n * dc))
                n += 1

aoc.check_part1(len(nodes), 1045)
