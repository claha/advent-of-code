"""Advent Of Code #08."""
with open("input") as f:
    data = f.read()
instructions = data.splitlines()


class Instruction:
    """Class representing an instruction."""

    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"

    def __init__(self, instruction):
        """Initialize instruction."""
        self._operation, self._argument = instruction.split(" ")
        self._argument = int(self._argument)

    @property
    def operation(self):
        """Get instruction operation."""
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Set operation."""
        assert operation in [Instruction.ACC, Instruction.JMP, Instruction.NOP]
        self._operation = operation

    @property
    def argument(self):
        """Get instruction argument."""
        return self._argument

    def is_acc(self):
        """Check if instruction operation is acc."""
        return self._operation == Instruction.ACC

    def is_jmp(self):
        """Check if instruction operation is jmp."""
        return self._operation == Instruction.JMP

    def is_nop(self):
        """Check if instruction operation is nop."""
        return self._operation == Instruction.NOP


class Assembler:
    """Class representing an assembler."""

    def __init__(self, instructions):
        """Initialize assembler."""
        self._instructions = [Instruction(instruction) for instruction in instructions]
        self._instruction_index = 0
        self._accumulator = 0
        self._executed = set()

    @property
    def accumulator(self):
        """Get accumulator value."""
        return self._accumulator

    def get_current_instruction(self):
        """Get current instruction."""
        return self._instructions[self._instruction_index]

    def is_infinite_loop(self):
        """Check if in infinite loop."""
        return self._instruction_index in self._executed

    def has_terminated(self):
        """Check if program has terminated."""
        return not self._instruction_index < len(self._instructions)

    def run(self, pre_instruction=None):
        """Run assembler instructions."""
        while not self.is_infinite_loop() and not self.has_terminated():
            self._executed.add(self._instruction_index)
            instruction = self.get_current_instruction()

            if pre_instruction is not None:
                pre_instruction(self._instruction_index, instruction)

            if instruction.is_nop():
                self._instruction_index += 1
            elif instruction.is_acc():
                self._accumulator += instruction.argument
                self._instruction_index += 1
            elif instruction.is_jmp():
                self._instruction_index += instruction.argument


# Part 1
assembler = Assembler(instructions)
assembler.run()
print("Part 1:", assembler.accumulator)
assert assembler.accumulator == 1262


# Part 2

# Collect index for all JMP and NOP instructions
jmp_instructions = []
nop_instructions = []


def pre_instruction(index, instruction):
    """Call before each instruction is executed."""
    if instruction.is_nop():
        nop_instructions.append(index)
    elif instruction.is_jmp():
        jmp_instructions.append(index)


assembler = Assembler(instructions)
assembler.run(pre_instruction)

# Change one JMP or NOP instruction and check if program terminates
for i in jmp_instructions + nop_instructions:

    def pre_instruction(index, instruction):
        """Call before each instruction is executed."""
        if index == i:
            if instruction.is_nop():
                instruction.operation = Instruction.JMP
            elif instruction.is_jmp():
                instruction.operation = Instruction.NOP

    assembler = Assembler(instructions)
    assembler.run(pre_instruction)

    if assembler.has_terminated():
        break

print("Part 2:", assembler.accumulator)
assert assembler.accumulator == 1643
