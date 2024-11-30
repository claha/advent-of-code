"""Advent Of Code #09."""

with open("input") as f:
    data = [list(map(int, line.strip().split(" "))) for line in f.readlines()]


def get_diff(x):
    """Get difference to next element."""
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]


def get_next(x):
    """Get next."""
    d = get_diff(x)
    if len(set(d)) == 1:
        return x[-1] + d[0]
    return x[-1] + get_next(d)


sum_next = sum([get_next(history) for history in data])
print("Part 1:", sum_next)
assert sum_next == 1861775706


sum_prev = sum([get_next(history[::-1]) for history in data])
print("Part 2:", sum_prev)
assert sum_prev == 1082
