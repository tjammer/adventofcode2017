from math import sqrt


def part_one(n):
    last_sqrt = int(sqrt(n))
    # if is sqrt
    last_square = last_sqrt**2
    if (n == last_square):
        return last_sqrt - 1
    # find last uneven sqrt
    if (last_sqrt % 2) == 0:
        last_sqrt -= 1

    # special case
    if (n % last_square) == 1:
        return last_sqrt

    # find edges
    edgelength = (last_sqrt + 1)
    edges = [last_square + (i+1) * edgelength for i in range(3)]
    edgedist = min((abs(edge - n) for edge in edges))

    return (last_sqrt + 1) - edgedist


def part_two(threshold):
    # build explicit grid
    n = 1001
    grid = [[0 for i in range(n)] for j in range(n)]
    startcoord = n // 2
    grid[startcoord][startcoord] = 1

    def sum_neighbors(x, y, grid):
        # all unvisited fields are 0
        return sum(grid[x+dx][y+dy] for dx in (-1, 0, 1) for dy in (-1, 0, 1)) - grid[x][y]

    def coord_gen(startcoord):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        changes = 0;
        x, y = startcoord, startcoord
        steps = 1

        while True:
            for i in range(steps):
                dx, dy = directions[changes % 4]
                x += dx
                y += dy
                yield x, y
            changes += 1
            for i in range(steps):
                dx, dy = directions[changes % 4]
                x += dx
                y += dy
                yield x,y
            changes += 1
            steps += 1

    coords = coord_gen(startcoord)
    for x, y in coords:
        grid[x][y] = sum_neighbors(x, y, grid)
        if grid[x][y] > threshold:
            return grid[x][y]


inp = 349975
