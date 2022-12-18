"""Advent Of Code #18."""
with open("input") as f:
    data = [tuple(map(int, line.split(","))) for line in f.readlines()]


def dist(x0, y0, z0, x1, y1, z1):
    """Calculate distance between points."""
    return abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1)


# Part 1
free = 0
for i in data:
    free += 6
    for j in data:
        if i == j:
            continue
        free -= int(dist(*i, *j) == 1)

print("Part 1:", free)
assert free == 3526

# Part 2
minx = min(x for x, _, _ in data) - 1
maxx = max(x for x, _, _ in data) + 1
miny = min(y for _, y, _ in data) - 1
maxy = max(y for _, y, _ in data) + 1
minz = min(z for _, _, z in data) - 1
maxz = max(z for _, _, z in data) + 1

DELTA = [
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
]

data_comp = [
    (x, y, z)
    for x in range(minx, maxx + 1)
    for y in range(miny, maxy + 1)
    for z in range(minz, maxz + 1)
    if (x, y, z) not in data
]

queue = [(-1, -1, -1)]
while queue:
    (x, y, z) = queue.pop()
    if (x, y, z) not in data_comp:
        continue
    data_comp.remove((x, y, z))
    for dx, dy, dz in DELTA:
        queue.append((x + dx, y + dy, z + dz))

free_comp = 0
for i in data_comp:
    free_comp += 6
    for j in data_comp:
        if i == j:
            continue
        free_comp -= int(dist(*i, *j) == 1)

print("Part 2:", free - free_comp)
assert free - free_comp == 2090
