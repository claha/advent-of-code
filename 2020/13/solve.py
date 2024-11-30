"""Advent Of Code #13."""

with open("input") as f:
    data = f.read().splitlines()
earliest_departure_timestamp = int(data[0])
buses = data[1].split(",")
buses = [int(bus) if bus != "x" else bus for bus in buses]

# Part 1
earliest_timestamp = 100000000
earliest_bus = None
for bus in buses:
    if bus == "x":
        continue
    timestamp = (1 + (earliest_departure_timestamp) // bus) * bus
    if timestamp - earliest_departure_timestamp < earliest_timestamp:
        earliest_timestamp = timestamp - earliest_departure_timestamp
        earliest_bus = bus

print("Part 1:", earliest_timestamp * earliest_bus)
assert earliest_timestamp * earliest_bus == 370

# Part 2
earliest_timestamp = None
t = 0
while True:
    found = True
    add = 1
    for i, bus in enumerate(buses):
        if i == 0 or bus == "x":
            continue
        if (buses[0] * t + i) % buses[i] == 0:
            add *= buses[i]
        else:
            found = False
    if found:
        earliest_timestamp = buses[0] * t
        break
    print(add)
    t += add

print("Part 2:", earliest_timestamp)
assert earliest_timestamp == 894954360381385
