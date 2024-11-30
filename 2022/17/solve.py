"""Advent Of Code #17."""

with open("input") as f:
    moves = f.read().strip()

LEFT = "<"
RIGHT = ">"

# Shapes
# Note: (y,x) is ordered such that shape[0] holds one of the points with min x
# and shape[-1] holds one of the points with max x
shapes = []

# ####
shapes.append([(0, 0), (0, 1), (0, 2), (0, 3)])

# .#.
# ###
# .#.
# shapes.append([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])
shapes.append([(1, 0), (0, 1), (2, 1), (1, 2)])

# ..#
# ..#
# ###
# shapes.append([(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)])
shapes.append([(2, 0), (0, 2), (1, 2), (2, 1), (2, 2)])

# #
# #
# #
# #
shapes.append([(0, 0), (1, 0), (2, 0), (3, 0)])

# ##
# ##
shapes.append([(0, 0), (0, 1), (1, 0), (1, 1)])


def move(shape, dy, dx):
    """Move shape dy, dx."""
    for i in range(len(shape)):
        shape[i] = (shape[i][0] + dy, shape[i][1] + dx)


def get_max_y(shape):
    """Get max y."""
    return max(shape[-1][0], shape[-2][0])


def collide(board, shape):
    """Check collision."""
    if shape[0][1] < 0:
        return True
    if shape[-1][1] > 6:
        return True
    return board & set(shape)


# Part 1
board = {(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)}
board_min_y = 4
board_max_y = 4
m = 0
N = 2022
i = 0
while i < N:
    shape = shapes[i % len(shapes)].copy()
    move(shape, dy=0, dx=2)
    move(shape, dy=board_min_y - board_max_y - get_max_y(shape), dx=0)

    while True:
        if moves[m] == RIGHT:
            move(shape, dy=0, dx=1)
            if collide(board, shape):
                move(shape, dy=0, dx=-1)
        elif moves[m] == LEFT:
            move(shape, dy=0, dx=-1)
            if collide(board, shape):
                move(shape, dy=0, dx=1)

        move(shape, dy=1, dx=0)
        if collide(board, shape):
            move(shape, dy=-1, dx=0)
            m = (m + 1) % len(moves)
            break

        m = (m + 1) % len(moves)

    for y, x in shape:
        board.add((y, x))
        board_min_y = min(board_min_y, y)

    i += 1

height = max(y for y, _ in board) - board_min_y
print("Part 1:", height)
assert height == 3232


# Part 2
board = {(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)}
board_min_y = 4
board_max_y = 4
m = 0
cache = {}
found = False
N = 1000000000000
i = 0
while i < N:
    shape = shapes[i % len(shapes)].copy()
    move(shape, dy=0, dx=2)
    move(shape, dy=board_min_y - board_max_y - get_max_y(shape), dx=0)

    while True:
        if moves[m] == RIGHT:
            move(shape, dy=0, dx=1)
            if collide(board, shape):
                move(shape, dy=0, dx=-1)
        elif moves[m] == LEFT:
            move(shape, dy=0, dx=-1)
            if collide(board, shape):
                move(shape, dy=0, dx=1)

        move(shape, dy=1, dx=0)
        if collide(board, shape):
            move(shape, dy=-1, dx=0)
            m = (m + 1) % len(moves)
            break

        m = (m + 1) % len(moves)

    for y, x in shape:
        board.add((y, x))
        board_min_y = min(board_min_y, y)

    i += 1

    if i < 2022 or found:
        continue

    key = (i % len(shapes), m)
    if key not in cache:
        cache[key] = (board_max_y - board_min_y, i)
    elif not found:
        dheight = board_max_y - board_min_y - cache[key][0]
        di = i - cache[key][1]
        num_cycles = (N - i) // di
        offset = dheight * num_cycles
        i += di * num_cycles
        found = True

height = max(y for y, _ in board) - board_min_y
print("Part 2:", height + offset)
assert height + offset == 1585632183915
