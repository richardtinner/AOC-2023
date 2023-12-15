numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def multi_find(s, r):
    return [pos for pos in range(len(s)) if s.startswith(r, pos)]


def parse_line2(line):
    first = 999
    first_digit = 0
    last = -1
    last_digit = 0

    for i in range(0, len(numbers)):
        hits = multi_find(line, numbers[i]) + multi_find(line, digits[i])
        for x in hits:
            if x < first:
                first = x
                first_digit = i + 1
            if x > last:
                last = x
                last_digit = i + 1

    return first_digit * 10 + last_digit


def parse_line(line):
    first_digit = ''
    last_digit = ''
    for c in line:
        if '0' <= c <= '9':
            if first_digit == '':
                first_digit = last_digit = c
            else:
                last_digit = c

    return int(first_digit) * 10 + int(last_digit)


with open("input1.txt") as my_file:
    sum1 = 0
    sum2 = 0
    for line in my_file:
        sum1 += parse_line(line)
        sum2 += parse_line2(line)

    print("Part1: ", sum1, "Part2: ", sum2)
