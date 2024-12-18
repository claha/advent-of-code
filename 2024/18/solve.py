"""Advent Of Code."""

import heapq

import aoc

falling_bytes = [list(map(int, line.split(","))) for line in aoc.input_readlines()]
SIZE = 71
start = (0, 0)
end = (SIZE - 1, SIZE - 1)


def simulate_corruption(falling_bytes: list[int], steps: int) -> list[list[bool]]:
    """Simulate falling bytes."""
    grid = [[False] * SIZE for _ in range(SIZE)]
    for i, (x, y) in enumerate(falling_bytes):
        if i >= steps:
            break
        grid[y][x] = True
    return grid


def dijkstra(
    grid: list[list[bool]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> int:
    """Run dijkstra."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    heap = [(0, start)]

    while heap:
        dist, (x, y) = heapq.heappop(heap)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < SIZE
                and 0 <= ny < SIZE
                and not grid[ny][nx]
                and (nx, ny) not in visited
            ):
                heapq.heappush(heap, (dist + 1, (nx, ny)))

    return float("inf")


# Part 1
steps = 1024
corrupted_grid = simulate_corruption(falling_bytes, steps)
shortest_path_length = dijkstra(corrupted_grid, start, end)

aoc.check_part1(shortest_path_length, 436)

# Part 2
while True:
    corrupted_grid = simulate_corruption(falling_bytes, steps)
    shortest_path_length = dijkstra(corrupted_grid, start, end)
    if shortest_path_length == float("inf"):
        break
    steps += 1

aoc.check_part2(falling_bytes[steps - 1], [61, 50])
