from enum import IntEnum, auto

def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    __match_args__ = ['x', 'y']

    def __init__(self, x, y): self.x, self.y = x, y
    def neighbors(self):
        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            yield self + d
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __mul__(self, sca): return Point(self.x * sca, self.y * sca)
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()
    def __contains__(self, other): return other[0] in range(self.x) and other[1] in range(self.y)
