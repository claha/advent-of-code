"""Advent Of Code #17."""
with open("input") as f:
    data = f.read()
matrix = data.splitlines()

ACTIVE = "#"
INACTIVE = "."

# Part 1
DXDYDZ = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            if (dx, dy, dz) != (0, 0, 0):
                DXDYDZ.append((dx, dy, dz))

active = set()
z = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == ACTIVE:
            active.add((x, y, z))

for _ in range(6):
    to_active = set()
    to_inactive = set()

    # Go through active and count its neighbors
    for x, y, z in active:
        neighbors = 0
        for dx, dy, dz in DXDYDZ:
            (nx, ny, nz) = (x + dx, y + dy, z + dz)
            if (nx, ny, nz) in active:
                neighbors += 1
        if neighbors not in [2, 3]:
            to_inactive.add((x, y, z))

    # Go through active and add its neighbors
    neighbors = {}
    for x, y, z in active:
        for dx, dy, dz in DXDYDZ:
            (nx, ny, nz) = (x + dx, y + dy, z + dz)
            if (nx, ny, nz) not in neighbors:
                neighbors[(nx, ny, nz)] = 0
            neighbors[(nx, ny, nz)] += 1
    for x, y, z in neighbors:
        if (x, y, z) not in active:
            if neighbors[(x, y, z)] == 3:
                to_active.add((x, y, z))

    # Update active
    active.update(to_active)
    active.difference_update(to_inactive)

print("Part 1:", len(active))
assert len(active) == 252

# Part 2
DXDYDZDW = []
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            for dw in [-1, 0, 1]:
                if (dx, dy, dz, dw) != (0, 0, 0, 0):
                    DXDYDZDW.append((dx, dy, dz, dw))

active = set()
z = 0
w = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == ACTIVE:
            active.add((x, y, z, w))

for _ in range(6):
    to_active = set()
    to_inactive = set()

    # Go through active and count its neighbors
    for x, y, z, w in active:
        neighbors = 0
        for dx, dy, dz, dw in DXDYDZDW:
            (nx, ny, nz, nw) = (x + dx, y + dy, z + dz, w + dw)
            if (nx, ny, nz, nw) in active:
                neighbors += 1
        if neighbors not in [2, 3]:
            to_inactive.add((x, y, z, w))

    # Go through active and add its neighbors
    neighbors = {}
    for x, y, z, w in active:
        for dx, dy, dz, dw in DXDYDZDW:
            (nx, ny, nz, nw) = (x + dx, y + dy, z + dz, w + dw)
            if (nx, ny, nz, nw) not in neighbors:
                neighbors[(nx, ny, nz, nw)] = 0
            neighbors[(nx, ny, nz, nw)] += 1
    for x, y, z, w in neighbors:
        if (x, y, z, w) not in active:
            if neighbors[(x, y, z, w)] == 3:
                to_active.add((x, y, z, w))

    # Update active
    active.update(to_active)
    active.difference_update(to_inactive)

print("Part 2:", len(active))
assert len(active) == 2160
