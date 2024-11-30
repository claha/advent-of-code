"""Advent Of Code #20."""

with open("input") as f:
    data = [int(line) for line in f.readlines()]

KEY = 811589153


def cycle(nums, times):
    """Cycle the numbers in order."""
    order = list(range(len(data)))
    for i in order * times:
        j = order.index(i)
        order.pop(j)
        order.insert((j + nums[i]) % len(order), i)
    i = order.index(nums.index(0))
    return sum(nums[order[(i + offset) % len(nums)]] for offset in [1000, 2000, 3000])


# Part 1
groove = cycle([num for num in data], 1)
print("Part 1:", groove)
assert groove == 11123


# Part 2
groove = cycle([num * KEY for num in data], 10)
print("Part 2:", groove)
assert groove == 4248669215955
