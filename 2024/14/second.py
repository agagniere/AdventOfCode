from utils import Point, lines
import re
from math import prod
from collections import defaultdict

bounds = Point(101, 103)
#bounds = Point(11, 7)

class Robot:
    def __init__(self, P, V):
        self.pos = P
        self.vel = V

    def pos_after(self, sec) -> Point:
        return self.pos + self.vel * sec

    def move(self):
        self.pos += self.vel

def parse(lines):
    R = []
    for line in lines:
        px, py, vx, vy = map(int, [m[0] for m in re.finditer(r'[+-]?\d+', line)])
        R += [Robot(Point(px, py), Point(vx, vy))]
    return R

if __name__ == "__main__":
    robots = parse(lines())
    for sec in range(1, 101 * 103):
        H = defaultdict(int)
        surrounded = 0
        for r in robots:
            r.move()
            P = r.pos % bounds
            H[P] += 1
        for r in robots:
            P = r.pos % bounds
            if all(H[n] > 0 for n in P.neighbors()):
                surrounded += 1
        if (surrounded > 100):
            print('-' * 10, sec, '-' * 10)
            for y in range(bounds.y):
                print(''.join(' 123456789+'[min(H[(x,y)],10)] for x in range(bounds.x)))
