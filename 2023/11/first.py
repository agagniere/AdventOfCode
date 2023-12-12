from utils import Point, lines

# Constants

X, Y = 0, 1

# Functions

def parse(lines: list[str]) -> (list[Point], dict[int, int]):
    galaxies = []
    empty = [0, 0]
    expand = [dict(), dict()]
    for y, line in enumerate(lines):
        if set(line) == {'.'}:
            empty[Y] += 1
            continue
        expand[Y][y] = empty[Y]
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append(Point(x, y))
    for x, column in enumerate(zip(*lines)):
        if set(column) == {'.'}:
            empty[X] += 1
        else:
            expand[X][x] = empty[X]
    return galaxies, expand

def expand(galaxies: list[Point], gaps: list[dict[int, int]], factor: int = 2) -> list[Point]:
    F = factor - 1
    return [galaxy + (gaps[X][galaxy.x] * F, gaps[Y][galaxy.y] * F) for galaxy in galaxies]

def measure_pair_distances(galaxies: list[Point]) -> list[int]:
    result = []
    for i, galaxy in enumerate(galaxies):
        for other in galaxies[:i]:
            result.append(galaxy.taxi_distance(other))
    return result

def part1(lines: list[str]) -> int:
    return sum(measure_pair_distances(expand(*parse(lines))))

# Entrypoint

if __name__ == '__main__':
    print(part1(list(lines())))

# ------------------------------

from unittest import TestCase

sample = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....'
]

class TestDay11_1(TestCase):

    expected_positions = {
        (0, 2), (0, 9), (1, 5), (3, 0),
        (4, 9), (6, 4), (7, 1), (7, 8),
        (9, 6)
    }

    expected_expansion = [
        {0:0, 1:0, 3:1, 4:1, 6:2, 7:2, 9:3 },
        {0:0, 1:0, 2:0, 4:1, 5:1, 6:1, 8:2, 9:2}
    ]

    expanded_sample = [
        '....#........',
        '.........#...',
        '#............',
        '.............',
        '.............',
        '........#....',
        '.#...........',
        '............#',
        '.............',
        '.............',
        '.........#...',
        '#....#.......'
    ]

    def test_part1(self):
        self.assertEqual(part1(sample), 374)

    def test_parse(self):
        S, E = parse(sample)
        self.assertEqual(set(S), self.expected_positions)
        self.assertEqual(E, self.expected_expansion)

    def test_expand(self):
        before = expand(*parse(sample))
        after, _ = parse(self.expanded_sample)
        self.assertEqual(set(before), set(after))

    def test_pair(self):
        pair_distances = measure_pair_distances(expand(*parse(sample)))
        self.assertEqual(len(pair_distances), 36)
        self.assertEqual(len({15, 17, 5} & set(pair_distances)), 3)
