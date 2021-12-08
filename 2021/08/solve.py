"""Advent Of Code #08."""
with open("input") as f:
    data = [d for d in f.readlines()]
data = [d.replace("|", "").split() for d in data]

# Part 1
count = 0
for segments in data:
    for i in [-1, -2, -3, -4]:
        if len(segments[i]) in [2, 4, 3, 7]:
            count += 1

print("Part 1:", count)
assert count == 532


# Part 2
digits = [
    {"a", "b", "c", "e", "f", "g"},
    {"c", "f"},
    {"a", "c", "d", "e", "g"},
    {"a", "c", "d", "f", "g"},
    {"b", "c", "d", "f"},
    {"a", "b", "d", "f", "g"},
    {"a", "b", "d", "e", "f", "g"},
    {"a", "c", "f"},
    {"a", "b", "c", "d", "e", "f", "g"},
    {"a", "b", "c", "d", "f", "g"},
]

compares = []
for i in range(9):
    for j in range(i + 1, 10):
        compares.append((i, j))

# Code used to determine what to map in the if/elif below
# freq1 = [0]*10
# freq2 = [0]*10
# for (i, j) in compares:
#     d1 = digits[i]
#     d2 = digits[j]
#     diff = (d1 | d2) - (d1 & d2)
#     if len(diff) == 1:
#         freq1[i] += 1
#         freq1[j] += 1
#     elif len(diff) == 2:
#         freq2[i] += 1
#         freq2[j] += 1

# for (i, j) in compares:
#     d1 = digits[i]
#     d2 = digits[j]
#     diff = (d1 | d2) - (d1 & d2)
#     if len(diff) == 1:
#         print(i, j, diff, freq1[i], freq1[j])

# for (i, j) in compares:
#     d1 = digits[i]
#     d2 = digits[j]
#     diff = (d1 | d2) - (d1 & d2)
#     if len(diff) == 2:
#         print(i, j, diff, freq2[i], freq2[j])

numbers = []
for segments in data:
    mapping = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
    }

    # Create frequency map
    freq1 = [0] * 10
    freq2 = [0] * 10
    for (i, j) in compares:
        d1 = set(segments[i])
        d2 = set(segments[j])
        diff = (d1 | d2) - (d1 & d2)
        if len(diff) == 1:
            freq1[i] += 1
            freq1[j] += 1
        if len(diff) == 2:
            freq2[i] += 1
            freq2[j] += 1

    # Add mappings based on 1 segment diffs
    for (i, j) in compares:
        d1 = set(segments[i])
        d2 = set(segments[j])
        diff = (d1 | d2) - (d1 & d2)
        if len(diff) == 1:
            key = min(diff)
            if freq1[i] == 1 and freq1[j] == 1:  # 1 and 7
                mapping[key] = "a"
            elif (freq1[i] == 1 and freq1[j] == 3) or (
                freq1[i] == 3 and freq1[j] == 1
            ):  # 0 and 8 or 3 and 9
                if len(segments[i]) == 5 or len(segments[j]) == 5:  # 3
                    mapping[key] = "b"
                elif len(segments[i]) == 7 or len(segments[j]) == 7:  # 8
                    mapping[key] = "d"
            elif freq1[i] == 2 and freq1[j] == 2:  # 5 and 6
                mapping[key] = "e"
            elif (freq1[i] == 2 and freq1[j] == 3) or (
                freq1[i] == 3 and freq1[j] == 2
            ):  # 5 and 9 or 6 and 8
                mapping[key] = "c"

    # Add mappings based on 2 segment diffs
    for (i, j) in compares:
        d1 = set(segments[i])
        d2 = set(segments[j])
        diff = (d1 | d2) - (d1 & d2)
        if len(diff) == 2:
            if (freq2[i] == 1 and freq2[j] == 4) or (
                freq2[i] == 4 and freq2[j] == 1
            ):  # 3 and 7
                key = min(diff) if mapping[min(diff)] is None else max(diff)
                mapping[key] = "g"

    # There should be one unmapped
    for key in mapping:
        if mapping[key] is None:
            mapping[key] = "f"
            break

    # Use mapping the get the number
    number = ""
    for i in [-4, -3, -2, -1]:
        d = {mapping[s] for s in segments[i]}
        number += str(digits.index(d))
    numbers.append(int(number))

print("Part 2:", sum(numbers))
assert sum(numbers) == 1011284
