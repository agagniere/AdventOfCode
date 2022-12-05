import sys

lines = map(str.strip, sys.stdin.readlines())

delta = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y
    def update(self, x, y):
        self.x, self.y = x, y
    def distance(self, other):
        return abs(self.x - other[0]) + abs(self.y - other[1])
    def module(self):
        return self.distance((0, 0))

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1])
    def __neg__(self):
        return Point(-self.x, -self.y)
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i):
        return self.x if i == 0 else self.y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __repr__(self):
        return "({} {})".format(self.x, self.y)
    def __hash__(self):
        return (self.x, self.y).__hash__()
