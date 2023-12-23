from utils import lines, Point
from collections import namedtuple, deque

def parse(lines) -> dict[Point, str]:
    board = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '#':
                board[Point(x,y)] = c
    return board

Node = namedtuple('Node', ['pos', 'been', 'length'])

DEP = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}

def find_longest(board: dict[Point, str]):
    start = min(board, key = Point.getY)
    end = max(board, key = Point.getY)
    fringe = deque([Node(pos = start,
                         been = set([start]),
                         length = 0)])
    hikes = []
    while fringe:
        cur = fringe.popleft()
        if cur.pos == end:
            hikes.append(cur.length)
            continue
        for neigh in filter((board.keys() - cur.been).__contains__, cur.pos.neighbors()):
            if board[neigh] == '.':
                fringe.append(Node(pos = neigh,
                                   been = cur.been | set([neigh]),
                                   length = cur.length + 1))
            else:
                nex = neigh + DEP[board[neigh]]
                if nex not in cur.been:
                    fringe.append(Node(pos = nex,
                                       been = cur.been | set([neigh, nex]),
                                       length = cur.length + 2))
    print(sorted(hikes))
    return max(hikes)

if __name__ == '__main__':
    print(find_longest(parse(lines())))
