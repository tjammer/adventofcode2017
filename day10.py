def part_one(inp):
    inp = list(map(int, inp.split(',')))

    def select_invert(lst, index, length):
        selected = (lst * 2)[index:index+length]
        # put back together
        for i, val in enumerate(reversed(selected)):
            lst[(index + i) % len(lst)] = val
        return lst

    index = 0
    lst = list(range(256))
    for i, val in enumerate(inp):
        lst = select_invert(lst, index, val)
        index += val + i
        index = index % len(lst)
    return lst[0] * lst[1]


def part_two(_inp):

    def select_invert(lst, index, length):
        selected = (lst * 2)[index:index+length]
        # put back together
        for i, val in enumerate(reversed(selected)):
            lst[(index + i) % len(lst)] = val
        return lst

    def construct_inp(_inp):
        inp = list(map(ord, _inp))
        print(inp)
        # add salt
        inp += list(map(int, '17, 31, 73, 47, 23'.split(', ')))
        return inp * 64

    def make_dense(lst):
        assert(len(lst) == 16)
        hsh = 0
        for i in lst:
            hsh ^= i
        return hsh

    def make_hex(nums):
        return ''.join(hex(i)[2:].zfill(2) for i in nums)

    inp = construct_inp(_inp.strip())
    index = 0
    lst = list(range(256))
    for i, val in enumerate(inp):
        lst = select_invert(lst, index, val)
        index += val + i
        index = index % len(lst)

    dense_hash = []
    for i in range(16):
        print(lst[i*16:i*16+16])
        dense_hash.append(make_dense(lst[i*16:i*16+16]))
    print(dense_hash)

    return make_hex(dense_hash)


inp = """197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"""
