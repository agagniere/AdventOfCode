from utils import lines, split, Point

from first import Part1

class Part2(Part1):

    @staticmethod

    def find_reflection(zone: list[str], flipped: list[tuple[str]]):
        for y, line in enumerate(zone[1:], 1):
            smudge = 0
            for x, col in enumerate(flipped):
                smudge += sum(1 for a, b in zip(col[y:], col[:y][::-1]) if a != b)
            if smudge == 1:
                return y
        return 0

if __name__ == '__main__':
    print(Part2.process(split(lines())))

# ------------------------------

from unittest import TestCase
from first import sample

class TestDay13_1(TestCase):

    expected_reflections = [(0, 3), (0, 1)]

    def test_find_reflection(self):
        for zone, expected in zip(sample, self.expected_reflections):
            with self.subTest(expected):
                self.assertEqual(Part2.find_reflection(list(zip(*zone)), zone), expected[0])
                self.assertEqual(Part2.find_reflection(zone, list(zip(*zone))), expected[1])

    def test_process(self):
        for zone, expected in zip(sample, self.expected_reflections):
            with self.subTest(expected):
                self.assertEqual(Part2.process_single(zone), expected)

    def test_part2(self):
        self.assertEqual(Part2.process(sample), 400)
