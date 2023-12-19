from utils import Point, lines

# Constants

TILES = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'F': ((0, 1), (1, 0)),
    '7': ((0, 1), (-1, 0)),
    'J': ((0, -1), (-1, 0)),
    'L': ((0, -1), (1, 0)),
}

DISPLAY = {
    '-': chr(0x2500),
    '|': chr(0x2502),
    'L': chr(0x2570),
    'F': chr(0x256d),
    '7': chr(0x256e),
    'J': chr(0x256f),
}

# Functions

def next_tile(incoming_direction: Point, cell: str) -> Point | None:
    a, b = TILES[cell]
    if incoming_direction == a:
        return b
    if incoming_direction == b:
        return a
    return None

def parse(lines) -> tuple[dict[Point, str], Point]:
    result = dict()
    start = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            result[x,y] = c
            if c == 'S':
                start = Point(x,y)
    return result, start

def find_loop(board: dict[Point, str], start: Point) -> dict[Point, Point]:
    for neighbor in filter(board.__contains__, start.neighbors()):
        loop = dict()
        previous = start
        current = neighbor
        while board[current] != '.':
            loop[current] = previous
            delta = next_tile(previous - current, board[current])
            if not delta:
                break
            current, previous = current + delta, current
            if current == start:
                loop[start] = (neighbor, previous)
                return loop

def part1(lines) -> int:
    return len(find_loop(*parse(lines))) // 2

def visualize(lines):
    GREY_ON_BLACK = '\033[40;37m'
    BOLD_WHITE = '\033[97;1m'

    loop = find_loop(*parse(lines))
    for y, line in enumerate(lines):
        print(GREY_ON_BLACK + ''.join(DISPLAY.get(c, BOLD_WHITE + '*' + GREY_ON_BLACK) if (x,y) in loop else ' ' for x, c in enumerate(line)) + '\033[0m')

# Entrypoint

if __name__ == '__main__':
    board = list(lines())
    visualize(board)
    print(part1(board))

# ------------------------------

from unittest import TestCase


class TestDay10_1(TestCase):

    samples = [
        [
            '-L|F7',
            '7S-7|',
            'L|7||',
            '-L-J|',
            'L|-JF'
        ],[
            '7-F7-',
            '.FJ|7',
            'SJLL7',
            '|F--J',
            'LJ.LJ'
        ]
    ]

    start_positions = [(1,1), (0,2)]
    loops_demilength = [4, 8]

    def test_parse(self):
        for lines, expected in zip(self.samples, self.start_positions):
            with self.subTest(expected):
                board, start = parse(lines)
                self.assertEqual(start, expected)

    def test_next(self):
        cases = {
            ((-1, 0), 'F'): None,
            ((0, -1), 'F'): None,
            ((1, 0), 'F'): (0, 1),
            ((0, 1), 'F'): (1, 0),
            ((0, 1), '|'): (0, -1),
            ((0, -1), '|'): (0, 1),
            ((1, 0), '|'): None,
            ((1, 0), '-'): (-1, 0),
            ((0, -1), '-'): None,
            ((0, -1), 'J'): (-1, 0),
            ((0, -1), '7'): None,
            ((0, -1), 'L'): (1, 0),
        }
        for pair, expected in cases.items():
            with self.subTest(pair):
                self.assertEqual(next_tile(*pair), expected)

    def test_part1(self):
        for lines, expected in zip(self.samples, self.loops_demilength):
            with self.subTest(expected):
                self.assertEqual(part1(lines), expected)
