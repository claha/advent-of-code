"""Advent Of Code #19."""
with open("input") as f:
    rules, parts = f.read().split("\n\n")

rules = [rule.strip() for rule in rules.split()]
parts = [part.strip() for part in parts.split()]
rules = {rule.split("{")[0]: rule[:-1].split("{")[1].split(",") for rule in rules}


def solve(
    rule: str,
    x: (int, int),
    m: (int, int),
    a: (int, int),
    s: (int, int),
):
    """Solve the problem."""
    if rule == "A":
        return (
            (x[1] - x[0] + 1)
            * (m[1] - m[0] + 1)
            * (a[1] - a[0] + 1)
            * (s[1] - s[0] + 1)
        )
    elif rule == "R":
        return 0

    count = 0
    conditions = rules[rule]

    for condition in conditions:
        if "<" in condition:
            next_rule = condition.split(":")[-1]
            threshold = int(condition.split(":")[0].split("<")[-1])
            if condition[0] == "x" and x[0] < threshold:
                threshold = min(threshold - 1, x[1])
                count += solve(next_rule, (x[0], threshold), m, a, s)
                x = (threshold + 1, x[1])
            elif condition[0] == "m" and m[0] < threshold:
                threshold = min(threshold - 1, m[1])
                count += solve(next_rule, x, (m[0], threshold), a, s)
                m = (threshold + 1, m[1])
            elif condition[0] == "a" and a[0] < threshold:
                threshold = min(threshold - 1, a[1])
                count += solve(next_rule, x, m, (a[0], threshold), s)
                a = (threshold + 1, a[1])
            elif condition[0] == "s" and s[0] < threshold:
                threshold = min(threshold - 1, s[1])
                count += solve(next_rule, x, m, a, (s[0], threshold))
                s = (threshold + 1, s[1])
        elif ">" in condition:
            next_rule = condition.split(":")[-1]
            threshold = int(condition.split(":")[0].split(">")[-1])
            if condition[0] == "x" and x[1] > threshold:
                threshold = max(threshold + 1, x[0])
                count += solve(next_rule, (threshold, x[1]), m, a, s)
                x = (x[0], threshold - 1)
            elif condition[0] == "m" and m[1] > threshold:
                threshold = max(threshold + 1, m[0])
                count += solve(next_rule, x, (threshold, m[1]), a, s)
                m = (m[0], threshold - 1)
            elif condition[0] == "a" and a[1] > threshold:
                threshold = max(threshold + 1, a[0])
                count += solve(next_rule, x, m, (threshold, a[1]), s)
                a = (a[0], threshold - 1)
            elif condition[0] == "s" and s[1] > threshold:
                threshold = max(threshold + 1, s[0])
                count += solve(next_rule, x, m, a, (threshold, s[1]))
                s = (s[0], threshold - 1)
        else:
            count += solve(condition, x, m, a, s)

    return count


# Part 1
ratings = 0
for part in parts:
    [x, m, a, s] = [int(value[2:]) for value in part[1:-1].split(",")]
    if solve("in", (x, x), (m, m), (a, a), (s, s)):
        ratings += x + m + a + s
print("Part 1:", ratings)
assert ratings == 432427

# Part 2
count = solve("in", (1, 4000), (1, 4000), (1, 4000), (1, 4000))
print("Part 2:", count)
assert count == 143760172569135
