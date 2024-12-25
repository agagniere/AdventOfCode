from utils import Point, lines
from collections import deque, namedtuple

def parse(lines):
    return [Point(*map(int, line.split(','))) for line in lines]

bounds = Point(71, 71)

Node = namedtuple('Node', ['pos', 'cost'])

def solve(points):
    seen = set([(0,0)])
    been = set()
    fringe = deque([Node(Point(0,0), 0)])
    while fringe:
        cur = fringe.popleft()
        been.add(cur.pos)
        if cur.pos == bounds - (1, 1):
            return cur.cost
        for n in cur.pos.neighbors():
            if n not in bounds or n in points:
                continue
            if n not in seen:
                seen.add(n)
                fringe.append(Node(n, cur.cost + 1))
    return None
    # def draw(x, y):
    #     if (x, y) in points:
    #         return '#'
    #     if (x, y) in been:
    #         return 'O'
    #     if (x, y) in seen:
    #         return '.'
    #     return ' '
    # for y in range(bounds.y):
    #     print(''.join(draw(x, y) for x in range(bounds.x)))

if __name__ == '__main__':
    points = parse(lines())
    print(solve(set(points[:1024])))
