"""Advent Of Code #17."""

import heapq as heap

with open("input") as f:
    data = [d.strip() for d in f.readlines()]

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dy, dx)


def dijkstra(graph, start, end, min_straight, max_straight):
    """Run dijkstras algorithm."""
    visited = set()
    queue = []
    cost = {start: 0}
    heap.heappush(queue, (0, start))

    while queue:
        _, node = heap.heappop(queue)
        if (node[0], node[1]) == end:
            break
        visited.add(node)
        for dy, dx in DELTA:
            y = node[0] + dy
            x = node[1] + dx

            if not (0 <= y < len(graph) and 0 <= x < len(graph[0])):
                continue

            if (node[2], node[3]) == (-dy, -dx):
                continue

            if (node[2], node[3]) == (dy, dx):
                n = node[4] + 1
            else:
                if (node[1], node[0]) != (0, 0) and not (node[4] >= min_straight):
                    continue
                n = 1
            if n > max_straight:
                continue
            next_node = (y, x, dy, dx, n)

            if next_node in visited:
                continue

            weight = int(graph[y][x])
            if next_node not in cost or cost[node] + weight < cost[next_node]:
                cost[next_node] = cost[node] + weight
                heap.heappush(queue, (cost[node], next_node))

    costs = []
    for y, x, dy, dx, n in cost:
        if (y, x) == end:
            costs.append(cost[(y, x, dy, dx, n)])
    if costs:
        return min(costs)
    return None


# Part 1
start = (0, 0, 0, 0, 0)
end = (len(data) - 1, len(data[0]) - 1)
cost = dijkstra(data, start, end, min_straight=1, max_straight=3)
print("Part 1:", cost)
# assert cost ==

# Part 1
start = (0, 0, 0, 0, 0)
end = (len(data) - 1, len(data[0]) - 1)
cost = dijkstra(data, start, end, min_straight=4, max_straight=10)
print("Part 2:", cost)
# assert cost ==
