"""Advent Of Code."""

import aoc
from collections import defaultdict

data = aoc.input_readlines()

splitters = set()
beams = set()
for y, line in enumerate(data):
    for x, char in enumerate(line.strip()):
        if char == "S":
            beams.add((y, x))
        if char == "^":
            splitters.add((y, x))

# Part 1
answer = 0
for _ in range(len(data)):
    new_beams = set()
    for y, x in beams:
        if (y + 1, x) in splitters:
            new_beams.add((y + 1, x - 1))
            new_beams.add((y + 1, x + 1))
            answer += 1
        else:
            new_beams.add((y + 1, x))
    beams = new_beams
aoc.check_part1(answer, 1642)

# Part 2
beams = defaultdict(lambda: 0)
for y, line in enumerate(data):
    for x, char in enumerate(line.strip()):
        if char == "S":
            beams[(y, x)] = 1

for yc in range(len(data)):
    for y, x in [(y, x) for (y, x) in beams.keys() if y == yc]:
        if (y + 1, x) in splitters:
            beams[(y + 1, x - 1)] += beams[(y, x)]
            beams[(y + 1, x + 1)] += beams[(y, x)]
        else:
            beams[(y + 1, x)] += beams[(y, x)]

answer = 0
for y, x in beams.keys():
    if y == len(data):
        answer += beams[(y, x)]

aoc.check_part2(answer, 47274292756692)
