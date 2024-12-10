"""Advent Of Code."""

import aoc

data = aoc.input_readlines()
ROWS = len(data)
COLS = len(data[0])


def possible_moves(y: int, x: int) -> list[tuple[int, int]]:
    """Possible moves."""
    return ((y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x))


def bfs(start: tuple[int, int], *, exhaustive: bool) -> int:
    """BFS."""
    moves = [start]

    reached = []

    while moves:
        moves_next = []
        for y, x in moves:
            for yn, xn in possible_moves(y, x):
                if not (0 <= yn < ROWS and 0 <= xn < COLS):
                    continue

                if int(data[yn][xn]) - int(data[y][x]) != 1:
                    continue

                if data[yn][xn] == "9":
                    reached.append((yn, xn))
                    continue

                moves_next.append((yn, xn))

        moves = moves_next
        if not exhaustive:
            moves = set(moves)

    if not exhaustive:
        reached = set(reached)

    return len(reached)


trailheads = []
for y in range(ROWS):
    trailheads.extend((y, x) for x in range(COLS) if data[y][x] == "0")

# Part 1
score = 0
for y, x in trailheads:
    score += bfs((y, x), exhaustive=False)
aoc.check_part1(score, 582)

# Part 2
score = 0
for y, x in trailheads:
    score += bfs((y, x), exhaustive=True)
aoc.check_part2(score, 1302)
