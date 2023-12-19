from utils import lines


def parse(line: str) -> list[int]:
    return list(map(int, line.split()))

def extrapolate(sequence: list[int]) -> int:
    diff = [b - a for a, b in zip(sequence, sequence[1:])]
    if len(set(diff)) == 1:
        return sequence[-1] + diff[0]
    return sequence[-1] + extrapolate(diff)

def part1(lines) -> int:
    return sum(extrapolate(parse(line)) for line in lines)

if __name__ == '__main__':
    print(part1(lines()))

# ------------------------------

from unittest import TestCase


class TestDay9_1(TestCase):

    sample = {
        '0 3 6 9 12 15': 18,
        '1 3 6 10 15 21': 28,
        '10 13 16 21 30 45': 68,
    }

    def test_extrapolate(self):
        for line, expected in self.sample.items():
            with self.subTest(line):
                self.assertEqual(extrapolate(parse(line)), expected)

    def test_part1(self):
        self.assertEqual(part1(self.sample.keys()), 114)
