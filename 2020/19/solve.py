"""Advent Of Code #19."""

with open("input") as f:
    data = f.read()

rules_data, messages = data.split("\n\n")
rules_data = rules_data.replace('"', "")

rules = {}
for rule in rules_data.splitlines():
    key, value = rule.split(": ")
    rules[key] = value


def create_exp(rule, rules):
    """Create expression."""
    exp = ""
    opened = False
    for sub_rule in rules[rule].split(" "):
        if sub_rule in rules:
            if not opened:
                exp += "("
                opened = True
            sub_exp = create_exp(sub_rule, rules)
            if len(sub_exp) == 1:
                exp += sub_exp
            else:
                exp += "(" + sub_exp + ")"
        else:
            if opened:
                exp += ")"
                opened = False
            exp += sub_rule
    if opened:
        exp += ")"
    return exp


def expand_exp(exp):
    """Expand expression."""
    eexp = {""}
    i = 0
    while i < len(exp):
        if exp[i] == "(":
            count = 0
            j = i + 1
            while j < len(exp):
                if exp[j] == "(":
                    count += 1
                elif exp[j] == ")":
                    if count == 0:
                        break
                    count -= 1
                j += 1
            sub_eexp = expand_exp(exp[i + 1 : j])
            i = j + 1
            new_eexp = set()
            if "" in eexp:
                eexp.remove("")
                for j in sub_eexp:
                    eexp.add(j)
            else:
                for j in eexp:
                    for k in sub_eexp:
                        new_eexp.add(j + k)
                eexp = new_eexp
        elif exp[i] == "|":
            eexp.add("")
            i += 1
        else:
            new_eexp = set()
            for j in eexp:
                new_eexp.add(j + exp[i])
            eexp = new_eexp
            i += 1

    return eexp


# Part 1
exp = create_exp("0", rules)
eexp = expand_exp(exp)
matches = 0
for message in messages.splitlines():
    if message in eexp:
        matches += 1
print("Part 1:", matches)
assert matches == 222

# Part 2
# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# =>
# 0: (42 42 ...) ... (42 42 ... 31 31)
exp0 = create_exp("0", rules)
eexp0 = expand_exp(exp0)
exp42 = create_exp("42", rules)
eexp42 = expand_exp(exp42)
exp31 = create_exp("31", rules)
eexp31 = expand_exp(exp31)
exp_len = None
for e in eexp31.union(eexp42):
    if exp_len is None:
        exp_len = len(e)
    assert len(e) == exp_len

matches = 0
for message in messages.splitlines():
    if message in eexp0:
        matches += 1
    else:
        if message[0:exp_len] not in eexp42:
            continue
        if message[-exp_len:] not in eexp31:
            continue
        count42 = 0
        count31 = 0
        found42after31 = False
        for i in range(exp_len, len(message) - exp_len, exp_len):
            if message[i : i + exp_len] in eexp42:
                if count31 > 0:
                    found42after31 = True
                count42 += 1
            if message[i : i + exp_len] in eexp31:
                count31 += 1
        if not found42after31 and count42 > count31:
            matches += 1

print("Part 2:", matches)
assert matches == 339
