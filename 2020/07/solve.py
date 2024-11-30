"""Advent Of Code #07."""

with open("input") as f:
    data = f.read().splitlines()

rules = {}
for rule in data:
    key, values = rule.split(" bags contain ")
    values = values.replace(".", "").replace(" bags", "").replace(" bag", "")
    values = values.split(", ")
    rules[key] = []
    if values != ["no other"]:
        for value in values:
            value = value.split(" ")
            rules[key].append((int(value[0]), value[1] + " " + value[2]))


# Part 1
def check_bag(bag, target):
    """Check if bag contains target."""
    if target in [r[1] for r in rules[bag]]:
        return True
    for rule in rules[bag]:
        if check_bag(rule[1], target):
            return True
    return False


count = 0
for rule in rules:
    count += check_bag(rule, "shiny gold")
print("Part 1:", count)
assert count == 139


# Part 2
def count_bags_in(bag):
    """Count number of bags inside bag."""
    count = 0
    for rule in rules[bag]:
        count += rule[0] * (1 + count_bags_in(rule[1]))
    return count


count = count_bags_in("shiny gold")
print("Part 2:", count)
assert count == 58175
