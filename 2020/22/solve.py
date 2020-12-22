"""Advent Of Code #22."""
with open("input") as f:
    data = f.read()

player1, player2 = data.split("\n\n")


def calculate_score(deck):
    """Calculate score."""
    score = 0
    for i, card in enumerate(reversed(deck)):
        score += (i + 1) * card
    return score


# Part 1
deck1 = [int(card) for card in player1.splitlines()[1:]]
deck2 = [int(card) for card in player2.splitlines()[1:]]


def play(deck1, deck2):
    """Play a game of combat."""
    while len(deck1) and len(deck2):
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return deck1, deck2


deck1, deck2 = play(deck1, deck2)
assert len(deck1) == 0 or len(deck2) == 0
score = calculate_score(deck1 + deck2)
print("Part 1:", score)
assert score == 32366

# Part 2
deck1 = [int(card) for card in player1.splitlines()[1:]]
deck2 = [int(card) for card in player2.splitlines()[1:]]


def play(deck1, deck2):
    """Play a game of recrusive combat."""
    games = set()
    while len(deck1) and len(deck2):
        game = (str(deck1), str(deck2))
        if game in games:
            return deck1, []
        games.add(game)

        card1, card2 = deck1.pop(0), deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            sub_deck1, sub_deck2 = play(deck1[:card1], deck2[:card2])
            if sub_deck1:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])
        else:
            if card1 > card2:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])

    return deck1, deck2


deck1, deck2 = play(deck1, deck2)
assert len(deck1) == 0 or len(deck2) == 0
score = calculate_score(deck1 + deck2)
print("Part 2:", score)
assert score == 30891
