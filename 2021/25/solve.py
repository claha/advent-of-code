"""Advent Of Code #25."""
with open("input") as f:
    data = [line.strip() for line in f.readlines()]

y_max = len(data)
x_max = len(data[0])

herd = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        herd[(y, x)] = data[y][x]


def move(herd, cucumber, dy, dx, y_max, x_max):
    """Move a herd."""
    moves = []
    for (y, x) in herd:
        if herd[(y, x)] != cucumber:
            continue
        y_next = (y + dy) % y_max
        x_next = (x + dx) % x_max
        if herd[(y_next, x_next)] == ".":
            moves.append(((y, x), (y_next, x_next)))

    for (y, x), (y_next, x_next) in moves:
        herd[(y, x)] = "."
        herd[(y_next, x_next)] = cucumber

    return len(moves)


step = 1
while move(herd, ">", 0, 1, y_max, x_max) + move(herd, "v", 1, 0, y_max, x_max):
    step += 1


# Part 1
print("Part 1:", step)
assert step == 400
