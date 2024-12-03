"""Advent Of Code."""

import aoc

left = []
right = []

for line in aoc.input_readlines():
    first, second = map(int, line.split())
    left.append(first)
    right.append(second)
left = sorted(left)
right = sorted(right)

# Part 1
diff = [abs(values[0] - values[1]) for values in zip(left, right)]
answer = sum(diff)
aoc.check_part1(answer, 2580760)

# Part 2
answer = 0
for value in left:
    answer += value * right.count(value)
aoc.check_part2(answer, 25358365)
