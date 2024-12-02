"""Advent Of Code #02."""

from pathlib import Path

with Path.open("input") as f:
    data = [list(map(int, line.split())) for line in f]


def is_safe(record: list[int]) -> bool:
    """Check if a record is safe or not."""
    diff = [record[i + 1] - record[i] for i in range(len(record) - 1)]
    if any(d > 0 for d in diff) and any(d < 0 for d in diff):
        return False
    diff = list(map(abs, diff))
    dmax = max(diff)
    dmin = min(diff)
    return not (dmax > 3 or dmin < 1)


# Part 1
safe = 0
for record in data:
    safe += int(is_safe(record))

print("Part 1:", safe)
assert safe == 379

# Part 2
for record in data:
    if is_safe(record):
        continue
    for i in range(len(record)):
        record_mod = record[:]
        record_mod.pop(i)
        if is_safe(record_mod):
            safe += 1
            break

print("Part 2:", safe)
assert safe == 430
