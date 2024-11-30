"""Advent Of Code #10."""

with open("input") as f:
    field = [list(line.strip()) for line in f.readlines()]

graph = {}
for r in range(len(field)):
    for c in range(len(field[r])):
        t = field[r][c]
        if t == "F":
            graph[(r, c)] = [(r + 1, c), (r, c + 1)]
        elif t == "-":
            graph[(r, c)] = [(r, c - 1), (r, c + 1)]
        elif t == "7":
            graph[(r, c)] = [(r, c - 1), (r + 1, c)]
        elif t == "|":
            graph[(r, c)] = [(r - 1, c), (r + 1, c)]
        elif t == "J":
            graph[(r, c)] = [(r - 1, c), (r, c - 1)]
        elif t == "L":
            graph[(r, c)] = [(r, c + 1), (r - 1, c)]
        elif t == "S":
            start = (r, c)
            graph[(r, c)] = [(r, c - 1), (r, c + 1)]  # input

queue = graph[start][::]
visited = {start}
while queue:
    node = queue.pop()
    if node == start:
        break
    for n in graph[node]:
        if n in queue:
            continue
        if n in visited:
            continue
        queue.append(n)
    visited.add(node)

for r in range(len(field)):
    for c in range(len(field[r])):
        if (r, c) not in visited:
            field[r][c] = "."

candidates = set()
outside = set()
for r in range(len(field)):
    for c in range(len(field[r])):
        if (r, c) in visited:
            continue
        if r == 0 or r == len(field) - 1 or c == 0 or c == len(field[r]) - 1:
            outside.add((r, c))
        else:
            candidates.add((r, c))

count = len(field) * len(field[0])
while count != len(candidates):
    count = len(candidates)
    torm = set()
    for r, c in candidates:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (r + dr, c + dc) in outside:
                outside.add((r, c))
                torm.add((r, c))
                break
    candidates -= torm

print("Part 1:", int(len(visited) / 2))
assert int(len(visited) / 2) == 6831

#
fieldx = [["."] * (len(field[0]) * 3) for _ in range(len(field) * 3)]

for r in range(len(field)):
    for c in range(len(field[r])):
        t = field[r][c]
        if t == ".":
            pass
        elif t == "|":
            for dr, dc in [(-1, 0), (0, 0), (1, 0)]:
                fieldx[3 * r + 1 + dr][3 * c + 1 + dc] = "|"
        elif t == "-" or t == "S":  # input
            for dr, dc in [(0, -1), (0, 0), (0, 1)]:
                fieldx[3 * r + 1 + dr][3 * c + 1 + dc] = "-"
        elif t == "F":
            fieldx[3 * r + 1 + 0][3 * c + 1 + 0] = "F"
            fieldx[3 * r + 1 + 0][3 * c + 1 + 1] = "-"
            fieldx[3 * r + 1 + 1][3 * c + 1 + 0] = "|"
        elif t == "7":
            fieldx[3 * r + 1 + 0][3 * c + 1 + 0] = "7"
            fieldx[3 * r + 1 + 0][3 * c + 1 - 1] = "-"
            fieldx[3 * r + 1 + 1][3 * c + 1 + 0] = "|"
        elif t == "L":
            fieldx[3 * r + 1 + 0][3 * c + 1 + 0] = "L"
            fieldx[3 * r + 1 + 0][3 * c + 1 + 1] = "-"
            fieldx[3 * r + 1 - 1][3 * c + 1 + 0] = "|"
        elif t == "J":
            fieldx[3 * r + 1 + 0][3 * c + 1 + 0] = "J"
            fieldx[3 * r + 1 + 0][3 * c + 1 - 1] = "-"
            fieldx[3 * r + 1 - 1][3 * c + 1 + 0] = "|"

# visited -> visitedx
visitedx = set()
for r, c in visited:
    t = field[r][c]
    if t == "|":
        for dr, dc in [(-1, 0), (0, 0), (1, 0)]:
            visitedx.add((3 * r + 1 + dr, 3 * c + 1 + dc))
    elif t == "-" or t == "S":  # input
        for dr, dc in [(0, -1), (0, 0), (0, 1)]:
            visitedx.add((3 * r + 1 + dr, 3 * c + 1 + dc))
    elif t == "F":
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 0))
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 1))
        visitedx.add((3 * r + 1 + 1, 3 * c + 1 + 0))
    elif t == "7":
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 0))
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 - 1))
        visitedx.add((3 * r + 1 + 1, 3 * c + 1 + 0))
    elif t == "L":
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 0))
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 1))
        visitedx.add((3 * r + 1 - 1, 3 * c + 1 + 0))
    elif t == "J":
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 + 0))
        visitedx.add((3 * r + 1 + 0, 3 * c + 1 - 1))
        visitedx.add((3 * r + 1 - 1, 3 * c + 1 + 0))

candidatesx = set()
outsidex = set()
for r in range(len(fieldx)):
    for c in range(len(fieldx[r])):
        if (r, c) in visitedx:
            continue
        if r == 0 or r == len(fieldx) - 1 or c == 0 or c == len(fieldx[r]) - 1:
            outsidex.add((r, c))
        else:
            candidatesx.add((r, c))

count = len(fieldx) * len(fieldx[0])
while count != len(candidatesx):
    count = len(candidatesx)
    torm = set()
    for r, c in candidatesx:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (r + dr, c + dc) in outsidex:
                outsidex.add((r, c))
                torm.add((r, c))
                break
    candidatesx -= torm

count = sum([(3 * r + 1, 3 * c + 1) in candidatesx for (r, c) in candidates])

print("Part 2:", count)
assert count == 305
