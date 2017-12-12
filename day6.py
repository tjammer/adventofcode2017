def argmax(banks):
    mx = max(banks)
    for i, bank in enumerate(banks):
        if bank == mx:
            return i

def redistribute(banks, index):
    count = banks[index]
    for i in range(count):
        banks[((index+1) + i) % len(banks)] += 1
    banks[index] -= count
    return banks


def part_one(banks):
    ctr = 0
    past_banks = []
    while True:
        past_banks.append(list(banks))
        index = argmax(banks)
        banks = redistribute(banks, index)
        ctr += 1
        if (banks in past_banks):
            return ctr


def part_two(banks):
    ctr = 0
    past_banks = []
    while True:
        past_banks.append(list(banks))
        index = argmax(banks)
        banks = redistribute(banks, index)
        ctr += 1
        if (banks in past_banks):
            for i, old_bank in enumerate(past_banks):
                if old_bank == banks:
                    return ctr - i

inp = """10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"""
banks = list(map(int, inp.split()))


if __name__ == '__main__':
    print('part_one: {}'.format(part_one(banks)))
    print('part_two: {}'.format(part_two(banks)))
