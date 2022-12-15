"""Advent Of Code #15."""
import re

with open("input") as f:
    data = [list(map(int, re.findall(r"-?\d+", line))) for line in f.readlines()]


def dist(x0, y0, x1, y1):
    """Get manhattan distance."""
    return abs(x0 - x1) + abs(y0 - y1)


dists = [dist(sx, sy, bx, by) for (sx, sy, bx, by) in data]


# Part 1
Y = 2000000
no_beacon = set()

for i in range(len(data)):
    (sx, sy, bx, by) = data[i]
    d = dists[i]
    dy = abs(sy - Y)
    if dy > d:
        continue
    for x in range(sx - (d - dy), sx + (d - dy) + 1):
        no_beacon.add((x, Y))

for (sx, sy, bx, by) in data:
    if (bx, by) in no_beacon:
        no_beacon.remove((bx, by))
    if (sx, sy) in no_beacon:
        no_beacon.remove((sx, sy))


print("Part 1:", len(no_beacon))
assert len(no_beacon) == 4737567


# Part 2
Y = 4000000

for y in range(Y):
    x = 0
    while x < Y:
        found = False
        for i in range(len(data)):
            (sx, sy, _, _) = data[i]
            d = dists[i]
            dxy = dist(sx, sy, x, y)
            if dxy <= d:
                if x < sx:
                    x = sx + (sx - x)  # mirror in sx
                x += d - dxy
                found = True
                break
        if not found:
            print("Part 2:", x * Y + y)
            assert x * Y + y == 13267474686239
            break
        else:
            x += 1
    if not found:
        break
