"""Advent Of Code #23."""
import networkx

with open("input") as file:
    connections = [line.strip() for line in file]

graph = networkx.Graph()
for connection in connections:
    component, _, others = connection.partition(":")
    components = [c.strip() for c in others.split()]
    graph.add_edges_from((component, neighbor) for neighbor in components)

cut = networkx.minimum_edge_cut(graph)
graph.remove_edges_from(cut)

sizes = [len(c) for c in networkx.connected_components(graph)]

print("Part 1:", sizes[0] * sizes[1])
assert sizes[0] * sizes[1] == 582626
