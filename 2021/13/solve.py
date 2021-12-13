"""Advent Of Code #13."""
with open("input") as f:
    data = [d.strip() for d in f.readlines()]

paper = set()
instructions = []
for d in data:
    if "," in d:
        x, y = d.split(",")
        x = int(x)
        y = int(y)
        paper.add((x, y))
    elif "=" in d:
        instruction, line = d.split("=")
        line = int(line)
        instructions.append((instruction, line))


def fold_along_y(paper, line):
    """Fold along y."""
    paper_new = set()
    for (x, y) in paper:
        if y > line:
            y -= 2 * (y - line)
        paper_new.add((x, y))
    return paper_new


def fold_along_x(paper, line):
    """Fold along x."""
    paper_new = set()
    for (x, y) in paper:
        if x > line:
            x -= 2 * (x - line)
        paper_new.add((x, y))
    return paper_new


fold_function = {
    "fold along y": fold_along_y,
    "fold along x": fold_along_x,
}


# Part 1
fold = fold_function[instructions[0][0]]
paper = fold(paper, instructions[0][1])
print("Part 1:", len(paper))
assert len(paper) == 687


# Part 2
for instruction in instructions[1:]:
    fold = fold_function[instruction[0]]
    paper = fold(paper, instruction[1])

max_y = max(y for (_, y) in paper) + 1
max_x = max(x for (x, _) in paper) + 1
code = ""
for y in range(max_y):
    for x in range(max_x):
        if (x, y) in paper:
            code += "#"
        else:
            code += " "
    code = code.strip() + "\n"

print("Part 2:")
print(code)
assert (
    code
    == """\
####  ##  #  #  ##  #  # ###  ####  ##
#    #  # # #  #  # # #  #  #    # #  #
###  #    ##   #    ##   ###    #  #
#    # ## # #  #    # #  #  #  #   # ##
#    #  # # #  #  # # #  #  # #    #  #
#     ### #  #  ##  #  # ###  ####  ###
"""
)
