"""Advent Of Code #01."""

with open("input") as f:
    data = [int(d) for d in f.read().split()]


# Part 1
count = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        count += 1
print("Part 1:", count)
assert count == 1298


# Part 2
count = 0
for i in range(3, len(data)):
    if data[i] > data[i - 3]:
        count += 1
print("Part 2:", count)
assert count == 1248
