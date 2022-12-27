"""Advent Of Code #25."""
with open("input") as f:
    data = [line.strip() for line in f.readlines()]


def decode(x):
    """SNAFU to integer."""
    mult = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum(mult[c] * 5**i for i, c in enumerate(reversed(x)))


def encode(x):
    """Integer to SNAFU."""
    char = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    n = ""
    while x:
        x, m = divmod(x + 2, 5)
        n += char[m - 2]
    return n[::-1]


# Part 1
number = sum(decode(n) for n in data)
number = encode(number)
print("Part 1:", number)
assert number == "2-=12=2-2-2-=0012==2"
