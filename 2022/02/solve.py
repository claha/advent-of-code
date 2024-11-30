"""Advent Of Code #02."""

with open("input") as f:
    data = [d for d in f.read().split()]

LUT = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissor",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissor",
}

SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissor": 3,
}

LOSE = {
    "Rock": "Scissor",
    "Paper": "Rock",
    "Scissor": "Paper",
}

WIN = {
    "Rock": "Paper",
    "Paper": "Scissor",
    "Scissor": "Rock",
}


def get_score(p1, p2):
    """Get score."""
    score = SCORE[p2]
    if p1 == "Rock" and p2 == "Paper":
        score += 6
    elif p1 == "Paper" and p2 == "Scissor":
        score += 6
    elif p1 == "Scissor" and p2 == "Rock":
        score += 6
    elif p1 == p2:
        score += 3
    return score


# Part 1
score = 0
for i in range(0, len(data), 2):
    p1 = LUT[data[i]]
    p2 = LUT[data[i + 1]]

    score += get_score(p1, p2)

print("Part 1:", score)
assert score == 13484


# Part 2
score = 0
for i in range(0, len(data), 2):
    p1 = LUT[data[i]]
    p2 = data[i + 1]

    if p2 == "X":
        p2 = LOSE[p1]
    elif p2 == "Y":
        p2 = p1
    elif p2 == "Z":
        p2 = WIN[p1]

    score += get_score(p1, p2)

print("Part 2:", score)
assert score == 13433
