"""Advent Of Code #06."""
with open("input") as f:
    data = f.read().strip()

# Part 1
N = 4
i = 0
while len(set(data[i : i + 4])) != N:
    i += 1
i += N

print("Part 1:", i)
assert i == 1034


# Part 2
N = 14
i = 0
while len(set(data[i : i + 14])) != N:
    i += 1
i += N

print("Part 2:", i)
assert i == 2472
