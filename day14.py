from day10 import part_two as knot_hash


def hex_to_bin(hexstr):
    return ''.join('{0:04b}'.format(int(dig, 16)) for dig in hexstr)


def part_one(inp):
    return sum(sum(map(int, hex_to_bin(knot_hash(''.join((inp, '-{}'.format(i))))))) for i in range(128))



def part_two(inp):
    grid = [list(map(lambda x: bool(int(x)), hex_to_bin(knot_hash(''.join((inp, '-{}'.format(i))))))) for i in range(128)]

    def map_out_region(grid, x, y, reg):
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = max(min(127, x+dx), 0)
            ny = max(min(127, y+dy), 0)
            if grid[nx][ny] is True:
                grid[nx][ny] = reg
                map_out_region(grid, nx, ny, reg)

    ctr = 0
    for x in range(128):
        for y in range(128):
            if grid[x][y] is True:
                grid[x][y] = ctr
                map_out_region(grid, x, y, ctr)
                ctr += 1
    return ctr


inp = 'stpzcrnm'


if __name__ == '__main__':
    print('part_one: {}'.format(part_one(inp)))
    print('part_two: {}'.format(part_two(inp)))
