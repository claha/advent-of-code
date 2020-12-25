"""Advent Of Code #25."""
with open("input") as f:
    data = f.read()
[card_public_key, door_public_key] = [int(key) for key in data.splitlines()]


# Part 1
def transform(number, subject_number):
    """Transform number."""
    return (number * subject_number) % 20201227


subject_number = 7
number = 1
loop = 1
while True:
    number = transform(number, subject_number)
    if number == card_public_key:
        public_key = door_public_key
        secret_loop_size = loop
        break
    elif number == door_public_key:
        public_key = card_public_key
        secret_loop_size = loop
        break
    loop += 1

subject_number = public_key
number = 1
for _ in range(secret_loop_size):
    number = transform(number, subject_number)
print("Part 1:", number)
assert number == 10187657
