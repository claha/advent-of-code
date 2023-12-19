"""Advent Of Code #05."""
with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

tables = {}
for line in lines:
    if line.startswith("seeds: "):
        seeds = list(map(int, line.split(": ")[1].split(" ")))
    elif "map" in line:
        key = line.split(" ")[0]
        tables[key] = []
    else:
        tables[key].append(list(map(int, line.split(" "))))


def convert(x, tables):
    """Convert from one type to another."""
    for dst, src, size in tables:
        if src <= x < src + size:
            return dst + (x - src)
    return x


def seed_to_location(x):
    """Convert seed to location."""
    for table in [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]:
        x = convert(x, tables[table])
    return x


lowest = 1000000000
for seed in seeds:
    location = seed_to_location(seed)
    lowest = min(lowest, location)
print("Part 1:", lowest)
assert lowest == 484023871

lowest = 1000000000
for i in range(0, len(seeds), 2):
    a = seeds[i]
    b = seeds[i] + seeds[i + 1] - 1
    while a < seeds[i] + seeds[i + 1]:
        loc_a = seed_to_location(a)
        loc_b = seed_to_location(b)
        diff = b - a
        loc_diff = abs(loc_a - loc_b)
        if diff == 1 or diff == loc_diff:
            lowest = min(lowest, min(loc_a, loc_b))
            a = b + 1
            b = seeds[i] + seeds[i + 1] - 1
        else:
            b = b - (b - a) // 2

print("Part 2:", lowest)
assert lowest == 46294175
