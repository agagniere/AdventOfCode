def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def neighbors(self):
        for d in ((a, b) for a in range(-1, 2) for b in range(-1, 2) if a or b):
            yield self + d
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()
