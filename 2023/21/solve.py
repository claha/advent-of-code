"""Advent Of Code #21."""
from collections import deque

import numpy as np

with open("input") as f:
    garden = [line.strip() for line in f.readlines()]


DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]

assert len(garden) == len(garden[0])
N = len(garden)
sy, sx = N // 2, N // 2
assert garden[sy][sx] == "S"
garden[sy] = garden[sy].replace("S", ".")


def get_distance(garden, N, sy, sx, steps):
    """Get number of reachable with exactly steps."""
    """Get distance."""
    distance = set()
    visited = set()
    queue = deque()
    queue.append((sy, sx, 0))
    while queue:
        (y, x, s) = queue.popleft()
        # Already been here
        if (y, x, s) in visited:
            continue
        visited.add((y, x, s))
        # Out of bounds
        if not (0 <= y < N and 0 <= x < N):
            continue
        # Rock
        if garden[y][x] == "#":
            continue
        # Maximum steps
        if s > steps:
            continue
        if s == steps:
            distance.add((y, x))
        else:
            for dy, dx in DELTA:
                queue.append((y + dy, x + dx, s + 1))

    return len(distance)


# Part 1
distance = get_distance(garden, N, sy, sx, 64)
print("Part 1:", distance)
assert distance == 3637


# Part 2
gardenN = [row * 5 for row in garden]
gardenN.extend(gardenN * (5 - 1))
sy = sx = len(gardenN) // 2
a0 = get_distance(gardenN, len(gardenN), sy, sx, 65 + (1 - 1) * 131)
a1 = get_distance(gardenN, len(gardenN), sy, sx, 65 + (2 - 1) * 131)
a2 = get_distance(gardenN, len(gardenN), sy, sx, 65 + (3 - 1) * 131)

A = np.matrix(
    [
        [0, 0, 1],
        [1, 1, 1],
        [4, 2, 1],
    ]
)
b = np.array([a0, a1, a2])
x = np.linalg.solve(A, b).astype(np.int64)

# How far can we get
MAGIC = 26501365
n = MAGIC // 131
assert MAGIC - n * 131 == 65

answer = x[0] * n * n + x[1] * n + x[2]
print("Part 2:", answer)
assert answer == 601113643448699
