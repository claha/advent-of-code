"""Advent Of Code #02."""
with open("input") as f:
    data = f.read().split()

# Part 1
valid = 0
for i in range(0, len(data), 3):
    threshold = [int(t) for t in data[i].split("-")]
    low = threshold[0]
    high = threshold[1]
    letter = data[i + 1][0]
    password = data[i + 2]

    count = password.count(letter)
    if low <= count <= high:
        valid += 1

print("Part 1:", valid)
assert valid == 600

# Part 2
valid = 0
for i in range(0, len(data), 3):
    positions = [int(t) for t in data[i].split("-")]
    position1 = positions[0] - 1  # Make zero indexed
    position2 = positions[1] - 1  # Make zero indexed
    letter = data[i + 1][0]
    password = data[i + 2]

    if (password[position1] == letter) ^ (password[position2] == letter):
        valid += 1

print("Part 2:", valid)
assert valid == 245
