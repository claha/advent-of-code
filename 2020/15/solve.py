"""Advent Of Code #15."""
with open("input") as f:
    data = f.read().splitlines()
data = [int(d) for d in data]

# Part 1
mem = {}
for i in range(len(data) - 1):
    mem[data[i]] = i + 1

last = data[-1]
for i in range(len(mem) + 1, 2020):
    if last in mem:
        prev = mem[last]
        mem[last] = i
        last = i - prev
    else:
        mem[last] = i
        last = 0

print("Part 1:", last)
assert last == 1618

# Part 2
for i in range(2020, 30000000):
    if last in mem:
        prev = mem[last]
        mem[last] = i
        last = i - prev
    else:
        mem[last] = i
        last = 0

print("Part 2:", last)
assert last == 548531
