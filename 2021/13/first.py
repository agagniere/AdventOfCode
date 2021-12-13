class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]
    def __setitem__(self, i, v):
        if i:
            self.y = v
        else:
            self.x = v
    def __getitem__(self, i):
        return self.y if i else self.x
    def __hash__(self):
        return (self.x, self.y).__hash__()

def lines():
    while True:
        try:
            yield input()
        except:
            break

dots = []
for line in lines():
    if not line:
        break
    dots += [Point(*map(int, line.split(',')))]

axe, v = next(lines()).split()[2].split('=')
v = int(v)
axe = "xy".index(axe)
for dot in dots:
    if dot[axe] > v:
        dot[axe] = 2 * v - dot[axe]

print(len(set(dots)))
