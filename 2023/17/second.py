from collections import Counter, defaultdict, deque, namedtuple
from heapq import heappop, heappush

from first import Node, parse
from utils import Point, lines


def crucible(board, end):
    h = end.taxi_distance

    visited = set()
    best = {}

    fringe = [Node(pos = Point(0, 0),
                   prev_delta = Point(0, 0),
                   histo = [(0, 0)],
                   cost = 0,
                   est_total = h((0,0)))]
    while fringe:
        p = heappop(fringe)
        if p in visited:
            continue
        if p.pos == end and p.cost == best[p]:
            print(f'{"Cells":15}: {end.x * end.y:7}\n{"Node visited":15}: {len(visited):7}\n{"Left in fringe":15}: {len(fringe):7}')
            been = set(p.histo)
            for y in range(end.y + 1):
                print(''.join('O' if (x,y) in been else ' ' for x in range(end.x + 1)))
            return p.cost
        visited.add(p)

        for dep in [Point(1, 0), Point(-1, 0)] if p.prev_delta[0] == 0 else [Point(0, 1), Point(0, -1)]:
            cost = 0
            histo = []
            for i in range(1, 11):
                n = p.pos + (dep * i)
                if n not in board:
                    break
                cost += board[n]
                histo.append(n)
                if i < 4:
                    continue
                N = Node(pos = n,
                         prev_delta = -dep,
                         histo = p.histo + histo,
                         cost = p.cost + cost,
                         est_total = p.cost + cost + h(n))
                if N not in visited and (N not in best or N.cost < best[N]):
                    best[N] = N.cost
                    heappush(fringe, N)


if __name__ == '__main__':
    print(crucible(*parse(lines())))
