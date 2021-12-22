"""Advent Of Code #21."""
with open("input") as f:
    data = [int(line.split(": ")[1]) for line in f.readlines()]


def move(position, steps):
    """Move to new position."""
    return (position + steps - 1) % 10 + 1


# Part 1
player1_position = data[0]
player1_score = 0
player2_position = data[1]
player2_score = 0
dice = 0

while True:
    steps = 0
    for _ in range(3):
        dice += 1
        steps += dice
    player1_position = move(player1_position, steps)
    player1_score += player1_position
    if player1_score >= 1000:
        break

    steps = 0
    for _ in range(3):
        dice += 1
        steps += dice
    player2_position = move(player2_position, steps)
    player2_score += player2_position
    if player2_score >= 1000:
        break

score = player2_score if player1_score >= 1000 else player1_score
print("Part 1:", score * dice)
assert score * dice == 551901


# Part 2
class Game:
    """Game."""

    def __init__(self):
        """Create a game that caches results."""
        self.cache = {}
        self.steps = []
        for i in [1, 2, 3]:
            for j in [1, 2, 3]:
                for k in [1, 2, 3]:
                    self.steps.append(i + j + k)

    def play(self, player1_position, player1_score, player2_position, player2_score):
        """Play the game and play more games."""
        player1_wins = 0
        player2_wins = 0

        for steps in self.steps:
            # Do not overwrite original position since it should be used again
            player_position = move(player1_position, steps)
            player_score = player1_score + player_position

            if player_score >= 21:
                player1_wins += 1
            else:
                key = (player2_position, player2_score, player_position, player_score)
                if key in self.cache:
                    player2_wins_cache, player1_wins_cache = self.cache[key]
                else:
                    player2_wins_cache, player1_wins_cache = self.play(*key)
                    self.cache[key] = (player2_wins_cache, player1_wins_cache)
                player1_wins += player1_wins_cache
                player2_wins += player2_wins_cache

        return player1_wins, player2_wins


game = Game()
player1_wins, player2_wins = game.play(data[0], 0, data[1], 0)
player_wins = max(player1_wins, player2_wins)
print("Part 2:", player_wins)
assert player_wins == 272847859601291
