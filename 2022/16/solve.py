"""Advent Of Code #16."""
import re
from collections import deque

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

flow_rate = {}
graph = {}

for line in data:
    valves = re.findall("[A-Z][A-Z]", line)
    flow = int(re.findall(r"\d+", line)[0])
    flow_rate[valves[0]] = flow
    graph[valves[0]] = valves[1:]


def shortest_path(graph, node0, node1):
    """Get shortest path between nodes."""
    paths = deque([[node0]])
    visited = {node0}

    while paths:
        path = paths.popleft()
        neighbour = graph[path[-1]]

        if node1 in neighbour:
            return path + [node1]

        for node in neighbour:
            if node in visited:
                continue
            paths.append(path + [node])
            visited.add(node)

    return []


def bfs(graph, node, threshold):
    """Get a list of all possible paths from node."""
    paths = []
    queue = deque([[node]])
    while queue:
        path = queue.popleft()
        node, cost = path[-1]
        visited = None
        for neighbour, c in graph[node]:
            if cost + c + 1 > threshold:
                continue
            if visited is None:
                visited = {n for n, _ in path}
            if neighbour in visited:
                continue
            queue.append(path + [(neighbour, cost + c + 1)])
            paths.append(path[1:] + [(neighbour, cost + c + 1)])
    return paths


graph2 = {}
for start in flow_rate:
    if flow_rate[start] == 0 and start != "AA":
        continue
    graph2[start] = []
    for stop in flow_rate:
        if flow_rate[stop] == 0:
            continue
        if stop == start:
            continue
        graph2[start].append((stop, len(shortest_path(graph, start, stop)) - 1))


def calc_preassure(path, threshold):
    """Calculate preassure from path."""
    return sum([(threshold - cost) * flow_rate[node] for node, cost in path])


# Part 1
paths = bfs(graph2, ("AA", 0), 30)
max_preassure = 0
for path in paths:
    preassure = calc_preassure(path, 30)
    max_preassure = max(max_preassure, preassure)
print("Part 1:", max_preassure)
assert max_preassure == 1857


# Part 2
paths = bfs(graph2, ("AA", 0), 26)
paths_uniq = {}
max_preassure_uniq = 0
for path in paths:
    key = "".join(sorted([node for node, _ in path]))
    preassure = calc_preassure(path, 26)
    if key not in paths_uniq:
        paths_uniq[key] = 0
    if preassure > paths_uniq[key]:
        paths_uniq[key] = preassure
    if preassure > max_preassure_uniq:
        max_preassure_uniq = preassure

max_preassure = 0
for p0 in paths_uniq:
    if paths_uniq[p0] + max_preassure_uniq < max_preassure:
        continue
    s0 = {p0[i : i + 2] for i in range(0, len(p0), 2)}
    for p1 in paths_uniq:
        s1 = {p1[i : i + 2] for i in range(0, len(p1), 2)}
        if not s0 & s1:
            max_preassure = max(max_preassure, paths_uniq[p0] + paths_uniq[p1])

print("Part 2:", max_preassure)
assert max_preassure == 2536
