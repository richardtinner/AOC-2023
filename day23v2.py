import sys
import copy

max_path = dict()

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


def move(grid, came_from, pos, steps, max_steps, part1):
    #print('move, pos = ', pos, ' steps = ', steps)
    global max_path

    if pos == grid.end:
        print("end, steps = ", steps)
        if steps > max_steps:
            max_steps = steps
            max_path = copy.deepcopy(came_from)
        return max_steps

    steps += 1
    for n in grid.get_neighbours(pos, part1):
        if n not in came_from:
            came_from[n] = pos
            max_steps = move(grid, came_from, n, steps, max_steps, part1)
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

    max_steps1 = move(grid, came_from, grid.start, 0, 0, True)
    #grid.plot_route(max_path)
    #print(grid)
    print('Part1: ', max_steps1)

    came_from.clear()
    max_steps2 = move(grid, came_from, grid.start, 0, 0, False)
    print('Part2: ', max_steps2)


