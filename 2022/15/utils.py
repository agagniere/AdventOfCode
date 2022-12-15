
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def neighbors(self):
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            yield self + d
    def under(self):
        for d in [(0, 1), (-1, 1), (1, 1)]:
            yield self + d
    def tuning(self):
        return self.x * 4000000 + self.y
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

def parse_quarter(s: str) -> int:
    return int(''.join(c for c in s if c.isdigit() or c=='-'))

def parse_half(s: str) -> Point:
    return Point(*map(parse_quarter, s.split()[-2:]))

def parse(iterable) -> list:
    data = []
    beacons = []
    for line in iterable:
        key, value = line.split(': ')
        S, B = map(parse_half, [key, value])
        D = S.taxi_distance(B)
        data += [ (S, D) ]
        beacons.append(B)
    return data, beacons
