"""Advent Of Code."""

import aoc

instructions = [line for line in aoc.input_readlines()]

# Part 1
answer = 0
dial = 50

for inst in instructions:
    dir = 1 if inst[0] == "R" else -1
    dist = int(inst[1:])
    dial = (dial + dir * dist) % 100
    answer += dial == 0

aoc.check_part1(answer, 1021)

# Part 2
answer = 0
dial = 50

for inst in instructions:
    dir = 1 if inst[0] == "R" else -1
    dist = int(inst[1:])
    for _ in range(dist):
        dial = (dial + dir) % 100
        if dial == 0:
            answer += 1

aoc.check_part2(answer, 5933)
