"""Advent Of Code #20."""
with open("input") as f:
    data = [d for d in f.read().split()]

enhancement = data[0].replace(".", "0").replace("#", "1")
image = []
for row in range(1, len(data)):
    image.append(data[row].replace(".", "0").replace("#", "1"))


def enhance_image(image, enhancement, N, infinite):
    """Enhance image."""
    # Add two rows and columns since corners and borders will
    # have an effect on the enhanced image.
    extra = 2
    for _ in range(extra):
        image.insert(0, infinite * N)
        image.append(infinite * N)
    N += 2 * extra
    for row in range(N):
        image[row] = infinite * extra + image[row] + infinite * extra

    enhanced_image = []
    for row in range(1, N - 1):
        enhanced_row = ""
        for col in range(1, N - 1):
            value = ""
            value += image[row - 1][col - 1 : col + 2]
            value += image[row + 0][col - 1 : col + 2]
            value += image[row + 1][col - 1 : col + 2]
            value = int(value, 2)
            enhanced_row += enhancement[value]
        enhanced_image.append(enhanced_row)
    return enhanced_image


# Before the first enhancement the rest of the infinite image is not lit but
# this can change depending on the enhancement algorithm, namely the value of
# enhancement[0] and enhancement[511] (0b000000000 and 0b111111111).
infinite = "0"

# Part 1
for _ in range(2):
    image = enhance_image(image, enhancement, len(image), infinite)
    infinite = enhancement[-1] if infinite == "1" else enhancement[0]
lit = sum(row.count("1") for row in image)
print("Part 1:", lit)
assert lit == 5268


# Part 2
for _ in range(50 - 2):
    image = enhance_image(image, enhancement, len(image), infinite)
    infinite = enhancement[-1] if infinite == "1" else enhancement[0]
lit = sum(row.count("1") for row in image)
print("Part 2:", lit)
assert lit == 16875
