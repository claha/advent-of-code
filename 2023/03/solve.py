"""Advent Of Code #03."""
with open("input") as f:
    schematic = [line.strip() for line in f.readlines()]


DELTA = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def is_number(c):
    """Check if char is number."""
    return "0" <= c <= "9"


def is_symbol(c):
    """Check if char is symbol."""
    return not is_number(c) and c != "."


sum_part_numbers = 0
num = ""
has_symbol = False
is_gear = None
gears = {}
for row in range(len(schematic)):
    for col in range(len(schematic[row])):
        c = schematic[row][col]
        if is_number(c):
            num += c
            for dy, dx in DELTA:
                try:
                    if is_symbol(schematic[row + dy][col + dx]):
                        has_symbol = True
                        if schematic[row + dy][col + dx] == "*":
                            is_gear = (row + dy, col + dx)
                except Exception:
                    pass
        elif num:
            if has_symbol:
                sum_part_numbers += int(num)
                if is_gear:
                    if is_gear not in gears:
                        gears[is_gear] = []
                    gears[is_gear].append(int(num))

            num = ""
            has_symbol = False
            is_gear = False

print("Part 1:", sum_part_numbers)
assert sum_part_numbers == 527364

gear_ratios = 0
for gear in gears.values():
    if len(gear) == 2:
        gear_ratios += gear[0] * gear[1]
print("Part 2:", gear_ratios)
assert gear_ratios == 79026871
