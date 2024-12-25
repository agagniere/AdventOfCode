from utils import Point, lines
from collections import deque, namedtuple
from first import parse, solve

if __name__ == '__main__':
    points = parse(lines())
    fallen = set(points[:1024])
    for p in points[1024:]:
        fallen.add(p)
        if not solve(fallen):
            print(f'{p.x},{p.y}')
            break
