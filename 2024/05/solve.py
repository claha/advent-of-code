"""Advent Of Code."""

import aoc

rules, updates = aoc.input_read().split("\n\n")
rules = [list(map(int, rule.split("|"))) for rule in rules.split()]
rules_lut = {}
for a, b in rules:
    rules_lut[b] = set()
    rules_lut[a] = set()
for a, b in rules:
    rules_lut[a].add(b)
rules = rules_lut
updates = [list(map(int, update.split(","))) for update in updates.split("\n")]


def is_first_correct(update: list[int]) -> bool:
    """Check first number in update is correct."""
    return all(u in rules[update[0]] for u in update[1:])


def is_correct(update: list[int]) -> bool:
    """Check that update is correct."""
    if len(update) == 2:  # noqa: PLR2004
        return is_first_correct(update)
    return is_first_correct(update) and is_correct(update[1:])


def get_mid(update: list[int]) -> int:
    """Get the number in the middle."""
    return update[len(update) // 2]


# Part 1
total = sum([get_mid(update) for update in updates if is_correct(update)])
aoc.check_part1(total, 5108)


# Part 2
def fix(update: list[int]) -> list[int]:
    """Fix update so it is correct."""
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            update_mod = update[:]
            update_mod[i], update_mod[j] = update_mod[j], update_mod[i]
            if is_first_correct(update_mod[i:]):
                update = update_mod
                break
    return update


total = 0
for update in updates:
    if is_correct(update):
        continue
    total += get_mid(fix(update))

aoc.check_part2(total, 7380)
