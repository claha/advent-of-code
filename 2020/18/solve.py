"""Advent Of Code #18."""
with open("input") as f:
    data = f.read()
expressions = data.splitlines()


# Part 1
def find_end_parenthesis(exp, i):
    """Find end parenthesis."""
    count = 0
    while i < len(exp):
        if exp[i] == "(":
            count += 1
        elif exp[i] == ")":
            if count == 0:
                break
            count -= 1
        i += 1
    return i


def calc(exp):
    """Calculate expression."""
    i = 0
    if exp[i] == "(":
        j = find_end_parenthesis(exp, i + 1)
        sub_exp = exp[i + 1 : j]
        res = calc(sub_exp)
        i = j + 1
    else:
        res = int(exp[0])
        i += 1

    while i < len(exp):
        if exp[i] == "+":
            if exp[i + 1] == "(":
                j = find_end_parenthesis(exp, i + 2)
                sub_exp = exp[i + 2 : j]
                res += calc(sub_exp)
                i = j + 1
            else:
                res += int(exp[i + 1])
                i += 2
        elif exp[i] == "*":
            if exp[i + 1] == "(":
                j = find_end_parenthesis(exp, i + 2)
                sub_exp = exp[i + 2 : j]
                res *= calc(sub_exp)
                i = j + 1
            else:
                res *= int(exp[i + 1])
                i += 2
    return res


sum = 0
for expression in expressions:
    expression = expression.replace("(", "( ").replace(")", " )")
    expression = expression.split(" ")
    sum += calc(expression)
print("Part 1:", sum)
assert sum == 53660285675207

# Part 2
sum = 0
for expression in expressions:
    expression = "(" + expression.replace("*", ") * (") + ")"
    sum += eval(expression)

print("Part 2:", sum)
assert sum == 141993988282687
