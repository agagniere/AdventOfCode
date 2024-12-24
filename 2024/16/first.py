from utils import Point, lines, Cardinal
from collections import namedtuple, deque

def parse(lines):
    board = set()
    start = None
    end = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                continue
            if c == 'S':
                start = Point(x, y)
            elif c == 'E':
                end = Point(x, y)
            board.add((x,y))
    return board, start, end

Node = namedtuple('Node', ['pos', 'dir', 'turns', 'steps'])

def score(node: Node):
    return node.turns * 1000 + node.steps

if __name__ == '__main__':
    board, start, end = parse(lines())
    best = 999999

    seen = {}
    fringe = deque([Node(start, Cardinal.EAST, 0, 0)])
    while fringe:
        cur = fringe.popleft()
        if cur.pos == end:
            best = min(best, score(cur))
            print(score(cur))
            continue
        P = cur.pos.next(cur.dir)
        N = Node(P, cur.dir, cur.turns, cur.steps + 1)
        if P in board and ((P, cur.dir) not in seen or seen[P, cur.dir] > score(N)):
            seen[P, cur.dir] = score(N)
            fringe.append(N)
        for D in (cur.dir.next(), cur.dir.prev()):
            N = Node(cur.pos, D, cur.turns + 1, cur.steps)
            if (cur.pos, D) not in seen or seen[cur.pos, D] > score(N):
                seen[cur.pos, D] = score(N)
                fringe.append(N)
    print(best)
