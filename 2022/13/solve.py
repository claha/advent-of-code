"""Advent Of Code #13."""
with open("input") as f:
    data = f.read().strip().split("\n\n")

pairs = [pair.split("\n") for pair in data]
pairs = [(eval(left), eval(right)) for (left, right) in pairs]


def compare_int(left, right):
    """Compare left and right integers."""
    if left < right:
        return True
    if left == right:
        return None
    return False


def compare(left, right):
    """Compare left and right."""
    left_is_int = isinstance(left, int)
    right_is_int = isinstance(right, int)

    if left_is_int and right_is_int:
        return compare_int(left, right)

    if not left_is_int and not right_is_int:
        left_N = len(left)
        right_N = len(right)
        N = min(left_N, right_N)
        for i in range(N):
            res = compare(left[i], right[i])
            if res is None:
                continue
            return res
        return compare_int(left_N, right_N)

    if left_is_int:
        left = [left]
    elif right_is_int:
        right = [right]
    return compare(left, right)


# Part 1
ordered_pairs = []
for i, (left, right) in enumerate(pairs):
    if compare(left, right):
        ordered_pairs.append(i + 1)

print("Part 1:", sum(ordered_pairs))
assert sum(ordered_pairs) == 5292


# Part 2
divider_packets = [[[2]], [[6]]]
packets = []
for left, right in pairs:
    packets.append(left)
    packets.append(right)
packets.extend(divider_packets)

N = len(packets)
ordering = {i: 0 for i in range(N)}
for i in range(N):
    for j in range(i + 1, N):
        if compare(packets[i], packets[j]):
            ordering[j] += 1
        else:
            ordering[i] += 1
ordering = sorted([(value, key) for key, value in ordering.items()])

decoder_key = 1
for i, (_, j) in enumerate(ordering):
    if packets[j] in divider_packets:
        decoder_key *= i + 1
print("Part 2:", decoder_key)
assert decoder_key == 23868
