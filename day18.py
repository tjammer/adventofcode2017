def get_val(dct, val):
    try:
        return int(val)
    except ValueError:
        return dct[val]


def part_one(inp):
    lines = inp.strip().split('\n')
    dct = {line.split()[1]: 0 for line in lines}

    current_line = 0
    last_freq = None

    while True:
        line = lines[current_line]
        split = line.split()
        if len(split) == 2:
            instr, val = split
            if instr == 'snd':
                last_freq = dct[val]
                current_line += 1
                continue
            elif instr == 'rcv':
                if dct[val] > 0:
                    break
                current_line += 1
                continue
        else:
            instr, reg, val = split
            if instr == 'set':
                dct[reg] = get_val(dct, val)
            elif instr == 'add':
                dct[reg] += get_val(dct, val)
            elif instr == 'mul':
                dct[reg] *= get_val(dct, val)
            elif instr == 'mod':
                dct[reg] = dct[reg] % get_val(dct, val)
            elif instr == 'jgz':
                if dct[reg] > 0:
                    current_line += get_val(dct, val)
                    continue
            current_line += 1

    return last_freq


class Program():
    def __init__(self, lines, default):
        self.dct = {line.split()[1]: 0 for line in lines}
        self.dct['p'] = default
        self.lines = lines
        self.waiting = False
        self.terminated = False
        self.current_line = 0
        self.queue = []
        self.send_ctr = 0

    def step(self, other_queue):
        if self.terminated:
            return
        try:
            line = self.lines[self.current_line]
        except IndexError:
            self.terminated = True
            return
        split = line.split()
        if len(split) == 2:
            instr, val = split
            if instr == 'snd':
                self.queue.append(self.dct[val])
                self.current_line += 1
                self.send_ctr += 1
            elif instr == 'rcv':
                try:
                    self.dct[val] = other_queue.pop(0)
                    self.current_line += 1
                    self.waiting = False
                except IndexError:
                    self.waiting = True
            return
        else:
            instr, reg, val = split
            if instr == 'set':
                self.dct[reg] = get_val(self.dct, val)
            elif instr == 'add':
                self.dct[reg] += get_val(self.dct, val)
            elif instr == 'mul':
                self.dct[reg] *= get_val(self.dct, val)
            elif instr == 'mod':
                self.dct[reg] = self.dct[reg] % get_val(self.dct, val)
            elif instr == 'jgz':
                if get_val(self.dct, reg) > 0:
                    self.current_line += get_val(self.dct, val)
                    return
            self.current_line += 1

def part_two(inp):
    lines = inp.strip().split('\n')
    p0 = Program(lines, 0)
    p1 = Program(lines, 1)

    running = True
    i = 0
    while running:
        p0.step(p1.queue)
        p1.step(p0.queue)
        i += 1

        if (p1.waiting or p1.terminated) and (p0.waiting or p0.terminated):
            running = False


    return p1.send_ctr


