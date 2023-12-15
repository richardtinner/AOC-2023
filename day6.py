import math
import re
import timeit

times = []
distances = []

def process_race(race_time, best_distance):
    win = 0
    for t in range(0, race_time + 1):
        # race!
        speed = t
        d = (race_time - t) * speed
        if d > best_distance:
            win += 1
    return win


start_time = timeit.default_timer()
with open("input6.txt") as my_file:
    times = [int(x) for x in re.findall(r'\d+', my_file.readline())]
    distances = [int(x) for x in re.findall(r'\d+', my_file.readline())]

total_wins = 1
for i in range(0, len(times)):
    new_wins = process_race(times[i], distances[i])
    if new_wins != 0:
        total_wins *= new_wins

print("Part 1 ", total_wins)
print(timeit.default_timer() - start_time, "seconds")

# part 2
race_time = 48938595
best_distance = 296192812361391
#race_time = 71530
#best_distance = 940200
a = -1
b = race_time
c = -1 * best_distance

b2_4ac = math.sqrt(b*b - (4*a*c))
r1 = (-1*b + b2_4ac) / (2*a)
r2 = (-1*b - b2_4ac) / (2*a)
print(r1, r2)
print("Part 2= ", math.floor(r2) - math.ceil(r1) + 1)