from functools import reduce
from math import sqrt

class HailStone:
    def __init__(self, line):
        coords = line.split('@')
        self.x = int(coords[0].split(',')[0])
        self.y = int(coords[0].split(',')[1])
        self.z = int(coords[0].split(',')[2])
        self.vx = int(coords[1].split(',')[0])
        self.vy = int(coords[1].split(',')[1])
        self.vz = int(coords[1].split(',')[2])
        self.dx = self.vx
        self.dy = self.vy
        self.dz = self.vz

        if self.vx != 0:
            self.m = self.vy / self.vx
            self.c = self.y - self.m * self.x
        else:
            self.m = None
            self.c = self.x

    def __str__(self):
        return 'Pos: (' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + \
            ') - Vel: (' + str(self.vx) + ',' + str(self.vy) + ',' + str(self.vz) + ')' + \
            ' Y = ' + str(self.m) + 'X   +   ' + str(self.c)


def sign(x):
    return 0 if abs(x) == 0 else int(x / abs(x))


def paths_cross(hs1, hs2, min, max):
    #print('Hailstone A:', hs1)
    #print('Hailstone B:', hs2)

    if hs1.m == hs2.m:
        #print('Hailstones paths are parallel; they never intersect\n')
        return False
    elif hs1.m is None or hs2.m is None:
        #print('m is None:', hs1, hs2)
        return False

    int_x = (hs2.c - hs1.c) / (hs1.m - hs2.m)
    int_y = hs1.m * int_x + hs1.c
    int_y2 = hs2.m * int_x + hs2.c

    if min <= int_x <= max and min <= int_y <= max:
        if sign(int_x - hs1.x) == sign(hs1.vx) and sign(int_x - hs2.x) == sign(hs2.vx):
            #print('Hailstones paths will cross *inside* the test area (at x=', int_x, ', y=', int_y, ')\n')
            return True
        elif sign(int_x - hs1.x) == sign(hs1.vx) and sign(int_x - hs2.x) != sign(hs2.vx):
            #print('Hailstones paths crossed in the past for hailstone B\n')
            return False
        elif sign(int_x - hs1.x) != sign(hs1.vx) and sign(int_x - hs2.x) == sign(hs2.vx):
            #print('Hailstones paths crossed in the past for hailstone A\n')
            return False
        elif sign(int_x - hs1.x) != sign(hs1.vx) and sign(int_x - hs2.x) != sign(hs2.vx):
            #print('Hailstones paths crossed in the past for both hailstones\n')
            return False
    else:
        if sign(int_x - hs1.x) == sign(hs1.vx) and sign(int_x - hs2.x) == sign(hs2.vx):
            #print('Hailstones paths will cross outside the test area (at x=', int_x, ', y=', int_y, ')\n')
            return False
        elif sign(int_x - hs1.x) == sign(hs1.vx) and sign(int_x - hs2.x) != sign(hs2.vx):
            #print('Hailstones paths crossed in the past for hailstone B\n')
            return False
        elif sign(int_x - hs1.x) != sign(hs1.vx) and sign(int_x - hs2.x) == sign(hs2.vx):
            #print('Hailstones paths crossed in the past for hailstone A\n')
            return False
        elif sign(int_x - hs1.x) != sign(hs1.vx) and sign(int_x - hs2.x) != sign(hs2.vx):
            #print('Hailstones paths crossed in the past for both hailstones\n')
            return False

    return False


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


