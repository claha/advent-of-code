"""Advent Of Code."""

import aoc

batteries = aoc.input_readlines()

# Part 1
answer = 0
for battery in batteries:
    battery = list(battery)
    a = max(battery[:-1])
    b = max(battery[battery.index(a) + 1 :])
    answer += int(a + b)

aoc.check_part1(answer, 17109)

# Part 2
answer = 0
for battery in batteries:
    battery = list(battery)
    a = [max(battery[:-11])]
    for _ in range(11):
        battery = battery[battery.index(a[-1]) + 1 :]
        a.append(max(battery[: len(battery) - (11 - len(a))]))
    answer += int("".join(a))

aoc.check_part2(answer, 169347417057382)
