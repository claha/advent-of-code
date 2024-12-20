"""Advent Of Code."""

import re

import aoc

data = aoc.input_read()

RE_MUL = r"mul\(\d{1,3},\d{1,3}\)"
RE_DO = r"do\(\)"
RE_DONT = r"don't\(\)"
RE_OR = r"|"
exps = re.findall(RE_MUL + RE_OR + RE_DO + RE_OR + RE_DONT, data)


def mul(exp: str) -> int:
    """Extrct a and b and multiply them."""
    a, b = map(int, re.findall(r"\d{1,3}", exp))
    return a * b


# Part 1
total = sum(mul(exp) for exp in exps if re.match(RE_MUL, exp))
aoc.check_part1(total, 159833790)

# Part 2
enabled = True
total = 0
for exp in exps:
    if re.match(RE_DONT, exp):
        enabled = False
    elif re.match(RE_DO, exp):
        enabled = True
    elif enabled and re.match(RE_MUL, exp):
        total += mul(exp)

aoc.check_part2(total, 89349241)
