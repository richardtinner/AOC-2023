import timeit

brick_list = []
dropped_brick_list = []


class Brick:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        self.min_z = c1[2]
        self.max_z = c2[2]
        self.fallen = False

    def __str__(self):
        s = ""
        return ("(" + str(self.c1[0]) + ", " + str(self.c1[1]) + ", " + str(self.c1[2]) + ") ~ " + \
                "(" + str(self.c2[0]) + ", " + str(self.c2[1]) + ", " + str(self.c2[2]) + ")")

    def drop_to_min_z(self, z):
        drop = self.min_z - z
        self.c1[2] -= drop
        self.c2[2] -= drop
        self.max_z = self.c2[2]
        self.min_z = self.c1[2]

    def intersect(self, brick):
        x_intersect = y_intersect = False
        if self.c1[0] <= brick.c1[0] <= self.c2[0] or \
                self.c1[0] <= brick.c2[0] <= self.c2[0] or \
                (brick.c1[0] <= self.c1[0] and brick.c2[0] >= self.c2[0]):
            x_intersect = True

        if self.c1[1] <= brick.c1[1] <= self.c2[1] or \
                self.c1[1] <= brick.c2[1] <= self.c2[1] or \
                (brick.c1[1] <= self.c1[1] and brick.c2[1] >= self.c2[1]):
            y_intersect = True

        return x_intersect and y_intersect


def sortMinZ(value):
    return value.min_z


def sortMaxZ(value):
    return value.max_z


def print_brick_list(bl):
    for b in bl:
        print(b)


start_time = timeit.default_timer()
with open("input22.txt") as my_file:
    # read file and init grid
    lines = [line.strip() for line in my_file.readlines()]
    for line in lines:
        c1 = [int(line.split('~')[0].split(',')[0]), \
              int(line.split('~')[0].split(',')[1]), \
              int(line.split('~')[0].split(',')[2])]
        c2 = [int(line.split('~')[1].split(',')[0]), \
              int(line.split('~')[1].split(',')[1]), \
              int(line.split('~')[1].split(',')[2])]
        brick_list.append(Brick(c1, c2))

    # Drop bricks
    brick_list.sort(key=sortMinZ)

    for brick in brick_list:
        dropped_brick = brick  # create a copy of the brick to drop and add to the new dropped brick list
        if brick.min_z != 1:
            # get list of bricks below the current brick and see which are in the way
            lower_bricks = [b for b in brick_list if b.max_z < brick.min_z]
            lower_bricks.sort(key=sortMaxZ, reverse=True)
            min_z = 1  # Assume no other blocks in the way.
            for lower_brick in lower_bricks:
                if brick.intersect(lower_brick):
                    min_z = lower_brick.max_z + 1  # can only drop to one above this brick
                    break
            dropped_brick.drop_to_min_z(min_z)
        dropped_brick_list.append(dropped_brick)

    # Part 1: find which bricks can be disintegrated
    disintegrate_list = []
    for brick in dropped_brick_list:
        # get the list of bricks supported by the current brick
        supported_bricks = [b for b in dropped_brick_list if b.min_z == brick.max_z + 1 and brick.intersect(b)]

        if len(supported_bricks) == 0:
            # not supporting anything, so brick can be disintegrated with no impact
            disintegrate_list.append(brick)
        else:
            safe_to_disintegrate = True
            for supported_brick in supported_bricks:
                supporting_bricks = [b for b in dropped_brick_list if
                                     b.max_z == supported_brick.min_z - 1 and supported_brick.intersect(b)]
                if len(supporting_bricks) == 1:
                    safe_to_disintegrate = False
                    break
            if safe_to_disintegrate:
                disintegrate_list.append(brick)

    print("Part 1 = ", len(disintegrate_list))

    # Part 2 - remove each brick 1 by 1 and see which other bricks would fall.
    total_fallen = 0
    for brick in dropped_brick_list:
        fallen = 0
        brick.fallen = True  # set current brick to be fallen (but do not count in total)
        # only bricks that can fall are those above the brick
        possible_drop_list = [b for b in dropped_brick_list if b.min_z > brick.max_z]
        for possible_drop_brick in possible_drop_list:
            # get the list of bricks supporting the possible drop brick that are not fallen
            # if this is 0 then flag this brick as fallen
            supporting_bricks = [b for b in dropped_brick_list if b.max_z == possible_drop_brick.min_z - 1 \
                                 and possible_drop_brick.intersect(b) and not b.fallen]
            if len(supporting_bricks) == 0:
                possible_drop_brick.fallen = True
                fallen += 1
        total_fallen += fallen
        # Reset fallen flag on all bricks for next brick to check
        for b in dropped_brick_list:
            b.fallen = False

    print("Part 2, ", total_fallen)
    print(timeit.default_timer() - start_time, "seconds")
