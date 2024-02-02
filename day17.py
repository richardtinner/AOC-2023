import sys
import timeit
from queue import PriorityQueue

lines = []
history = {
    (0, 0): 1
}

moves = {
    'E': ['E', 'N', 'S'],
    'W': ['W', 'N', 'S'],
    'N': ['E', 'W', 'N'],
    'S': ['E', 'W', 'S'],
    '#': ['E', 'S']
}

end_pos = ()


def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbours(previous, pos):
    neighbours = []
    nq = PriorityQueue()
    for m in moves[previous[2]]:
        if m == 'E' and previous != 'EEE' and pos[1] < len(lines[0]) - 1:
            heat = int(lines[pos[0]][pos[1] + 1:pos[1] + 2])
            nq.put((heat, (pos[0], pos[1] + 1), 'E'))
        elif m == 'W' and previous != 'WWW' and pos[1] > 0:
            heat = int(lines[pos[0]][pos[1] - 1:pos[1]])
            nq.put((heat, (pos[0], pos[1] - 1), 'W'))
        elif m == 'N' and previous != 'NNN' and pos[0] > 0:
            heat = int(lines[pos[0] - 1][pos[1]:pos[1] + 1])
            nq.put((heat, (pos[0] - 1, pos[1]), 'N'))
        elif m == 'S' and previous != 'SSS' and pos[0] < len(lines) - 1:
            heat = int(lines[pos[0] + 1][pos[1]:pos[1] + 1])
            nq.put((heat, (pos[0] + 1, pos[1]), 'S'))

    while not nq.empty():
        n = nq.get()
        neighbours.append((n[1], n[2]))

    return neighbours


def move(pos, previous, total, starting_point):
    # increment total only if not the start or at end
    end_point = (pos[0] == len(lines[0]) - 1 and pos[1] == len(lines) - 1)
    if pos != (0, 0) and not end_point:
        total += int(lines[pos[0]][pos[1]:pos[1] + 1])

    if (pos == (0,0)):
        print('Start')

    # Check history
    if pos in history:
        if total >= history[pos]:
            return

    history[pos] = total

    # Are we at the finish?
    if end_point:
        print("End. Total = ", total)
        return

    # Move
    neighbours = get_neighbours(previous, pos)
    for n in neighbours:
        if previous == '###':
            print('###')
        move(n[0], previous[1:3] + n[1], total, False)

    # for m in moves[previous[2]]:
    #     if m == 'E' and previous != 'EEE' and pos[1] < len(lines[0]) - 1:
    #         move((pos[0], pos[1] + 1), previous[1:3] + m, total, False)
    #     elif m == 'W' and previous != 'WWW' and pos[1] > 0:
    #         move((pos[0], pos[1] - 1), previous[1:3] + m, total, False)
    #     elif m == 'N' and previous != 'NNN' and pos[0] > 0:
    #         move((pos[0] - 1, pos[1]), previous[1:3] + m, total, False)
    #     elif m == 'S' and previous != 'SSS' and pos[0] < len(lines) - 1:
    #         move((pos[0] + 1, pos[1]), previous[1:3] + m, total, False)

    return


sys.setrecursionlimit(100000)
with open("input17.txt") as my_file:
    # read file
    for line in my_file:
        lines.append(line.strip())

    end_pos = (len(lines) - 1, len(lines[0]) - 1)

    move((0, 0), '###', 0, True)
