"""Advent Of Code #06."""
times = [54, 81, 70, 88]
distances = [446, 1292, 1035, 1007]


# x is velocity/chargin time and (time - x) is how long the boat will travel
# (time - x) * x = distance
# x^2 - time * x + distance = 0
# x = -time/2 +/- sqrt((time/2)^2 - distance)
def solve(time, distance):
    """Solve equation."""
    return (
        (time / 2) - ((time / 2) ** 2 - distance) ** 0.5,
        (time / 2) + ((time / 2) ** 2 - distance) ** 0.5,
    )


# Part 1
count = 1
for time, distance in zip(times, distances):
    a, b = solve(time, distance)
    a = int(a) + 1
    if b == int(b):
        b = int(b) - 1
    else:
        b = int(b)
    count *= b + 1 - a
print("Part 1:", count)
assert count == 2065338


# Part 2
times = [54817088]
distances = [446129210351007]

count = 1
for time, distance in zip(times, distances):
    a, b = solve(time, distance)
    a = int(a) + 1
    if b == int(b):
        b = int(b) - 1
    else:
        b = int(b)
    count *= b + 1 - a
print("Part 2:", count)
assert count == 34934171
