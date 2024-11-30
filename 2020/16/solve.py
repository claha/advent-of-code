"""Advent Of Code #16."""

with open("input") as f:
    data = f.read().splitlines()


class Field:
    """Class representing a field."""

    def __init__(self, data):
        """Initialize field."""
        self.name = data.split(":")[0]
        ranges = data.split(": ")[1]
        self._min1 = int(ranges.split(" or ")[0].split("-")[0])
        self._max1 = int(ranges.split(" or ")[0].split("-")[1])
        self._min2 = int(ranges.split(" or ")[1].split("-")[0])
        self._max2 = int(ranges.split(" or ")[1].split("-")[1])

    def __contains__(self, num):
        """Check if num is inside field."""
        return self._min1 <= num <= self._max1 or self._min2 <= num <= self._max2


fields = []
my_ticket = None
tickets = []
i = 0
while i < len(data) and data[i]:
    fields.append(Field(data[i]))
    i += 1
i += 1
while i < len(data) and data[i]:
    if "your ticket" not in data[i]:
        my_ticket = [int(d) for d in data[i].split(",")]
    i += 1
i += 1
while i < len(data) and data[i]:
    if "nearby tickets" not in data[i]:
        ticket = [int(d) for d in data[i].split(",")]
        tickets.append(ticket)
    i += 1


def is_valid(ticket, fields):
    """Check if ticket is valid."""
    for num in ticket:
        valid = False
        for field in fields:
            if num in field:
                valid = True
                break
        if not valid:
            return False, num
    return True, 0


# Part 1
error = 0
for ticket in tickets:
    _, num = is_valid(ticket, fields)
    error += num
print("Part 1:", error)
assert error == 23009

# Part 2
valid_tickets = []
for ticket in tickets:
    ok, _ = is_valid(ticket, fields)
    if ok:
        valid_tickets.append(ticket)

candidates = {}
for field in fields:
    candidates[field.name] = []
    for i in range(len(valid_tickets[0])):
        candidate = True
        for ticket in valid_tickets:
            if ticket[i] not in field:
                candidate = False
                break
        if candidate:
            candidates[field.name].append(i)

removed = []
done = False
while not done:
    for candidate in candidates:
        if len(candidates[candidate]) == 1:
            if candidates[candidate][0] not in removed:
                pos = candidates[candidate][0]
                removed.append(pos)
                break

    for candidate in candidates:
        if len(candidates[candidate]) > 1:
            candidates[candidate].remove(pos)

    done = True
    for candidate in candidates:
        if len(candidates[candidate]) > 1:
            done = False
            break

value = 1
for candidate in candidates:
    if candidate.startswith("departure"):
        value *= my_ticket[candidates[candidate][0]]

print("Part 2:", value)
assert value == 10458887314153
