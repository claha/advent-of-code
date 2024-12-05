"""Advent Of Code."""

import aoc

data = aoc.input_readlines()


def count_xmas(seq: str) -> int:
    """Count XMAS and SAMX."""
    return seq.count("XMAS") + seq.count("SAMX")


# Part 1
count = 0
for row in data:
    count += count_xmas(row)

for c in range(len(data[0])):
    col = "".join(row[c] for row in data)
    count += count_xmas(col)

checked = set()
for r in range(len(data)):
    for c in range(len(data[r])):
        diag = ""
        dr = 0
        dc = 0
        while (
            r + dr < len(data) and r + dr >= 0 and c + dc < len(data[r]) and c + dc >= 0
        ):
            diag += data[r + dr][c + dc]
            checked.add((r + dr, c + dc))
            dr += 1
            dc += 1
            if (r + dr, c + dc) in checked:
                break
        count += count_xmas(diag)

checked = set()
for r in range(len(data)):
    for c in range(len(data[r])):
        diag = ""
        dr = 0
        dc = 0
        while (
            r + dr < len(data) and r + dr >= 0 and c + dc < len(data[r]) and c + dc >= 0
        ):
            diag += data[r + dr][c + dc]
            checked.add((r + dr, c + dc))
            dr += 1
            dc -= 1
            if (r + dr, c + dc) in checked:
                break
        count += count_xmas(diag)

aoc.check_part1(count, 2662)

# Part 2
MS = {"M", "S"}
count = 0
for r in range(1, len(data) - 1):
    for c in range(1, len(data[r]) - 1):
        if data[r][c] != "A":
            continue
        if {data[r - 1][c - 1], data[r + 1][c + 1]} != MS:
            continue
        if {data[r - 1][c + 1], data[r + 1][c - 1]} != MS:
            continue
        count += 1

aoc.check_part2(count, 2034)
