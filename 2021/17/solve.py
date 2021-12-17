"""Advent Of Code #17."""
import math
import re

with open("input") as f:
    data = f.read()
xmin, xmax, ymin, ymax = list(map(int, re.findall(r"-?\d+", data)))


def launch(dx, dy, target_xmin, target_xmax, target_ymin, target_ymax):
    """Launch probe and return its maximum height if target is hit."""
    ymax = None
    x, y = 0, 0
    while True:
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1

        ymax = max(y, ymax) if ymax is not None else y

        # Within target area
        if target_xmin <= x <= target_xmax and target_ymin <= y <= target_ymax:
            return ymax

        # Gone off target
        if x > target_xmax or y < target_ymin:
            break
        if dx == 0 and x < target_xmin:
            break


maximum = 0
hits = 0
# The x position is an artithmetic sum, x = dx + (dx - 1) + (dx - 2) + .. + 0 =
# (dx + 0) * (dx + 1) / 2 = dx * (dx + 1) / 2 which needs to be larger than xmin.
# Thus dx ^ 2 + dx - 2 * xmin > 0, dx = -1 / 2 +/- sqrt(1 / 4 + 2 * xmin)
# if dx is larger than xmax or dy is smaller than ymin the probe will be outside of the
# target area after one step. Should be possible to figure out an upper limit of dy as
# well but for now a "large" number is good enough.
for dx in range(math.ceil(-0.5 + (0.25 + 2 * xmin) ** 0.5), xmax + 1):
    for dy in range(ymin, 100):
        y = launch(dx, dy, xmin, xmax, ymin, ymax)
        if y is not None:
            hits += 1
            maximum = max(y, maximum)

# Part 1
print("Part 1:", maximum)
assert maximum == 2701


# Part 2
print("Part 2:", hits)
assert hits == 1070
