"""Advent Of Code #04."""

with open("input") as f:
    data = [
        list(int(d) for d in line.split(","))
        for line in f.read().replace("-", ",").split()
    ]


def contains(a, b, c, d):
    """Check if a..b contain c..d or the other way around."""
    return (c >= a and d <= b) or (a >= c and b <= d)


def overlap(a, b, c, d):
    """Check if a..b and c..d overlap."""
    return max(a, c) <= min(b, d)


# Part 1
count = sum(contains(*abcd) for abcd in data)

print("Part 1:", count)
assert count == 494


# Part 2
count = sum(overlap(*abcd) for abcd in data)

print("Part 2:", count)
assert count == 833
