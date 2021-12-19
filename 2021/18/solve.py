"""Advent Of Code #18."""
with open("input") as f:
    data = [eval(d) for d in f.read().split()]


class Node:
    """Representation of a node."""

    def __init__(self, left, right):
        """Create a node."""
        if isinstance(left, list):
            self.left = Node(left[0], left[1])
        else:
            self.left = left
        if isinstance(right, list):
            self.right = Node(right[0], right[1])
        else:
            self.right = right

    def use_explosion_right(self, value):
        """Use the explosion."""
        if not is_node(self.left):
            self.left += value
            return True
        else:
            if self.left.use_explosion_right(value):
                return True
        return False

    def use_explosion_left(self, value):
        """Use the explosion."""
        if not is_node(self.right):
            self.right += value
            return True
        else:
            if self.right.use_explosion_left(value):
                return True
        return False

    def explode(self, depth=0):
        """Explode node."""
        if depth == 4:
            if is_node(self.left) or is_node(self.right):
                return [None, None, False]
            return [self.left, self.right, True]

        exploding_left = None
        if is_node(self.left):
            exploding_left = self.left.explode(depth + 1)
        if exploding_left:
            if exploding_left[2]:
                self.left = 0
                exploding_left[2] = False
            elif exploding_left[0] and not is_node(self.left):
                self.left += exploding_left[0]
                exploding_left[0] = None
            if exploding_left[1] and not is_node(self.right):
                self.right += exploding_left[1]
                exploding_left[1] = None
            elif exploding_left[1]:
                if self.right.use_explosion_right(exploding_left[1]):
                    exploding_left[1] = None
            return exploding_left

        exploding_right = None
        if is_node(self.right):
            exploding_right = self.right.explode(depth + 1)
        if exploding_right:
            if exploding_right[2]:
                self.right = 0
                exploding_right[2] = False
            elif exploding_right[1] and not is_node(self.right):
                self.right += exploding_right[1]
                exploding_right[1] = None
            if exploding_right[0] and not is_node(self.left):
                self.left += exploding_right[0]
                exploding_right[0] = None
            elif exploding_right[0]:
                if self.left.use_explosion_left(exploding_right[0]):
                    exploding_right[0] = None
            return exploding_right

    def split(self):
        """Split node."""
        if not is_node(self.left):
            if self.left > 9:
                self.left = Node(int(self.left / 2), int(self.left / 2 + 0.5))
                return True
        elif self.left.split():
            return True

        if not is_node(self.right):
            if self.right > 9:
                self.right = Node(int(self.right / 2), int(self.right / 2 + 0.5))
                return True
        elif self.right.split():
            return True

    def reduce(self):
        """Reduce node."""
        while True:
            while self.explode():
                pass
            if not root.split():
                break

    def magnitude(self):
        """Calculate magnitude."""
        m = 0
        if is_node(self.left):
            m += 3 * self.left.magnitude()
        else:
            m += 3 * self.left
        if is_node(self.right):
            m += 2 * self.right.magnitude()
        else:
            m += 2 * self.right
        return m


def is_node(node):
    """Check node is an Node object."""
    return isinstance(node, Node)


# Part 1
root = Node(data[0], data[1])
root.reduce()
for i in range(2, len(data)):
    root = Node(root, Node(*data[i]))
    root.reduce()

magnitude = root.magnitude()
print("Part 1:", magnitude)
assert magnitude == 4033


# Part 2
max_magnitude = 0
for i in range(len(data)):
    for j in range(len(data)):
        root = Node(data[i], data[j])
        root.reduce()
        magnitude = root.magnitude()
        max_magnitude = max(magnitude, max_magnitude)


print("Part 2:", max_magnitude)
assert max_magnitude == 4864
