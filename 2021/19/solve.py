"""Advent Of Code #19."""
with open("input") as f:
    data = [d.strip() for d in f.readlines() if d.strip()]

scanner = []
for line in data:
    if line.startswith("---"):
        scanner.append([])
    else:
        scanner[-1].append(tuple(map(int, line.split(","))))

NUM_ORIENTATIONS = 24


def use_orientation(x, y, z, n):
    """Use 1 out of the 24 orientations."""
    # x -> x
    if n == 0:
        return (x, y, z)
    if n == 1:
        return (x, -y, -z)
    if n == 2:
        return (x, -z, y)
    if n == 3:
        return (x, z, -y)
    # x -> y
    if n == 4:
        return (-y, x, z)
    if n == 5:
        return (-z, x, -y)
    if n == 6:
        return (y, x, -z)
    if n == 7:
        return (z, x, y)
    # x -> z
    if n == 8:
        return (-y, -z, x)
    if n == 9:
        return (y, z, x)
    if n == 10:
        return (z, -y, x)
    if n == 11:
        return (-z, y, x)
    # x -> -x
    if n == 12:
        return (-x, -y, z)
    if n == 13:
        return (-x, -z, -y)
    if n == 14:
        return (-x, y, -z)
    if n == 15:
        return (-x, z, y)
    # x -> -y
    if n == 16:
        return (y, -x, z)
    if n == 17:
        return (-z, -x, y)
    if n == 18:
        return (-y, -x, -z)
    if n == 19:
        return (z, -x, -y)
    # x -> -z
    if n == 20:
        return (y, -z, -x)
    if n == 21:
        return (z, y, -x)
    if n == 22:
        return (-y, z, -x)
    if n == 23:
        return (-z, -y, -x)


def compare(scanner, reference, target):
    """Find matching beacons."""
    for jo in range(NUM_ORIENTATIONS):
        stats = {}
        for x0, y0, z0 in scanner[reference]:
            for x1, y1, z1 in scanner[target]:
                (x1, y1, z1) = use_orientation(x1, y1, z1, jo)
                dx = x0 - x1
                dy = y0 - y1
                dz = z0 - z1
                if (dx, dy, dz) not in stats:
                    stats[(dx, dy, dz)] = 0
                stats[(dx, dy, dz)] += 1
                if stats[(dx, dy, dz)] >= 12:
                    return (dx, dy, dz), jo


transformed = [0]
reference = 0
next_reference = []
positions = []

while len(transformed) < len(scanner):
    for target in range(len(scanner)):
        if target in transformed:
            continue

        result = compare(scanner, reference, target)
        if result is None:
            continue
        (dx, dy, dz), target_orientation = result
        positions.append((dx, dy, dz))
        for i in range(len(scanner[target])):
            scanner[target][i] = use_orientation(
                *scanner[target][i], target_orientation
            )
            scanner[target][i] = (
                scanner[target][i][0] + dx,
                scanner[target][i][1] + dy,
                scanner[target][i][2] + dz,
            )
        transformed.append(target)
        next_reference.append(target)
    reference = next_reference.pop(0)


# Part 1
beacons = set()
for i in range(len(scanner)):
    for j in range(len(scanner[i])):
        beacons.add(scanner[i][j])
print("Part 1:", len(beacons))
assert len(beacons) == 425


# Part 2
def manhattan_distance(p0, p1):
    """Calculate manhattan distance."""
    (x0, y0, z0) = p0
    (x1, y1, z1) = p1
    return abs(x0 - x1) + abs(y0 - y1) + abs(z0 - z1)


largest_distance = 0
for i in range(len(positions)):
    for j in range(i, len(positions)):
        distance = manhattan_distance(positions[i], positions[j])
        largest_distance = max(largest_distance, distance)
print("Part 2:", largest_distance)
assert largest_distance == 13354
