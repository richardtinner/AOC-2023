import re
import copy

history_list = []
orig_history_list = []

def all_zeros(li):
    all_zero = True
    for l in li:
        if l != 0:
            all_zero = False
            break
    return all_zero

def extrapolate_history1(history):
    all_diffs_zero = all_zeros(history)
    diff_list_array = [history]
    while not all_diffs_zero:
        diff_list = []
        for index, value in enumerate(diff_list_array[-1][1:]):
            diff_list.append(value - diff_list_array[-1][index])
        diff_list_array.append(diff_list)
        all_diffs_zero = all_zeros(diff_list)

    diff_list_array.reverse()
    diff_list_array[0].insert(0, 0)
    for index, diff_list in enumerate(diff_list_array[1:], 1):
        diff_list.append(diff_list[0] + diff_list_array[index-1][0])

    return diff_list_array[-1][0]

def extrapolate_history2(history):
    all_diffs_zero = all_zeros(history)
    diff_list_array = [history]
    while not all_diffs_zero:
        diff_list = []
        for index, value in enumerate(diff_list_array[-1][1:]):
            diff_list.append(value - diff_list_array[-1][index])
        diff_list_array.append(diff_list)
        all_diffs_zero = all_zeros(diff_list)

    print(diff_list_array)

    diff_list_array.reverse()
    diff_list_array[0].append(0)
    for index, diff_list in enumerate(diff_list_array[1:], 1):
        diff_list.insert(0, diff_list[0] - diff_list_array[index-1][0])

    print(diff_list_array)
    return diff_list_array[-1][0]


with open("input9.txt") as my_file:
    for line in my_file:
        history_list.append([int(x) for x in re.findall(r'[-+]?\d+', line)])

    orig_history_list = copy.deepcopy(history_list)
    total1 = 0
    for history in history_list:
        total1 += extrapolate_history1(history)

    print("Part1 = ", total1)

    total2 = 0
    for history in orig_history_list:
        total2 += extrapolate_history2(history)

    print("Part2 = ", total2)


