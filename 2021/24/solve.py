"""Advent Of Code #24."""

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

# The following code shows that the MONAD program is actually a sub program that
# is repeated 18 times and that only the parameters to three instructions differ.
# for i in range(18):
#     instructions = set()
#     for j in range(14):
#         instructions.add(data[j * 18 + i])
#     print(instructions)

params = []
for i in range(0, len(data), 18):
    params.append(
        (
            int(data[i + 4].split(" ")[-1]),  # div z a
            int(data[i + 5].split(" ")[-1]),  # add x b
            int(data[i + 15].split(" ")[-1]),  # add y c
        )
    )


# The following instructions are executed in the sub program with the
# different parameters a,b and c.
# inp w
# mul x 0
# add x z
# mod x 26
# div z a
# add x b
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y c
# mul y x
# add z y
# Which can be simplified to this function
def calc_z(z, w, a, b, c):
    """Calculate z."""
    x = int(int((z % 26 + b) == w) == 0)
    z = z // a * (25 * x + 1) + (w + c) * x
    return z


states = {0: (0, 0)}
for i, (a, b, c) in enumerate(params):
    states_new = {}
    for z, inp in states.items():
        if z >= 26 ** (len(params) - i):
            continue

        for w in range(1, 10):
            z_new = calc_z(z, w, a, b, c)

            low_new, high_new = inp[0] * 10 + w, inp[1] * 10 + w
            if z_new not in states_new:
                states_new[z_new] = (low_new, high_new)
            else:
                low_old, high_old = states_new[z_new]
                states_new[z_new] = (
                    min(low_old, low_new),
                    max(high_old, high_new),
                )
    states = states_new


# Part 1
print("Part 1:", states[0][1])
assert states[0][1] == 89913949293989


# Part 2
print("Part 2:", states[0][0])
assert states[0][0] == 12911816171712
