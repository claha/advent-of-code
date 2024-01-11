"""Advent Of Code #22."""
import copy


class Brick:
    """Brick."""

    def __init__(self, x0, y0, z0, x1, y1, z1):
        """Initialize a brick."""
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

    def __repr__(self):
        """Representation."""
        return f"Brick<({self.x0},{self.y0},{self.z0}),({self.x1},{self.y1},{self.z1})>"

    def __lt__(self, other):
        """Less than."""
        return self.z0 < other.z0

    def __eq__(self, other):
        """Equal."""
        return (
            self.x0 == other.x0
            and self.y0 == other.y0
            and self.z0 == other.z0
            and self.x1 == other.x1
            and self.y1 == other.y1
            and self.z1 == other.z1
        )

    def __hash__(self):
        """Hash."""
        return (
            hash(self.x0)
            + hash(self.y0)
            + hash(self.z0)
            + hash(self.x1)
            + hash(self.y1)
            + hash(self.z1)
        )

    def settle(self, bricks):
        """Make it settle at the bottom."""
        while self.z0 > 1 and not any([self.supported(brick) for brick in bricks]):
            self.z0 -= 1
            self.z1 -= 1

    def overlap(self, other):
        """Check if brick overlaps with other brick."""
        return not (
            self.x0 > other.x1
            or self.x1 < other.x0
            or self.y0 > other.y1
            or self.y1 < other.y0
        )

    def supported(self, other):
        """Check if brick is supported by other brick."""
        return self.overlap(other) and other.z1 + 1 == self.z0


with open("input") as f:
    bricks = [
        Brick(*list(map(int, line.strip().replace("~", ",").split(","))))
        for line in f.readlines()
    ]

bricks = sorted(bricks)
for brick in bricks:
    brick.settle(bricks)

supported = {i: [] for i in range(len(bricks))}
for i in range(len(bricks)):
    for j in range(len(bricks)):
        if j == i:
            continue
        if bricks[i].supported(bricks[j]):
            supported[i].append(j)

can_not_be_disintegrated = {
    supported[i][0] for i in range(len(bricks)) if len(supported[i]) == 1
}
print("Part 1:", len(bricks) - len(can_not_be_disintegrated))
assert len(bricks) - len(can_not_be_disintegrated) == 463


count = 0
for brick in can_not_be_disintegrated:
    moved = set()
    bs = copy.deepcopy(bricks)
    bs.remove(bs[brick])

    updated = True
    while updated:
        updated = False
        for b in bs:
            z = b.z0
            b.settle(bs)
            if b.z0 < z:
                moved.add(b)
                updated = True
    count += len(moved)
print("Part 2:", count)
assert count == 89727
