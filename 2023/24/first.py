from utils import lines, Point
from collections import namedtuple
from collections.abc import Iterable

Hail = namedtuple('Hail', ['pos', 'vel'])

class MyRange:

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __contains__(self, x):
        return self.min <= x and x <= self.max

def parse(lines: Iterable[str]) -> Iterable[Point]:
    for line in lines:
        yield Hail(*(Point(*map(int, half.split(', '))) for half in line.split(' @ ')))

def ray_intersection(A: Hail, B: Hail) -> Point:
    x = B.pos.x - A.pos.x
    y = B.pos.y - A.pos.y
    det = B.vel.x * A.vel.y - B.vel.y * A.vel.x
    if not det:
        return None
    u = (y * B.vel.x - x * B.vel.y) / det
    v = (y * A.vel.x - x * A.vel.y) / det
    if u >= 0 and v >= 0:
        return A.pos + (A.vel * u)

def part1(lines: Iterable[str], bounds: MyRange) -> int:
    count = 0
    hails = list(parse(lines))
    for i, A in enumerate(hails[1:], 1):
        for B in hails[:i]:
            I = ray_intersection(A, B)
            count += I is not None and I.x in bounds and I.y in bounds
    return count

if __name__ == '__main__':
    print(part1(lines(), MyRange(200000000000000, 400000000000000)))
