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

line = input()
x_limits, y_limits = [tuple(map(int, s.rstrip(',').split('=')[1].split('..'))) for s in line.split()[2:]]
target_UL, target_LR = Point(min(x_limits), max(y_limits)), Point(max(x_limits), min(y_limits))
print(target_UL, target_UL)

def simulate(initial_velocity):
    p = Point(0, 0)
    v = initial_velocity
    while p.y > target_UL.y or (v.x and p.x < target_UL.x):
        p += v
        if v.x:
            v.x -= 1
        v.y -= 1
    return target_UL.x <= p.x and p.x <= target_LR.x and target_LR.y <= p.y and p.y <= target_UL.y

counter = 0
for vx in range(1, target_LR.x + 1):
    for vy in range(target_LR.y, 100):
        counter += simulate(Point(vx, vy))
print(counter)
