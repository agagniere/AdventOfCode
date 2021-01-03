RULES = {}


class Leaf:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

    def __contains__(self, item):
        return self.value == item


class Compound:

    def __init__(self, possibilities):
        self.possibilities = possibilities
        self.cache = None

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

    def make_cache(self):
        self.cache = set(self)

    def __contains__(self, item):
        if self.cache:
            return item in self.cache
        for possibility in self.possibilities:
            if len(possibility) == 1:
                if item in RULES[possibility[0]]:
                    return True
            elif len(possibility) == 2:
                for sep in range(1, len(item)):
                    if item[:sep] in RULES[possibility[0]] and item[sep:] in RULES[possibility[1]]:
                        return True
            elif len(possibility) == 3:
                for sep1 in range(1, len(item) - 1):
                    for sep2 in range(sep1 + 1, len(item)):
                        if item[:sep1] in RULES[possibility[0]] and item[sep1:sep2] in RULES[possibility[1]] and item[sep2:] in RULES[possibility[2]]:
                            return True
        return False


count = 0
while True:
    try:
        line = input()
    except:
        break
    if ':' in line:
        name, definition = line.split(': ')
        ruleID = int(name)
        if definition[0] == '"':
            RULES[ruleID] = Leaf(definition[1:-1])
        else:
            RULES[ruleID] = Compound([list(map(int, possibility.split())) for possibility in definition.split(' | ')])
    elif not line:
        RULES[42].make_cache()
        RULES[31].make_cache()
    else:
        if line in RULES[0]:
            count += 1
print(count)
