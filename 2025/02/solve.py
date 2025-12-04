"""Advent Of Code."""

import aoc

ranges = [list(map(int, data.split("-"))) for data in aoc.input_read().split(",")]


# Part 1
def is_invalid(number: str):
    length = len(number)
    if length % 2 != 0:
        return False
    return number[: length // 2] == number[length // 2 :]


answer = 0
for start, end in ranges:
    for number in range(start, end + 1):
        if is_invalid(str(number)):
            answer += number

aoc.check_part1(answer, 30599400849)


# Part 2
def is_invalid(number: str):
    length = len(number)
    for sub_len in range(1, length):
        if length % sub_len == 0:
            sub = number[:sub_len]
            repeated = sub * (length // sub_len)
            if number == repeated and length // sub_len >= 2:
                return True
    return False


answer = 0
for start, end in ranges:
    for number in range(start, end + 1):
        if is_invalid(str(number)):
            answer += number

aoc.check_part2(answer, 46270373595)
