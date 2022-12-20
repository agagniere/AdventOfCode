
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def getX(self): return self.x
    def getY(self): return self.y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
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

def lines():
    while True:
        try:
            yield input()
        except:
            break


board = list(lines())
instructions = board[-1]
board = board[:-2]
L = max(map(len, board))
board = [row + ' ' * (L - len(row)) for row in board]
print('|\n'.join(board))

pretty_facing = '>v<^'
dep_from_facing = [(1, 0), (0, 1), (-1, 0), (0, -1)]
facing = 0

pos = Point(min(i for i, c in enumerate(board[0]) if c == '.'), 0)
acc = 0
for c in instructions + 'E':
    if c.isdigit():
        acc *= 10
        acc += ord(c) - ord('0')
    else:
        # print(pos, pretty_facing[facing], acc)
        while acc:
            n = pos + dep_from_facing[facing]
            if n.y not in range(len(board)) or n.x not in range(len(board[pos.y])) or board[n.y][n.x] == ' ':
                line = board[pos.y] if facing % 2 == 0 else [row[pos.x] for row in board]
                s = min(i for i,c in enumerate(line) if c != ' ')
                e = max(i for i,c in enumerate(line) if c != ' ')
                m = e - s + 1
                # print(f'Wrapping "{line}"', s, e, m)
                if facing % 2 == 0:
                    n = Point(s + ((n.x - s) % m), pos.y)
                else:
                    n = Point(pos.x, s + ((n.y - s) % m))
            # print(n, board[n.y][n.x])
            if board[n.y][n.x] == '#':
                break
            pos = n
            acc -= 1
        acc = 0
        if c in 'LR':
            facing += 1 + 2 * (c == 'L')
            facing %= 4
print(pos, pretty_facing[facing])

print(1000 * (pos.y + 1) + 4 * (pos.x + 1) + facing)
