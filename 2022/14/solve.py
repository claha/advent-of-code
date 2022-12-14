"""Advent Of Code #14."""
import re

with open("input") as f:
    data = [list(map(int, re.findall(r"\d+", line))) for line in f.readlines()]

rocksnow = set()

for path in data:
    x, y = path[0], path[1]
    for i in range(2, len(path), 2):
        for dx in range(min(x, path[i]), max(x, path[i]) + 1):
            for dy in range(min(y, path[i + 1]), max(y, path[i + 1]) + 1):
                rocksnow.add((dx, dy))
        x, y = path[i], path[i + 1]

MAX_Y = max(y for (_, y) in rocksnow)
SOURCE = (500, 0)


def fall(rocksnow, exit_condition):
    """Let the snow fall."""
    snow = 0
    while True:
        x, y = SOURCE

        while True:
            if (x, y + 1) not in rocksnow:
                y += 1
            elif (x - 1, y + 1) not in rocksnow:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in rocksnow:
                x += 1
                y += 1
            else:
                rocksnow.add((x, y))
                snow += 1
                break

            if y > MAX_Y + 1:
                rocksnow.add((x, y))
                break

        if exit_condition(x, y):
            return snow


# Part 1
snow = fall(rocksnow, lambda x, y: y > MAX_Y)
print("Part 1:", snow)
assert snow == 913


# Part 2
snow += fall(rocksnow, lambda x, y: (x, y) == SOURCE)
print("Part 2:", snow)
assert snow == 30762
