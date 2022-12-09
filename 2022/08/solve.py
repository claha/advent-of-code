"""Advent Of Code #08."""
with open("input") as f:
    data = f.read().strip().split("\n")

R = len(data)
C = len(data[0])


def is_visible(forrest, row, col, delta_row, delta_col):
    """Check if tree is visible from edge and how far it can see."""
    assert delta_row is None or delta_col is None
    view = 0

    if delta_col is None:
        for dr in delta_row:
            view += 1
            if forrest[dr][c] >= forrest[r][c]:
                return False, view
        return True, view

    for dc in delta_col:
        view += 1
        if forrest[r][dc] >= forrest[r][c]:
            return False, view
    return True, view


# Part 1
visible = 2 * R + 2 * C - 4
for r in range(1, R - 1):
    for c in range(1, C - 1):
        if (
            is_visible(data, r, c, range(r - 1, -1, -1), None)[0]
            or is_visible(data, r, c, range(r + 1, R), None)[0]
            or is_visible(data, r, c, None, range(c - 1, -1, -1))[0]
            or is_visible(data, r, c, None, range(c + 1, C))[0]
        ):
            visible += 1

print("Part 1:", visible)
assert visible == 1736


# Part 2
score = []
for r in range(1, R - 1):
    for c in range(1, C - 1):
        score.append(
            is_visible(data, r, c, range(r - 1, -1, -1), None)[1]
            * is_visible(data, r, c, range(r + 1, R), None)[1]
            * is_visible(data, r, c, None, range(c - 1, -1, -1))[1]
            * is_visible(data, r, c, None, range(c + 1, C))[1]
        )

print("Part 2:", max(score))
assert max(score) == 268800
