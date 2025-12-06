"""Advent Of Code."""

import aoc

problems = [line.strip().split() for line in aoc.input_readlines()]
problems = list(map(list, zip(*problems)))

# Part 1
answer = 0
for problem in problems:
    answer += eval(problem[-1].join(problem[:-1]))
aoc.check_part1(answer, 5733696195703)

# Part 2
problems = aoc.input_readlines()
answer = 0
numbers = [""]

for col in range(len(problems[0]) - 1, -1, -1):
    for i, line in enumerate(problems):
        if len(line) >= col + 1 and line[col] in ["+", "*"]:
            answer += eval(line[col].join(numbers))
            numbers = []
            break
        elif len(line) >= col + 1:
            numbers[-1] += line[col]
    if not numbers or (numbers and numbers[-1].strip()):
        numbers.append("")

aoc.check_part2(answer, 10951882745757)
