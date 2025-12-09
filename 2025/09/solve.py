"""Advent Of Code."""

import aoc
from shapely import Polygon

red_tiles = [list(map(int, line.split(","))) for line in aoc.input_readlines()]

# Part 1
answer = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        answer = max(answer, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

aoc.check_part1(answer, 4749672288)

# Part 2
polygon = Polygon(red_tiles)
answer = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_x = max(x1, x2)
        max_y = max(y1, y2)
        rectangle = Polygon(
            ((min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y))
        )

        if polygon.contains(rectangle):
            answer = max(answer, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

aoc.check_part2(answer, 1479665889)
