"""Advent Of Code."""

import aoc

garden = aoc.input_readlines()
R = len(garden)
C = len(garden[0])

visited = set()
regions = []
for r in range(R):
    for c in range(C):
        if (r, c) in visited:
            continue
        garden_type = garden[r][c]
        size = 0
        count = 0
        corners = 0
        neighbours = [(r, c)]

        while neighbours:
            cr, cc = neighbours.pop()
            if (cr, cc) in visited:
                continue
            visited.add((cr, cc))
            size += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = cr + dr
                nc = cc + dc
                if nr < 0 or nr >= R:
                    count += 1
                    continue
                if nc < 0 or nc >= C:
                    count += 1
                    continue
                if garden_type != garden[nr][nc]:
                    count += 1
                    continue
                if (nr, nc) not in visited:
                    neighbours.append((nr, nc))

            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nr = cr + dr
                nc = cc + dc
                if (nr < 0 or nr >= R or garden[nr][cc] != garden_type) and (
                    nc < 0 or nc >= C or garden[cr][nc] != garden_type
                ):
                    corners += 1

                if (
                    0 <= nr < R
                    and garden[nr][cc] == garden_type
                    and 0 <= nc < C
                    and garden[cr][nc] == garden_type
                    and garden[nr][nc] != garden_type
                ):
                    corners += 1

        regions.append((size, count, corners))

# Part 1
aoc.check_part1(sum(size * count for size, count, _ in regions), 1304764)

# Part 2
aoc.check_part2(sum(size * corners for size, _, corners in regions), 811148)
