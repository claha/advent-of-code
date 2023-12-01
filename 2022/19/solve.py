"""Advent Of Code #19."""
import re
from collections import deque
from copy import deepcopy
from dataclasses import dataclass

with open("input") as f:
    data = [tuple(map(int, re.findall(r"\d+", line))) for line in f.readlines()]


class Resource:
    """Resource."""

    ORE = "ORE"
    CLAY = "CLAY"
    OBSIDIAN = "OBSIDIAN"
    GEODE = "GEODE"


@dataclass
class Robot:
    """Robot."""

    build: dict[Resource, int]
    produce: Resource


@dataclass
class State:
    """State."""

    resources: dict[Resource, int]
    robots: dict[Resource, int]
    allowed: dict[Resource, bool]
    minute: 0

    def run(self):
        """Run one minute."""
        for resource, produce in self.robots.items():
            self.resources[resource] += produce
        self.minute += 1


blueprints = []
for info in data:
    blueprints.append(
        [
            Robot({Resource.ORE: info[5], Resource.OBSIDIAN: info[6]}, Resource.GEODE),
            Robot({Resource.ORE: info[3], Resource.CLAY: info[4]}, Resource.OBSIDIAN),
            Robot({Resource.ORE: info[2]}, Resource.CLAY),
            Robot({Resource.ORE: info[1]}, Resource.ORE),
        ]
    )


def bfs(blueprint, state, minutes):
    """Breadth first search."""
    paths = []
    queue = deque([state])

    resource_max = {
        Resource.ORE: max(robot.build.get(Resource.ORE, 0) for robot in blueprint),
        Resource.CLAY: max(robot.build.get(Resource.CLAY, 0) for robot in blueprint),
        Resource.OBSIDIAN: max(
            robot.build.get(Resource.OBSIDIAN, 0) for robot in blueprint
        ),
        Resource.GEODE: 1000,
    }

    while queue:
        state = queue.popleft()

        if state.minute > minutes - 1:
            paths.append(state)
            continue

        for robot in blueprint:
            # Check if allowed to build this robot
            if not state.allowed[robot.produce]:
                continue

            # No need to produce more than we can consume per minute
            if state.robots[robot.produce] >= resource_max[robot.produce]:
                continue

            # Check if robot can be built
            build = True
            for resource, amount in robot.build.items():
                if state.resources[resource] < amount:
                    build = False
                    break
            if build:
                state_next = deepcopy(state)
                for resource, amount in robot.build.items():
                    state_next.resources[resource] -= amount
                state_next.run()
                state_next.robots[robot.produce] += 1
                state_next.allowed[Resource.ORE] = True
                state_next.allowed[Resource.CLAY] = True
                state_next.allowed[Resource.OBSIDIAN] = True
                state_next.allowed[Resource.GEODE] = True
                queue.append(state_next)

                state.allowed[robot.produce] = False

                # This works for this input but not sure it is correct
                if robot.produce == Resource.GEODE:
                    state_next.allowed[Resource.ORE] = False
                    state_next.allowed[Resource.CLAY] = False
                    break
                if robot.produce == Resource.OBSIDIAN:
                    state_next.allowed[Resource.ORE] = False
                    break

        if not any(allowed for allowed in state.allowed.values()):
            continue
        state.run()
        queue.append(state)

    return paths


# Part 1
quality = 0
for i, blueprint in enumerate(blueprints):
    resources = {
        Resource.ORE: 0,
        Resource.CLAY: 0,
        Resource.OBSIDIAN: 0,
        Resource.GEODE: 0,
    }
    robots = {
        Resource.ORE: 1,
        Resource.CLAY: 0,
        Resource.OBSIDIAN: 0,
        Resource.GEODE: 0,
    }
    allowed = {
        Resource.ORE: True,
        Resource.CLAY: True,
        Resource.OBSIDIAN: True,
        Resource.GEODE: True,
    }
    minute = 0

    state = State(resources, robots, allowed, minute)
    states = bfs(blueprint, state, 24)
    quality += (i + 1) * max(state.resources[Resource.GEODE] for state in states)

print("Part 1:", quality)
assert quality == 1349


# Part 2
quality = 1
for i, blueprint in enumerate(blueprints[:3]):
    resources = {
        Resource.ORE: 0,
        Resource.CLAY: 0,
        Resource.OBSIDIAN: 0,
        Resource.GEODE: 0,
    }
    robots = {
        Resource.ORE: 1,
        Resource.CLAY: 0,
        Resource.OBSIDIAN: 0,
        Resource.GEODE: 0,
    }
    allowed = {
        Resource.ORE: True,
        Resource.CLAY: True,
        Resource.OBSIDIAN: True,
        Resource.GEODE: True,
    }
    minute = 0

    state = State(resources, robots, allowed, minute)
    states = bfs(blueprint, state, 32)
    quality *= max(state.resources[Resource.GEODE] for state in states)

print("Part 2:", quality)
assert quality == 21840
