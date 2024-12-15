def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    __match_args__ = ['x', 'y']

    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()
    def __lt__(self, other): return (self.x, self.y) < (other[0], other[1])
    def next(self, direction):
        match direction:
            case 'e': return self + (1, 0)
            case 'w': return self + (-1, 0)
            case 'se': return self + ((1, 1) if self.y % 2 == 0 else (0, 1))
            case 'ne': return self + ((1, -1) if self.y % 2 == 0 else (0, -1))
            case 'sw': return self + ((0, 1) if self.y % 2 == 0 else (-1, 1))
            case 'nw': return self + ((0, -1) if self.y % 2 == 0 else (-1, -1))
            case _:
                raise ValueError("Not a valid direction")
    def neighbors(self):
        for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
            yield self.next(direction)
