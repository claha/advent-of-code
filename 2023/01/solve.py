"""Advent Of Code #01."""
with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

NUMBERS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_num(line, reverse=False, ignore_text=True):
    """Find next num."""
    if reverse:
        numbers = [num[::-1] for num in NUMBERS]
        line = line[::-1]
    else:
        numbers = NUMBERS
    for i, c in enumerate(line):
        if "0" <= c <= "9":
            return c
        elif not ignore_text and i + 3 < len(line):
            for j, n in enumerate(numbers):
                if i + len(n) < len(line) and line[i : i + len(n)] == n:
                    return str(j + 1)


# Part 1
answer = sum([int(find_num(line) + find_num(line, reverse=True)) for line in lines])
print("Part 1:", answer)
assert answer == 56042

# Part 2
answer = sum(
    [
        int(
            find_num(line, ignore_text=False)
            + find_num(line, ignore_text=False, reverse=True)
        )
        for line in lines
    ]
)
print("Part 2:", answer)
assert answer == 55358
