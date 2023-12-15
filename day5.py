import re
import timeit

seeds = []
locations = []
seeds_to_soil_map = []
soil_to_fertiliser_map = []
fertiliser_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []


def read_map(in_map, file):
    file.readline()
    line = file.readline()
    while re.findall(r'\d+', line) != []:
        in_map.append([int(x) for x in re.findall(r'\d+', line)])
        line = my_file.readline()
    in_map.sort(key=lambda a: a[1])


def process_map(in_val, in_map):
    if in_val < in_map[0][1]:
        return in_val

    for index, map_item in enumerate(in_map):
        if in_val <= map_item[1] + map_item[2]:
            return map_item[0] + in_val - map_item[1]
        elif in_val < in_map[index + 1][1]:
            return in_val
    return in_val


with open("input5.txt") as my_file:
    seeds_line = my_file.readline()
    seeds = [int(x) for x in re.findall(r'\d+', seeds_line)]
    my_file.readline()

    read_map(seeds_to_soil_map, my_file)
    read_map(soil_to_fertiliser_map, my_file)
    read_map(fertiliser_to_water_map, my_file)
    read_map(water_to_light_map, my_file)
    read_map(light_to_temperature_map, my_file)
    read_map(temperature_to_humidity_map, my_file)
    read_map(humidity_to_location_map, my_file)

    start_time = timeit.default_timer()
    for seed in seeds:
        soil = process_map(seed, seeds_to_soil_map)
        fertiliser = process_map(soil, soil_to_fertiliser_map)
        water = process_map(fertiliser, fertiliser_to_water_map)
        light = process_map(water, water_to_light_map)
        temperature = process_map(light, light_to_temperature_map)
        humidity = process_map(temperature, temperature_to_humidity_map)
        locations.append(process_map(humidity, humidity_to_location_map))

    locations.sort()
    print("Part1 = ", locations[0])
    t = timeit.default_timer() - start_time
    print(t, "seconds")

    # Part 2
    min_location = 99999999999999999
    for s in range(0, len(seeds), 2):
        print(seeds[s], seeds[s + 1])
        for seed in range(seeds[s], seeds[s] + seeds[s + 1]):
            soil = process_map(seed, seeds_to_soil_map)
            fertiliser = process_map(soil, soil_to_fertiliser_map)
            water = process_map(fertiliser, fertiliser_to_water_map)
            light = process_map(water, water_to_light_map)
            temperature = process_map(light, light_to_temperature_map)
            humidity = process_map(temperature, temperature_to_humidity_map)
            location = process_map(humidity, humidity_to_location_map)
            if location < min_location:
                min_location = location

    print(min_location)
