"""Advent Of Code #07."""

with open("input") as f:
    data = [int(d) for d in f.read().split(",")]


# Part 1
def cost(a, b):
    """Amount of fuel to get from a to b."""
    return abs(a - b)


m = min(data)
c = sum(cost(d, m) for d in data)
for m_test in range(min(data) + 1, max(data) + 1):
    c_test = sum(cost(d, m_test) for d in data)
    if c_test < c:
        m = m_test
        c = c_test
    else:
        break

print("Part 1:", c)
assert c == 356922


# Part 2
def cost(a, b):
    """Amount of fuel to get from a to b."""
    return int(abs(a - b) * (1 + abs(a - b)) / 2)


m = min(data)
c = sum(cost(d, m_test) for d in data)
found_maxima = False
for m_test in range(min(data) + 1, max(data) + 1):
    c_test = sum(cost(d, m_test) for d in data)
    if c_test < c:
        found_maxima = True
        m = m_test
        c = c_test
    else:
        if found_maxima:
            break

print("Part 2:", c)
assert c == 100347031
