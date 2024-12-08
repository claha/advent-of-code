"""Advent Of Code."""

import aoc

data = aoc.input_readlines()

ROWS = len(data)
COLS = len(data[0])
obstacles = set()

for r in range(ROWS):
    for c in range(COLS):
        if data[r][c] == "#":
            obstacles.add((r, c))
        elif data[r][c] == "^":
            y, x = r, c


rotate = {
    (-1, 0): (0, 1),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (0, 1): (1, 0),
}


def get_route(
    y: int,
    x: int,
    dy: int,
    dx: int,
    obstacles: set[int],
) -> tuple[set[tuple[int, int]], bool]:
    """Get route while checking for loops."""
    loop = False
    path = set()
    while 0 <= y < ROWS and 0 <= x < COLS:
        if (y, x, dy, dx) in path:
            loop = True
            break

        path.add((y, x, dy, dx))
        y += dy
        x += dx
        if (y, x) in obstacles:
            y -= dy
            x -= dx
            dy, dx = rotate[(dy, dx)]

    path = {(y, x) for (y, x, _, _) in path}
    return path, loop


# Part 1
path, _ = get_route(y, x, -1, 0, obstacles)
aoc.check_part1(len(path), 4663)


# Part 2
options = 0
for r, c in path:
    if (r, c) == (y, x):
        continue
    _, loop = get_route(y, x, -1, 0, obstacles.union({(r, c)}))
    options += loop
aoc.check_part2(options, 1530)
