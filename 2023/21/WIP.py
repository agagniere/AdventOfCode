from collections import defaultdict
from utils import Point, lines

def parse(lines):
    garden = set()
    start = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '#':
                garden.add((x,y))
                if c == 'S':
                    start = Point(x, y)
    return garden, start, Point(x + 1, y + 1)

def part2(garden, start, dim, steps):
    previous = {start: set([Point(0,0)])}
    for i in range(steps):
        reached = defaultdict(set)
        for p, planes in previous.items():
            for n in p.neighbors():
                if n in garden:
                    reached[n] |= planes
                elif (n.x % dim.x, n.y % dim.y) in garden:
                    D = (n.x // dim.x, n.y // dim.y)
                    reached[Point(n.x % dim.x, n.y % dim.y)] |= set([p + D for p in planes])
        print(i, sum(map(len, previous.values())), previous.get(start, []))
        previous = reached
    return sum(map(len, previous.values()))

if __name__ == '__main__':
    print(part2(*parse(lines()), 40))
