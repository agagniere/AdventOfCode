from collections import deque

from utils import Point, lines
from first import MOVE


def parse_edge(lines) -> list[Point]:
    pos = Point(0, 0)
    poly = [pos]
    count = 0
    for line in lines:
        direction, length, color = line.split()
        length = int(color[2:-2], 16)
        direction = "RDLU"[int(color[-2])]
        pos += MOVE[direction] * int(length)
        poly.append(pos)
        count += int(length)
    return poly, count

def polygon_area(poly: list[Point]) -> int:
    return abs(sum(a.x * b.y - b.x * a.y for a, b in zip(poly[:-1], poly[1:])) / 2)

if __name__ == '__main__':
    edge, count = parse_edge(lines())
    A = polygon_area(edge)
    print(A + count // 2 + 1)
