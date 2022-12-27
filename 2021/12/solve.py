"""Advent Of Code #12."""
with open("input") as f:
    data = [d.split("-") for d in f.read().split()]

graph = {}
for connection in data:
    if connection[0] not in graph:
        graph[connection[0]] = []
    if connection[1] not in graph:
        graph[connection[1]] = []
    if connection[1] != "start":
        graph[connection[0]].append(connection[1])
    if connection[0] != "start":
        graph[connection[1]].append(connection[0])


def dfs(graph, path, revisited):
    """Depth first search."""
    global num_paths
    node = path[-1]

    if node == "end":
        num_paths += 1
        return

    for neighbour in graph[node]:
        if neighbour.lower() != neighbour or neighbour not in path:
            dfs(graph, path + [neighbour], revisited)
        elif not revisited:
            dfs(graph, path + [neighbour], True)


# Part 1
num_paths = 0
dfs(graph, ["start"], True)
print("Part 1:", num_paths)
assert num_paths == 5076


# Part 2
num_paths = 0
dfs(graph, ["start"], False)
print("Part 2:", num_paths)
assert num_paths == 145643
