"""Advent Of Code #22."""

import re
from dataclasses import dataclass, field
from typing import Any

with open("input") as f:
    data = [line.strip() for line in f.readlines()]

instructions = []
for line in data:
    instructions.append(
        (line.split(" ")[0], tuple(map(int, re.findall(r"-?\d+", line))))
    )


@dataclass
class Cuboid:
    """Cuboid."""

    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int
    on: bool
    removed: list[Any] = field(default_factory=list)

    def intersection(self, cuboid):
        """Calculate intersection as a cuboid."""
        if self.x1 < cuboid.x0 or self.y1 < cuboid.y0 or self.z1 < cuboid.z0:
            return None

        if self.x0 > cuboid.x1 or self.y0 > cuboid.y1 or self.z0 > cuboid.z1:
            return None

        return Cuboid(
            max(self.x0, cuboid.x0),
            min(self.x1, cuboid.x1),
            max(self.y0, cuboid.y0),
            min(self.y1, cuboid.y1),
            max(self.z0, cuboid.z0),
            min(self.z1, cuboid.z1),
            self.on,
        )

    def remove(self, cuboid):
        """Recursievly remove a cuboid."""
        cuboid = self.intersection(cuboid)
        if not cuboid:
            return
        for i in range(len(self.removed)):
            self.removed[i].remove(cuboid)
        self.removed.append(cuboid)

    @property
    def volume(self):
        """Get volume."""
        v = (self.x1 + 1 - self.x0) * (self.y1 + 1 - self.y0) * (self.z1 + 1 - self.z0)
        return v - sum(self.removed[i].volume for i in range(len(self.removed)))


# Part 1
cuboids = []
for instruction, (x0, x1, y0, y1, z0, z1) in instructions:
    if x0 < -50 and x1 < -50:
        continue
    if x0 > 50 and x1 > 50:
        continue
    if y0 < -50 and y1 < -50:
        continue
    if y0 > 50 and y1 > 50:
        continue
    if z0 < -50 and z1 < -50:
        continue
    if z0 > 50 and z1 > 50:
        continue
    cuboids.append(Cuboid(x0, x1, y0, y1, z0, z1, instruction == "on"))

volumes = []
for i in range(len(cuboids)):
    for j in range(len(volumes)):
        volumes[j].remove(cuboids[i])
    if cuboids[i].on:
        volumes.append(cuboids[i])

on = sum(cuboid.volume for cuboid in volumes)
print("Part 1:", on)
assert on == 583641


# Part 2
cuboids = []
for instruction, (x0, x1, y0, y1, z0, z1) in instructions:
    cuboids.append(Cuboid(x0, x1, y0, y1, z0, z1, instruction == "on"))

volumes = []
for i in range(len(cuboids)):
    for j in range(len(volumes)):
        volumes[j].remove(cuboids[i])
    if cuboids[i].on:
        volumes.append(cuboids[i])

on = sum(cuboid.volume for cuboid in volumes)
print("Part 2:", on)
assert on == 1182153534186233
