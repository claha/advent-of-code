"""Advent Of Code #12."""
with open("input") as f:
    data = [line.strip().split(" ") for line in f.readlines()]
data = [[list(d[0]), list(map(int, d[1].split(",")))] for d in data]

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"
solution = {}


def get_current_condition(record):
    """Get current condition."""
    record = "".join(record).split(OPERATIONAL)
    condition = []
    unknown = []
    for spring in record:
        d = spring.count(DAMAGED)
        u = spring.count(UNKNOWN)
        if d or u:
            condition.append(d)
            unknown.append(u)
    return condition, unknown


def cleanup_record_front(record, spring=OPERATIONAL):
    """Cleanup record front."""
    while record and record[0] == spring:
        record = record[1:]
    return record


def cleanup_record_back(record):
    """Cleanup record back."""
    while record and record[-1] == OPERATIONAL:
        record = record[:-1]
    return record


def cleanup_record_middle(record):
    """Cleanup record middle."""
    for i in range(
        len(record) - 1,
        0,
        -1,
    ):
        if record[i] == OPERATIONAL and record[i - 1] == OPERATIONAL:
            del record[i]
    return record


def solve(record, condition):
    """Solve for record with given condition."""
    record = cleanup_record_front(record)
    record = cleanup_record_back(record)

    curr_condition, curr_unknown = get_current_condition(record)

    while curr_unknown[0] == 0:
        record = cleanup_record_front(record, spring=DAMAGED)
        condition = condition[1:]
        curr_unknown = curr_unknown[1:]
        record = cleanup_record_front(record)

    # Check if solution exists
    key = "".join(record) + ",".join(map(str, condition))
    if key in solution:
        return solution[key]

    unknown = [i for i in range(len(record)) if record[i] == UNKNOWN]
    count = 0
    for state in [OPERATIONAL, DAMAGED]:
        record[unknown[0]] = state
        curr_condition, curr_unknown = get_current_condition(record)
        sum_curr = sum(curr_condition)
        sum_cond = sum(condition)
        sum_unkn = sum(curr_unknown)
        if sum_curr > sum_cond or sum_curr + sum_unkn < sum_cond:
            continue

        if any(
            len(curr_condition) >= n
            and sum(curr_unknown[: n + 1]) == 0
            and curr_condition[n] != condition[n]
            for n in range(len(condition))
        ):
            continue

        if len(unknown) == 1:
            count += int(curr_condition == condition)
        else:
            count += solve(record[:], condition)
            solution[key] = count
    return count


count = 0
for record, condition in data:
    record = cleanup_record_front(record)
    record = cleanup_record_back(record)

    # Cleanup multiple OPERATIONAL in middle
    for i in range(
        len(record) - 1,
        0,
        -1,
    ):
        if record[i] == OPERATIONAL and record[i - 1] == OPERATIONAL:
            del record[i]

    count += solve(record[:], condition)


print("Part 1:", count)
assert count == 7718

# Part 2
for i in range(len(data)):
    data[i][0] = (
        data[i][0]
        + ["?"]
        + data[i][0]
        + ["?"]
        + data[i][0]
        + ["?"]
        + data[i][0]
        + ["?"]
        + data[i][0]
    )
    data[i][1] *= 5

count = 0
for record, condition in data:
    record = cleanup_record_front(record)
    record = cleanup_record_back(record)
    record = cleanup_record_middle(record)
    count += solve(record, condition)

print("Part 2:", count)
assert count == 128741994134728
