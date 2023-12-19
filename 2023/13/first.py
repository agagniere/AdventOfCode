from utils import Point, lines, split


class Part1:

    @staticmethod
    def find_reflection(zone: list[str], flipped: list[tuple[str]]):
        for y, line in enumerate(zone[1:], 1):
            for x, col in enumerate(flipped):
                if not all(a == b for a, b in zip(col[y:], col[:y][::-1])):
                    break
            else:
                return y
        return 0

    @classmethod
    def process_single(cls, zone: list[str]):
        flipped = list(zip(*zone))
        return (cls.find_reflection(flipped, zone), cls.find_reflection(zone, flipped))

    @classmethod
    def process(cls, zones: list[list[str]]) -> int:
        total = sum((cls.process_single(zone) for zone in zones), start = Point(0, 0))
        return total.x + 100 * total.y

if __name__ == '__main__':
    print(Part1.process(split(lines())))

# ------------------------------

from unittest import TestCase

sample = [
    [
        '#.##..##.',
        '..#.##.#.',
        '##......#',
        '##......#',
        '..#.##.#.',
        '..##..##.',
        '#.#.##.#.'
    ], [
        '#...##..#',
        '#....#..#',
        '..##..###',
        '#####.##.',
        '#####.##.',
        '..##..###',
        '#....#..#'
    ]
]

class TestDay13_1(TestCase):

    expected_reflections = [(5, 0), (0, 4)]

    def test_find_reflection(self):
        for zone, expected in zip(sample, self.expected_reflections):
            with self.subTest(expected):
                self.assertEqual(Part1.find_reflection(list(zip(*zone)), zone), expected[0])
                self.assertEqual(Part1.find_reflection(zone, list(zip(*zone))), expected[1])

    def test_process(self):
        for zone, expected in zip(sample, self.expected_reflections):
            with self.subTest(expected):
                self.assertEqual(Part1.process_single(zone), expected)

    def test_part1(self):
        self.assertEqual(Part1.process(sample), 405)
