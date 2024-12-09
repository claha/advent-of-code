"""Advent Of Code."""

import aoc

SPACE = chr(10000)

data = list(map(int, list(aoc.input_read())))


def even(x: int) -> bool:
    """Check if even."""
    return x % 2 == 0


def encode(x: int) -> str:
    """Encode integer to single character string."""
    return chr(x)


def decode(x: str) -> int:
    """Decode single character string to integer."""
    return ord(x)


def is_space(x: str) -> bool:
    """Check if space character."""
    return x == SPACE


def has_space(x: list[str]) -> bool:
    """Check if space charcter in list."""
    return SPACE in x


# Part 1
disk = []
for i, v in enumerate(data):
    if even(i):
        disk.extend([encode(i // 2)] * v)
    else:
        disk.extend([SPACE] * v)

i = 0
while i < len(disk):
    while is_space(disk[-1]):
        disk.pop()
    while i < len(disk) and is_space(disk[i]):
        disk[i] = disk.pop()
    i += 1

checksum = sum([i * decode(v) for i, v in enumerate(disk)])
aoc.check_part1(checksum, 6154342787400)


# Part 2
disk = []
for i, v in enumerate(data):
    if v == 0:
        continue
    if even(i):
        disk.extend([encode(i // 2) * v])
    else:
        disk.extend([SPACE * v])

j = len(disk) - 1
N = len(data) // 2

for _ in range(N):
    while j >= 0 and has_space(disk[j]):
        j -= 1
    block = disk[j]
    i = 0
    while i < j:
        while not has_space(disk[i]):
            i += 1
        if not (i < j):
            break
        diff = len(disk[i]) - len(block)
        if diff >= 0:
            if diff > 0:
                disk.insert(i + 1, SPACE * diff)
                j += 1
            disk[i] = block
            disk[j] = SPACE * len(block)
            break
        else:
            i += 1
    j -= 1

disk = list("".join(disk))
checksum = sum([i * decode(v) for i, v in enumerate(disk) if not has_space(v)])
aoc.check_part2(checksum, 6183632723350)
