"""Advent Of Code #01."""

from pathlib import Path

left = []
right = []

with Path.open("input") as f:
    for line in f:
        first, second = map(int, line.split())
        left.append(first)
        right.append(second)
left = sorted(left)
right = sorted(right)

# Part 1
diff = [abs(values[0] - values[1]) for values in zip(left, right)]
answer = sum(diff)
print("Part 1:", answer)
assert answer == 2580760

# Part 2
answer = 0
for value in left:
    answer += value * right.count(value)
print("Part 2:", answer)
assert answer == 25358365
