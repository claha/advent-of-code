"""Advent Of Code #03."""

with open("input") as f:
    data = [d for d in f.read().strip().split()]


def get_prio(x):
    """Get priority."""
    if x >= "a":
        return ord(x) - 96
    return ord(x) - 38


# Part 1
score = 0
for r in data:
    c0 = set(r[: len(r) // 2])
    c1 = set(r[len(r) // 2 :])
    score += get_prio(c0.intersection(c1).pop())
print("Part 1:", score)
assert score == 7875


# Part 2
score = 0
for r in range(0, len(data), 3):
    c0 = set(data[r])
    c1 = set(data[r + 1])
    c2 = set(data[r + 2])
    score += get_prio(c0.intersection(c1, c2).pop())
print("Part 2:", score)
assert score == 2479
