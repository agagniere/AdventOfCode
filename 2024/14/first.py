from utils import Point, lines
import re
from math import prod

bounds = Point(101, 103)
#bounds = Point(11, 7)

class Robot:
    def __init__(self, P, V):
        self.pos = P
        self.vel = V

    def pos_after(self, sec) -> Point:
        return self.pos + self.vel * sec

    def move(self):
        self.pos += sel.vel

def parse(lines):
    R = []
    for line in lines:
        px, py, vx, vy = map(int, [m[0] for m in re.finditer(r'[+-]?\d+', line)])
        R += [Robot(Point(px, py), Point(vx, vy))]
    return R

if __name__ == "__main__":
    robots = parse(lines())
    after100 = [r.pos_after(100) for r in robots]
    quads = [0,0,0,0]
    for r in after100:
        P = r % bounds
        #print(r, P)
        if P.x < bounds.x // 2:
            if P.y < bounds.y // 2:
                quads[0] += 1
            elif P.y > bounds.y // 2:
                quads[1] += 1
        elif P.x > bounds.x // 2:
            if P.y < bounds.y // 2:
                quads[2] += 1
            elif P.y > bounds.y // 2:
                quads[3] += 1
    print(quads)
    print(prod(quads))
