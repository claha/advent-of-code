"""Advent Of Code #12."""

import heapq as heap

with open("input") as f:
    data = [d.strip() for d in f.readlines()]

for i, line in enumerate(data):
    if "S" in line:
        start = (i, line.index("S"))
        data[i] = data[i].replace("S", "a")
    if "E" in line:
        end = (i, line.index("E"))
        data[i] = data[i].replace("E", "z")

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx)


def dijkstra(graph, start, end):
    """Run dijkstras algorithm."""
    visited = set()
    queue = []
    cost = {start: 0}
    heap.heappush(queue, (0, start))

    while queue:
        _, node = heap.heappop(queue)
        if node == end:
            break
        visited.add(node)
        h = graph[node[0]][node[1]]
        weight = 1

        for dy, dx in DELTA:
            y = node[0] + dy
            x = node[1] + dx

            if not (0 <= y < len(graph) and 0 <= x < len(graph[0])):
                continue

            if (y, x) in visited:
                continue

            if ord(graph[y][x]) > ord(h) + 1:
                continue

            if (y, x) not in cost or cost[node] + weight < cost[(y, x)]:
                cost[(y, x)] = cost[node] + weight
                heap.heappush(queue, (cost[node], (y, x)))

    if end in cost:
        return cost[end]
    return None


# Part 1
cost = dijkstra(data, start, end)
print("Part 1:", cost)
assert cost == 468


# Part 2
costs = []
for y, row in enumerate(data):
    for x, h in enumerate(row):
        if h == "a":
            costs.append(dijkstra(data, (y, x), end))
min_cost = min(filter(lambda x: x is not None, costs))

print("Part 2:", min_cost)
assert min_cost == 459
