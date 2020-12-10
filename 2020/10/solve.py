"""Advent Of Code #10."""
with open("input") as f:
    data = [int(d) for d in f.read().split()]
jolts = [0] + sorted(data) + [max(data) + 3]

# Part 1
diff_1 = 0
diff_3 = 0
for i in range(1, len(jolts)):
    diff = jolts[i] - jolts[i - 1]
    diff_1 += diff == 1
    diff_3 += diff == 3

print("Part 1:", diff_1 * diff_3)
assert diff_1 * diff_3 == 1980

# Part 2
arrangements = 1
consecutive_ones = 0
for i in range(1, len(jolts)):
    diff = jolts[i] - jolts[i - 1]
    if diff == 1:
        consecutive_ones += 1
    else:
        # 3 3 (original)
        if consecutive_ones == 0:
            arrangements *= 1
        # 3 1 3 (original)
        elif consecutive_ones == 1:
            arrangements *= 1
        # 3 1 1 3 (original)
        # 3 - 2 3
        elif consecutive_ones == 2:
            arrangements *= 2
        # 3 1 1 1 3 (original)
        # 3 - 2 1 3
        # 3 1 - 2 3
        # 3 - - 3 3
        elif consecutive_ones == 3:
            arrangements *= 4
        # 3 1 1 1 1 3 (original)
        # 3 - 2 1 1 3
        # 3 1 - 2 1 3
        # 3 1 1 - 2 3
        # 3 - - 3 1 3
        # 3 - 2 - 2 3
        # 3 1 - - 3 3
        elif consecutive_ones == 4:
            arrangements *= 7
        else:
            raise Exception("Add factor for %s consecutive ones" % consecutive_ones)

        consecutive_ones = 0
print("Part 2:", arrangements)
assert arrangements == 4628074479616
