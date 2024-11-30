"""Advent Of Code #09."""

with open("input") as f:
    data = [d.strip() for d in f.readlines()]

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx)

# Part 1
r = 0
h = len(data)
w = len(data[0])
low_points = []
for y in range(h):
    for x in range(w):
        low = True
        for dy, dx in DELTA:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                if data[y][x] >= data[y + dy][x + dx]:
                    low = False
                    break
        if low:
            low_points.append((y, x))
            r += 1 + int(data[y][x])

print("Part 1:", r)
assert r == 512


# Part 2
def bfs(data, point):
    """Breadth first search."""
    visited = []
    queue = []
    visited.append(point)
    queue.append(point)

    while queue:
        (y, x) = queue.pop(0)
        for dy, dx in DELTA:
            if 0 <= y + dy < h and 0 <= x + dx < w:
                if data[y + dy][x + dx] != "9" and data[y + dy][x + dx] > data[y][x]:
                    if (y + dy, x + dx) not in visited:
                        visited.append((y + dy, x + dx))
                        queue.append((y + dy, x + dx))
    return len(visited)


basins = []
for point in low_points:
    basins.append(bfs(data, point))
basins = sorted(basins)
print("Part 2:", basins[-1] * basins[-2] * basins[-3])
assert basins[-1] * basins[-2] * basins[-3] == 1600104
