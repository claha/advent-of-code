"""Advent Of Code #03."""

with open("input") as f:
    data = [d for d in f.read().split()]


# Part 1
def calc_gamma_epsilon(data):
    """Calculate gamma and epsilon."""
    gamma = ""
    epsilon = ""
    frequency = []

    for d in data:
        for bit, value in enumerate(d):
            if len(frequency) <= bit:
                frequency.append({"0": 0, "1": 0})
            frequency[bit][value] += 1

    for stat in frequency:
        if stat["0"] > stat["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return gamma, epsilon


gamma, epsilon = calc_gamma_epsilon(data)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("Part 1:", gamma * epsilon)
assert gamma * epsilon == 2003336

# Part 2
oxygen = data.copy()
co2 = data.copy()

bit = 0
while len(oxygen) > 1:
    gamma, _ = calc_gamma_epsilon(oxygen)
    for i in range(len(oxygen) - 1, -1, -1):
        if oxygen[i][bit] != gamma[bit]:
            del oxygen[i]
    bit += 1
oxygen = int(oxygen[0], 2)

bit = 0
while len(co2) > 1:
    _, epsilon = calc_gamma_epsilon(co2)
    for i in range(len(co2) - 1, -1, -1):
        if co2[i][bit] != epsilon[bit]:
            del co2[i]
    bit += 1
co2 = int(co2[0], 2)

print("Part 2:", oxygen * co2)
assert oxygen * co2 == 1877139
