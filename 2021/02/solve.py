"""Advent Of Code #02."""
with open("input") as f:
    data = [d for d in f.read().split()]


# Part 1
horizontal = 0
depth = 0
for i in range(0, len(data), 2):
    command = data[i]
    units = int(data[i + 1])
    if command == "forward":
        horizontal += units
    elif command == "up":
        depth -= units
    elif command == "down":
        depth += units
print("Part 1:", horizontal * depth)
assert horizontal * depth == 1868935


# Part 2
horizontal = 0
depth = 0
aim = 0
for i in range(0, len(data), 2):
    command = data[i]
    units = int(data[i + 1])
    if command == "forward":
        horizontal += units
        depth += aim * units
    elif command == "up":
        aim -= units
    elif command == "down":
        aim += units
print("Part 2:", horizontal * depth)
assert horizontal * depth == 1965970888
