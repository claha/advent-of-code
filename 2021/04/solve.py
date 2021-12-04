"""Advent Of Code #04."""
with open("input") as f:
    data = f.read().split()

BOARD_SIZE = 5


class Board:
    """Representation of a board."""

    def __init__(self, numbers):
        """Create a board."""
        self.numbers = numbers
        self.last_marked = None

    def mark(self, n):
        """Mark number on board."""
        if n in self.numbers:
            self.numbers[self.numbers.index(n)] = 0
            self.last_marked = n

    def won(self):
        """Check if board has won."""
        for i in range(0, len(self.numbers), BOARD_SIZE):
            if sum(self.numbers[i : i + BOARD_SIZE]) == 0:
                return True
        for i in range(0, BOARD_SIZE):
            if sum(self.numbers[i::BOARD_SIZE]) == 0:
                return True
        return False

    def score(self):
        """Get score of board."""
        return sum(self.numbers) * self.last_marked


def play(boards, order, played):
    """Play until a board wins and return its score."""
    for i, n in enumerate(order[played:]):
        for board in boards:
            board.mark(n)
        for board in boards:
            if board.won():
                return board.score(), played + i


order = [int(d) for d in data[0].split(",")]
board_numbers = [int(d) for d in data[1:]]
boards = []
for i in range(0, len(board_numbers), BOARD_SIZE * BOARD_SIZE):
    boards.append(Board(board_numbers[i : i + BOARD_SIZE * BOARD_SIZE]))

# Part 1
score, played = play(boards, order, 0)
print("Part 1:", score)
assert score == 33348

# Part 2
while len(boards) > 1:
    for i in range(len(boards)):
        if boards[i].won():
            del boards[i]
            break
    score, played = play(boards, order, played)
print("Part 2:", score)
assert score == 8112
