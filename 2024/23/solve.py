"""Advent Of Code."""

import networkx as nx

import aoc

data = [line.split("-") for line in aoc.input_readlines()]
graph = nx.Graph()
for a, b in data:
    graph.add_edge(a, b)

# Part 1
cliques = nx.enumerate_all_cliques(graph)
triangles = [list(triangle) for triangle in cliques if len(triangle) == 3]  # noqa: PLR2004
ans = [t for t in triangles if any(i.startswith("t") for i in t)]
aoc.check_part1(len(ans), 1344)

# Part 2
largest_clique = max(nx.find_cliques(graph), key=len)
aoc.check_part2(
    ",".join(sorted(largest_clique)),
    "ab,al,cq,cr,da,db,dr,fw,ly,mn,od,py,uh",
)
