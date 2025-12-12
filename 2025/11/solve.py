import aoc

from collections import defaultdict
from functools import lru_cache

data = aoc.input_readlines()

graph = defaultdict(list)
for line in data:
    if line.strip():
        node, connections = line.split(": ")
        graph[node] = connections.split()


def count_paths(graph, start, target):
    @lru_cache(None)
    def dp(node):
        if node == target:
            return 1
        return sum([dp(child) for child in graph[node]])

    return dp(start)


def count_paths_visit(graph, start, target):
    @lru_cache(None)
    def dp(node, mask):
        if node == target:
            return 1 if mask == 3 else 0
        current_mask = mask | (2 * (node == "fft") + 1 * (node == "dac"))
        return sum([dp(child, current_mask) for child in graph[node]])

    return dp(start, 0)


# Part 1
answer = count_paths(graph, "you", "out")
aoc.check_part1(answer, 652)

# Part 2
answer = count_paths_visit(graph, "svr", "out")
aoc.check_part2(answer, 362956369749210)
