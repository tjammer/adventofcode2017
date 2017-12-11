def part_one(inp):
    x = 0
    y = 0
    steps = {
        'n':  (0, 1),
        's':  (0, -1),
        'ne': (1, 0.5),
        'se': (1, -0.5),
        'sw': (-1, -0.5),
        'nw': (-1, 0.5)}
    for d in inp.split(','):
        dx, dy = steps[d]
        x += dx
        y += dy
    x = abs(x)
    y = abs(y)
    mn = min(x, y / 0.5)
    return int(x + y - 0.5 * mn)


def part_two(inp):

    def calc_dist(x, y):
        mn = min(abs(x), abs(y / 0.5))
        return int(x + y - 0.5 * mn)

    x = 0
    y = 0
    mx = 0
    steps = {
        'n':  (0, 1),
        's':  (0, -1),
        'ne': (1, 0.5),
        'se': (1, -0.5),
        'sw': (-1, -0.5),
        'nw': (-1, 0.5)}
    for d in inp.split(','):
        dx, dy = steps[d]
        x += dx
        y += dy
        mx = max((calc_dist(x, y), mx))

    return mx
