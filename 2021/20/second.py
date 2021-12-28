class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
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

def lines():
    while True:
        try:
            yield input()
        except:
            break

dep = [Point(i % 3 - 1, i // 3 - 1) for i in range(9)]

canvas = [c == '#' for c in input()]
input()

image = list(lines())
W, H = len(image[0]), len(image)
pixels = set()
for y, row in enumerate(image):
    for x, c in enumerate(row):
        if c == "#":
            pixels.add((x, y))

UL, DR = Point(0,0), Point(W, H)
for step in range(50):
    UL -= (1, 1)
    DR += (1, 1)
    transform = set()
    for y in range(UL.y, DR.y):
        for x in range(UL.x, DR.x):
            if canvas[int(''.join(["01"[p in pixels or (canvas[0] and step % 2 and (p.x not in range(UL.x+1, DR.x-1) or p.y not in range(UL.y+1, DR.y-1)))] for p in map(Point(x, y).__add__, dep)]), base=2)]:
                transform.add((x, y))
    pixels = transform
    print(len(pixels))
