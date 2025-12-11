"""Advent Of Code."""

import aoc

from itertools import product
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, PULP_CBC_CMD, value

machines = [line.split(" ") for line in aoc.input_readlines()]
diagrams = [list(machine[0][1:-1]) for machine in machines]
buttons = [
    list(map(lambda x: eval(x.replace(")", "]").replace("(", "[")), machine[1:-1]))
    for machine in machines
]
targets = [list(map(int, machine[-1][1:-1].split(","))) for machine in machines]

# Part 1
answer = 0
for diagram, button_wiring in zip(diagrams, buttons):
    target = [1 if c == "#" else 0 for c in diagram]

    min_presses = float("inf")

    for presses in product([0, 1], repeat=len(button_wiring)):
        lights = [0] * len(diagram)

        for press_count, wires in zip(presses, button_wiring):
            if press_count == 1:
                for wire in wires:
                    lights[wire] ^= 1

        if lights == target:
            min_presses = min(min_presses, sum(presses))

    answer += min_presses

aoc.check_part1(answer, 428)

# Part 2
answer = 0
for target, button_wiring in zip(targets, buttons):
    prob = LpProblem("button_wiring", LpMinimize)
    x = [
        LpVariable(f"x{i}", lowBound=0, cat="Integer")
        for i in range(len(button_wiring))
    ]
    prob += lpSum(x)

    col = 0
    for goal in target:
        prob += lpSum(x[i] for i, btn in enumerate(button_wiring) if col in btn) == goal
        col += 1

    prob.solve(PULP_CBC_CMD(msg=False))
    answer += int(value(prob.objective))

aoc.check_part2(answer, 16613)
