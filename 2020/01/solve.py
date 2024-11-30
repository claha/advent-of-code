"""Advent Of Code #01."""

with open("input") as f:
    data = [int(d) for d in f.read().split()]


# Part 1
def get_pair(data, target):
    """Get pair from data that sums up to target."""
    lut = set()
    for a in data:
        b = target - a
        if b in lut:
            return a, b
        lut.add(a)


a, b = get_pair(data, 2020)
print("Part 1:", a * b)
assert a * b == 997899


# Part 2
def get_triplet(data, target):
    """Get triplet from data that sums up to target."""
    for i, a in enumerate(data[:-1]):
        lut = set()
        for b in data[i + 1 :]:
            c = target - a - b
            if c in lut:
                return a, b, c
            lut.add(b)


a, b, c = get_triplet(data, 2020)
print("Part 2:", a * b * c)
assert a * b * c == 131248694
