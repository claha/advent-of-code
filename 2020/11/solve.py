"""Advent Of Code #11."""

with open("input") as f:
    data = f.read()

FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"

waiting_area_original = [list(line) for line in data.splitlines()]


def count_occupied_neighbours(waiting_area, row, col, look_further=False):
    """Count number of occupied neighbours."""
    height = len(waiting_area)
    width = len(waiting_area[0])
    count = 0
    for delta_row, delta_col in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        new_row = row + delta_row
        new_col = col + delta_col
        while 0 <= new_row < height and 0 <= new_col < width:
            if waiting_area[new_row][new_col] == OCCUPIED_SEAT:
                count += 1
                break
            elif waiting_area[new_row][new_col] == EMPTY_SEAT:
                break
            new_row += delta_row
            new_col += delta_col
            if not look_further:
                break
    return count


def count_occupied_seats(waiting_area):
    """Count number of occupied seats."""
    count = 0
    for row in range(len(waiting_area)):
        for col in range(len(waiting_area[0])):
            if waiting_area[row][col] == OCCUPIED_SEAT:
                count += 1
    return count


# Part 1
waiting_area = [waiting_row[:] for waiting_row in waiting_area_original]
while True:
    change = []

    for row in range(len(waiting_area)):
        for col in range(len(waiting_area[0])):
            state = waiting_area[row][col]
            if state == EMPTY_SEAT:
                if count_occupied_neighbours(waiting_area, row, col) == 0:
                    change.append((row, col, OCCUPIED_SEAT))
            elif state == OCCUPIED_SEAT:
                if count_occupied_neighbours(waiting_area, row, col) >= 4:  # Part 1
                    change.append((row, col, EMPTY_SEAT))

    if not change:
        break
    for r, c, s in change:
        waiting_area[r][c] = s

count = count_occupied_seats(waiting_area)
print("Part 1:", count)
assert count == 2359

# Part 2
waiting_area = [waiting_row[:] for waiting_row in waiting_area_original]
while True:
    change = []

    for row in range(len(waiting_area)):
        for col in range(len(waiting_area[0])):
            state = waiting_area[row][col]
            if state == EMPTY_SEAT:
                if count_occupied_neighbours(waiting_area, row, col, True) == 0:
                    change.append((row, col, OCCUPIED_SEAT))
            elif state == OCCUPIED_SEAT:
                if count_occupied_neighbours(waiting_area, row, col, True) >= 5:
                    change.append((row, col, EMPTY_SEAT))

    if not change:
        break
    for r, c, s in change:
        waiting_area[r][c] = s

count = count_occupied_seats(waiting_area)
print("Part 2:", count)
assert count == 2131
