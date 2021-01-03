RULES = {}


class Leaf:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class Compound:

    def __init__(self, possibilities):
        self.possibilities = possibilities

    def __iter__(self):
        for possibility in self.possibilities:
            beginnings = [""]
            for element in possibility:
                current = []
                for variant in RULES[element]:
                    for beg in beginnings:
                        current += [beg + variant]
                beginnings = current
            for answer in beginnings:
                yield answer


count = 0
while True:
    try:
        line = input()
    except:
        break
    if ':' in line:
        name, definition = line.split(': ')
        if definition[0] == '"':
            RULES[int(name)] = Leaf(definition[1:-1])
        else:
            RULES[int(name)] = Compound([list(map(int, possibility.split())) for possibility in definition.split(' | ')])
    elif not line:
        print("Read", end=' ')
        possibilities = set(RULES[0])
        print(len(possibilities), "possibilities")
    elif line in possibilities:
        count += 1
print(count)
