"""Advent Of Code #05."""

with open("input") as f:
    data = f.read().splitlines()

boarding_passes = [
    int(
        boarding_pass.replace("B", "1")
        .replace("F", "0")
        .replace("R", "1")
        .replace("L", "0"),
        2,
    )
    for boarding_pass in data
]
boarding_passes.sort()

# Part 1
highest = boarding_passes[-1]
print("Part 1:", highest)
assert highest == 858

# Part 2
empty = None
for i in range(len(boarding_passes) - 1):
    if boarding_passes[i + 1] - boarding_passes[i] != 1:
        empty = boarding_passes[i] + 1
print("Part 2:", empty)
assert empty == 557
