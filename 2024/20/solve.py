"""Advent Of Code."""

from collections import deque
from itertools import combinations

import aoc

grid = aoc.input_readlines()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            start = (y, x)
        elif grid[y][x] == "E":
            end = (y, x)

H = len(grid)
W = len(grid[0])
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs() -> list[int]:
    """Run bfs."""
    q = deque([(*start, [start])])
    seen = {start}
    while q:
        y, x, path = q.popleft()
        if (y, x) == end:
            return path
        for dy, dx in DIR:
            ny = y + dy
            nx = x + dx
            if (
                0 <= ny < H
                and 0 <= nx < W
                and grid[ny][nx] != "#"
                and (ny, nx) not in seen
            ):
                seen.add((ny, nx))
                q.append((ny, nx, [*path, (ny, nx)]))
    return None


def count_cheats(path: list[int], cheat: int) -> int:
    """Count cheats that save 100ps."""
    path_length = len(path) - 1
    cost_start = {yx: i for i, yx in enumerate(path)}
    cost_end = {yx: i for i, yx in enumerate(reversed(path))}
    count = 0
    for (y0, x0), (y1, x1) in combinations(path, 2):
        dist = abs(y1 - y0) + abs(x1 - x0)
        if dist > cheat:
            continue
        if path_length - (cost_start[(y0, x0)] + cost_end[(y1, x1)] + dist) >= 100:  # noqa: PLR2004
            count += 1
    return count


shortest_path = bfs()


# Part 1
aoc.check_part1(count_cheats(shortest_path, cheat=2), 1422)

# Pat 2
aoc.check_part2(count_cheats(shortest_path, cheat=20), 1009299)
