from enum import IntEnum, auto

def lines():
    while True:
        try:
            yield input()
        except:
            break

class Cardinal(IntEnum):
    EAST = 0
    SOUTH = auto()
    WEST = auto()
    NORTH = auto()

    def next(self):
        return Cardinal((self + 1) % 4)

    def prev(self):
        return Cardinal((self - 1) % 4)

class Point:
    __match_args__ = ['x', 'y']

    def __init__(self, x, y): self.x, self.y = x, y
    def neighbors(self):
        for d in Cardinal:
            yield self.next(d)
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __mul__(self, sca): return Point(self.x * sca, self.y * sca)
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()
    def __lt__(self, other): return (self.x, self.y) < (other[0], other[1])
    def __mod__(self, other): return Point(self.x % other[0], self.y % other[1])
    def next(self, direction: Cardinal):
        return self + {
            Cardinal.EAST: (1, 0),
            Cardinal.SOUTH: (0, 1),
            Cardinal.WEST: (-1, 0),
            Cardinal.NORTH: (0, -1)
        }[direction]
