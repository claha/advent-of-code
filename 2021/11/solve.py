"""Advent Of Code #11."""

with open("input") as f:
    cavern = [list(map(int, list(d))) for d in f.read().split()]

SIZE = 10
ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Part 1
flashes = 0
for _ in range(100):
    for y in range(SIZE):
        for x in range(SIZE):
            cavern[y][x] += 1

    to_flash = []

    for y in range(SIZE):
        for x in range(SIZE):
            if cavern[y][x] == 10:
                to_flash.append((y, x))
                cavern[y][x] += 1
                flashes += 1

    while to_flash:
        (y, x) = to_flash.pop(0)
        for dy, dx in ADJ:
            if 0 <= y + dy < SIZE and 0 <= x + dx < SIZE:
                cavern[y + dy][x + dx] += 1
                if cavern[y + dy][x + dx] == 10:
                    to_flash.append((y + dy, x + dx))
                    cavern[y + dy][x + dx] += 1
                    flashes += 1

    for y in range(SIZE):
        for x in range(SIZE):
            if cavern[y][x] > 9:
                cavern[y][x] = 0

print("Part 1:", flashes)
assert flashes == 1603


# Part 2
step = 101
while True:
    for y in range(SIZE):
        for x in range(SIZE):
            cavern[y][x] += 1

    to_flash = []

    for y in range(SIZE):
        for x in range(SIZE):
            if cavern[y][x] == 10:
                to_flash.append((y, x))
                cavern[y][x] += 1
                flashes += 1

    while to_flash:
        (y, x) = to_flash.pop(0)
        for dy, dx in ADJ:
            if 0 <= y + dy < SIZE and 0 <= x + dx < SIZE:
                cavern[y + dy][x + dx] += 1
                if cavern[y + dy][x + dx] == 10:
                    to_flash.append((y + dy, x + dx))
                    cavern[y + dy][x + dx] += 1
                    flashes += 1

    num_flashes = 0
    for y in range(SIZE):
        for x in range(SIZE):
            if cavern[y][x] > 9:
                cavern[y][x] = 0
                num_flashes += 1

    if num_flashes == SIZE * SIZE:
        break
    step += 1

print("Part 2:", step)
assert step == 222
