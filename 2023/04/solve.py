"""Advent Of Code #03."""

with open("input") as f:
    cards = [line.strip() for line in f.readlines()]

points = 0

cards_count = {i: 1 for i in range(len(cards))}

for i, card in enumerate(cards):
    card_id, all_cards = card.split(": ")
    winning, my = all_cards.split(" | ")
    winning = winning.split(" ")
    my = my.split(" ")
    winning = [int(c) for c in winning if c]
    my = [int(c) for c in my if c]

    numbers = [c for c in my if c in winning]
    if numbers:
        points += 2 ** (len(numbers) - 1)
        for j in range(len(numbers)):
            cards_count[i + 1 + j] += cards_count[i]

print("Part 1:", points)
assert points == 32609

print("Part 2:", sum(cards_count.values()))
assert sum(cards_count.values()) == 14624680
