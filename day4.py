import re
import timeit

winning_numbers = []
numbers = []
count = []

# Parse the input
start_time = timeit.default_timer()
with open("input4.txt") as my_file:
    for line in my_file:
        split = re.split(':|\|', line)
        winning_numbers.append(split[1].strip().split())
        numbers.append(split[2].strip().split())
        count.append(1)

# Part 1
sum1 = 0
for index, nums in enumerate(numbers):
    card_score = 0
    for n in nums:
        for wn in winning_numbers[index]:
            if n == wn:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2
    sum1 += card_score

print('Part 1, sum =', sum1)

# Part 2
for index, nums in enumerate(numbers):
    # first count the matching numbers on the card
    matching_numbers = 0
    for n in nums:
        for wn in winning_numbers[index]:
            if n == wn:
                matching_numbers += 1

    # Add the copy cards for each of the matching numbers
    for n in range (0, matching_numbers):
        count[index+n+1] += count[index]

print('Part 2, sum =', sum(count))
print(timeit.default_timer() - start_time, "seconds")
