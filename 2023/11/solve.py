"""Advent Of Code #11."""
with open("input") as f:
    image = [list(line.strip()) for line in f.readlines()]

galaxies = []
for r in range(len(image)):
    for c in range(len(image[r])):
        if image[r][c] == "#":
            galaxies.append((r, c))

new_rows = []
for r in range(len(image)):
    if image[r].count(".") == len(image[r]):
        new_rows.append(r)

new_cols = []
for c in range(len(image[0])):
    col = [image[r][c] for r in range(len(image))]
    if col.count(".") == len(image):
        new_cols.append(c)

# Part 1
row_map = {r: r for r in range(len(image))}
for new in new_rows[::-1]:
    new = row_map[new]
    for r in row_map.keys():
        if r > new:
            row_map[r] += 1

col_map = {c: c for c in range(len(image[0]))}
for new in new_cols[::-1]:
    new = col_map[new]
    for c in col_map.keys():
        if c > new:
            col_map[c] += 1

distance = 0
for i in range(len(galaxies)):
    (r0, c0) = galaxies[i]
    r0 = row_map[r0]
    c0 = col_map[c0]
    for j in range(i + 1, len(galaxies)):
        (r1, c1) = galaxies[j]
        r1 = row_map[r1]
        c1 = col_map[c1]
        distance += abs(r1 - r0) + abs(c1 - c0)
print("Part 1", distance)
assert distance == 9609130

# Part 2
N = 1000000 - 1
row_map = {r: r for r in range(len(image))}
for new in new_rows[::-1]:
    new = row_map[new]
    for r in row_map.keys():
        if r > new:
            row_map[r] += N

col_map = {c: c for c in range(len(image[0]))}
for new in new_cols[::-1]:
    new = col_map[new]
    for c in col_map.keys():
        if c > new:
            col_map[c] += N

distance = 0
for i in range(len(galaxies)):
    (r0, c0) = galaxies[i]
    r0 = row_map[r0]
    c0 = col_map[c0]
    for j in range(i + 1, len(galaxies)):
        (r1, c1) = galaxies[j]
        r1 = row_map[r1]
        c1 = col_map[c1]
        distance += abs(r1 - r0) + abs(c1 - c0)
print("Part 2", distance)
assert distance == 702152204842
