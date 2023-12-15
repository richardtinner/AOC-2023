import re
from itertools import combinations
import timeit


def validate(code, spring_list):
    last_spring_index = 0
    next_spring_index = -1
    valid = True
    for c in code:
        new_sequence = True
        next_spring_index += 1
        count = c - 1

        # First check there is gap between previous sequence
        if spring_list[next_spring_index] - spring_list[last_spring_index] == 1:
            valid = False
            break

        # And now iterate over rest of sequence
        while count > 0:
            next_spring_index += 1
            if spring_list[next_spring_index] - spring_list[next_spring_index-1] != 1:
                valid = False
                break
            count -= 1
        last_spring_index = next_spring_index
        if not valid:
            break

    return valid


start_time = timeit.default_timer()
with open("input12.txt") as my_file:
    lines = []
    codes = []
    springs = []
    maybe_springs = []

    # Read and parse the file
    for line in my_file:
        lines.append(line.split()[0].strip())
        codes.append([int(i) for i in line.split()[1].split(',')])
        springs.append([int(i) for i, char in enumerate(lines[-1]) if char =='#'])
        maybe_springs.append([int(i) for i, char in enumerate(lines[-1]) if char == '?'])

    count = 0
    total_count = 0
    for index, line in enumerate(lines):
        spring_combs = combinations(maybe_springs[index], sum(codes[index]) - len(springs[index]))
        for spring_comb in spring_combs:
            comb = list(spring_comb) + springs[index]
            comb.sort()
            if validate(codes[index], comb):
                count += 1
        total_count += count
        #print("Possible solutions: ", line, codes[index], count)
        count = 0

    print("Part1 = ", total_count)
    print(timeit.default_timer() - start_time, "seconds")


start_time = timeit.default_timer()
with open("input12.txt") as my_file:
    lines = []
    codes = []
    springs = []
    maybe_springs = []

    # Read and parse the file
    for line in my_file:
        l1 = line.split()[0].strip()
        l2 = line.split()[1].split(',')
        ll = l1 + '?' + l1 + '?' + l1 + '?' + l1 + '?' + l1
        lines.append(ll)
        codes.append([int(i) for i in l2])
        codes[-1] = codes[-1] + codes[-1] + codes[-1] + codes[-1] + codes[-1]
        springs.append([int(i) for i, char in enumerate(lines[-1]) if char =='#'])
        maybe_springs.append([int(i) for i, char in enumerate(lines[-1]) if char == '?'])

    count = 0
    total_count = 0
    for index, line in enumerate(lines):
        spring_combs = combinations(maybe_springs[index], sum(codes[index]) - len(springs[index]))
        for spring_comb in spring_combs:
            comb = list(spring_comb) + springs[index]
            comb.sort()
            if validate(codes[index], comb):
                count += 1
        total_count += count
        print("Possible solutions: ", line, codes[index], count)
        count = 0

    print("Part2 = ", total_count)
    print(timeit.default_timer() - start_time, "seconds")