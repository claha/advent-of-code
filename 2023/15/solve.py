"""Advent Of Code #15."""
with open("input") as f:
    seq = f.read().strip().split(",")


def algo(s):
    """Run the algorithm."""
    v = 0
    for c in s:
        v = ((v + ord(c)) * 17) % 256
    return v


# Part 1
result = sum([algo(s) for s in seq])
print("Part 1:", result)
assert result == 498538

# Part 2
box = {i + 1: {} for i in range(256)}
for s in seq:
    if "=" in s:
        label, focal = s.split("=")
        focal = int(focal)
        i = algo(label) + 1
        box[i][label] = (
            focal,
            box[i][label][1] if label in box[i] else len(box[i]) + 1,
        )
    else:
        label = s.split("-")[0]
        i = algo(label) + 1
        if label not in box[i]:
            continue
        (_, index) = box[i][label]
        del box[i][label]
        for lab in box[i]:
            (focal, j) = box[i][lab]
            if j > index:
                box[i][lab] = (focal, j - 1)

power = 0
for index in box:
    power += sum([index * slot * focal for (focal, slot) in box[index].values()])
print("Part 2:", power)
assert power == 286278
