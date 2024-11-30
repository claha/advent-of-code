"""Advent Of Code #24."""

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

valley = [row[1:-1] for row in data[1:-1]]


def possible_moves(y, x):
    """Possible moves."""
    return ((y, x), (y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x))


def bfs(start, stop, step=1):
    """Search kinda like bfs."""
    moves = {start}

    while True:
        moves_next = set()
        for y, x in moves:
            for yn, xn in possible_moves(y, x):
                if (yn, xn) == stop:
                    return step

                if not (0 <= yn < height and 0 <= xn < width):
                    continue

                # Check if any blizzard will also be here
                if valley[yn][(xn - step) % width] == ">":
                    continue
                if valley[yn][(xn + step) % width] == "<":
                    continue
                if valley[(yn - step) % height][xn] == "v":
                    continue
                if valley[(yn + step) % height][xn] == "^":
                    continue

                moves_next.add((yn, xn))

        moves = moves_next

        # No were to move, start over (i.e. stood still a few step)
        if not moves:
            moves.add(start)

        step += 1


height, width = len(valley), len(valley[0])
start, stop = (-1, 0), (height, width - 1)


# Part 1
steps = bfs(start, stop)
print("Part 1:", steps)
assert steps == 311

# Part 2
steps = bfs(start, stop, bfs(stop, start, steps))
print("Part 2:", steps)
assert steps == 869
