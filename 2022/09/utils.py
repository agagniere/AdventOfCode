import math

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def distance(self, other): return math.sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2)
    def module(self): return self.distance((0, 0))
    def neighors(self):
        for d in delta.values():
            yield self + d
    def extended_neighors(self):
        for d in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
            yield self + d
    def getX(self): return self.x
    def getY(self): return self.y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    #def __radd__(self, other): return
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    #def __rmul__(self, scalar): return self * scalar
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()

delta = {
    'U': Point(0, 1),
    'D': Point(0, -1),
    'L': Point(-1, 0),
    'R': Point(1, 0)
}


def lines():
    while True:
        try:
            yield input()
        except:
            break

def solve(length, instructions) -> set:
    rope = [Point(0,0) for _ in range(length)]
    seen = set()

    for instruction in instructions:
        D, n = instruction.split()
        for _ in range(int(n)):
            rope[0] += delta[D]
            for i in range(1, len(rope)):
                if rope[i].taxi_distance(rope[i-1]) > 3:
                    rope[i] = min(rope[i-1].extended_neighors(), key = rope[i].distance)
                elif rope[i].distance(rope[i-1]) >= 2:
                    rope[i] = min(rope[i-1].neighors(), key = rope[i].distance)
            seen.add(rope[-1])
    return seen

# What follows is absolutely not needed, just to visualize

def display(seen :set):
    "Outputs the positions in the PBM format, that can then be converted to any format with imagemagick"
    y_min = min(map(Point.getY, seen))
    y_max = max(map(Point.getY, seen))
    x_min = min(map(Point.getX, seen))
    x_max = max(map(Point.getX, seen))
    print("P1")
    print(x_max - x_min + 1, y_max - y_min + 1)
    for y in range(y_max, y_min - 1, -1):
        print(''.join(['01'[(x, y) in seen] for x in range(x_min, x_max + 1)]))

def art(length, instructions) -> set:
    "Outputs the positions in the XPM format, that can then be converted to any format with imagemagick"
    rope = [Point(0,0) for _ in range(length)]
    seen = [set() for _ in range(length)]
    for instruction in instructions:
        D, n = instruction.split()
        for _ in range(int(n)):
            rope[0] += delta[D]
            seen[0].add(rope[0])
            for i in range(1, len(rope)):
                if rope[i].taxi_distance(rope[i-1]) > 3:
                    rope[i] = min(rope[i-1].extended_neighors(), key = rope[i].distance)
                elif rope[i].distance(rope[i-1]) >= 2:
                    rope[i] = min(rope[i-1].neighors(), key = rope[i].distance)
                seen[i].add(rope[i])

    y_min = min(map(Point.getY, seen[0]))
    y_max = max(map(Point.getY, seen[0]))
    x_min = min(map(Point.getX, seen[0]))
    x_max = max(map(Point.getX, seen[0]))
    colors = [(255 * i // length, 255 * (length - i) // length, 255 * (length - i // 2) // length) for i in range(length)]
    print('/* XPM */')
    print('static char * aoc2022d9_xpm[] = {')
    print(f'"{x_max - x_min + 1} {y_max - y_min + 1} {length + 1} 1",')
    print(f'". c #111111",')
    for i, c in enumerate(colors):
        r, g, b = c
        print(f'"{i} c #{r:02x}{g:02x}{b:02x}",')
    for y in range(y_max, y_min - 1, -1):
        line = []
        for x in range(x_min, x_max + 1):
            line.append('.')
            for h in range(length - 1, -1, -1):
                if (x, y) in seen[h]:
                    line[-1] = str(h)
                    break
        print('"' + ''.join(line) + '",')
    print('};')
