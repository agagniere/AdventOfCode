from utils import lines, Point
from collections import Counter, defaultdict

def part1(lines):
    previous = defaultdict(int)
    result = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                previous[x] = y + 1
            elif c == 'O':
                result += [previous[x]]
                previous[x] += 1
    #print(dict(Counter(result)))
    return sum(y + 1 - v for v in result)

if __name__ == '__main__':
    print(part1(lines()))
