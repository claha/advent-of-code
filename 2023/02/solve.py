"""Advent Of Code #02."""
with open("input") as f:
    games = [line.strip() for line in f.readlines()]

possible_games_sum = 0
power_sum = 0

for game in games:
    game_id, rounds = game.split(": ")
    game_id = int(game_id[4:])
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for round in rounds.split("; "):
        hands = round.split(", ")
        for hand in hands:
            count, color = hand.split(" ")
            count = int(count)

            maxes[color] = max(maxes[color], count)

    if maxes["red"] <= 12 and maxes["green"] <= 13 and maxes["blue"] <= 14:
        possible_games_sum += game_id

    power_sum += maxes["red"] * maxes["green"] * maxes["blue"]

print("Part 1:", possible_games_sum)
assert possible_games_sum == 2156
print("Part 2:", power_sum)
assert power_sum == 66909
