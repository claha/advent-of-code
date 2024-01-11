"""Advent Of Code #24."""
import numpy as np

with open("input") as f:
    stones = [
        list(map(int, line.strip().replace(" @", ",").split(",")))
        for line in f.readlines()
    ]

TEST_AREA = (200000000000000, 400000000000000)


def intersection(stone0, stone1):
    """Calculate y,x intersection."""
    x0, y0, _, dx0, dy0, _ = stone0
    x1, y1, _, dx1, dy1, _ = stone1

    # Check if lines are parallel
    det = dy0 * dx1 - dy1 * dx0
    if det == 0:
        return None, None

    # Calculate the intersection point
    t = ((y1 - y0) * dx1 - (x1 - x0) * dy1) / det
    y, x = (y0 + t * dy0, x0 + t * dx0)

    # Check that it is valid
    if y < y0 and dy0 > 0:
        return None, None
    if y > y0 and dy0 < 0:
        return None, None
    if x < x0 and dx0 > 0:
        return None, None
    if x > x0 and dx0 < 0:
        return None, None
    if y < y1 and dy1 > 0:
        return None, None
    if y > y1 and dy1 < 0:
        return None, None
    if x < x1 and dx1 > 0:
        return None, None
    if x > x1 and dx1 < 0:
        return None, None

    return y, x


# Part 1
inside = 0
for i, s0 in enumerate(stones):
    for j, s1 in enumerate(stones[i + 1 :]):
        y, x = intersection(s0, s1)
        if (
            y is not None
            and x is not None
            and TEST_AREA[0] <= y <= TEST_AREA[1]
            and TEST_AREA[0] <= x <= TEST_AREA[1]
        ):
            inside += 1
print("Part 1:", inside)
assert inside == 26657

# Part 2
# x,y,z,dx,dy,dz is the rock
# For a stone x0,y0,z0,dx0,dy0,dz0
# x + t0 * dx = x0 + t0 * dx0    t0 = (x0 - x)/(dx - dx0)  (1)
# y + t0 * dy = y0 + t0 * dy0 => t0 = (y0 - y)/(dy - dy0)  (2)
# z + t0 * dz = z0 + t0 * dz0    t0 = (z0 - z)/(dz - dz0)  (3)
# Set (1) = (2) =>
# (x0 - x)/(dx - dx0) = (y0 - y)/(dy - dy0) => (x0 - x)(dy - dy0) = (y0 - y)(dx - dx0) =>
# x0 * dy - x0 * dy0 - x * dy + x * dy0 = y0 * dx - y0 * dx0 - y * dx + y * dx0 =>
# y * dx - x * dy = y0 * dx - y0 * dx0 - y * dx + y * dx0 - x0 * dy + x0 * dy0 - x * dy0  (4)
# Doing the same with a stone x1,y1,z1,dx1,dy1,dz1 gives
# y * dx - x * dy = y1 * dx - y1 * dx1 - y * dx + y * dx1 - x1 * dy + x1 * dy1 - x * dy1  (5)
# So then (4) = (5) =>
# (dy1 - dy0) * x + (dx0 - dx1) * y + (y0 - y1) * dx + (x1 - x0) * dy = - x0 * dy0 + y0 * dx0 + x1 * dy1 - y1 * dx1
# i.e. A*x + B*y + C*dx + D*dy = E, which is a system of linear equations
coeffs = []
consts = []
for i in range(len(stones)):
    x0, y0, z0, dx0, dy0, dz0 = stones[i]
    for j in range(i + 1, len(stones)):
        x1, y1, z1, dx1, dy1, dz1 = stones[j]
        A = dy1 - dy0
        B = dx0 - dx1
        C = y0 - y1
        D = x1 - x0
        E = -x0 * dy0 + y0 * dx0 + x1 * dy1 - y1 * dx1
        coeffs.append([A, B, C, D])
        consts.append(E)
solxy = np.linalg.solve(np.array(coeffs[:4]), np.array(consts[:4]))

y = solxy[1]
dy = solxy[3]
coeffs = []
consts = []
for i in range(len(stones)):
    x0, y0, z0, dx0, dy0, dz0 = stones[i]
    for j in range(i + 1, len(stones)):
        x1, y1, z1, dx1, dy1, dz1 = stones[j]
        A = dy1 - dy0
        B = dz0 - dz1
        C = y0 - y1
        D = z1 - z0
        E = -z0 * dy0 + y0 * dz0 + z1 * dy1 - y1 * dz1
        coeffs.append([A, C])
        consts.append(E - B * y - D * dy)
solz = np.linalg.solve(np.array(coeffs[:2]), np.array(consts[:2]))

print(
    "Part 2:", int(solxy[0] + solxy[1] + solz[0] + 0.5)
)  # Didn't need +0.5 on my other computer...
assert int(solxy[0] + solxy[1] + solz[0] + 0.5) == 828418331313365
