def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z
    def taxi_distance(self, other): return sum(abs(s - o) for s, o in zip(self, other))
    def is_neighbors(self, other):  return self.taxi_distance(other) == 1
    def neighbors(self):
        yield Point(self.x -1, self.y, self.z)
        yield Point(self.x +1, self.y, self.z)
        yield Point(self.x, self.y -1, self.z)
        yield Point(self.x, self.y +1, self.z)
        yield Point(self.x, self.y, self.z -1)
        yield Point(self.x, self.y, self.z +1)
    def getX(self): return self.x
    def getY(self): return self.y
    def getZ(self): return self.z
    def __add__(self, other):   return Point(*(s + o for s, o in zip(self, other)))
    def __neg__(self):          return Point(*(-c for c in self))
    def __mul__(self, scalar):  return Point(*(c * scalar for c in self))
    def __eq__(self, other):    return self.x == other[0] and self.y == other[1] and self.z == other[2]
    def __getitem__(self, i):   return [self.x, self.y, self.z][i]
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    def __str__(self):  return "({}, {}, {})".format(self.x, self.y, self.z)
    def __repr__(self): return "({} {} {})".format(self.x, self.y, self.z)
    def __hash__(self): return (self.x, self.y, self.z).__hash__()
