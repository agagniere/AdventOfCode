ORTHO = {
    '#': '[]',
    '.': '`.',
    '>': '=>',
    '<': '<=',
    'v': '\\/',
    '^': '/\\',
    ' ': '  '
}

PRETTY_FACING = '>v<^'
NEIGHBORS     = [(1, 0), (0, 1), (-1, 0), (0, -1)]

RIGHT = 0
DOWN  = 1
LEFT  = 2
UP    = 3


'''
    0
1 2 3
    4 5
'''
MOVEMENT_SAMPLE = {
    0: {
        RIGHT: (5, LEFT),
        LEFT:  (2, DOWN),
        DOWN:  (3, DOWN),
        UP:    (1, DOWN)
    },
    1: {
        RIGHT: (2, RIGHT),
        LEFT:  (5, UP),
        DOWN:  (4, UP),
        UP:    (0, DOWN)
    },
    2: {
        RIGHT: (3, RIGHT),
        LEFT:  (1, LEFT),
        DOWN:  (4, RIGHT),
        UP:    (0, RIGHT)
    },
    3: {
        RIGHT: (5, DOWN),
        LEFT:  (2, LEFT),
        DOWN:  (4, DOWN),
        UP:    (0, UP)
    },
    4: {
        RIGHT: (5, RIGHT),
        LEFT:  (2, UP),
        DOWN:  (1, UP),
        UP:    (3, UP)
    },
    5: {
        RIGHT: (0, LEFT),
        LEFT:  (4, LEFT),
        DOWN:  (1, RIGHT),
        UP:    (3, LEFT)
    }
}

'''
  0 1
  2
3 4
5
'''
MOVEMENT_INPUT = {
    0: {
        RIGHT: (1, RIGHT),
        LEFT:  (3, RIGHT),
        DOWN:  (2, DOWN),
        UP:    (5, RIGHT)
    },
    1: {
        RIGHT: (4, LEFT),
        LEFT:  (0, LEFT),
        DOWN:  (2, LEFT),
        UP:    (5, UP)
    },
    2: {
        RIGHT: (1, UP),
        LEFT:  (3, DOWN),
        DOWN:  (4, DOWN),
        UP:    (0, UP)
    },
    3: {
        RIGHT: (4, RIGHT),
        LEFT:  (0, RIGHT),
        DOWN:  (5, DOWN),
        UP:    (2, RIGHT)
    },
    4: {
        RIGHT: (1, LEFT),
        LEFT:  (3, LEFT),
        DOWN:  (5, LEFT),
        UP:    (2, UP)
    },
    5: {
        RIGHT: (4, UP),
        LEFT:  (0, DOWN),
        DOWN:  (1, DOWN),
        UP:    (3, UP)
    }
}



class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def getX(self): return self.x
    def getY(self): return self.y
    def code(self): return self.y * 1000 + self.x * 4
    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)
        return Point(self.x + other[0], self.y + other[1])
    def __mod__(self, scalar):
        return Point(self.x % scalar, self.y % scalar)
    def __radd__(self, other): return self + other
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar): return self * scalar
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()

class Face:
    def __init__(self, chars, pos):
        self.chars = list(map(list, chars))
        self.pos = pos

    def __getitem__(self, p):
        return self.chars[p[1]][p[0]]

    def __setitem__(self, p, v):
        self.chars[p[1]][p[0]] = v

    def __str__(self):
        return '\n'.join(''.join(map(ORTHO.__getitem__, line)) for line in self.chars)

def lines():
    while True:
        try:
            yield input()
        except:
            break

def parse(iterable):
    all_lines = list(iterable)
    return all_lines[:-2], all_lines[-1]

def get_cube(net):
    side = 50 if len(net) > 16 else 4
    faces = []
    positions = []
    for y in range(0, len(net), side):
        for x in range(0, len(net[y]), side):
            if net[y][x] != ' ':
                faces.append(Face([net[y + j][x:][:side] for j in range(side)],
                                  Point(x, y)))
    return faces, side

net, instructions = parse(lines())
faces, side = get_cube(net)
movement = MOVEMENT_INPUT if side == 50 else MOVEMENT_SAMPLE

facing = RIGHT
face = 0
pos_on_face = Point(0, 0)
acc = 0
for c in instructions + 'E':
    if c.isdigit():
        acc *= 10
        acc += ord(c) - ord('0')
    else:
        while acc:
            faces[face][pos_on_face] = PRETTY_FACING[facing]
            n = pos_on_face + NEIGHBORS[facing]
            next_face = face
            next_facing = facing
            if n.x not in range(side) or n.y not in range(side):
                next_face, next_facing = movement[face][facing]
                if next_facing == facing:
                    pass
                elif next_facing % 2 == facing % 2:
                    if facing % 2 == 0:
                        n = Point(pos_on_face.x, side - 1 - pos_on_face.y)
                    else:
                        n = Point(side - 1 - pos_on_face.x, pos_on_face.y)
                else:
                    if facing == RIGHT and next_facing == DOWN:
                        n = Point(-n.y - 1, 0)
                    elif facing == DOWN and next_facing == RIGHT:
                        n = Point(0, -n.x - 1)
                    elif facing == LEFT and next_facing == UP:
                        n = Point(-n.y - 1, -1)
                    elif facing == UP and next_facing == LEFT:
                        n = Point(-1, -n.x - 1)
                    else:
                        n = Point(pos_on_face.y, pos_on_face.x)
                n += side
                n %= side
                print(pos_on_face, PRETTY_FACING[facing], '->', n, PRETTY_FACING[next_facing])
            if faces[next_face][n] == '#':
                break
            pos_on_face = n
            face = next_face
            facing = next_facing
            acc -= 1
        acc = 0
        if c in 'LR':
            facing += 1 + 2 * (c == 'L')
            facing %= 4
buf = [list(' ' * side * 4) for _ in range(side * 4)]
for f in faces:
    for y in range(side):
        for x in range(side):
            buf[f.pos.y + y][f.pos.x + x] = f[x,y]
#print('\n'.join(''.join(map(ORTHO.__getitem__, line)) for line in buf))
print('\n'.join(''.join(line) for line in buf))
print(pos_on_face, PRETTY_FACING[facing])
ans = pos_on_face + faces[face].pos + 1
print(ans, PRETTY_FACING[facing])
print(ans.code() + facing)
