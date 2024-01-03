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
    return garden, start

def part1(garden, start, steps):
    previous = [start]
    for _ in range(steps):
        reached = set()
        for p in previous:
            reached |= set(filter(garden.__contains__, p.neighbors()))
        print(len(reached))
        previous = reached
    return len(previous)

if __name__ == '__main__':
    print(part1(*parse(lines()), 64))
