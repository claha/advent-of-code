"""Advent Of Code #10."""
with open("input") as f:
    data = [d.strip() for d in f.readlines()]

OPEN_CHUNK = ["(", "[", "{", "<"]
CLOSE_CHUNK = [")", "]", "}", ">"]

# Part 1
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
score = 0
tbc = {}  # to be closed
incomplete = []
for line in data:
    error = None
    for c in OPEN_CHUNK:
        tbc[c] = []
    for i, c in enumerate(line):
        if c in OPEN_CHUNK:
            tbc[c].append(i)
        elif c in CLOSE_CHUNK:
            oc = OPEN_CHUNK[CLOSE_CHUNK.index(c)]
            if len(tbc[oc]) > 0:
                oci = tbc[oc].pop()
                for tbci in tbc.values():
                    if not tbci:
                        continue
                    if tbci[-1] > oci:
                        error = c
            else:
                error = c
        if error:
            break

    if error is None:
        incomplete.append(tbc.copy())
    else:
        score += points[error]

print("Part 1:", score)
assert score == 167379


# Part 2
points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
scores = []
for tbc in incomplete:
    score = 0
    while True:
        maxes = {}
        for c in OPEN_CHUNK:
            if tbc[c]:
                maxes[c] = tbc[c][-1]
        if not maxes:
            break
        c = max(maxes, key=maxes.get)
        score *= 5
        score += points[c]
        tbc[c].pop()
    scores.append(score)
scores = sorted(scores)
score = scores[len(scores) // 2]
print("Part 2:", score)
assert score == 2776842859
