"""Advent Of Code #10."""

with open("input") as f:
    data = f.read().strip().split("\n")

# Part 1
X = [1]
for instr in data:
    if instr == "noop":
        X.append(X[-1])
    elif instr.startswith("addx"):
        X.append(X[-1])
        X.append(X[-1] + int(instr.split(" ")[-1]))

total = sum(X[i - 1] * i for i in range(20, 221, 40))
print("Part 1:", total)
assert total == 11220


# Part 2
H = 6
W = 40
screen = ""
for r in range(H):
    for c in range(W):
        i = r * W + c
        if X[i] - 1 <= c <= X[i] + 1:
            screen += "#"
        else:
            screen += "."
    screen += "\n"

print("Part 2:")
print(screen)
assert (
    screen
    == """\
###..####.###...##....##.####.#....#..#.
#..#....#.#..#.#..#....#.#....#....#.#..
###....#..#..#.#..#....#.###..#....##...
#..#..#...###..####....#.#....#....#.#..
#..#.#....#....#..#.#..#.#....#....#.#..
###..####.#....#..#..##..####.####.#..#.
"""
)
