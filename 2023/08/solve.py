"""Advent Of Code #08."""

import re

network = {}
with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

instructions = lines[0]
for line in lines[1:]:
    nodes = re.findall("[0-9A-Z]+", line)
    network[nodes[0]] = (nodes[1], nodes[2])


# Part 1
node = "AAA"
steps = 0
i = 0
while not node == "ZZZ":
    if instructions[i] == "L":
        node = network[node][0]
    else:
        node = network[node][1]
    i = (i + 1) % len(instructions)
    steps += 1

print("Part 1:", steps)
assert steps == 15989


# Part 2
def search(node):
    """Search for node ending with Z."""
    steps = 0
    i = 0
    while not node.endswith("Z"):
        if instructions[i] == "L":
            node = network[node][0]
        else:
            node = network[node][1]
        i = (i + 1) % len(instructions)
        steps += 1
    return steps


def gcd(a, b):
    """Greatest common divisor."""
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    """Least common multiple."""
    return (a * b) / gcd(a, b)


nodes = [node for node in network.keys() if node.endswith("A")]
steps = [search(node) for node in nodes]
answer = 1
for step in steps:
    answer = lcm(answer, step)
answer = int(answer)
print("Part 2:", answer)
assert answer == 13830919117339
