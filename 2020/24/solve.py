"""Advent Of Code #24."""

with open("input") as f:
    data = f.read()
paths = data.splitlines()

# Use cube coordinates to repesent hexagons
directions = {
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
}

# Part 1
black = set()
for path in paths:
    (x, y, z) = (0, 0, 0)
    i = 0
    while i < len(path):
        if path[i] in directions:
            x += directions[path[i]][0]
            y += directions[path[i]][1]
            z += directions[path[i]][2]
            i += 1
        else:
            if path[i : i + 2] in directions:
                x += directions[path[i : i + 2]][0]
                y += directions[path[i : i + 2]][1]
                z += directions[path[i : i + 2]][2]
                i += 2
            else:
                assert False
    if (x, y, z) in black:
        black.remove((x, y, z))
    else:
        black.add((x, y, z))

print("Part 1:", len(black))
assert len(black) == 326

# Part 2
for _ in range(100):
    to_black = set()
    to_white = set()

    for x, y, z in black:
        neighbors = 0
        for dx, dy, dz in directions.values():
            (nx, ny, nz) = (x + dx, y + dy, z + dz)
            if (nx, ny, nz) in black:
                neighbors += 1
        if neighbors == 0 or neighbors > 2:
            to_white.add((x, y, z))

    neighbors = {}
    for x, y, z in black:
        for dx, dy, dz in directions.values():
            (nx, ny, nz) = (x + dx, y + dy, z + dz)
            if (nx, ny, nz) not in neighbors:
                neighbors[(nx, ny, nz)] = 0
            neighbors[(nx, ny, nz)] += 1
    for x, y, z in neighbors:
        if (x, y, z) not in black:
            if neighbors[(x, y, z)] == 2:
                to_black.add((x, y, z))

    black.update(to_black)
    black.difference_update(to_white)

print("Part 2:", len(black))
assert len(black) == 3979
