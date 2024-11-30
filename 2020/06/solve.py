"""Advent Of Code #06."""

with open("input") as f:
    data = f.read()

groups = data.split("\n\n")
groups = [group.splitlines() for group in groups]

# Part 1
answers = 0
for group in groups:
    group_answers = set()
    for questions in group:
        group_answers = group_answers.union(set(questions))
    answers += len(group_answers)
print("Part 1:", answers)
assert answers == 6911

# Part 2
answers = 0
for group in groups:
    group_answers = set(group[0])
    for questions in group[1:]:
        group_answers = group_answers.intersection(set(questions))
    answers += len(group_answers)
print("Part 2:", answers)
assert answers == 3473
