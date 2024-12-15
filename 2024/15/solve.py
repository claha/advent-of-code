"""Advent Of Code."""

import aoc

W, M = aoc.input_read().split("\n\n")
W = W.split("\n")
M = "".join(M.strip().split("\n"))
walls = set()
boxes = set()

DIR = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


for y in range(len(W)):
    for x in range(len(W[0])):
        if W[y][x] == "#":
            walls.add((y, x))
        if W[y][x] == "O":
            boxes.add((y, x))
        if W[y][x] == "@":
            ry, rx = (y, x)

for m in M:
    dy, dx = DIR[m]

    if (ry + dy, rx + dx) in walls:
        continue
    if (ry + dy, rx + dx) not in boxes:
        ry += dy
        rx += dx
        continue

    n = 1
    while (ry + n * dy, rx + n * dx) in boxes:
        n += 1
    if (ry + n * dy, rx + n * dx) in walls:
        continue
    boxes.remove((ry + dy, rx + dx))
    boxes.add((ry + n * dy, rx + n * dx))
    ry += dy
    rx += dx


value = sum([100 * y + x for (y, x) in boxes])
aoc.check_part1(value, 1486930)


# Part 2
walls = set()
boxes = {}
for y in range(len(W)):
    for x in range(len(W[0])):
        if W[y][x] == "#":
            walls.add((y, 2 * x))
            walls.add((y, 2 * x + 1))
        if W[y][x] == "O":
            boxes[(y, 2 * x)] = (y, 2 * x + 1)
        if W[y][x] == "@":
            ry, rx = (y, 2 * x)


def check(  # noqa: PLR0913
    walls: set[tuple[int, int]],
    boxes: dict[tuple[int, int], tuple[int, int]],
    ry: int,
    rx: int,
    dy: int,
    dx: int,
) -> bool:
    """Check if possible to move and push."""
    ny = ry + dy
    nx = rx + dx
    if (ny, nx) in walls:
        return False

    if (ny, nx) not in boxes and (ny, nx) not in boxes.values():
        return True

    if dx == 0:
        if (ny, nx) in boxes.values():
            return check(walls, boxes, ny, nx, dy, dx) and check(
                walls,
                boxes,
                ny,
                nx - 1,
                dy,
                dx,
            )
        if (ny, nx) in boxes:
            return check(walls, boxes, ny, nx, dy, dx) and check(
                walls,
                boxes,
                ny,
                nx + 1,
                dy,
                dx,
            )
    if dx == -1:
        return check(walls, boxes, ny, nx - 1, dy, dx)
    if dx == 1:
        return check(walls, boxes, ny, nx + 1, dy, dx)

    msg = f"Unknown dx: {dx}"
    raise ValueError(msg)


def move(  # noqa: PLR0913
    walls: set[tuple[int, int]],
    boxes: dict[tuple[int, int], tuple[int, int]],
    ry: int,
    rx: int,
    dy: int,
    dx: int,
) -> None:
    """Move and push in given direction, assumes check passed."""
    nx = rx + dx
    ny = ry + dy
    if (ny, nx) in walls:
        return

    if (ny, nx) not in boxes and (ny, nx) not in boxes.values():
        return

    if dx == 0:
        if (ny, nx) in boxes.values():
            move(walls, boxes, ny, nx, dy, dx)
            move(walls, boxes, ny, nx - 1, dy, dx)
            boxes.pop((ny, nx - 1))
            boxes[(ny + dy, nx - 1)] = (ny + dy, nx)
        elif (ny, nx) in boxes:
            move(walls, boxes, ny, nx, dy, dx)
            move(walls, boxes, ny, nx + 1, dy, dx)
            boxes.pop((ny, nx))
            boxes[(ny + dy, nx)] = (ny + dy, nx + 1)
    elif dx == -1:
        move(walls, boxes, ny, nx - 1, dy, dx)
        boxes.pop((ny, nx - 1))
        boxes[(ny, nx - 2)] = (ny, nx - 1)
    elif dx == 1:
        move(walls, boxes, ny, nx + 1, dy, dx)
        boxes.pop((ny, nx))
        boxes[(ny, nx + 1)] = (ny, nx + 2)


for m in M:
    dy, dx = DIR[m]

    if check(walls, boxes, ry, rx, dy, dx):
        move(walls, boxes, ry, rx, dy, dx)
        ry += dy
        rx += dx

value = sum([100 * y + x for (y, x) in boxes])
aoc.check_part2(value, 1492011)
