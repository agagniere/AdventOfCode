from first import expand, measure_pair_distances, parse
from utils import Point, lines

# Functions

def part2(lines: list[str], factor: int = 1000000) -> int:
    return sum(measure_pair_distances(expand(*parse(lines), factor)))

# Entrypoint

if __name__ == '__main__':
    print(part2(list(lines())))

# ------------------------------

from unittest import TestCase

from first import sample


class TestDay11_2(TestCase):

    def test_part1(self):
        cases = [
            (10, 1030),
            (100, 8410)
        ]
        for scale, expected in cases:
            with self.subTest(scale):
                self.assertEqual(part2(sample, scale), expected)
