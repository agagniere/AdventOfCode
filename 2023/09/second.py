from first import parse
from utils import lines


def extrapolate(sequence: list[int]) -> int:
    diff = [b - a for a, b in zip(sequence, sequence[1:])]
    if len(set(diff)) == 1:
        return sequence[0] - diff[0]
    return sequence[0] - extrapolate(diff)

def part2(lines) -> int:
    return sum(extrapolate(parse(line)) for line in lines)

if __name__ == '__main__':
    print(part2(lines()))

# ------------------------------

from unittest import TestCase


class TestDay9_2(TestCase):

    sample = {
        '0 3 6 9 12 15': -3,
        '1 3 6 10 15 21': 0,
        '10 13 16 21 30 45': 5,
    }

    def test_extrapolate(self):
        for line, expected in self.sample.items():
            with self.subTest(line):
                self.assertEqual(extrapolate(parse(line)), expected)

    def test_part1(self):
        self.assertEqual(part2(self.sample.keys()), 2)