with open("input24.txt") as my_file:
    min_x = 200000000000000
    min_y = 400000000000000

    hail_stones = [HailStone(line) for line in my_file.readlines()]

    count = 0
    # for hs1_index, hs1 in enumerate(hail_stones):
    #     for hs2_index in range(hs1_index + 1, len(hail_stones)):
    #         if paths_cross(hs1, hail_stones[hs2_index], min_x, min_y):
    #             count += 1
    #
    # print("Part 1, count = ", count)

    # vx_map = dict()
    # for hs in hail_stones:
    #     if hs.vx in vx_map:
    #         vx_map[hs.vx].append(hs)
    #     else:
    #         vx_map[hs.vx] = [hs]
    #
    # vx = [hs.vx for hs in hail_stones]
    # vx.sort()
    #
    # possible_vx = set()
    # for i in range(0, len(vx)-2):
    #     if vx[i] == vx[i+1]:
    #         xdiff1 = vx_map[vx[i]][0].x - vx_map[vx[i]][1].x
    #         #print(vx_map[vx[i]][0], '\n', vx_map[vx[i]][1])
    #         #print(vx[i], xdiff1)
    #         f = factors(abs(xdiff1))
    #         if len(possible_vx) == 0:
    #             # first time, so create the initial list, that future iterations will reduce
    #             possible_vx = {vx[i] + pf for pf in f}
    #             possible_vx_minus = {vx[i] - pf for pf in f}
    #             possible_vx = possible_vx.union(possible_vx_minus)
    #             print("Possible vx:", possible_vx)
    #         else:
    #             possible_vx2 = {vx[i] + pf for pf in f}
    #             possible_vx2_minus = {vx[i] - pf for pf in f}
    #             possible_vx2 = possible_vx2.union(possible_vx2_minus)
    #             print(possible_vx2)
    #             possible_vx = possible_vx.intersection(possible_vx2)
    #             print("Possible vx:", possible_vx)
    #             if len(possible_vx) == 1:
    #                 break
    #
    # vy_map = dict()
    # for hs in hail_stones:
    #     if hs.vy in vy_map:
    #         vy_map[hs.vy].append(hs)
    #     else:
    #         vy_map[hs.vy] = [hs]
    #
    # vy = [hs.vy for hs in hail_stones]
    # vy.sort()
    #
    # possible_vy = set()
    # for i in range(0, len(vy)-2):
    #     if vy[i] == vy[i+1]:
    #         ydiff1 = vy_map[vy[i]][0].y - vy_map[vy[i]][1].y
    #         if ydiff1 == 0:
    #             continue
    #         #print(vy_map[vy[i]][0], '\n', vy_map[vy[i]][1])
    #         #print(vy[i], ydiff1)
    #         f = factors(abs(ydiff1))
    #         if len(possible_vy) == 0:
    #             # first time, so create the initial list, that future iterations will reduce
    #             possible_vy = {vy[i] + pf for pf in f}
    #             possible_vy_minus = {vy[i] - pf for pf in f}
    #             possible_vy = possible_vy.union(possible_vy_minus)
    #             print("Possible vy:", possible_vy)
    #         else:
    #             possible_vy2 = {vy[i] + pf for pf in f}
    #             possible_vy2_minus = {vy[i] - pf for pf in f}
    #             possible_vy2 = possible_vy2.union(possible_vy2_minus)
    #             print(possible_vy2)
    #             possible_vy = possible_vy.intersection(possible_vy2)
    #             print("Possible vy:", possible_vy)
    #             if len(possible_vy) == 1:
    #                 break
    #
    # vz_map = dict()
    # for hs in hail_stones:
    #     if hs.vz in vz_map:
    #         vz_map[hs.vz].append(hs)
    #     else:
    #         vz_map[hs.vz] = [hs]
    #
    # vz = [hs.vz for hs in hail_stones]
    # vz.sort()
    #
    # possible_vz = set()
    # for i in range(0, len(vz) - 2):
    #     if vz[i] == vz[i + 1]:
    #         zdiff1 = vz_map[vz[i]][0].z - vz_map[vz[i]][1].z
    #         if zdiff1 == 0:
    #             continue
    #         # print(vz_map[vz[i]][0], '\n', vz_map[vz[i]][1])
    #         # print(vz[i], zdiff1)
    #         f = factors(abs(zdiff1))
    #         if len(possible_vz) == 0:
    #             # first time, so create the initial list, that future iterations will reduce
    #             possible_vz = {vz[i] + pf for pf in f}
    #             possible_vz_minus = {vz[i] - pf for pf in f}
    #             possible_vz = possible_vz.union(possible_vz_minus)
    #             print("Possible vz:", possible_vz)
    #         else:
    #             possible_vz2 = {vz[i] + pf for pf in f}
    #             possible_vz2_minus = {vz[i] - pf for pf in f}
    #             possible_vz2 = possible_vz2.union(possible_vz2_minus)
    #             print(possible_vz2)
    #             possible_vz = possible_vz.intersection(possible_vz2)
    #             print("Possible vz:", possible_vz)
    #             if len(possible_vz) == 1:
    #                 break
    #
    # print(possible_vx, possible_vy, possible_vz)
    DX = -125 #list(possible_vx)[0]
    DY = 25 #list(possible_vy)[0]
    DZ = 272 #list(possible_vz)[0]

    h = hail_stones[0]
    hp = hail_stones[1]

    c1 = hp.dy - h.dy
    c2 = h.dx - hp.dx
    c3 = hp.x*hp.dy - hp.y*hp.dx - h.x*h.dy + h.y*h.dx - (h.y - hp.y)*DX - (hp.x-h.x)*DY

    d1 = hp.dz - h.dz
    d2 = h.dx - hp.dx
    d3 = hp.x*hp.dz - hp.z*hp.dx - h.x*h.dz + h.z*h.dx - (h.z-hp.z)*DX - (hp.x-h.x)*DZ

    e1 = hp.dy - h.dy
    e2 = h.dz - hp.dz
    e3 = hp.z*hp.dy - hp.y*hp.dz - h.z*h.dy + h.y*h.dz - (h.y-hp.y)*DZ - (hp.z-h.z)*DY

    f1 = e2*c1/c2
    f2 = e2*c3/c2 + e3
    f3 = e1*d3/d2
    f4 = e1*d1/d2

    X = (f2 + f3) / (f1 + f4)
    print(X)

