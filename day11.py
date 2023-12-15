import re

galaxy_map = []
galaxies = []


def print_map(in_map):
    for row in in_map:
        print(row)


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1

    return 0


def insert_column(in_map, col_index):
    new_col = col_index+1
    for row_index, row in enumerate(in_map):
        in_map[row_index] = row[0:col_index] + '*' + row[col_index:]
    return


def parse_galaxies(in_map, out_list):
    for row_index, row in enumerate(in_map):
        for col_index in range(0, len(in_map[0])):
            if in_map[row_index][col_index] == '#':
                out_list.append((row_index, col_index))


def calculate_distance(in_map, g1, g2):
    dr = sign(g2[0] - g1[0])
    dc = sign(g2[1] - g1[1])
    distance = 0

    if dc != 0:
        for col_index in range(g1[1] + dc, g2[1] + dc, dc):
            if in_map[g1[0]][col_index] == '.' or in_map[g1[0]][col_index] == '#':
                distance += 1
            elif in_map[g1[0]][col_index] == '*':
                distance += 9

    if dr != 0:
        for row_index in range(g1[0] + dr, g2[0] + dr, dr):
            if in_map[row_index][g2[1]] == '.' or in_map[row_index][g2[1]] == '#':
                distance += 1
            elif in_map[row_index][g2[1]] == '*':
                distance += 10


    return distance

with open("input11.txt") as my_file:

    # First read the file
    for line in my_file:
        galaxy_map.append(line.strip())

    # Add extra blank row every time there is a blank row
    blank_row = galaxy_map[0].replace('#','.')
    blank_row = blank_row. replace('.', '*')
    for row_index in range(len(galaxy_map)-1, -1, -1):
        if len(re.findall("#", galaxy_map[row_index]))== 0:
            galaxy_map.insert(row_index, blank_row)
            print(row_index, end =' ')

    # Add extra blank column every time there is a blank column
    print()
    for col_index in range(len(galaxy_map[0])-1, -1, -1):
        galaxy_found = False
        for row_index, row in enumerate(galaxy_map):
            if galaxy_map[row_index][col_index] == '#':
                galaxy_found = True
                break
        if not galaxy_found:
            insert_column(galaxy_map, col_index)
            print(col_index, end=' ')

    # Parse the map and read the galaxies
    parse_galaxies(galaxy_map, galaxies)

    # Part 1 calculate distances
    part1_distance = 0
    for g1_index, galaxy1 in enumerate(galaxies):
        for g2_index, galaxy2 in enumerate(galaxies[g1_index+1:], g1_index+1):
            part1_distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    print()
    print("Part 1:", part1_distance)

    # Part 2 calculate distances.
    # part2_distance = 0
    # count = 0
    # for g1_index, galaxy1 in enumerate(galaxies):
    #     for g2_index, galaxy2 in enumerate(galaxies[g1_index+1:], g1_index+1):
    #         count += 1
    #         part2_distance += calculate_distance(galaxy_map, galaxy1, galaxy2)
    #
    # print("Part 2:", part2_distance)

