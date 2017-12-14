def build_dict(inp):
    lines = (line.split(': ') for line in inp.strip().split('\n'))
    return {int(key): int(val) for key, val in lines}


def is_at_zero(i, val):
    ln = val + val - 2
    return i % ln == 0


def severity_with_delay(dct, delay=0, count_zero=False):
    package_pos = -delay

    severity = 0
    ctr = 0
    for key, val in dct.items():
        if is_at_zero(key+delay, val):
            severity += key * val
            if count_zero:
                severity = 1
                break
    return severity


def part_one(inp):
    dct = build_dict(inp)

    return severity_with_delay(dct)


def part_two(inp):
    dct = build_dict(inp)

    delay = 0
    while severity_with_delay(dct, delay, True) != 0:
        delay += 1

    return delay

inp = """0: 3
1: 2
2: 6
4: 4
6: 4
8: 10
10: 6
12: 8
14: 5
16: 6
18: 8
20: 8
22: 12
24: 6
26: 9
28: 8
30: 8
32: 10
34: 12
36: 12
38: 8
40: 12
42: 12
44: 14
46: 12
48: 12
50: 12
52: 12
54: 14
56: 14
58: 14
60: 12
62: 14
64: 14
66: 17
68: 14
72: 18
74: 14
76: 20
78: 14
82: 18
86: 14
90: 18
92: 14"""


if __name__ == '__main__':
    print('part_one: {}'.format(part_one(inp)))
    print('part_two: {}'.format(part_two(inp)))
