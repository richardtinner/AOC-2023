import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def valid_grab(grab):
    for g in grab:
        if re.search("blue", g) and int(re.findall(r'\d+', g)[0]) > MAX_BLUE:
            return False
        if re.search("red", g) and int(re.findall(r'\d+', g)[0]) > MAX_RED:
            return False
        if re.search("green", g) and int(re.findall(r'\d+', g)[0]) > MAX_GREEN:
            return False
    return True


def parse_game1(line):
    # split the input into the multiple grabs, and extract the game number from the first one.
    split = re.split(':|;', line)
    game = int(re.findall(r'\d+', split[0])[0])

    # Iterate through grabs and validate whether it is possible.
    for index, item in enumerate(split[1:], 1):
        if not valid_grab(re.split(r',', item)):
            return 0

    return game


def parse_grab(grab):
    red = green = blue = 0

    for g in grab:
        if re.search("blue", g):
            blue = int(re.findall(r'\d+', g)[0])
        if re.search("green", g):
            green = int(re.findall(r'\d+', g)[0])
        if re.search("red", g):
            red = int(re.findall(r'\d+', g)[0])

    return red, green, blue


def parse_game2(line):
    mx_red = mx_green = mx_blue = 0

    # split the input into the multiple grabs, note first split is game number
    split = re.split(':|;', line)

    # Iterate through grabs and calculate minimum number of cubes possible
    for index, item in enumerate(split[1:], 1):
        grab = parse_grab(re.split(r',', item))
        if grab[0] > mx_red:
            mx_red = grab[0]
        if grab[1] > mx_green:
            mx_green = grab[1]
        if grab[2] > mx_blue:
            mx_blue = grab[2]

    return mx_red * mx_green * mx_blue


with open("input2.txt") as my_file:
    sum1 = 0
    sum2 = 0
    for line in my_file:
        sum1 += parse_game1(line)
        sum2 += parse_game2(line)

    print("Part 1 sum = ", sum1)
    print("Part 2 sum = ", sum2)
