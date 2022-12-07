"""Advent Of Code #07."""
with open("input") as f:
    data = f.read().strip().split("\n")

size = {}
cwd = []

# Part 1
i = 0
while i < len(data):
    line = data[i].strip()
    if line.startswith("$"):
        cmd = line[2:]
        if cmd.startswith("cd"):
            arg = cmd[3:]
            if arg == "..":
                cwd.pop()
            elif arg == "/":
                cwd = ["/"]
            else:
                cwd.append(arg)
            i += 1
            if "/".join(cwd) not in size:
                size["/".join(cwd)] = 0
        elif cmd.startswith("ls"):
            while True:
                i += 1
                if i >= len(data) or data[i].startswith("$"):
                    break
                if not data[i].startswith("dir"):
                    s = int(data[i].split(" ")[0])
                    for j in range(1, len(cwd) + 1):
                        size["/".join(cwd[:j])] += s

total = sum([value for value in size.values() if value < 100000])
print("Part 1:", total)
assert total == 1582412


# Part 2
total = 70000000
need = 30000000
free = total - size["/"]
minimum = total
for value in size.values():
    if value >= need - free:
        minimum = min(minimum, value)
print("Part 2:", minimum)
assert minimum == 3696336
