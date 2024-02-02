from queue import PriorityQueue

lines = []
all_nodes = []
frontier = PriorityQueue()
start = (0, 0)
came_from = dict()
came_from[start] = None
cost_so_far = dict()
cost_so_far[start] = 0

history = [None, None, None]


def neighbours(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        if 0 <= neighbor[0] < len(lines) and 0 <= neighbor[1] < len(lines[0]):
            result.append(neighbor)
    return result


def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_cost(pos):
    return int(lines[pos[0]][pos[1]])


def valid_move(pos_from, pos_to):
    h1 = h2 = None
    h1 = came_from[pos_from]
    if h1 in came_from:
        h2 = came_from[h1]
    if h1 is None or h2 is None:
        return True

    if pos_to[1] == pos_from[1] == h1[1] == h2[1] or \
            pos_to[0] == pos_from[0] == h1[0] == h2[0]:
        return False

    return True


with open("input17.txt") as my_file:
    # read file and initialise the node grid / frontier
    for line in my_file:
        lines.append(line.strip())

    all_nodes = [[row, col] for row in range(len(lines)) for col in range(len(lines[0]))]
    end = (len(lines) - 1, len(lines[0]) - 1)
    frontier.put((0, start))

    # Find the path
    while not frontier.empty():
        current = frontier.get()
        if current[1] == end:
            print('End - ', cost_so_far[end])

        for next in neighbours(current[1]):
            if (next == end):
                print("end")
            new_cost = cost_so_far[current[1]] + get_cost(next) + heuristic(end, next)
            if valid_move(current[1], next) and (next not in cost_so_far or new_cost < cost_so_far[next]):
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current[1]

    # Display the path
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    print(path)
    print(cost_so_far[end])
