"""Advent Of Code #23."""
import sys

sys.setrecursionlimit(10000)

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(graph, path):
    """Depth first search."""
    (y, x, _) = path[-1]

    if y == len(data) - 1:
        return path

    longest_path = []
    for neighbor in graph[(y, x)]:
        if (neighbor[0], neighbor[1]) not in [(a, b) for a, b, _ in path]:
            new_path = dfs(graph, path + [neighbor])
            if sum([c for _, _, c in new_path]) > sum([c for _, _, c in longest_path]):
                longest_path = new_path

    return longest_path


# Part 1
graph = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            continue
        graph[(y, x)] = []
        for dy, dx in DELTA:
            ny = y + dy
            nx = x + dx
            if not (0 <= ny < len(data) and 0 <= nx < len(data[0])):
                continue
            neighbor = data[ny][nx]
            if neighbor == ".":
                graph[(y, x)].append((ny, nx, 1))
            elif neighbor == ">" and (dy, dx) == (0, 1):
                graph[(y, x)].append((ny, nx, 1))
            elif neighbor == "<" and (dy, dx) == (0, -1):
                graph[(y, x)].append((ny, nx, 1))
            elif neighbor == "v" and (dy, dx) == (1, 0):
                graph[(y, x)].append((ny, nx, 1))
            elif neighbor == "^" and (dy, dx) == (-1, 0):
                graph[(y, x)].append((ny, nx, 1))


start = (0, data[0].index("."), 0)
path = dfs(graph, [start])
length = sum([step[2] for step in path])
print("Part 1:", length)
assert length == 2174

# Part 2
graph = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            continue
        graph[(y, x)] = []
        for dy, dx in DELTA:
            ny = y + dy
            nx = x + dx
            if not (0 <= ny < len(data) and 0 <= nx < len(data[0])):
                continue
            neighbor = data[ny][nx]
            if neighbor != "#":
                graph[(y, x)].append((ny, nx, 1))
while True:
    count = 0
    for y, x in graph:
        if len(graph[(y, x)]) == 2:
            count += 1
            neighbor0 = graph[(y, x)][0]
            neighbor1 = graph[(y, x)][1]
            for ty, tx, tn in graph[neighbor0[:2]]:
                if (ty, tx) == (y, x):
                    graph[neighbor0[:2]].remove((ty, tx, tn))
                    break
            for ty, tx, tn in graph[neighbor1[:2]]:
                if (ty, tx) == (y, x):
                    graph[neighbor1[:2]].remove((ty, tx, tn))
                    break
            graph[neighbor0[:2]].append(
                (neighbor1[0], neighbor1[1], neighbor1[2] + neighbor0[2])
            )
            graph[neighbor1[:2]].append(
                (neighbor0[0], neighbor0[1], neighbor0[2] + neighbor1[2])
            )
            del graph[(y, x)]
            break
    if count == 0:
        break

path = dfs(graph, [start])
length = sum([step[2] for step in path])
print("Part 2:", length)
assert length == 6506
