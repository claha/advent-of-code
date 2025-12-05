"""Advent Of Code."""

import aoc

ranges = []
ids = []
in_ranges = True
for line in aoc.input_readlines():
    if line.strip() == "":
        in_ranges = False
        continue
    if in_ranges:
        start, end = map(int, line.strip().split("-"))
        ranges.append((start, end))
    else:
        ids.append(int(line.strip()))

sorted_ranges = sorted(ranges)
non_overlapping_ranges = [sorted_ranges[0]]

for current in sorted_ranges[1:]:
    last = non_overlapping_ranges[-1]
    if current[0] <= last[1] + 1:
        non_overlapping_ranges[-1] = (last[0], max(last[1], current[1]))
    else:
        non_overlapping_ranges.append(current)


# Part 1
def is_in_range(value, ranges):
    for start, end in ranges:
        if start <= value <= end:
            return True
    return False


answer = 0
for id_val in ids:
    if is_in_range(id_val, non_overlapping_ranges):
        answer += 1

aoc.check_part1(answer, 520)

# Part 2
answer = 0
for start, end in non_overlapping_ranges:
    answer += end - start + 1

aoc.check_part2(answer, 347338785050515)
