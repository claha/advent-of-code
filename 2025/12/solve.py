"""Advent Of Code."""

import aoc

shapes = list()
regions = []
for line in aoc.input_readlines():
    line = line.strip()
    if line.endswith(":"):
        shapes.append([])
    elif "x" in line:
        regions.append(
            list(map(int, line.replace("x", " ").replace(":", "").split(" ")))
        )
    elif line:
        shapes[-1].append(line)


def shape_area(shape):
    return sum(row.count("#") for row in shape)


# Part 1
answer = 0
for width, height, *presents in regions:
    shapes_to_fit = []
    for i, v in enumerate(presents):
        for _ in range(v):
            shapes_to_fit.append(shapes[i])
    shapes_area = sum(shape_area(shape) for shape in shapes_to_fit)
    if shapes_area > width * height:
        continue
    answer += 1
aoc.check_part1(answer, 410)
