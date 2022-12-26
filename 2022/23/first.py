from collections import defaultdict

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def getX(self): return self.x
    def getY(self): return self.y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __radd__(self, other): return self + other
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar): return self * scalar
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()

def lines():
    while True:
        try:
            yield input()
        except:
            break

def parse(iterable) -> list:
    elves = []
    for y, row in enumerate(iterable):
        for x, c in enumerate(row):
            if c == '#':
                elves += [Point(x, y)]
    return elves

def display(points):
    x_min = min(points, key = Point.getX).x
    x_max = max(points, key = Point.getX).x
    empty = 0
    for y in range(min(points, key = Point.getY).y, max(points, key = Point.getY).y + 1):
        line = ''.join('.#'[(x, y) in points] for x in range(x_min, x_max + 1))
        print(line)
        empty += line.count('.')
    print(empty)

neighbors = [
    [(0, -1), (-1, -1), (1, -1)],
    [(0,  1), (-1,  1), (1,  1)],
    [(-1, 0), (-1, -1), (-1, 1)],
    [( 1, 0), ( 1, -1), ( 1, 1)]
]

elves = parse(lines())
S = set(elves)
display(S)
for turn in range(10):
    prev = elves
    P = S
    elves = []
    intent = defaultdict(list)
    done = True
    for e in prev:
        deltas = [((i // 3) - 1, (i % 3) - 1) for i in range(9) if i != 4]
        neighs = set([e + n for n in deltas])
        if not neighs & P:
            elves += [e]
            continue
        done = False
        found = False
        for three in [[e + n for n in neighbors[(i + turn) % len(neighbors)]] for i in range(len(neighbors))]:
            if not set(three) & P:
                intent[three[0]] += [e]
                found = True
                break
        if not found:
            elves += [e]
    if done:
        print('Done')
        display(set(elves))
        break
    for wanted, past in intent.items():
        if len(past) == 1:
            elves += [wanted]
        else:
            elves += past
    S = set(elves)
    display(S)
