def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def neighbor(self, D): return self + [(0,-1),(1,0),(0,1),(-1,0)][D]
    def neighbors(self):
        for i in range(4):
            yield self.neighbor(i)
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()
    #def __contains__(self, other): return other.x in range(self.x) and other.y in range(self.y)
