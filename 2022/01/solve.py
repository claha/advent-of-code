"""Advent Of Code #01."""
with open("input") as f:
    data = [d for d in f.read().split("\n")]


# Part 1
calories = []
cal = 0
for c in data:
    if not c:
        calories.append(cal)
        cal = 0
    else:
        cal += int(c)
calories = sorted(calories)
print("Part 1:", calories[-1])
assert calories[-1] == 73211


# Part 2
print("Part 2:", sum(calories[-3:]))
assert sum(calories[-3:]) == 213958
