"""Advent Of Code #18."""
from shapely.geometry.polygon import Polygon

with open("input") as f:
    plan = [line.strip().split(" ") for line in f.readlines()]


DIR = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "0": (0, 1),
    "2": (0, -1),
    "3": (-1, 0),
    "1": (1, 0),
}

# Part 1
path = set()
points = []
(y, x) = (0, 0)
path.add((y, x))
points.append((y, x))
for d, n, _ in plan:
    n = int(n)
    for i in range(int(n)):
        y += DIR[d][0]
        x += DIR[d][1]
        path.add((y, x))
    points.append((x, y))

poly = Polygon(points)
answer = poly.area + len(path) / 2 + 1
print("Part 1:", answer)
assert answer == 54058824661845

# Part 2
path = set()
points = []
(y, x) = (0, 0)
path.add((y, x))
points.append((y, x))
for _, _, h in plan:
    h = h[2:-1]
    d = h[-1]
    n = int(h[:-1], 16)
    for i in range(n):
        y += DIR[d][0]
        x += DIR[d][1]
        path.add((y, x))
    points.append((x, y))


answer = int(poly.area + len(path) / 2 + 1)
print("Part 2:", answer)
assert answer == 54058824661845
