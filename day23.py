from heapq import heappop, heappush

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

    def get_neighbours(self, pos):
        neighbours = []
        for d, dv in dirs.items():
            new_pos = (pos[0] + dv[0], pos[1] + dv[1])
            if not self[new_pos[0], new_pos[1]]:
                continue
            if (self[new_pos[0], new_pos[1]] == '>' and d == 'E') or \
                    (self[new_pos[0], new_pos[1]] == '<' and d == 'W') or \
                    (self[new_pos[0], new_pos[1]] == 'v' and d == 'S') or \
                    (self[new_pos[0], new_pos[1]] == '^' and d == 'N') or \
                    (self[new_pos[0], new_pos[1]] == '.'):
                neighbours.append(new_pos)

        return neighbours

    def plot_route(self, came_from):
        if self.end in came_from:
            current = self.end
            while current:
                self.grid[current[0]] = self.grid[current[0]][0:current[1]] + 'O' + self.grid[current[0]][current[1]+1:]
                current = came_from[current]

    def __str__(self):
        str = ''
        for line in self.grid:
            str += line + '\n'
        return str


with open("input23.txt") as my_file:
    lines = [line.strip() for line in my_file.readlines()]
    grid = Grid2d(lines)
    frontier = []
    came_from = dict()
    came_from[grid.start] = None
    heappush(frontier, grid.start)
    print(grid.end)

    current = None
    while frontier:
        current = heappop(frontier)
        if current == grid.end:
            break
        for next in grid.get_neighbours(current):
            if next not in came_from:
                heappush(frontier, next)
                came_from[next] = current

    grid.plot_route(came_from)
    print(grid)





