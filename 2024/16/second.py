from utils import Point, lines, Cardinal
from collections import namedtuple, deque
from first import parse, score

Node = namedtuple('Node', ['pos', 'dir', 'turns', 'steps', 'been'])

if __name__ == '__main__':
    board, start, end = parse(lines())
    best = 999999
    been = set()

    seen = {}
    fringe = deque([Node(start, Cardinal.EAST, 0, 0, set([start]))])
    while fringe:
        cur = fringe.popleft()
        if cur.pos == end:
            if score(cur) > best:
                continue
            if score(cur) < best:
                best = score(cur)
                been = set()
                print(score(cur))
            been |= cur.been
            continue
        P = cur.pos.next(cur.dir)
        N = Node(P, cur.dir, cur.turns, cur.steps + 1, cur.been | set([P]))
        if P in board and ((P, cur.dir) not in seen or seen[P, cur.dir] >= score(N)):
            seen[P, cur.dir] = score(N)
            fringe.append(N)
        for D in (cur.dir.next(), cur.dir.prev()):
            N = Node(cur.pos, D, cur.turns + 1, cur.steps, cur.been)
            if (cur.pos, D) not in seen or seen[cur.pos, D] >= score(N):
                seen[cur.pos, D] = score(N)
                fringe.append(N)
    print(len(been))
