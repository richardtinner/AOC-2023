import timeit

lines = []

with open("input14.txt") as my_file:
    # read file
    for line in my_file:
        lines.append(line.strip())

    # Process rocks moving to top
    start_time = timeit.default_timer()
    found = 1
    while found > 0:
        found = 0
        for index, line in enumerate(lines[1:], 1):
            for ch_index, char in enumerate(line):
                if char == 'O':
                    if lines[index-1][ch_index] == '.':
                        # Have found a round rock that can be moved
                        lines[index - 1] = lines[index - 1][:ch_index] + 'O' + lines[index - 1][ch_index+1:]
                        lines[index] = lines[index][:ch_index] + '.' + lines[index][ch_index+1:]
                        found += 1

    # calculate score
    total_score = 0
    for index, line in enumerate(lines):
        row_score = len(lines) - index
        total_score += row_score * line.count('O')
    print("Part 1 = ", total_score)
    end_time = timeit.default_timer() - start_time
    print(end_time, "seconds")
    print("Part 2 estimate = ", end_time * 1000000000, " seconds")
    print("Part 2 estimate = ", end_time * 1000000000/(60*60), " hours")
