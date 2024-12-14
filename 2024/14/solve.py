"""Advent Of Code."""

import re

import aoc

robots = [list(map(int, re.findall(r"-?\d+", line))) for line in aoc.input_readlines()]
HEIGHT = 103
WIDTH = 101


def draw(robots: list[tuple[int, int, int, int]]) -> None:
    """Draw the robots."""
    points = [(x, y) for (x, y, _, _) in robots]
    picture = ""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in points:
                picture += str(points.count((x, y)))
            else:
                picture += " "
        picture += "\n"
    print(picture)  # noqa: T201


# Part 1
for _ in range(100):
    for i in range(len(robots)):
        robots[i][0] = (robots[i][0] + robots[i][2]) % WIDTH
        robots[i][1] = (robots[i][1] + robots[i][3]) % HEIGHT

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for x, y, _, _ in robots:
    if x < WIDTH // 2:
        if y < HEIGHT // 2:
            q1 += 1
        elif y > HEIGHT // 2:
            q2 += 1
    if x > WIDTH // 2:
        if y < HEIGHT // 2:
            q3 += 1
        elif y > HEIGHT // 2:
            q4 += 1

aoc.check_part1(q1 * q2 * q3 * q4, 222208000)

# Part 2
n = 100
while True:
    n += 1
    for i in range(len(robots)):
        robots[i][0] = (robots[i][0] + robots[i][2]) % WIDTH
        robots[i][1] = (robots[i][1] + robots[i][3]) % HEIGHT
    points = [(x, y) for x, y, _, _ in robots]
    if len(points) == len(set(points)):  # no overlapping robots
        draw(robots)
        break

aoc.check_part2(n, 7623)
