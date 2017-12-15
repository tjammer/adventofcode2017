def compare(a, b):
    return a & 0xffff == b & 0xffff


def gen(start, factor):
    divisor = 2147483647
    while True:
        start *= factor
        start = start % divisor
        yield start


def gen_b(start, factor, mod):
    for a in gen(start, factor):
        if a % mod == 0:
            yield a


def part_one(a_start, b_start):
    a = gen(a_start, 16807)
    b = gen(b_start, 48271)
    return sum(1 for i in range(4*10**7) if compare(next(a), next(b)))


def part_two(a_start, b_start):
    a = gen_b(a_start, 16807, 4)
    b = gen_b(b_start, 48271, 8)
    return sum(1 for i in range(5*10**6) if compare(next(a), next(b)))


inp = (699, 124)


if __name__ == '__main__':
    print(part_one(*inp))
    print(part_two(*inp))
