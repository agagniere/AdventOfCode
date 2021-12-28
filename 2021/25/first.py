def lines():
    while True:
        try:
            yield input()
        except:
            break

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def distance(self, other):
        return abs(self.x - other[0]) + abs(self.y - other[1])
    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])
    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1])
    def __neg__(self):
        return Point(-self.x, -self.y)
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    def __mod__(self, other):
        return Point(self.x % other[0], self.y % other[1])
    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i):
        return self.x if i == 0 else self.y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return (self.x, self.y).__hash__()
    def range(self):
        for y in range(self.y):
            for x in range(self.x):
                yield Point(x, y)

board = list(lines())
bounds = Point(len(board[0]), len(board))

east = set()
south = set()
for y, row in enumerate(board):
    for x, c in enumerate(row):
        if c == '>':
            east.add(Point(x, y))
        if c == 'v':
            south.add(Point(x, y))

print(east)
print(south)

moved = True
step = 0
while moved:
    moved = False
    use = east | south
    new_east = set()
    for cucumber in east:
        front = (cucumber + (1, 0)) % bounds
        new_east.add(cucumber if front in use else front)
        if front not in use:
            moved = True
    use = new_east | south
    new_south = set()
    for cucumber in south:
        front = (cucumber + (0, 1)) % bounds
        new_south.add(cucumber if front in use else front)
        if front not in use:
            moved = True
    east = new_east
    south = new_south
    step += 1
    #print(f"After {step} steps:")
    #for y in range(bounds.y):
    #    print(''.join(['>' if (x,y) in east else 'v' if (x, y) in south else '.' for x in range(bounds.x)]))
    #print("")
print(step)
