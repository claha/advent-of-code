"""Advent Of Code #09."""
with open("input") as f:
    data = f.read().strip().split("\n")
data = [d.split(" ") for d in data]


def move_head(head, direction):
    """Move head in given direction."""
    dy, dx = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (1, 0),
        "D": (-1, 0),
    }[direction]
    return (head[0] + dy, head[1] + dx)


def move_tail(head, tail):
    """Move tail based on head position."""
    dy = head[0] - tail[0]
    dx = head[1] - tail[1]
    if abs(dy) <= 1 and abs(dx) <= 1:
        return tail

    if abs(dy) == 2:
        dy //= 2
    if abs(dx) == 2:
        dx //= 2
    return (tail[0] + dy, tail[1] + dx)


# Part 1
h = (0, 0)
t = (0, 0)
visited = set()
visited.add(t)
for (direction, steps) in data:
    for _ in range(int(steps)):
        h = move_head(h, direction)
        t = move_tail(h, t)
        visited.add(t)

print("Part 1:", len(visited))
assert len(visited) == 6181

# Part 2
rope = [(0, 0) for _ in range(10)]
visited = set()
visited.add(rope[-1])
for (direction, steps) in data:
    for _ in range(int(steps)):
        rope[0] = move_head(rope[0], direction)
        for i in range(1, len(rope)):
            rope[i] = move_tail(rope[i - 1], rope[i])
        visited.add(rope[-1])

print("Part 2:", len(visited))
assert len(visited) == 2386
