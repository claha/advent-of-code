"""Advent Of Code #14."""

with open("input") as f:
    data = f.read()
program = data.splitlines()

# Part 1
mem = {}
for line in program:
    line = line.split(" = ")

    if line[0] == "mask":
        mask = line[1]
    else:
        address = int(line[0][4:-1])
        value = list("{:036b}".format(int(line[1])))

        mem[address] = value
        for i in range(len(mask)):
            if mask[i] == "1":
                mem[address][i] = "1"
            elif mask[i] == "0":
                mem[address][i] = "0"

sum = 0
for address in mem:
    sum += int("".join(mem[address]), 2)
print("Part 1:", sum)
# assert sum == 6317049172545

# Part 2
mem = {}
for line in program:
    line = line.split(" = ")

    if line[0] == "mask":
        mask = line[1]
    else:
        address = list("{:036b}".format(int(line[0][4:-1])))
        value = int(line[1])
        for i in range(len(mask)):
            if mask[i] != "0":
                address[i] = mask[i]

        addresses = [address]
        done = False
        while not done:
            for i in range(len(addresses)):
                for j in range(len(addresses[i])):
                    if addresses[i][j] == "X":
                        addresses.append(addresses[i][:])
                        addresses[i][j] = "0"
                        addresses[-1][j] = "1"
            done = True
            for address in addresses:
                if "X" in address:
                    done = False
                    break
        for address in addresses:
            mem[int("".join(address), 2)] = value

sum = 0
for address in mem:
    sum += mem[address]
print("Part 2:", sum)
assert sum == 3434009980379
