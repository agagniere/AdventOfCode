from collections import defaultdict

from first import count_energy
from utils import Point, lines


def part2(lines: list[str]) -> int:
    results = []
    for y in range(len(lines)):
        results += [
            count_energy(lines, Point(0, y), (1, 0)),
            count_energy(lines, Point(len(lines[0]) - 1, y), (-1, 0))
        ]
    for x in range(len(lines[0])):
        results += [
            count_energy(lines, Point(x, 0), (0, 1)),
            count_energy(lines, Point(x, len(lines) - 1), (0, -1))
        ]
    return max(results)

if __name__ == '__main__':
    print(part2(list(lines())))
