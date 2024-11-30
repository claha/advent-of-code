"""Advent Of Code #06."""

with open("input") as f:
    data = [int(d) for d in f.read().split(",")]

fishes = []
for i in range(9):
    fishes.append(0)
for d in data:
    fishes[d] += 1

# Part 1
for day in range(80):
    born = fishes[0]
    fishes = fishes[1:] + fishes[:1]
    fishes[6] += born

count = sum(fishes)
print("Part 1:", count)
assert count == 351092

# Part 2
for day in range(80, 256):
    born = fishes[0]
    fishes = fishes[1:] + fishes[:1]
    fishes[6] += born

count = sum(fishes)
print("Part 2:", count)
assert count == 1595330616005
