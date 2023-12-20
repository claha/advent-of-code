"""Advent Of Code #20."""
modules = {}
flipflops = {}
conjunctions = {}

for line in open("input"):
    source, _, *destinations = line.replace(",", "").split()
    source_type = ""
    if source[0] in "%&":
        source_type, source = source[0], source[1:]

    modules[source] = source_type, destinations

    for destination in destinations:
        if destination not in conjunctions:
            conjunctions[destination] = {}
        conjunctions[destination][source] = 0
        if destination == "rx":
            rx = source


def is_flipflop(module):
    """Is module a flipflop."""
    module_type, _ = modules[module]
    return module_type == "%"


def is_conjunction(module):
    """Is module a cunjunction."""
    module_type, _ = modules[module]
    return module_type == "&"


def update_rx(module, presses):
    """Update rx."""
    _, destinations = modules[module]
    if "rx" in destinations:
        for module, pulse in conjunctions[module].items():
            rx[module] = presses if pulse else rx[module]


rx = {source: 0 for source in conjunctions[rx]}
presses = 0
count = [0, 0]

while True:
    if presses == 1000:
        answer = count[0] * count[1]
        print("Part 1:", answer)
        assert answer == 938065580
    presses += 1

    if all(rx.values()):
        answer = 1
        for value in rx.values():
            answer *= value
        print("Part 2:", answer)
        assert answer == 250628960065793
        break

    queue = []

    def add_destinations_to_queue(module, pulse):
        """Add all destinations to the queue."""
        _, destinations = modules[module]
        for destination in destinations:
            queue.append((module, destination, pulse))

    module = "broadcaster"
    pulse = 0
    count[pulse] += 1
    add_destinations_to_queue(module, pulse)

    while queue:
        source, module, pulse = queue.pop(0)
        count[pulse] += 1

        if module not in modules:
            continue
        _, destinations = modules[module]

        if is_flipflop(module) and pulse == 0:
            if module not in flipflops:
                flipflops[module] = 0
            flipflops[module] = not flipflops[module]
            pulse = flipflops[module]
            add_destinations_to_queue(module, pulse)
        elif is_conjunction(module):
            conjunctions[module][source] = pulse
            pulse = int(not all(conjunctions[module].values()))
            add_destinations_to_queue(module, pulse)
            update_rx(module, presses)
