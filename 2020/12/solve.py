"""Advent Of Code #12."""
with open("input") as f:
    data = f.read().splitlines()

instructions = [(instruction[0], int(instruction[1:])) for instruction in data]

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
LEFT = "L"
RIGHT = "R"
FORWARD = "F"

# Part 1
(y, x, d) = (0, 0, EAST)

for action, value in instructions:
    # Pre process action
    if action == FORWARD:
        action = d
    elif action == RIGHT:
        action = LEFT
        if value == 90:
            value = 270
        elif value == 270:
            value = 90

    # Handle action
    if action == NORTH:
        y += value
    elif action == SOUTH:
        y -= value
    elif action == EAST:
        x += value
    elif action == WEST:
        x -= value
    elif action == LEFT:
        if value == 90:
            if d == NORTH:
                d = WEST
            elif d == SOUTH:
                d = EAST
            elif d == EAST:
                d = NORTH
            elif d == WEST:
                d = SOUTH
        elif value == 180:
            if d == NORTH:
                d = SOUTH
            elif d == SOUTH:
                d = NORTH
            elif d == EAST:
                d = WEST
            elif d == WEST:
                d = EAST
        elif value == 270:
            if d == NORTH:
                d = EAST
            elif d == SOUTH:
                d = WEST
            elif d == EAST:
                d = SOUTH
            elif d == WEST:
                d = NORTH
        else:
            raise Exception("Not able to rotate %d" % value)
    elif action == RIGHT:
        raise Exception("There should be no action: R")

distance = abs(y) + abs(x)
print("Part 1:", distance)
assert distance == 882

# Part 2
(y, x) = (0, 0)
(wy, wx) = (1, 10)

for action, value in instructions:
    # Pre process action
    if action == RIGHT:
        action = LEFT
        if value == 90:
            value = 270
        elif value == 270:
            value = 90

    # Handle action
    if action == NORTH:
        wy += value
    elif action == SOUTH:
        wy -= value
    elif action == EAST:
        wx += value
    elif action == WEST:
        wx -= value
    elif action == LEFT:
        dy = wy - y
        dx = wx - x
        if value == 90:
            dy, dx = dx, -dy
        elif value == 180:
            dy, dx = -dy, -dx
        elif value == 270:
            dy, dx = -dx, dy
        else:
            raise Exception("Not able to rotate %d" % value)
        wy = dy + y
        wx = dx + x
    elif action == RIGHT:
        raise Exception("There should be no action: R")
    elif action == FORWARD:
        dy = wy - y
        dx = wx - x
        y += value * dy
        x += value * dx
        wy = y + dy
        wx = x + dx

distance = abs(y) + abs(x)
print("Part 2:", distance)
assert distance == 28885
