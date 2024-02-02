lines = []
frontier = []

dirs = {'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)}

class Grid2d:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        for index, line in enumerate(grid):
            if line.find('S') > -1:
                self.start_row = index
                self.start_col = line.find('S')


    def __getitem__(self, item):
        # returns None if outside the grid
        if len(item) > 2:
            raise ValueError('Grid2D expected a list like of length 2. Length of item longer than expected')

        x, y = item
        x = x % self.height
        y = y % self.width
        return self.grid[x][y]
        #if 0 <= x < self.height:
        #    if 0 <= y < self.width:
        #        return self.grid[x][y]
        #return None

    def __str__(self):
        s = ""
        for line in self.grid:
            s = s + line + '\n'
        return s


with open("input21.txt") as my_file:
    # read file and init grid
    lines = [line.strip() for line in my_file.readlines()]
    grid = Grid2d(lines)

    # start point is grid.start_row, grid.start_col
    start = [grid.start_row, grid.start_col]
    frontier.append(start)

    # iterate over frontier removing every point and adding it's neighbours
    for s in range(0, 70):
        new_frontier = []
        for pos in frontier:
            for d in dirs.values():
                new_pos = [pos[0] + d[0], pos[1] + d[1]]
                if grid[new_pos] and grid[new_pos] != '#' and new_pos not in new_frontier:
                    new_frontier.append(new_pos)

        print(s, len(new_frontier), len(frontier), len(new_frontier) - len(frontier))
        frontier = new_frontier

    print("Part 1, ", len(frontier))




