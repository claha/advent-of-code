"""Advent Of Code #09."""
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


PREAMBLE = 25
invalid = None
for i in range(PREAMBLE, len(data)):
    if get_pair(data[i - PREAMBLE : i], data[i]) is None:
        invalid = data[i]
        break

print("Part 1:", invalid)
assert invalid == 105950735


# Part 2
cumsum = [0] * (len(data) + 1)
for i in range(1, len(data) + 1):
    cumsum[i] = cumsum[i - 1] + data[i - 1]

weakness = []
for start in range(len(data)):
    for end in range(start + 2, len(data) + 1):
        if cumsum[end] - cumsum[start] == invalid:
            weakness = data[start:end]
            break
    if weakness:
        break

weakness = min(weakness) + max(weakness)
print("Part 2:", weakness)
assert weakness == 13826915
