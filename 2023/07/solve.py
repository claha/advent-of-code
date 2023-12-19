"""Advent Of Code #07."""
with open("input") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]

CARD_RANK = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def get_hand_type(hand, use_joker=False):
    """Determine the hand type."""
    value_counts = {value: hand.count(value) for value in set(hand)}

    score = 0

    if 5 in value_counts.values():
        score += 6
    elif 4 in value_counts.values():
        score += 5
        if use_joker and "J" in value_counts:
            score += 1  # Int five of a kind
    elif set(value_counts.values()) == {3, 2}:
        score += 4
        if use_joker and "J" in value_counts:
            score += 2  # Int five of a kind
    elif 3 in value_counts.values():
        score += 3
        if use_joker and "J" in value_counts:
            score += 2  # Into four of a kind
    elif list(value_counts.values()).count(2) == 2:
        score += 2
        if use_joker and "J" in value_counts:
            if value_counts["J"] == 1:
                score += 2  # Into full house
            elif value_counts["J"] == 2:
                score += 3  # Into four of a kind
    elif 2 in value_counts.values():
        score += 1
        if use_joker and "J" in value_counts:
            if value_counts["J"] == 2:
                score += 2  # Into three of a kind
            elif value_counts["J"] == 1:
                score += 2  # Into three of a kind
    else:
        score += 0
        if use_joker and "J" in value_counts:
            score += 1

    score *= 10000000000

    for i, card in enumerate(reversed(hand)):
        if use_joker and card == "J":
            score += 1 * 10 ** (2 * i)
        else:
            score += CARD_RANK[card] * 10 ** (2 * i)

    return score


# Part 1
score = 0
for i, (hand, bid) in enumerate(sorted(lines, key=lambda x: get_hand_type(x[0]))):
    score += (i + 1) * int(bid)

print("Part 1:", score)
assert score == 253933213

# Part 2
score = 0
for i, (hand, bid) in enumerate(
    sorted(lines, key=lambda x: get_hand_type(x[0], use_joker=True))
):
    score += (i + 1) * int(bid)

print("Part 2:", score)
assert score == 253473930
