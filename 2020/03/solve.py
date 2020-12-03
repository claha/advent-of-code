"""Advent Of Code #03."""


class Forest:
    """Class representing a forest."""

    OPEN = "."
    TREE = "#"

    def __init__(self, data):
        """Initialize the forest."""
        self._data = data
        self.height = len(data)
        self.width = len(data[0])

    def is_open(self, y, x):
        """Check if (y,x) is open."""
        return self._data[y][x] == Forest.OPEN

    def is_tree(self, y, x):
        """Check if (y,x) is a tree."""
        return self._data[y][x] == Forest.TREE


with open("input") as f:
    data = f.read().split()

forest = Forest(data)


# Part 1
def walk_and_count_trees(dy, dx):
    """Walk (dy, dx) and count trees."""
    trees = 0
    y = 0
    x = 0

    while y < forest.height:
        if forest.is_tree(y, x):
            trees += 1
        y += dy
        x += dx
        x %= forest.width

    return trees


trees = walk_and_count_trees(1, 3)
print("Part 1:", trees)
assert trees == 220

# Part 2
trees = 1
for (dy, dx) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    trees *= walk_and_count_trees(dy, dx)
print("Part 2:", trees)
assert trees == 2138320800
