from first import DISPLAY, TILES, find_loop, parse
from utils import Point, lines


# Constants

INFER_TILE = {tuple(sorted(pair)): c for c, pair in TILES.items()}

# Functions

def restore_start(start: Point, loop: set[Point]) -> str:
    return INFER_TILE[tuple(sorted(n - start for n in start.neighbors() if n in loop))]

def enclosed(lines, loop: set[Point]) -> set[Point]:
    result = []
    inside = False
    pending = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x, y) in loop:
                if c in 'FL':
                    pending = 'FL'.index(c)
                elif c in '7J|' and '7J|'.index(c) != pending:
                    inside = not inside
            elif inside:
                result.append((x,y))
    return set(result)

def part2(lines, visualize = False):
    board = list(lines)
    board_map, start = parse(board)
    loop = find_loop(board_map, start)
    board[start.y] = board[start.y][:start.x] + restore_start(start, loop[start]) + board[start.y][start.x + 1:]
    inside = enclosed(board, loop)
    if visualize:
        for y, line in enumerate(board):
            print('\033[37;40m' + ''.join(DISPLAY[c] if (x,y) in loop else '\033[97;1;5m*\033[0;40;37m' if (x,y) in inside else ' '
                                          for x, c in enumerate(line)) + '\033[0m')
    return len(inside)

# Entrypoint

if __name__ == '__main__':
    print(part2(lines(), True))

# ------------------------------

from unittest import TestCase

class TestDay10_2(TestCase):

    samples = [
        [
            '7-F7-',
            '.FJ|7',
            'SJLL7',
            '|F--J',
            'LJ.LJ'
        ],[
            '..........',
            '.S------7.',
            '.|F----7|.',
            '.||OOOO||.',
            '.||OOOO||.',
            '.|L-7F-J|.',
            '.|II||II|.',
            '.L--JL--J.',
            '..........'
        ],[
            '.F----7F7F7F7F-7....',
            '.|F--7||||||||FJ....',
            '.||.FJ||||||||L7....',
            'FJL7L7LJLJ||LJ.L-7..',
            'L--J.L7...LJS7F-7L7.',
            '....F-J..F7FJ|L7L7L7',
            '....L7.F7||L7|.L7L7|',
            '.....|FJLJ|FJ|F7|.LJ',
            '....FJL-7.||.||||...',
            '....L---J.LJ.LJLJ...'
        ],[
            'FF7FSF7F7F7F7F7F---7',
            'L|LJ||||||||||||F--J',
            'FL-7LJLJ||||||LJL-77',
            'F--JF--7||LJLJ7F7FJ-',
            'L---JF-JLJ.||-FJLJJ7',
            '|F|F-JF---7F7-L7L|7|',
            '|FFJF7L7F-JF7|JL---7',
            '7-L-JL7||F7|L7F-7F7|',
            'L.L7LFJ|||||FJL7||LJ',
            'L7JLJL-JLJLJL--JLJ.L'
        ]
    ]

    enclosed_tiles = [1, 4, 8, 10]

    def test_restore(self):
        cases = [
            (Point(1,1), {(2,1), (1,2)}, 'F'),
            (Point(0,2), {(0,1), (0,3)}, '|'),
            (Point(2,2), {(2,1), (1,2)}, 'J'),
            (Point(3,7), {(2,7), (3,8)}, '7'),
            (Point(7,3), {(7,2), (8,3)}, 'L'),
        ]
        for start, neigbors, expected in cases:
            with self.subTest(expected):
                self.assertEqual(restore_start(start, neigbors), expected)

    def test_part2(self):
        for lines, expected in zip(self.samples, self.enclosed_tiles):
            with self.subTest(expected):
                self.assertEqual(part2(lines), expected)
