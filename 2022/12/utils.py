from collections import deque

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def taxi_distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def neighbors(self):
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            yield self + d

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

def store_lines():
    return list(iter(lines()))

def extract_start_end(board: list):
    S = E = None
    for y, row in enumerate(board):
        if 'S' in row or 'E' in row:
            for x, c in enumerate(row):
                if c == 'S':
                    S = Point(x, y)
                elif c == 'E':
                    E = Point(x, y)
    return S, E

def min_steps_to_reach(starts: list, end: Point, board: list) -> int:
    fringe = deque([(0, 0, s) for s in starts])
    seen = set(starts)
    while fringe:
        cost, height, pos = fringe.popleft()
        for neigh in pos.neighbors():
            if (neigh in seen
                or neigh.y not in range(len(board))
                or neigh.x not in range(len(board[neigh.y]))):
                continue
            if board[neigh.y][neigh.x] == 'E':
                if height >= 24:
                    return cost + 1
                neigh_height = 25
            else:
                neigh_height = ord(board[neigh.y][neigh.x]) - ord('a')
            if neigh_height <= height + 1:
                seen.add(neigh)
                fringe.append( (cost + 1, neigh_height, neigh) )
    return +inf
