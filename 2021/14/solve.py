"""Advent Of Code #14."""

with open("input") as f:
    data = [d.strip() for d in f.readlines()]

polymer = data[0]
rules = {}
for d in data[2:]:
    a, b = d.split(" -> ")
    rules[a] = [a[0] + b, b + a[1]]


def count_letters(polymer, freq):
    """Count letters."""
    letters = {}
    letters[polymer[0]] = 1
    letters[polymer[-1]] = 1
    for key, value in freq.items():
        if key[0] not in letters:
            letters[key[0]] = 0
        if key[1] not in letters:
            letters[key[1]] = 0
        letters[key[0]] += value
        letters[key[1]] += value
    for key in letters:
        letters[key] //= 2
    return letters


# Part 1
freq = {}
for i in range(len(polymer) - 1):
    key = polymer[i : i + 2]
    if key not in freq:
        freq[key] = 0
    freq[key] += 1

for _ in range(10):
    freq_new = {}
    for key in freq:
        for k in rules[key]:
            if k not in freq_new:
                freq_new[k] = 0
            freq_new[k] += freq[key]
    freq = freq_new

letters = count_letters(polymer, freq)
diff = max(letters.values()) - min(letters.values())
print("Part 1:", diff)
assert diff == 2360


# Part 2
for _ in range(30):
    freq_new = {}
    for key in freq:
        for k in rules[key]:
            if k not in freq_new:
                freq_new[k] = 0
            freq_new[k] += freq[key]
    freq = freq_new

letters = count_letters(polymer, freq)
diff = max(letters.values()) - min(letters.values())
print("Part 2:", diff)
assert diff == 2967977072188
