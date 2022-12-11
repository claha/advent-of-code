"""Advent Of Code #11."""
from copy import deepcopy
from functools import reduce

with open("input") as f:
    data = [d.strip() for d in f.readlines()]


class Monkey:
    """Monkey."""

    def __init__(self, items, op, test_factor, index_true, index_false):
        """Create a monkey."""
        self.items = items
        ops = op.split(" ")
        if ops[1] == "+":
            self.op = lambda x: x + int(ops[2])
        elif ops[1] == "*":
            if ops[2] == "old":
                self.op = lambda x: x * x
            else:
                self.op = lambda x: x * int(ops[2])
        self.test_factor = test_factor
        self.test = lambda x: x % test_factor == 0
        self.index_true = index_true
        self.index_false = index_false
        self.count = 0


monkies_orig = []
for line in data + [""]:
    if line.startswith("Monkey"):
        pass
    elif line.startswith("Starting items:"):
        items = list(map(int, line.split(": ")[1].split(", ")))
    elif line.startswith("Operation:"):
        operation = line.split(" = ")[1]
    elif line.startswith("Test:"):
        test_factor = int(line.split("divisible by ")[1])
    elif line.startswith("If true:"):
        index_true = int(line.split("throw to monkey ")[1])
    elif line.startswith("If false:"):
        index_false = int(line.split("throw to monkey ")[1])
    else:
        monkies_orig.append(
            Monkey(items, operation, test_factor, index_true, index_false)
        )


# Part 1
monkies = deepcopy(monkies_orig)
for _ in range(20):
    for m in range(len(monkies)):
        while monkies[m].items:
            item = monkies[m].items.pop(0)
            monkies[m].count += 1
            item = monkies[m].op(item)
            item //= 3

            if monkies[m].test(item):
                monkies[monkies[m].index_true].items.append(item)
            else:
                monkies[monkies[m].index_false].items.append(item)

count = sorted([m.count for m in monkies])
print("Part 1:", count[-2] * count[-1])
assert count[-2] * count[-1] == 76728


# Part 2
monkies = deepcopy(monkies_orig)
magic_mod = reduce(lambda x, y: x * y, (monkey.test_factor for monkey in monkies))
for _ in range(10000):
    for m in range(len(monkies)):
        while monkies[m].items:
            item = monkies[m].items.pop(0)
            monkies[m].count += 1
            item = monkies[m].op(item)
            item %= magic_mod

            if monkies[m].test(item):
                monkies[monkies[m].index_true].items.append(item)
            else:
                monkies[monkies[m].index_false].items.append(item)

count = sorted([m.count for m in monkies])
print("Part 2:", count[-2] * count[-1])
assert count[-2] * count[-1] == 21553910156
