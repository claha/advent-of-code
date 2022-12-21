"""Advent Of Code #21."""
with open("input") as f:
    data = [line.strip().replace(": ", " = ") for line in f.readlines()]


# Part 1
def run(data):
    """Run all the expressions."""
    executed = [False] * len(data)
    while not all(executed):
        for i, expr in enumerate(data):
            if executed[i]:
                continue
            try:
                exec(expr)
                executed[i] = True
            except NameError:
                pass
    return eval("int(root)")


root = run(data)
print("Part 1:", root)
assert root == 170237589447588


# Part 2
for i, expr in enumerate(data):
    if expr.startswith("root = "):
        data[i] = expr.replace(" + ", " == ")
        break
for i, expr in enumerate(data):
    if expr.startswith("humn = "):
        data.pop(i)
        break


def run(data, expr):
    """Run all the expressions."""
    data.insert(0, expr)
    executed = [False] * len(data)

    for i, expr in enumerate(data):
        if expr.startswith("root = "):
            variables = data[i].split("root = ")[-1].split(" == ")

    while not all(executed):
        for i, expr in enumerate(data):
            if executed[i]:
                continue
            try:
                exec(expr)
                executed[i] = True
            except NameError:
                pass

    return eval(f"{variables[0]}, {variables[1]}")


guess = ""
for i in range(13):
    for j in range(10):
        n = guess + str(j) + "0" * (12 - len(guess))
        variables = run(data[:], f"humn = {n}")

        if variables[0] == variables[1]:
            guess += str(j)
            break
        if variables[0] <= variables[1]:
            guess += str(j - 1)
            break
    if len(guess) < i + 1:
        guess += "9"

guess = int(guess)
print("Part 2:", guess)
assert guess == 3712643961892
