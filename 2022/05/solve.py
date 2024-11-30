"""Advent Of Code #05."""

import re
from copy import deepcopy

with open("input") as f:
    creates, moves = f.read().split("\n\n")

creates = [list(row) for row in creates.split("\n")]
creates_orig = {}
# Stack id in last row of input
for i, c in enumerate(creates[-1]):
    if not c.strip():
        continue
    c = int(c)
    creates_orig[c] = []
    for j in range(len(creates) - 1):
        if i < len(creates[j]) and creates[j][i].strip():
            creates_orig[c].append(creates[j][i])

moves = [list(map(int, re.findall(r"\d+", move))) for move in moves.strip().split("\n")]


# Part 1
creates = deepcopy(creates_orig)
for n, f, t in moves:
    for _ in range(n):
        creates[t].insert(0, creates[f].pop(0))

top = "".join(creates[i][0] for i in range(1, 10))
print("Part 1:", top)
assert top == "QMBMJDFTD"


# Part 2
creates = deepcopy(creates_orig)
for n, f, t in moves:
    for i in range(n - 1, -1, -1):
        creates[t].insert(0, creates[f].pop(i))

top = "".join(creates[i][0] for i in range(1, 10))
print("Part 2:", top)
assert top == "NBTVTJNFJ"
