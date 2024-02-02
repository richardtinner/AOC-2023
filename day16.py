import sys
import timeit
import copy

lines = []
energised = []
history = {}

actions = {
    'E' : {'.' : ['E'], '-' : ['E'], '|' : ['N', 'S'], '/' : ['N'], '\\' : ['S']},
    'W' : {'.' : ['W'], '-' : ['W'], '|' : ['N', 'S'], '/' : ['S'], '\\' : ['N']},
    'N' : {'.' : ['N'], '|' : ['N'], '-' : ['E', 'W'], '/' : ['E'], '\\' : ['W']},
    'S' : {'.' : ['S'], '|' : ['S'], '-' : ['E', 'W'], '/' : ['W'], '\\' : ['E']}
}


def move(pos, direction):
    if pos in history:
        if direction in history[pos]:
            return
        else:
            history[pos].append(direction)
    else:
        history[pos] = [direction]

    energised[pos[0]] = energised[pos[0]][0:pos[1]] + '#' + energised[pos[0]][pos[1]+1:]
    current_tile = lines[pos[0]][pos[1]]
    next_moves = actions[direction][current_tile]

    for m in next_moves:
        if m == 'E' and pos[1] < (len(lines[0]) - 1):
            move((pos[0], pos[1]+1), m)
        elif m == 'W' and pos[1] > 0:
            move((pos[0], pos[1] - 1), m)
        elif m == 'N' and pos[0] > 0:
            move((pos[0] - 1, pos[1]), m)
        elif m == 'S' and pos[0] < (len(lines) - 1):
            move((pos[0] + 1, pos[1]), m)

    return


sys.setrecursionlimit(10000)
with open("input16.txt") as my_file:
    # read file
    for line in my_file:
        lines.append(line.strip())
        energised.append(line.strip())

    start_time = timeit.default_timer()
    move((0, 0), 'E')
    total = 0
    for energy_line in energised:
        total += energy_line.count('#')

    print('Part1 = ', total)
    end_time = timeit.default_timer() - start_time
    print(end_time, "seconds")
    print("Estimated part2 end time = ", 2*end_time*len(lines) + 2*end_time*len(lines[0]))

    start_time = timeit.default_timer()
    most_energy = 0
    for index, line in enumerate(lines):
        energised=copy.deepcopy(lines)
        history = {}
        move((index, 0), 'E')
        total = 0
        for energy_line in energised:
            total += energy_line.count('#')
        if total > most_energy:
            most_energy = total
            print(most_energy)

    for index, line in enumerate(lines):
        energised=copy.deepcopy(lines)
        history = {}
        move((index, len(line)-1), 'W')
        total = 0
        for energy_line in energised:
            total += energy_line.count('#')
        if total > most_energy:
            most_energy = total
            print(most_energy)

    for index, char in enumerate(lines[0]):
        energised=copy.deepcopy(lines)
        history = {}
        move((0, index), 'S')
        total = 0
        for energy_line in energised:
            total += energy_line.count('#')
        if total > most_energy:
            most_energy = total
            print(most_energy)

    for index, char in enumerate(lines[0]):
        energised=copy.deepcopy(lines)
        history = {}
        move((len(lines)-1, index), 'N')
        total = 0
        for energy_line in energised:
            total += energy_line.count('#')
        if total > most_energy:
            most_energy = total
            print(most_energy)

    print('Part2 = ', most_energy)
    end_time = timeit.default_timer() - start_time
    print(end_time, "seconds")



