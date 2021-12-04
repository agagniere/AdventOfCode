sign = lambda x: x and (1, -1)[x < 0]

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def distance(self, other):
        return math.sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2)
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

seen = {}
count = 0
while True:
    try:
        line = input()
    except:
        break
    start, end = [Point(*map(int,s.split(','))) for s in line.split(' -> ')]
    diff = end - start
    if diff.x == 0 or diff.y == 0:
        way = (sign(diff.x), sign(diff.y))
        p = start
        keep_on = True
        while keep_on:
            if p in seen and seen[p] == 1:
                count += 1
            seen[p] = seen.get(p, 0) + 1
            keep_on = (p != end)
            p += way

for y in range(10):
    print(''.join([str(seen.get((x, y), 0)) for x in range(10)]))

print(count)
