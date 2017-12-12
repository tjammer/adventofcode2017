def part_one(inp):
    def probe_node(network, node, visited):
        for val in network[node]:
            if val == 0:
                return True
            if val not in visited:
                visited.append(val)
                result = probe_node(network, val, visited)
                if result:
                    return result
        return False

    def build_network(inp):
        network = {}
        for line in inp.strip().split('\n'):
            key = int(line.split(' <-> ')[0])
            vals = list(map(int, line.split(' <-> ')[1].split(', ')))
            network[key] = vals
        return network

    network = build_network(inp)

    return sum(int(probe_node(network, node, [])) for node in network)


def part_two(inp):
    def build_network(inp):
        network = []
        for line in inp.strip().split('\n'):
            key = int(line.split(' <-> ')[0])
            vals = list(map(int, line.split(' <-> ')[1].split(', ')))
            network.append(set(vals + [key]))
        return network

    network = build_network(inp)
    set_num = len(network)
    while True:
        sets = []
        for st in network:
            found = False
            for i, other in enumerate(sets):
                if (len(st.intersection(other))) > 0:
                    sets[i] = st.union(other)
                    found = True
            if not found:
                sets.append(st)

        if set_num == len(sets):
            break
        set_num = len(sets)
        network = list(sets)

    return len(network)
