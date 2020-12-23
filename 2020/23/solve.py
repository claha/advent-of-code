"""Advent Of Code #23."""
with open("input") as f:
    data = f.read().strip()
cups = [int(cup) for cup in data]


def play(current, lut, moves):
    """Play a game of crab cups."""

    N = len(lut) - 1
    for _ in range(moves):
        # Pick next three cups
        pick = [lut[current], lut[lut[current]], lut[lut[lut[current]]]]

        # Select destination cup
        dest = current - 1
        while dest in pick + [0]:
            dest -= 1
            if dest < 0:
                dest = N

        # current should point at what pick[2] used to point at
        # pick[2] should point at what dest used to point at
        # destination should point at pick[0]
        lut[current], lut[pick[2]], lut[dest] = lut[pick[2]], lut[dest], pick[0]

        # Select new current cup
        current = lut[current]


# Part 1
N = len(cups)
lut = [0] * (N + 1)
for i, cup in enumerate(cups):
    lut[cup] = cups[(i + 1) % N]

play(cups[0], lut, 100)
label = ""
n = 1
for i in range(1, N):
    n = lut[n]
    label += str(n)

print("Part 1:", label)
assert label == "52937846"

# Part 2
for cup in range(max(cups) + 1, 1000000 + 1):
    cups.append(cup)
N = len(cups)
lut = [0] * (N + 1)
for i, cup in enumerate(cups):
    lut[cup] = cups[(i + 1) % len(cups)]

play(cups[0], lut, 10000000)

print("Part 2:", lut[1] * lut[lut[1]])
assert lut[1] * lut[lut[1]] == 8456532414
