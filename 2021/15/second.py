from heapq import heappush, heappop

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
    def __hash__(self):
        return (self.x, self.y).__hash__()

def lines():
    while True:
        try:
            yield input()
        except:
            break

board = [list(map(int, row)) for row in lines()]
dim_board = Point(len(board[0]), len(board))
dim_cave = dim_board * 5
start = Point(0,0)
end = dim_cave - (1, 1)

def get_risk(p):
    r = board[p.y % dim_board.y][p.x % dim_board.x]
    xtra = p.x // dim_board.x + p.y // dim_board.y
    return 1 + ((r - 1 + xtra) % 9)

def adjacents(p):
    if p.x < end.x:
        yield p + (1, 0)
    if p.y < end.y:
        yield p + (0, 1)
    if p.x:
        yield p - (1, 0)
    if p.y:
        yield p - (0, 1)

#print('\n'.join([''.join([str(get_risk(Point(x, y))) for x in range(5 * len(board[0]))]) for y in range(5 * len(board))]))

uid = 0
fringe = [(start.distance(end), 0, uid, start)]
seen = set([start])
while fringe:
    _, risk, _, pos = heappop(fringe)
    if pos == end:
        print(risk)
        break
    for neigh in filter(lambda x: x not in seen, adjacents(pos)):
        seen.add(neigh)
        acc_risk = risk + get_risk(neigh)
        uid += 1
        heappush(fringe, (acc_risk + end.distance(neigh), acc_risk, uid, neigh))
