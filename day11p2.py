import re

galaxy_map = []
galaxies = []
blank_rows = []
blank_columns = []

def print_map(in_map):
    for row in in_map:
        print(row)


def parse_galaxies(in_map, out_list):
    for row_index, row in enumerate(in_map):
        for col_index in range(0, len(in_map[0])):
            if in_map[row_index][col_index] == '#':
                out_list.append((row_index, col_index))


def row_expansion(g1, g2, expansion_factor):
    expansion = 0
    if g1[0] != g2[0]:
        for row in blank_rows:
            if g1[0] < row < g2[0] or g2[0] < row < g1[0]:
                expansion += expansion_factor
    return expansion


def col_expansion(g1, g2, expansion_factor):
    expansion = 0
    if g1[1] != g2[1]:
        for col in blank_columns:
            if g1[1] < col < g2[1] or g2[1] < col < g1[1]:
                expansion += expansion_factor
    return expansion


with open("input11.txt") as my_file:

    # First read the file
    for line in my_file:
        galaxy_map.append(line.strip())

    # Find the blank rows
    blank_rows = {i for i, row in enumerate(galaxy_map) if all([char == '.' for char in row])}

    # Find the blank columns
    blank_columns = {i for i in range(len(galaxy_map[0])) if all(row[i] == '.' for row in galaxy_map)}

    # Parse the map and read the galaxies
    parse_galaxies(galaxy_map, galaxies)

    print(blank_rows)
    print(blank_columns)

    # Part 1 calculate distances
    part1_distance = 0
    for g1_index, galaxy1 in enumerate(galaxies):
        for g2_index, galaxy2 in enumerate(galaxies[g1_index+1:], g1_index+1):
            part1_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
            part1_distance += row_expansion(galaxy1, galaxy2, 1)
            part1_distance += col_expansion(galaxy1, galaxy2, 1)

    print("Part 1:", part1_distance)

    # Part 2 calculate distances.
    part2_distance = 0
    for g1_index, galaxy1 in enumerate(galaxies):
        for g2_index, galaxy2 in enumerate(galaxies[g1_index + 1:], g1_index + 1):
            part2_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
            part2_distance += row_expansion(galaxy1, galaxy2, 999999)
            part2_distance += col_expansion(galaxy1, galaxy2, 999999)

    print("Part 2:", part2_distance)