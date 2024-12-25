"""Advent Of Code."""

import aoc


def process(op: str, op1: int, op2: int) -> int:
    """Process operation."""
    if op == "AND":
        return op1 & op2
    if op == "OR":
        return op1 | op2
    if op == "XOR":
        return op1 ^ op2
    return None


data = aoc.input_readlines()
highest_z = "z00"
wires = {}
operations = []
for line in data:
    if ":" in line:
        wire, value = line.split(": ")
        wires[wire] = int(value)
    elif "->" in line:
        op1, op, op2, _, res = line.split(" ")
        operations.append((op1, op, op2, res))
        if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

# Part 1
ops = operations[:]
while len(ops):
    op1, op, op2, res = ops.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        ops.append((op1, op, op2, res))
z_wires = sorted([wire for wire in wires if wire[0] == "z"], reverse=True)
bits = [str(wires[wire]) for wire in z_wires]
value = int("".join(bits), 2)
aoc.check_part1(value, 66055249060558)


# Part 2
wrong = set()
for op1, op, op2, res in operations:
    if (res[0] == "z" and op != "XOR" and res != highest_z) or (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    elif op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, _ in operations:
            if res in (subop1, subop2) and subop != "OR":
                wrong.add(res)
    elif op == "XOR":
        for subop1, subop, subop2, _ in operations:
            if res in (subop1, subop2) and subop == "OR":
                wrong.add(res)
aoc.check_part2(",".join(sorted(wrong)), "fcd,fhp,hmk,rvf,tpc,z16,z20,z33")
