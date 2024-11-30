"""Advent Of Code #05."""

import math
from dataclasses import dataclass

with open("input") as f:
    data = [d.strip().replace(" -> ", ",").split(",") for d in f.readlines()]
data = [list(map(int, d)) for d in data]


@dataclass
class Line:
    """Class representing a line."""

    x1: int
    y1: int
    x2: int
    y2: int

    def horizontal(self):
        """Return if line is horizontal."""
        return self.x1 == self.x2

    def vertical(self):
        """Return if line is vertical."""
        return self.y1 == self.y2

    def walk(self):
        """Walk the line and return all points on it."""
        points = []

        dy = self.y2 - self.y1
        dx = self.x2 - self.x1
        gcd = math.gcd(dy, dx)
        dy //= gcd
        dx //= gcd

        y = self.y1
        x = self.x1
        while y != self.y2 or x != self.x2:
            points.append((y, x))
            y += dy
            x += dx
        points.append((y, x))

        return points


lines = [Line(d[0], d[1], d[2], d[3]) for d in data]

# Part 1
board = {}
for line in lines:
    # Only process horizontal or vertical lines
    if not line.horizontal() and not line.vertical():
        continue
    points = line.walk()
    for point in points:
        if point not in board:
            board[point] = 0
        board[point] += 1

count = 0
for crossings in board.values():
    if crossings > 1:
        count += 1

print("Part 1:", count)
assert count == 4655

# Part 2
for line in lines:
    # Horizontal and vertical lines have already been processed
    if line.horizontal() or line.vertical():
        continue
    points = line.walk()
    for point in points:
        if point not in board:
            board[point] = 0
        board[point] += 1

count = 0
for crossings in board.values():
    if crossings > 1:
        count += 1
print("Part 2:", count)
assert count == 20500
