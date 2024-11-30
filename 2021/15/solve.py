"""Advent Of Code #15."""

import heapq as heap

with open("input") as f:
    data = [d.strip() for d in f.readlines()]

DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra(graph):
    """Run dijkstras algorithm."""
    size = len(graph)
    visited = set()
    queue = []
    cost = {(0, 0): 0}
    heap.heappush(queue, (0, (0, 0)))

    while queue:
        _, node = heap.heappop(queue)
        if node == (size - 1, size - 1):
            break
        visited.add(node)
        for dy, dx in DELTA:
            y = node[0] + dy
            x = node[1] + dx
            if (0 <= y < size) and (0 <= x < size) and (y, x) not in visited:
                weight = int(graph[y][x])
                if (y, x) not in cost or cost[node] + weight < cost[(y, x)]:
                    cost[(y, x)] = cost[node] + weight
                    heap.heappush(queue, (cost[node], (y, x)))
    return cost[(size - 1, size - 1)]


# Part 1
cost = dijkstra(data)
print("Part 1:", cost)
assert cost == 388

# Part 2
size = len(data)
for offset in range(1, 5):
    for y in range(size):
        data.append("")
        for x in range(size):
            value = int(data[y][x]) + offset
            if value > 9:
                value -= 9
            data[-1] += str(value)

for y in range(len(data)):
    for offset in range(1, 5):
        for x in range(size):
            value = int(data[y][x]) + offset
            if value > 9:
                value -= 9
            data[y] += str(value)

cost = dijkstra(data)
print("Part 2:", cost)
assert cost == 2819
