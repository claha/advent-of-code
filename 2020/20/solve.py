"""Advent Of Code #20."""
import math

with open("input") as f:
    data = f.read().strip().split("\n\n")


class Tile:
    """Class representing a tile."""

    def __init__(self, data):
        """Initialize tile."""
        lines = data.splitlines()
        self._id = int(lines[0][5:-1])
        self._height = len(lines[1:])
        self._width = len(lines[1])
        self._pixels = []
        for line in lines[1:]:
            self._pixels.extend(line)

    def flip(self):
        """Flip tile."""
        assert self._height == self._width
        N = self._height
        for r in range(N // 2):
            for c in range(N):
                self._pixels[r * N + c], self._pixels[(N - 1 - r) * N + c] = (
                    self._pixels[(N - 1 - r) * N + c],
                    self._pixels[r * N + c],
                )

    def rotate(self):
        """Rotate tile."""
        assert self._height == self._width
        N = self._height
        for c in range(N // 2):
            for r in range(c, N - c - 1):
                temp = self._pixels[c * N + r]
                self._pixels[c * N + r] = self._pixels[r * N + N - 1 - c]
                self._pixels[r * N + N - 1 - c] = self._pixels[
                    (N - 1 - c) * N + N - 1 - r
                ]
                self._pixels[(N - 1 - c) * N + N - 1 - r] = self._pixels[
                    (N - 1 - r) * N + c
                ]
                self._pixels[(N - 1 - r) * N + c] = temp

    @property
    def size(self):
        """Get tile size."""
        assert self._height == self._width
        return self._height

    @property
    def top(self):
        """Get top edge."""
        value = ""
        r = 0
        for c in range(self._width):
            value += self._pixels[r * self._width + c]
        return value

    @property
    def right(self):
        """Get right edge."""
        value = ""
        c = self._width - 1
        for r in range(self._height):
            value += self._pixels[r * self._width + c]
        return value

    @property
    def bottom(self):
        """Get bottom edge."""
        value = ""
        r = self._height - 1
        for c in range(self._width):
            value += self._pixels[r * self._width + c]
        return value

    @property
    def left(self):
        """Get left edge."""
        value = ""
        c = 0
        for r in range(self._height):
            value += self._pixels[r * self._width + c]
        return value

    @property
    def id(self):
        """Get id."""
        return self._id

    def __str__(self):
        """Represent tile as a string."""
        s = ""
        for r in range(self._height):
            for c in range(self._width):
                s += self._pixels[r * self._width + c]
            s += "\n"
        s += "\n"
        return s

    def fill_image(self, image, image_width, start_row, start_col):
        """Fill image with tile, without border."""
        for r in range(1, self._height - 1):
            for c in range(1, self._width - 1):
                image[
                    (start_row + r - 1) * image_width + start_col + c - 1
                ] = self._pixels[r * self._width + c]


tiles = []
for i in range(len(data)):
    tiles.append(Tile(data[i]))

# Part 1
matches = {}
for i in range(len(tiles)):
    matches[tiles[i].id] = []

    for j in range(len(tiles)):
        if i == j:
            continue

        for _ in range(4):
            if tiles[i].bottom == tiles[j].top:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].top == tiles[j].bottom:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].right == tiles[j].left:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].left == tiles[j].right:
                matches[tiles[i].id].append(tiles[j].id)
            tiles[j].rotate()

        tiles[j].flip()
        for _ in range(4):
            if tiles[i].bottom == tiles[j].top:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].top == tiles[j].bottom:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].right == tiles[j].left:
                matches[tiles[i].id].append(tiles[j].id)
            if tiles[i].left == tiles[j].right:
                matches[tiles[i].id].append(tiles[j].id)
            tiles[j].rotate()
        tiles[j].flip()

corners = []
for tile_id in matches:
    if len(matches[tile_id]) <= 2:
        corners.append(tile_id)
answer = 1
for corner in corners:
    answer *= corner
print("Part 1:", answer)
assert answer == 17250897231301

# Part 2
monster = list(
    """\
                  # \
#    ##    ##    ###\
 #  #  #  #  #  #   \
"""
)
monster_height = 3
monster_width = 20


def count_monsters(image):
    """Count monsters in image."""
    count = 0
    for r in range(N - monster_height):
        for c in range(N - monster_width):
            is_monster = True
            for mr in range(monster_height):
                for mc in range(monster_width):
                    if monster[mr * monster_width + mc] == "#":
                        if image[(r + mr) * N + (c + mc)] != "#":
                            is_monster = False
            if is_monster:
                count += 1
    return count


def find_tile(tiles, id):
    """Find tile using id."""
    for tile in tiles:
        if tile.id == id:
            return tile


# Create empty image
N = int(math.sqrt(len(tiles))) * (tiles[0].size - 2)  # removing borders
image = [" "] * (N * N)

# Start with a corner
tile = find_tile(tiles, corners[0])
for r in range(0, N, tile.size - 2):
    # Save for next row
    above = tile

    for c in range(0, N, tile.size - 2):
        tile.fill_image(image, N, r, c)

        # Find tile that matches
        match = None
        for tile_id in matches[tile.id]:
            tile_candidate = find_tile(tiles, tile_id)
            for _ in range(4):
                if tile_candidate.left == tile.right:
                    match = tile_candidate
                    break
                tile_candidate.rotate()

            if match is not None:
                break

            tile_candidate.flip()
            for _ in range(4):
                if tile_candidate.left == tile.right:
                    match = tile_candidate
                    break
                tile_candidate.rotate()

            if match is not None:
                break
            tile_candidate.flip()

        tile = match

    # Find tile that matches tile on start of row above
    tile = above
    match = None
    for tile_id in matches[tile.id]:
        tile_candidate = find_tile(tiles, tile_id)
        for _ in range(4):
            if tile_candidate.top == tile.bottom:
                match = tile_candidate
                break
            tile_candidate.rotate()

        if match is not None:
            break

        tile_candidate.flip()
        for _ in range(4):
            if tile_candidate.top == tile.bottom:
                match = tile_candidate
                break
            tile_candidate.rotate()

        if match is not None:
            break
        tile_candidate.flip()

    tile = match

# Find monsters
num_monsters = 0
for _ in range(4):
    for c in range(N // 2):
        for r in range(c, N - c - 1):
            temp = image[c * N + r]
            image[c * N + r] = image[r * N + N - 1 - c]
            image[r * N + N - 1 - c] = image[(N - 1 - c) * N + N - 1 - r]
            image[(N - 1 - c) * N + N - 1 - r] = image[(N - 1 - r) * N + c]
            image[(N - 1 - r) * N + c] = temp
    num_monsters = count_monsters(image)
    # Only monsters in one configuration
    if num_monsters > 0:
        break

if num_monsters == 0:
    for r in range(N // 2):
        for c in range(N):
            image[r * N + c], image[(N - 1 - r) * N + c] = (
                image[(N - 1 - r) * N + c],
                image[r * N + c],
            )
    for _ in range(4):
        for c in range(N // 2):
            for r in range(c, N - c - 1):
                temp = image[c * N + r]
                image[c * N + r] = image[r * N + N - 1 - c]
                image[r * N + N - 1 - c] = image[(N - 1 - c) * N + N - 1 - r]
                image[(N - 1 - c) * N + N - 1 - r] = image[(N - 1 - r) * N + c]
                image[(N - 1 - r) * N + c] = temp
        num_monsters = count_monsters(image)
        # Only monsters in one configuration
        if num_monsters > 0:
            break

roughness = image.count("#") - num_monsters * monster.count("#")
print("Part 2:", roughness)
assert roughness == 1576
