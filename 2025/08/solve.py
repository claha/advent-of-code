"""Advent Of Code."""

import aoc
from collections import Counter

data = [list(map(int, line.split(","))) for line in aoc.input_readlines()]


def dist(x0, y0, z0, x1, y1, z1):
    return (x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2


def find(c):
    if parent[c] != c:
        parent[c] = find(parent[c])
    return parent[c]


def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py


dists = []
for i in range(len(data)):
    dists.extend([(dist(*data[i], *data[j]), i, j) for j in range(i + 1, len(data))])
dists.sort()

parent = list(range(len(data)))

# Part 1
for _ in range(1000):
    _, i, j = dists.pop(0)
    if find(i) != find(j):
        union(i, j)

sizes = sorted(Counter(find(i) for i in range(len(data))).values())
answer = sizes[-1] * sizes[-2] * sizes[-3]
aoc.check_part1(answer, 102816)

# Part 2
last_i, last_j = None, None
while dists:
    _, i, j = dists.pop(0)
    if find(i) != find(j):
        union(i, j)
        last_i, last_j = i, j

answer = data[last_i][0] * data[last_j][0]
aoc.check_part2(answer, 100011612)
