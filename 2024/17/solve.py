"""Advent Of Code."""

import re

import aoc

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

OP_LIT = 3
OP_A = 4
OP_B = 5
OP_C = 6


class Computer:
    """Computer."""

    def __init__(self, reg_a: int, reg_b: int, reg_c: int, program: list[int]) -> None:
        """Create a computer."""
        self.registers = {"A": reg_a, "B": reg_b, "C": reg_c}
        self.program = program
        self.instruction_pointer = 0
        self.output = []

    def run(self) -> None:
        """Run all the instructions."""
        while self.instruction_pointer < len(self.program):
            opcode = self.program[self.instruction_pointer]
            operand = self.program[self.instruction_pointer + 1]
            self.execute_instruction(opcode, operand)

    def get_combo_operand_value(self, operand: int) -> int:
        """Get combo operand value."""
        if operand <= OP_LIT:
            return operand
        if operand == OP_A:
            return self.registers["A"]
        if operand == OP_B:
            return self.registers["B"]
        if operand == OP_C:
            return self.registers["C"]

        msg = "Combo operand 7 is invalid."
        raise ValueError(msg)

    def execute_instruction(self, opcode: int, operand: int) -> None:
        """Run a single instruction."""
        if opcode == ADV:
            denominator = 2 ** self.get_combo_operand_value(operand)
            self.registers["A"] //= denominator
        elif opcode == BXL:
            self.registers["B"] ^= operand
        elif opcode == BST:
            self.registers["B"] = self.get_combo_operand_value(operand) % 8
        elif opcode == JNZ:
            if self.registers["A"] != 0:
                self.instruction_pointer = operand
                return
        elif opcode == BXC:
            self.registers["B"] ^= self.registers["C"]
        elif opcode == OUT:
            value = self.get_combo_operand_value(operand) % 8
            self.output.append(value)
        elif opcode == BDV:
            denominator = 2 ** self.get_combo_operand_value(operand)
            self.registers["B"] = self.registers["A"] // denominator
        elif opcode == CDV:
            denominator = 2 ** self.get_combo_operand_value(operand)
            self.registers["C"] = self.registers["A"] // denominator
        else:
            msg = f"Invalid opcode: {opcode}"
            raise ValueError(msg)

        self.instruction_pointer += 2


data = aoc.input_read()
numbers = list(map(int, re.findall(r"\d+", data)))
a = numbers[0]
b = numbers[1]
c = numbers[2]
program = numbers[3:]

# Part 1
computer = Computer(
    reg_a=a,
    reg_b=b,
    reg_c=c,
    program=program,
)

computer.run()

aoc.check_part1(",".join(map(str, computer.output)), "7,1,2,3,2,6,7,2,5")


# Part 2
def find(a: int, i: int) -> int:
    """Find a."""
    computer = Computer(
        reg_a=a,
        reg_b=b,
        reg_c=c,
        program=program,
    )
    computer.run()

    if computer.output == program:
        return a
    if computer.output == program[-i:] or not i:
        for n in range(8):
            answer = find(8 * a + n, i + 1)
            if answer:
                return answer
    return None


a = find(0, 0)
aoc.check_part2(a, 202356708354602)
