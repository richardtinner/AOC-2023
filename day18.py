dig_plan = []
vertices = [[0, 0]]
vertices2 = [[0, 0]]

mf = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
dir_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def calculate_polygon_area(vl):
    area = 0.0
    j = len(vl) - 1
    for i in range(0, len(vl)):
        area += (vl[j][0] + vl[i][0]) * (vl[j][1] - vl[i][1])
        j = i

    return int(abs(area / 2.0))


with open("input18.txt") as my_file:
    # read file
    edge_length1 = 0
    edge_length2 = 0
    for line in my_file:
        v = vertices[-1]
        dp = line.strip().split()
        dig_plan.append([dp[0], int(dp[1]), dp[2], dir_map[dp[2][7:8]], int(dp[2][2:7], 16)])
        edge_length1 += int(dp[1])
        edge_length2 += int(dig_plan[-1][4])

    for dp in dig_plan:
        v = vertices[-1]
        v2 = vertices2[-1]
        nv = [v[0] + int(dp[1]) * mf[dp[0]][0], v[1] + int(dp[1]) * mf[dp[0]][1]]
        nv2 = [v2[0] + int(dp[4]) * mf[dp[3]][0], v2[1] + int(dp[4]) * mf[dp[3]][1]]
        vertices.append(nv)
        vertices2.append(nv2)

    # vertices.pop(-1)
    area1 = calculate_polygon_area(vertices) + (edge_length1 / 2) + 1
    area2 = calculate_polygon_area(vertices2) + (edge_length2 / 2) + 1
    print(dig_plan)

    print("Part1 = ", area1)
    print("Part2 = ", area2)
