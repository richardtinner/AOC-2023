import re
import math
import networkx as nx
import matplotlib.pyplot as plt

directions = []
current_positions = []
min_steps = []
network = {}


def all_finished(positions, steps):
    finished = False
    check_finished = False
    for index, p in enumerate(positions):
        if p[2] == 'Z' and min_steps[index] == 0:
            min_steps[index] = steps
            check_finished = True

    if check_finished:
        finished = True
        for s in min_steps:
            if s == 0:
                finished = False
    return finished


def is_prime(num):
    prime = True
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(i, num/i)
                prime = False
                break
    else:
        return False

    return prime



with open("input8.txt") as my_file:
    G = nx.Graph()
    directions = my_file.readline().strip()
    my_file.readline()
    for line in my_file:
        parse = re.findall('[A-Z]+', line)
        network[parse[0]] = {'L': parse[1], 'R': parse[2]}
        G.add_node(parse[0])
        G.add_edge(parse[0], parse[1])
        G.add_edge(parse[0], parse[2])

    current_pos = 'AAA'
    steps = 0
    finished = False
    while not finished:
        for d in directions:
            current_pos = network[current_pos][d]
            steps += 1
            if current_pos == 'ZZZ':
                finished = True
                break

    print("Part1, ", steps)

    # part 2. Need to parse the input to find all of the start positions that end with A
    for key in network:
        if key[2] == 'A':
            current_positions.append(key)
            min_steps.append(0)

    print(current_positions)

    steps = 0
    finished = False
    while not finished:
        for d in directions:
            steps += 1
            for index, pos in enumerate(current_positions):
                current_positions[index] = network[pos][d]
            if all_finished(current_positions, steps):
                finished = True
                break

    print(min_steps)
    print("Part 2 =", math.lcm(*min_steps))
    for ms in min_steps:
        print (ms, is_prime(ms))

    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]


    nx.draw(S[0], pos=nx.circular_layout(S[0]), with_labels=True, font_weight='bold')

    plt.show()




