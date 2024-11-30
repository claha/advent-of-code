"""Advent Of Code #22."""

import re

with open("input") as f:
    data = f.read().split("\n\n")

board = data[0].split("\n")
moves = re.findall(r"(\d+|R|L)", data[1])

width = max(len(row) for row in board)
for i in range(len(board)):
    board[i] += " " * (width - len(board[i]))

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

R = {
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
    UP: RIGHT,
}

L = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
}

S = {
    RIGHT: 0,
    DOWN: 1,
    LEFT: 2,
    UP: 3,
}


def out_of_range(y, x, board):
    """Check if out of range."""
    if y > len(board) - 1:
        return True
    elif y < 0:
        return True
    elif x > len(board[y]) - 1:
        return True
    elif x < 0:
        return True
    elif board[y][x] == " ":
        return True
    return False


# Part 1
y = 0
x = board[y].index(".")

dy = 0
dx = 1

for move in moves:
    if move == "R":
        dy, dx = R[(dy, dx)]
    elif move == "L":
        dy, dx = L[(dy, dx)]
    else:
        for _ in range(int(move)):
            if out_of_range(y + dy, x + dx, board):
                y_old, x_old = y, x
                while not out_of_range(y - dy, x - dx, board):
                    y -= dy
                    x -= dx
                if board[y][x] == "#":
                    y, x = y_old, x_old
            elif board[y + dy][x + dx] == "#":
                break
            else:
                y, x = y + dy, x + dx

password = 1000 * (y + 1) + (x + 1) * 4 + S[(dy, dx)]
print("Part 1:", password)
assert password == 189140


# Part 2

# ....11112222 0
# ....11112222
# ....11112222
# ....11112222
# ....3333.... N
# ....3333....
# ....3333....
# ....3333....
# 44445555.... 2 * N
# 44445555....
# 44445555....
# 44445555....
# 6666........ 3 * N
# 6666........
# 6666........
# 6666........

N = 50


def wrap(y, x, dy, dx, board):
    """Wrap around the cube."""
    if y < N:
        if x < 2 * N:
            if (dy, dx) == UP:
                y, x = x + 2 * N, 0
                dy, dx = RIGHT
            elif (dy, dx) == LEFT:
                y, x = 3 * N - 1 - y, 0
                dy, dx = RIGHT
            else:
                raise
        else:
            if (dy, dx) == DOWN:
                y, x = x - N, 2 * N - 1
                dy, dx = LEFT
            elif (dy, dx) == UP:
                y, x = 4 * N - 1, x - 2 * N
                dy, dx = UP
            elif (dy, dx) == RIGHT:
                y, x = 3 * N - 1 - y, 2 * N - 1
                dy, dx = LEFT
            else:
                raise
    elif y < 2 * N:
        if x < 2 * N:
            if (dy, dx) == LEFT:
                y, x = 2 * N, y - N
                dy, dx = DOWN
            elif (dy, dx) == RIGHT:
                y, x = N - 1, N + y
                dy, dx = UP
            else:
                raise
        else:
            raise
    elif y < 3 * N:
        if x < N:
            if (dy, dx) == LEFT:
                y, x = 3 * N - 1 - y, N
                dy, dx = RIGHT
            elif (dy, dx) == UP:
                y, x = N + x, N
                dy, dx = RIGHT
            else:
                raise
        else:
            if (dy, dx) == DOWN:
                y, x = 2 * N + x, N - 1
                dy, dx = LEFT
            elif (dy, dx) == RIGHT:
                y, x = 3 * N - 1 - y, 3 * N - 1
                dy, dx = LEFT
            else:
                raise
    else:
        assert x < N
        if (dy, dx) == LEFT:
            y, x = 0, y - 2 * N
            dy, dx = DOWN
        elif (dy, dx) == DOWN:
            y, x = 0, 2 * N + x
            dy, dx = DOWN
        elif (dy, dx) == RIGHT:
            y, x = 3 * N - 1, y - 2 * N
            dy, dx = UP
        else:
            raise

    return y, x, dy, dx


y = 0
x = board[y].index(".")

dy = 0
dx = 1

for move in moves:
    if move == "R":
        dy, dx = R[(dy, dx)]
    elif move == "L":
        dy, dx = L[(dy, dx)]
    else:
        for _ in range(int(move)):
            if out_of_range(y + dy, x + dx, board):
                y_old, x_old = y, x
                dy_old, dx_old = dy, dx
                y, x, dy, dx = wrap(y, x, dy, dx, board)
                if board[y][x] == "#":
                    y, x = y_old, x_old
                    dy, dx = dy_old, dx_old
            elif board[y + dy][x + dx] == "#":
                break
            else:
                y, x = y + dy, x + dx

password = 1000 * (y + 1) + (x + 1) * 4 + S[(dy, dx)]
print("Part 2:", password)
assert password == 115063
