def part_one(inp):
    l = list(range(1))
    current = 0
    for i in range(2017):
        current = (current + inp) % len(l) + 1
        l.insert(current, i + 1)
    return l[current + 1]


def part_two(inp):
    current = 0
    res = 0
    for i in range(50000000):
        current = (current + inp) % (i + 1) + 1
        if current == 1:
            res = i + 1
    return res


inp = 377


if __name__ == '__main__':
    print(part_one(inp))
    print(part_two(inp))
