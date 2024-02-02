strings = []
boxes = []


def calculate_hash(sequence):
    hsh = 0
    for char in sequence:
        hsh += ord(char)
        hsh *= 17
        hsh = hsh % 256

    return hsh


with open("input15.txt") as my_file:
    # read file
    strings = my_file.read().strip().split(',')

    sum = 0
    for string in strings:
        sum += calculate_hash(string)

    print("Part1 = ", sum)

    # Initialise boxes array
    for i in range(0, 256):
        boxes.append({})

    # Iterate through each step
    box = -1
    for string in strings:
        code = string.split('=')
        if len(code) == 2:
            box = calculate_hash(code[0])
            boxes[box][code[0]] = int(code[1])
        else:
            code = string.split('-')
            box = calculate_hash(code[0])
            if code[0] in boxes[box]:
                boxes[box].pop(code[0])

    # calculate
    sum = 0
    for box_index, box in enumerate(boxes, 1):
        for lens_index, lens in enumerate(box, 1):
            val = box_index * lens_index * int(box[lens])
            sum += val

    print("Part2 = ", sum)
