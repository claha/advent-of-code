"""Advent Of Code #14."""

with open("input") as f:
    data = [list(line.strip()) for line in f.readlines()]

ROUND = "O"
CUBE = "#"
EMPTY = "."
round_rocks = set()
cube_rocks = set()

HEIGHT = len(data)
WIDTH = len(data[0])


def calculate_load(round_rocks):
    """Calc load of rocks."""
    load = 0
    for y, _ in round_rocks:
        load += HEIGHT - y
    return load


def check(y, x, round_rocks, cube_rocks):
    """Check bounds."""
    if y < 0 or y >= HEIGHT:
        return False
    if x < 0 or x >= WIDTH:
        return False
    if (y, x) in round_rocks:
        return False
    if (y, x) in cube_rocks:
        return False
    return True


def tilt(round_rocks, cube_rocks, dy, dx):
    """Tilt board."""
    if dx == 0:
        if dy == -1:
            Y = range(HEIGHT)
        else:
            Y = range(HEIGHT - 1, -1, -1)
        for y in Y:
            for x in range(WIDTH):
                if (y, x) not in round_rocks:
                    continue
                round_rocks.remove((y, x))
                new_y = y
                new_x = x
                while check(new_y + dy, new_x + dx, round_rocks, cube_rocks):
                    new_y += dy
                    new_x += dx
                round_rocks.add((new_y, new_x))
    else:
        if dx == -1:
            X = range(WIDTH)
        else:
            X = range(WIDTH - 1, -1, -1)
        for x in X:
            for y in range(HEIGHT):
                if (y, x) not in round_rocks:
                    continue
                round_rocks.remove((y, x))
                new_y = y
                new_x = x
                while check(new_y + dy, new_x + dx, round_rocks, cube_rocks):
                    new_y += dy
                    new_x += dx
                round_rocks.add((new_y, new_x))


#
for y, row in enumerate(data):
    for x, item in enumerate(row):
        if item == ROUND:
            round_rocks.add((y, x))
        elif item == CUBE:
            cube_rocks.add((y, x))

# Part 1
tilt(round_rocks, cube_rocks, dy=-1, dx=0)
load = calculate_load(round_rocks)
print("Part 1:", load)
assert load == 111339


# Part 2
def find_repeating_pattern(lst):
    """Find repeating pattern."""
    n = len(lst)
    for pattern_length in range(1, n // 2 + 1):
        for start_index in range(pattern_length):
            pattern = lst[start_index : start_index + pattern_length]
            is_repeating = all(
                lst[i : i + pattern_length] == pattern
                for i in range(start_index, n - pattern_length + 1, pattern_length)
            )
            if is_repeating:
                return pattern, start_index
    return None, None


def get_value_at_index(repeating_pattern, start_index, desired_index):
    """Get value from index."""
    pattern_length = len(repeating_pattern)
    relative_index = (desired_index - start_index) % pattern_length
    return repeating_pattern[relative_index]


tilt(round_rocks, cube_rocks, dy=0, dx=-1)
tilt(round_rocks, cube_rocks, dy=1, dx=0)
tilt(round_rocks, cube_rocks, dy=0, dx=1)

N = 1000000000
loads = [calculate_load(round_rocks)]
while True:
    tilt(round_rocks, cube_rocks, dy=-1, dx=0)
    tilt(round_rocks, cube_rocks, dy=0, dx=-1)
    tilt(round_rocks, cube_rocks, dy=1, dx=0)
    tilt(round_rocks, cube_rocks, dy=0, dx=1)
    loads.append(calculate_load(round_rocks))
    pattern, start = find_repeating_pattern(loads)
    if pattern:
        if (len(loads) - start) % len(pattern) == 0:
            break
        load = get_value_at_index(pattern, start, N - 1)

pattern, start = find_repeating_pattern(loads)
load = get_value_at_index(pattern, start, N - 1)
print("Part 2:", load)
assert load == 93736
