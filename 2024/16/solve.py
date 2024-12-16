"""Advent Of Code."""

from collections import defaultdict, deque
from heapq import heappop, heappush

import aoc

grid = []
for y, row in enumerate(aoc.input_readlines()):
    grid.append(list(row))
    if "S" in row:
        start = (y, row.index("S"))
    if "E" in row:
        end = (y, row.index("E"))

ROWS = len(grid)
COLS = len(grid[0])

DIRECTIONS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

ROTATIONS = {
    "N": {"W", "E"},
    "E": {"N", "S"},
    "S": {"E", "W"},
    "W": {"S", "N"},
}

INF = float("inf")


def dijkstra(
    grid: list[list[int]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> float:
    """Run Dijkstra's algorithm."""
    visited = defaultdict(lambda: INF)
    pq = []

    heappush(pq, (0, start[0], start[1], "E"))

    while pq:
        cost, y, x, direction = heappop(pq)

        if (y, x) == end:
            return cost

        if visited[(y, x, direction)] <= cost:
            continue
        visited[(y, x, direction)] = cost

        dy, dx = DIRECTIONS[direction]
        ny, nx = y + dy, x + dx
        if 0 <= ny < ROWS and 0 <= nx < COLS and grid[ny][nx] != "#":
            heappush(pq, (cost + 1, ny, nx, direction))

        for new_direction in ROTATIONS[direction]:
            new_cost = cost + 1000
            heappush(pq, (new_cost, y, x, new_direction))

    return INF


# Part 1
lowest_score = dijkstra(grid, start, end)
aoc.check_part1(lowest_score, 94436)

# Part 2
all_seen = {}
queue = deque([(start[0], start[1], "E", 0, set())])
lowest_score_seen = {}

while queue:
    cr, cc, cd, cs, path = queue.popleft()
    path.add((cr, cc))
    all_seen[(cr, cc, cd)] = min(cs, all_seen.get((cr, cc, cd), INF))

    if (cr, cc) == end and cs == lowest_score:
        lowest_score_seen = path.union(lowest_score_seen)

    nr = cr + DIRECTIONS[cd][0]
    nc = cc + DIRECTIONS[cd][1]
    ns = cs + 1
    if grid[nr][nc] != "#" and ns <= all_seen.get((nr, nc, cd), INF):
        new_path = path.copy()
        all_seen[(nr, nc, cd)] = ns
        queue.append((nr, nc, cd, ns, new_path))

    for nd in ROTATIONS[cd]:
        nr = cr + DIRECTIONS[nd][0]
        nc = cc + DIRECTIONS[nd][1]
        ns = cs + 1001
        if grid[nr][nc] != "#" and ns <= all_seen.get((nr, nc, nd), INF):
            new_path = path.copy()
            all_seen[(nr, nc, nd)] = ns
            queue.append((nr, nc, nd, ns, new_path))

aoc.check_part2(len(lowest_score_seen), 481)
