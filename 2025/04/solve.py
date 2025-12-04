"""Advent Of Code."""

import aoc

data = aoc.input_readlines()

rolls = set()
for y, line in enumerate(data):
    for x, char in enumerate(line.strip()):
        if char == "@":
            rolls.add((y, x))


def count_neighbors(y, x):
    neighbors = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if (y + dy, x + dx) in rolls:
                neighbors += 1
    return neighbors


# Part 1
answer = 0
for y, x in rolls:
    if count_neighbors(y, x) < 4:
        answer += 1

aoc.check_part1(answer, 1393)

# Part 2
answer = 0
while True:
    rolls_copy = rolls.copy()
    for y, x in rolls_copy:
        if count_neighbors(y, x) < 4:
            answer += 1
            rolls.remove((y, x))
    if len(rolls) == len(rolls_copy):
        break

aoc.check_part2(answer, 8643)
