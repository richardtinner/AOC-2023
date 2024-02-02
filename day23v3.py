import sys
import copy

max_path = dict()
graph = dict()
distances = dict()

dirs = {'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)}


class Grid2d:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = (0, self.grid[0].find('.'))
        self.end = (len(grid) - 1, self.grid[len(grid) - 1].find('.'))

    def __getitem__(self, item):
        # returns None if outside the grid
        if len(item) > 2:
            raise ValueError('Grid2D expected a list like of length 2. Length of item longer than expected')
        x, y = item
        if 0 <= x < self.height:
            if 0 <= y < self.width:
                return self.grid[x][y]
        return None

    def get_neighbours(self, pos, part1):
        neighbours = []
        for d, dv in dirs.items():
            new_pos = (pos[0] + dv[0], pos[1] + dv[1])
            if not self[new_pos[0], new_pos[1]]:
                continue
            if part1:
                if (self[new_pos[0], new_pos[1]] == '>' and d == 'E') or \
                        (self[new_pos[0], new_pos[1]] == '<' and d == 'W') or \
                        (self[new_pos[0], new_pos[1]] == 'v' and d == 'S') or \
                        (self[new_pos[0], new_pos[1]] == '^' and d == 'N') or \
                        (self[new_pos[0], new_pos[1]] == '.'):
                    neighbours.append(new_pos)
            else:
                if self[new_pos[0], new_pos[1]] != '#':
                    neighbours.append(new_pos)

        return neighbours

    def plot_route(self, came_from):
        if self.end in came_from:
            current = self.end
            while current:
                self.grid[current[0]] = self.grid[current[0]][0:current[1]] + 'O' + self.grid[current[0]][
                                                                                    current[1] + 1:]
                current = came_from[current]

    def __str__(self):
        str = ''
        for line in self.grid:
            str += line + '\n'
        return str

    def find_nodes(self):
        nodes = [self.start, self.end]
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                pos = (row_index, col_index)
                if self[pos] == '#':
                    continue
                if len(self.get_neighbours(pos, False)) > 2:
                    nodes.append(pos)
        return nodes


def move(grid, nodes, start, came_from, pos, steps, part1):
    steps += 1
    global graph
    global distances
    print(start, pos, steps)

    if pos in nodes and pos != start:
        print('===========')
        if pos in graph:
            if start not in graph[pos]:
                graph[pos].append(start)
        else:
            graph[pos] = [start]
        if start in graph:
            if pos not in graph[start]:
                graph[start].append(pos)
        else:
            graph[start] = [pos]
        distances[(pos, start)] = steps
        distances[(start, pos)] = steps
        return

    for n in grid.get_neighbours(pos, part1):
        if n not in came_from:
            came_from[n] = pos
            move(grid, nodes, start, came_from, n, steps, part1)
            del came_from[n]
            #print('----- pos = ', pos, ' setps = ', steps)

    return


def build_graph(grid, pos, steps, max_steps, came_from, part1):


def traverse_graph(grid, pos, steps, max_steps, came_from, part1):
    global graph
    global distances
    global max_path

    steps += distances[(pos, came_from[pos])]
    if pos == grid.end:
        if steps > max_steps:
            print('end, new max = ', steps)
            max_steps = steps
            max_path = copy.deepcopy(came_from)
        return max_steps

    for n in graph[pos]:
        if n not in came_from:
            came_from[n] = pos
            max_steps = traverse_graph(grid, n, steps, max_steps, came_from, part1)
            del came_from[n]
            #print('----- pos = ', pos, ' setps = ', steps)

    return max_steps



sys.setrecursionlimit(100000)

with open("input23.txt") as my_file:
    lines = [line.strip() for line in my_file.readlines()]
    grid = Grid2d(lines)
    current = grid.start
    came_from = dict()
    came_from[grid.start] = None

    # Create the graph
    nodes = grid.find_nodes()
    print(len(nodes))
    distances[(None, (0,1))] = 0
    distances[((0,1), None)] = 0
    for n in nodes:
        neighbours = grid.get_neighbours(n, False)
        print('****************')
        print(n, ' neighbours = ', neighbours)
        for nbour in neighbours:
            print('*****', nbour)
            came_from[nbour] = n
            move(grid, nodes, n, came_from, nbour, 0, False)
            del came_from[nbour]

    # iterate through graph to find the shortest distance
    came_from.clear()
    came_from[grid.start] = None
    max_distance = traverse_graph(grid, grid.start, 0, 0, came_from, False)

    print(max_distance)

    for gi, g in graph.items():
        print(gi, g)
    print('=======')
    for di, d in distances.items():
        print(di, d)

    print(max_path)
    for a,b in max_path.items():
        print(b, '->', a, distances[(a,b)])