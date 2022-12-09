from math import prod

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()

def lines():
    while True:
        try:
            yield input()
        except:
            break

def store_forest():
    return [list(map(int, line)) for line in lines()]

def dict_forest():
    return {Point(x,y): int(tree) for y, row in enumerate(lines()) for x, tree in enumerate(row)}

def scenic_score(forest :dict, tree :Point) -> int:
    def aux(direction :Point):
        p = tree
        d = 0
        while True:
            p += direction
            if p not in forest:
                break
            d += 1
            if forest[p] >= forest[tree]:
                break
        return d
    return prod(aux(d) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)])


def visible_from_h(forest :list, reverse :bool):
    result = set()
    for y, row in enumerate(forest):
        M = -1
        for x, tree in list(enumerate(row))[::-1 if reverse else 1]:
            if tree > M:
                M = tree
                result.add((x, y))
                #print(x, y, tree)
    return result

def visible_from_v(forest :list, reverse :bool):
    result = set()
    for x in range(len(forest[0])):
        M = -1
        for y in list(range(len(forest)))[::-1 if reverse else 1]:
            tree = forest[y][x]
            if tree > M:
                M = tree
                result.add((x, y))
                #print(x, y, tree)
    return result

def visible_from(forest :list):
    return visible_from_h(forest, True) | visible_from_h(forest, False) | visible_from_v(forest, True) | visible_from_v(forest, False)
