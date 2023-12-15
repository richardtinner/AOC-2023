patterns = []


def count_differences(stra, strb):
    diffs = 0
    for ix, cx in enumerate(stra):
        if cx != strb[ix]:
            diffs+=1
    return diffs


def find_vertical_symmatries(pattern, part1):
    total_diffs = 0
    line_of_symmetry = -1
    for index in range(1, len(pattern[0])):
        total_diffs = 0
        sym_count = index
        if sym_count >= len(pattern[0]) / 2:
            sym_count = len(pattern[0]) - index
        symmetry = True
        while sym_count > 0:
            column1 = column2 = ''
            for i in range(0, len(pattern)):
                column1 += pattern[i][index + sym_count - 1]
                column2 += pattern[i][index - sym_count]
            if part1:
               if column1 != column2:
                    symmetry = False
                    break
            else:
                total_diffs += count_differences(column1, column2)
            sym_count -= 1

        if part1:
            if symmetry:
                line_of_symmetry = index
                break
        else:
            if total_diffs == 1:
                line_of_symmetry = index
                symmetry = True
                break
            else:
                symmetry = False

    if symmetry:
        return line_of_symmetry
    else:
        return 0


def find_horizontal_symmatries(pattern, part1):
    total_diffs = 0
    line_of_symmetry = -1
    for index, row in enumerate(pattern[1:], 1):
        total_diffs = 0
        sym_count = index
        if index >= len(pattern) / 2:
            sym_count = len(pattern) - index
        symmetry = True
        while sym_count > 0:
            if part1:
                if pattern[index + sym_count - 1] != pattern[index - sym_count]:
                    symmetry = False
                    break
            else:
                total_diffs += count_differences(pattern[index + sym_count - 1], pattern[index - sym_count])
            sym_count -= 1

        if part1:
            if symmetry:
                line_of_symmetry = index
                break
        else:
            if total_diffs == 1:
                line_of_symmetry = index
                symmetry = True
                break
            else:
                symmetry = False

    if symmetry:
        return line_of_symmetry
    else:
        return 0


with open("input13.txt") as my_file:
    pattern = []
    for line in my_file:
        if line != "\n":
            pattern.append(line.strip())
        else:
            patterns.append(pattern)
            pattern = []

    if len(pattern) != 0:
        patterns.append(pattern)
        pattern = []

    count = 0
    for index, pattern in enumerate(patterns):
        count += find_vertical_symmatries(pattern, True)
        count += find_horizontal_symmatries(pattern, True) * 100
    print("Part1 ", count)

    count = 0
    for index, pattern in enumerate(patterns):
        count += find_vertical_symmatries(pattern, False)
        count += find_horizontal_symmatries(pattern, False) * 100
    print("Part2 ", count)

