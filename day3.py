schematic = []


def process_row(row, col_index):
    num = 0
    on_gear = False
    ratios = []
    for c_index, col in enumerate(row[1:(len(row))], 1):
        if col.isdigit():
            num = num * 10 + int(col)
            if col_index - 1 <= c_index <= col_index + 1:
                on_gear = True
        else:
            # check if we have finished parsing a number and therefore need to process
            if num > 0:
                if on_gear:
                    ratios.append(num)
                    on_gear = False
                num = 0

    return ratios


def process_gear(row_index, col_index):
    ratios = process_row(schematic[row_index - 1], col_index)
    ratios += process_row(schematic[row_index], col_index)
    ratios += process_row(schematic[row_index + 1], col_index)
    if len(ratios) == 2:
        return ratios[0] * ratios[1]

    return 0


def process_number(number, row_index, col_index):
    max = len(str(number)) + 2
    for r in range(row_index - 1, row_index + 2):
        for c in range(col_index - max + 1, col_index + 1):
            if schematic[r][c] == '.' or schematic[r][c].isdigit():
                continue
            else:
                # must be a symbol, so count this number
                return number

    return 0


# Read the file into an array, and add an empty row around the outside.
# This will make the iterate over the grid simpler as will not need logic to consider outside cells
with open("input3.txt") as my_file:
    for line in my_file:
        line = '.' + line.strip() + '.'
        schematic.append(line)

empty_row = ""
for i in schematic[0]:
    empty_row += '.'
schematic.insert(0, empty_row)
schematic.append(empty_row)

# Part 1
sum = 0
for row_index, row in enumerate(schematic[1:(len(schematic) - 1)], 1):
    # Iterate over the row
    number = 0
    for col_index, col in enumerate(row[1:(len(row))], 1):
        if col.isdigit():
            number = number * 10 + int(col)
        else:
            # check if we have finished parsing a number and therefore need to process
            if number > 0:
                sum += process_number(number, row_index, col_index)
                number = 0

print("Part1 sum = ", sum)

# Part 2
sum2 = 0
for row_index, row in enumerate(schematic[1:(len(schematic) - 1)], 1):
    # Iterate over the row
    number = 0
    for col_index, col in enumerate(row[1:(len(row))], 1):
        if col == '*':
            sum2 += process_gear(row_index, col_index)

print("Part2 sum = ", sum2)
