
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def neighbors(self):
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            yield self + d
    def under(self):
        for d in [(0, 1), (-1, 1), (1, 1)]:
            yield self + d
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

def parse(iterable):
    rocks = set()
    for line in iterable:
        trail = [Point(*map(int, point.split(','))) for point in line.split(' -> ')]
        for A, B in zip(trail, trail[1:]):
            rocks.add(A)
            while A != B:
                A = min(A.neighbors(), key=B.taxi_distance)
                rocks.add(A)
    y_max = max(map(Point.getY, rocks))
    for y in range(min(map(Point.getY, rocks)), y_max+1):
        print(''.join([' #'[(x,y) in rocks] for x in range(min(map(Point.getX, rocks)), max(map(Point.getX, rocks)) + 1)]))
    return rocks, y_max

def solve(rocks: set, y_max: int, floor: bool) -> int:
    sands = set()
    while True:
        S = Point(500, 0)
        if S in sands:
            for y in range(0, y_max+2):
                print(''.join([' #O'[((x,y) in rocks) + 2*((x,y) in sands)] for x in range(400, 601)]))
            return len(sands)
        while S.y <= y_max:
            stuck = True
            for N in S.under():
                if N not in sands and N not in rocks:
                    stuck = False
                    break
            if stuck:
                sands.add(S)
                break
            else:
                S = N
        if S.y > y_max:
            if floor:
                for y in range(0, y_max+2):
                    print(''.join([' #O'[((x,y) in rocks) + 2*((x,y) in sands)] for x in range(400, 601)]))
                return len(sands)
            sands.add(S)
