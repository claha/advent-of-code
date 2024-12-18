"""Advent Of Code."""

import aoc

towel_patterns = []
designs = []
for line in aoc.input_readlines():
    if not towel_patterns:
        towel_patterns = line.strip().split(", ")
    elif line.strip():
        designs.append(line.strip())


# Part 1
def count_possible_designs(towel_patterns: list[str], designs: list[str]) -> int:
    """Count possible designs."""

    def can_construct(design: str) -> bool:
        """Check if possible to create pattern."""
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for pattern in towel_patterns:
                np = len(pattern)
                if i >= np and dp[i - np] and design[i - np : i] == pattern:
                    dp[i] = True
                    break
        return dp[-1]

    possible_count = 0
    for design in designs:
        if can_construct(design):
            possible_count += 1

    return possible_count


count = count_possible_designs(towel_patterns, designs)
aoc.check_part1(count, 251)


# Part 2
def count_total_arrangements(towel_patterns: list[str], designs: list[str]) -> int:
    """Count total arragements."""

    def count_ways(design: str) -> int:
        """Count ways to create designs."""
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for pattern in towel_patterns:
                np = len(pattern)
                if i >= np and design[i - np : i] == pattern:
                    dp[i] += dp[i - np]
        return dp[-1]

    total_ways = 0
    for design in designs:
        total_ways += count_ways(design)

    return total_ways


count = count_total_arrangements(towel_patterns, designs)
aoc.check_part2(count, 616957151871345)
