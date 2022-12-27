"""Advent Of Code #23."""
with open("input") as f:
    data = [line.strip() for line in f.readlines()]

N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)
NE = (-1, 1)
NW = (-1, -1)
SE = (1, 1)
SW = (1, -1)
DIRS = [
    [N, NE, NW],
    [S, SE, SW],
    [W, NW, SW],
    [E, NE, SE],
]


class Elf:
    """Elf."""

    def __init__(self, y, x):
        """Create elf."""
        self.y = y
        self.x = x
        self.yp = None
        self.xp = None

    def propose(self, coords):
        """Propose move."""
        changes = False
        free = {}
        for (dy, dx) in [N, S, W, E, NE, NW, SE, SW]:
            free[(dy, dx)] = (self.y + dy, self.x + dx) not in coords
        self.yp = self.y
        self.xp = self.x

        if not all(free.values()):
            self.yp = self.y
            self.xp = self.x
            for [(dy0, dx0), (dy1, dx1), (dy2, dx2)] in DIRS:
                if free[(dy0, dx0)] and free[(dy1, dx1)] and free[(dy2, dx2)]:
                    self.yp = self.y + dy0
                    self.xp = self.x + dx0
                    changes = True
                    break

        return changes

    def move(self, proposes):
        """Move elf."""
        if proposes[(self.yp, self.xp)] == 1:
            self.y = self.yp
            self.x = self.xp
        self.yp = None
        self.xp = None


elfs = set()
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "#":
            elfs.add(Elf(y, x))

# Part 1
for _ in range(10):
    coords = {(e.y, e.x) for e in elfs}
    for elf in elfs:
        elf.propose(coords)

    proposes = {}
    for elf in elfs:
        if (elf.yp, elf.xp) not in proposes:
            proposes[(elf.yp, elf.xp)] = 0
        proposes[(elf.yp, elf.xp)] += 1
    for elf in elfs:
        elf.move(proposes)

    DIRS.append(DIRS.pop(0))

miny = min(elf.y for elf in elfs)
maxy = max(elf.y for elf in elfs)
minx = min(elf.x for elf in elfs)
maxx = max(elf.x for elf in elfs)

empty = (maxy + 1 - miny) * (maxx + 1 - minx) - len(elfs)
print("Part 1:", empty)
assert empty == 3877


# Part 2
rounds = 10
while True:
    rounds += 1
    changes = False
    coords = {(e.y, e.x) for e in elfs}
    for elf in elfs:
        changes |= elf.propose(coords)

    if not changes:
        break

    proposes = {}
    for elf in elfs:
        if (elf.yp, elf.xp) not in proposes:
            proposes[(elf.yp, elf.xp)] = 0
        proposes[(elf.yp, elf.xp)] += 1

    for elf in elfs:
        elf.move(proposes)

    DIRS.append(DIRS.pop(0))

print("Part 2:", rounds)
assert rounds == 982
