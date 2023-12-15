from enum import Enum
import sys
import re

sys.setrecursionlimit(100000)

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

landscape = []
empty_landscape = []

def next_step(direction, row_index, col_index, steps):
    steps += 1
    print(landscape[row_index][col_index], end='')
    empty_landscape[row_index] = \
        empty_landscape[row_index][0:col_index-1] + \
        landscape[row_index][col_index] + \
        empty_landscape[row_index][col_index:]

    # Direction is the direction you are heading not the direction you have came from.
    if direction == Direction.NORTH:
        row_index -= 1
    elif direction == Direction.WEST:
        col_index -=1
    elif direction == Direction.SOUTH:
        row_index += 1
    else:
        col_index += 1

    # if we're back at S then we've finished the loop
    if landscape[row_index][col_index] == 'S':
        return steps

    # Not back at S, so need to go again
    current_pipe = landscape[row_index][col_index]
    if current_pipe == '|' or current_pipe == '-':
        steps = next_step(direction, row_index, col_index, steps)
    elif current_pipe == 'L':
        if direction == Direction.SOUTH:
            steps = next_step(Direction.EAST, row_index, col_index, steps)
        else:
            steps = next_step(Direction.NORTH, row_index, col_index, steps)
    elif current_pipe == 'J':
        if direction == Direction.SOUTH:
            steps = next_step(Direction.WEST, row_index, col_index, steps)
        else:
            steps = next_step(Direction.NORTH, row_index, col_index, steps)
    elif current_pipe == 'F':
        if direction == Direction.NORTH:
            steps = next_step(Direction.EAST, row_index, col_index, steps)
        else:
            steps = next_step(Direction.SOUTH, row_index, col_index, steps)
    elif current_pipe == '7':
        if direction == Direction.NORTH:
            steps = next_step(Direction.WEST, row_index, col_index, steps)
        else:
            steps = next_step(Direction.SOUTH, row_index, col_index, steps)

    return steps

def print_landscape(ls):
    for r in ls:
        print(r)


def check_south_inside(check_row, check_col):
    count = 0
    for row in empty_landscape[check_row+1:]:
        if len(re.findall("\||-|L|J|7|F|S", row[check_col])) == 1:
            count += 1

    if count % 2 != 0:
        return True
    else:
        return False

def check_north_inside(check_row, check_col):
    count = 0
    for row in empty_landscape[0:check_row]:
        if len(re.findall("\||-|L|J|7|F|S", row[check_col])) == 1:
            count += 1

    if count % 2 != 0:
        return True
    else:
        return False



with open("input10.txt") as my_file:
    for line in my_file:
        landscape.append(line.strip())

    # Add border to avoid need for boundary checks
    blank_row = ''
    for i in landscape[0]:
        blank_row += '.'
    landscape.append(blank_row)
    landscape.insert(0, blank_row)

    for index, row in enumerate(landscape):
        landscape[index] = '.' + row + '.'
        empty_landscape.append(blank_row)

    # find start
    start_row = 0
    start_col = 0
    for row_index, row in enumerate(landscape):
        for col_index, col in enumerate(row):
            if col == 'S':
                start_row = row_index
                start_col = col_index


    # iterate loop. need to find a valid first move
    first_direction = Direction.WEST
    if landscape[start_row-1][start_col] == '|' or \
        landscape[start_row-1][start_col] == '7' or \
        landscape[start_row-1][start_col] == 'F':
        first_direction = Direction.NORTH
    elif landscape[start_row][start_col+1] == '-' or \
        landscape[start_row][start_col+1] == '7' or \
        landscape[start_row][start_col+1] == 'J':
        first_direction = Direction.EAST
    elif landscape[start_row+1][start_col] == 'I' or \
        landscape[start_row+1][start_col] == 'L' or \
        landscape[start_row+1][start_col] == 'J':
        first_direction = Direction.EAST

    total_steps = next_step(first_direction, start_row, start_col, 0)

    print("")
    print("Part 1 = ", int(total_steps/2))

    print_landscape(empty_landscape)
    inside_count = 0
    outside_count = 0
    for row_index, row in enumerate(empty_landscape):
        for col_index, col in enumerate(row):
            if col != '.':
                continue
            else:
                if len(re.findall("\||-|L|J|7|F|S", row[col_index:])) % 2 != 0 and \
                        len(re.findall("\||-|L|J|7|F|S", row[0:col_index])) % 2 != 0:
                    print(row)
                    print("1:", re.findall("\||-|L|J|7|F|S", row[0:col_index]))
                    print("2:", re.findall("\||-|L|J|7|F|S", row[col_index:]))
                    #if check_north_inside(row_index, col_index) and check_south_inside(row_index, col_index):
                    inside_count +=1
                else:
                    outside_count += 1

    print(inside_count, outside_count)


