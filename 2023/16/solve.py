"""Advent Of Code #16."""

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

forward_mirrors = set()  # /
backward_mirrors = set()  # \
vertical_splitters = set()  # |
horizontal_splitters = set()  # -
for y, row in enumerate(data):
    for x, value in enumerate(row):
        if value == "/":
            forward_mirrors.add((y, x))
        elif value == "\\":
            backward_mirrors.add((y, x))
        elif value == "|":
            vertical_splitters.add((y, x))
        elif value == "-":
            horizontal_splitters.add((y, x))

DOWN = (1, 0)
UP = (-1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

FORWARD_MIRRORS = {
    DOWN: LEFT,
    UP: RIGHT,
    RIGHT: UP,
    LEFT: DOWN,
}

BACKWARD_MIRROR = {
    DOWN: RIGHT,
    UP: LEFT,
    RIGHT: DOWN,
    LEFT: UP,
}


def check_collision(y, x, dy, dx):
    """Check mirror and splitter collisions."""
    if (y, x) in forward_mirrors:
        return FORWARD_MIRRORS[(dy, dx)], None
    elif (y, x) in backward_mirrors:
        return BACKWARD_MIRROR[(dy, dx)], None
    elif (y, x) in vertical_splitters and (dy, dx) in [RIGHT, LEFT]:
        return UP, (y, x, *DOWN)
    elif (y, x) in horizontal_splitters and (dy, dx) in [UP, DOWN]:
        return LEFT, (y, x, *RIGHT)
    else:
        return (dy, dx), None


def get_energized(y, x, dy, dx):
    """Get amount of energy."""
    energized = set()
    beams = [(y, x, dy, dx)]
    while beams:
        (y, x, dy, dx) = beams[0]
        (dy, dx), beam = check_collision(y, x, dy, dx)
        if beam:
            beams.append(beam)

        while (y, x, dy, dx) not in energized:
            if y < 0 or y > len(data) - 1:
                break
            if x < 0 or x > len(data[0]) - 1:
                break
            energized.add((y, x, dy, dx))
            y += dy
            x += dx
            (dy, dx), beam = check_collision(y, x, dy, dx)
            if beam:
                beams.append(beam)
        del beams[0]

    energized = {(y, x) for (y, x, _, _) in energized}
    return energized


# Part 1
energized = get_energized(0, 0, 0, 1)
print("Part 1:", len(energized))
assert len(energized) == 6921

# Part 2
energized = []
for y in range(len(data)):
    energized.append(len(get_energized(y, 0, 0, 1)))
    energized.append(len(get_energized(y, len(data[0]) - 1, 0, -1)))
for x in range(len(data[0])):
    energized.append(len(get_energized(0, x, 1, 0)))
    energized.append(len(get_energized(len(data) - 1, x, -1, 0)))

print("Part 2:", max(energized))
assert max(energized) == 7594
