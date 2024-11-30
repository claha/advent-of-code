"""Advent Of Code #23."""

import heapq as heap

with open("input") as f:
    data = f.read()

occupied = {
    "l": data[31],
    "p": data[45],
    "m": data[33],
    "q": data[47],
    "n": data[35],
    "r": data[49],
    "o": data[37],
    "s": data[51],
}

# #############
# #abcdefghijk#
# ###l#m#n#o###
# ###p#q#r#s###
# #############
graph = {
    "a": ["b"],
    "b": ["a", "c"],
    "c": ["b", "d", "l"],
    "d": ["c", "e"],
    "e": ["d", "f", "m"],
    "f": ["e", "g"],
    "g": ["f", "h", "n"],
    "h": ["g", "i"],
    "i": ["h", "j", "o"],
    "j": ["i", "k"],
    "k": ["j"],
    "l": ["c", "p"],
    "m": ["e", "q"],
    "n": ["g", "r"],
    "o": ["i", "s"],
    "p": ["l"],
    "q": ["m"],
    "r": ["n"],
    "s": ["o"],
}

rooms = {
    "l": "A",
    "p": "A",
    "m": "B",
    "q": "B",
    "n": "C",
    "r": "C",
    "o": "D",
    "s": "D",
}

nostop = {"c", "e", "g", "i"}

hallway = {"a", "b", "d", "f", "h", "j", "k"}


def bfs(graph, node, nostop, hallway):
    """Get a list of all possible paths from node."""
    paths = []
    queue = []
    queue.append([node])

    while queue:
        path = queue.pop(0)
        node = path[-1]
        for neighbour in graph[node]:
            if neighbour in path:
                continue
            queue.append(path + [neighbour])
            if neighbour in nostop:
                continue
            if path[0] in hallway and neighbour in hallway:
                continue
            paths.append(path[1:] + [neighbour])

    return paths


# Calculate paths
paths = {}
for node in graph.keys():
    paths[node] = bfs(graph, node, nostop, hallway)


def is_path_occupied(path, occupied):
    """Is path occupied."""
    for node in occupied:
        if node in path:
            return True
    return False


def is_correct_room(amphipod, path, rooms, occupied):
    """Is amphipod in correct room."""
    invalid_node = []
    valid_node = []
    for node in rooms:
        if rooms[node] != amphipod:
            invalid_node.append(node)
        else:
            valid_node.append(node)

    for node in invalid_node:
        if node == path[-1]:
            return False

    for i in range(len(valid_node)):
        if valid_node[i] == path[-1]:
            for j in range(len(valid_node)):
                if i == j:
                    continue
                if valid_node[j] in occupied:
                    if occupied[valid_node[j]] != amphipod:
                        return False
                else:
                    # Empty below, do not stop here
                    if valid_node[j] > valid_node[i]:
                        return False
    return True


def get_possible_paths(node, paths, occupied, rooms, hallway):
    """Get possible paths."""
    amphipod = occupied[node]
    possible_paths = []
    if node in rooms and is_correct_room(amphipod, [node], rooms, occupied):
        return possible_paths

    for path in paths[node]:
        if is_path_occupied(path, occupied):
            continue
        if path[-1] in rooms and not is_correct_room(amphipod, path, rooms, occupied):
            continue
        possible_paths.append(path)

    return possible_paths


class State:
    """Represent a state."""

    def __init__(self, energy, occupied):
        """Create a state."""
        self.occupied = occupied
        self.energy = energy

    def __gt__(self, other):
        """Implement greater than."""
        return self.energy > other.energy

    def __str__(self):
        """Get state as a string."""
        s = ""
        for x in "abcdefghijklmnopqrstuvwxyz|":
            if x in self.occupied:
                s += x
                s += self.occupied[x]
        return s


def dijkstra(paths, occupied, rooms, hallway):
    """Run dijkstra to find minimum energy."""
    queue = []
    heap.heappush(queue, State(0, occupied))

    lowest_energies = {}
    lowest_energies[str(State(0, occupied))] = 0

    while queue:
        state = heap.heappop(queue)
        energy = lowest_energies[str(state)]
        occupied = state.occupied

        for node in occupied:
            possible_paths = get_possible_paths(node, paths, occupied, rooms, hallway)
            possible_paths_room = []
            for path in possible_paths:
                if path[-1] in rooms:
                    possible_paths_room.append(path)
            if len(possible_paths_room) > 0:
                possible_paths = possible_paths_room

            for path in possible_paths:
                amphipod = occupied[node]
                new_node = path[-1]
                new_occupied = occupied.copy()
                del new_occupied[node]
                new_occupied[new_node] = amphipod

                lowest_energy = lowest_energies.get(
                    str(State(0, new_occupied)), 1000000
                )

                if amphipod == "A":
                    new_energy = energy + 1 * len(path)
                elif amphipod == "B":
                    new_energy = energy + 10 * len(path)
                elif amphipod == "C":
                    new_energy = energy + 100 * len(path)
                elif amphipod == "D":
                    new_energy = energy + 1000 * len(path)

                if new_energy < lowest_energy:
                    new_state = State(new_energy, new_occupied)
                    lowest_energies[str(new_state)] = new_energy
                    heap.heappush(queue, new_state)

    return lowest_energies[str(State(0, rooms))]


# Part 1
min_energy = dijkstra(paths, occupied, rooms, hallway)
print("Part 1:", min_energy)
assert min_energy == 14346


# Part 2
# #############
# #abcdefghijk#
# ###l#m#n#o###
# ###p#q#r#s###
# ###t#u#v#w###
# ###x#y#z#|###
# #############

# Update graph
graph["p"] = ["l", "t"]
graph["q"] = ["m", "u"]
graph["r"] = ["n", "v"]
graph["s"] = ["o", "w"]
graph["t"] = ["p", "x"]
graph["u"] = ["q", "y"]
graph["v"] = ["r", "z"]
graph["w"] = ["s", "|"]
graph["x"] = ["t"]
graph["y"] = ["u"]
graph["z"] = ["v"]
graph["|"] = ["w"]

# Calculate new paths
paths = {}
for node in graph.keys():
    paths[node] = bfs(graph, node, nostop, hallway)

# Update rooms
rooms["t"] = "A"
rooms["x"] = "A"
rooms["u"] = "B"
rooms["y"] = "B"
rooms["v"] = "C"
rooms["z"] = "C"
rooms["w"] = "D"
rooms["|"] = "D"

# Update occupied
occupied["x"] = occupied["p"]
occupied["p"] = "D"
occupied["t"] = "D"

occupied["y"] = occupied["q"]
occupied["q"] = "C"
occupied["u"] = "B"

occupied["z"] = occupied["r"]
occupied["r"] = "B"
occupied["v"] = "A"

occupied["|"] = occupied["s"]
occupied["s"] = "A"
occupied["w"] = "C"

min_energy = dijkstra(paths, occupied, rooms, hallway)
print("Part 2:", min_energy)
assert min_energy == 48984
