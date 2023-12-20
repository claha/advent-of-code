"""Advent Of Code #13."""
with open("input") as f:
    matrices = [matrix.strip() for matrix in f.read().split("\n\n")]


def mirror_size(x, N, M=1):
    """Calc size of mirror."""
    if x < N - x:
        return (x + 1) * M
    return (N - x) * M


def find_reflection(data):
    """Find all reflections."""
    candidates = []
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            candidates.append(i)

    invalid_candidates = []
    fixable_candidates = []  # Can be fixed with one bit
    for c in candidates:
        a, b = c - 1, c + 2
        while a >= 0 and b < len(data):
            if data[a] != data[b]:
                invalid_candidates.append(c)
                if bin(abs(data[a] - data[b])).count("1") == 1:
                    fixable_candidates.append((c, a, b))
                break
            a -= 1
            b += 1
    for c in invalid_candidates:
        candidates.remove(c)

    for i in range(len(data) - 1):
        if bin(abs(data[i] - data[i + 1])).count("1") == 1:
            fixable_candidates.append((i, i, i + 1))

    invalid_candidates = []
    for c, a, b in fixable_candidates:
        attempt = data[::]
        attempt[a] = attempt[b]
        a, b = c - 1, c + 2
        while a >= 0 and b < len(data):
            if attempt[a] != attempt[b]:
                invalid_candidates.append(c)
                break
            a -= 1
            b += 1
    fixable_candidates = [c for c, _, _ in fixable_candidates]
    for c in invalid_candidates:
        fixable_candidates.remove(c)

    if len(candidates) == 0:
        candidate = None
    elif len(candidates) == 1:
        candidate = candidates[0]

    if len(fixable_candidates) == 0:
        fixable = None
    elif len(fixable_candidates) == 1:
        fixable = fixable_candidates[0]
    elif len(fixable_candidates) == 2:
        if mirror_size(fixable_candidates[0], len(data)) > mirror_size(
            fixable_candidates[1], len(data)
        ):
            fixable = fixable_candidates[0]
        else:
            fixable = fixable_candidates[1]

    return candidate, fixable


num_rows = 0
num_columns = 0
num_rows_smudge = 0
num_columns_smudge = 0

for m in matrices:
    m = m.replace("#", "1").replace(".", "0").split("\n")
    rows = [int(r, 2) for r in m]
    cols = ["".join([m[r][c] for r in range(len(m))]) for c in range(len(m[0]))]
    cols = [int(c, 2) for c in cols]
    row_ref, row_ref_smudge = find_reflection(rows)
    col_ref, col_ref_smudge = find_reflection(cols)

    if row_ref is not None and col_ref is not None:
        if mirror_size(row_ref, len(rows), len(cols)) >= mirror_size(
            col_ref, len(cols), len(rows)
        ):
            col_ref = None
        else:
            row_ref = None
    if row_ref is not None:
        num_rows += row_ref + 1
    else:
        num_columns += col_ref + 1

    if row_ref_smudge is not None and col_ref_smudge is not None:
        if mirror_size(row_ref_smudge, len(rows), len(cols)) >= mirror_size(
            col_ref_smudge, len(cols), len(rows)
        ):
            col_ref_smudge = None
        else:
            row_ref_smudge = None
    if row_ref_smudge is not None:
        num_rows_smudge += row_ref_smudge + 1
    else:
        num_columns_smudge += col_ref_smudge + 1

print("Part 1:", 100 * num_rows + num_columns)
assert 100 * num_rows + num_columns == 31877
print("Part 2:", 100 * num_rows_smudge + num_columns_smudge)
assert 100 * num_rows_smudge + num_columns_smudge == 42996
