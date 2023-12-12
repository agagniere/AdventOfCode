from first import count_arrangements, parse
from utils import lines


def expand(springs: str, groups: tuple[int]) -> (str, tuple[int]):
    return '?'.join([springs for _ in range(5)]), groups * 5

def part2(lines) -> int:
    return sum(count_arrangements(*expand(*parse(line))) for line in lines)

if __name__ == '__main__':
    print(part2(lines()))
    print(count_arrangements.cache_info())

# ------------------------------

from unittest import TestCase


class TestDay12_1(TestCase):

    sample = {
        '???.### 1,1,3': 1,
        '.??..??...?##. 1,1,3': 16384,
        '?#?#?#?#?#?#?#? 1,3,1,6': 1,
        '????.#...#... 4,1,1': 16,
        '????.######..#####. 1,6,5': 2500,
        '?###???????? 3,2,1': 506250
    }

    def test_single(self):
        for line, expected in self.sample.items():
            with self.subTest(line):
                self.assertEqual(count_arrangements(*expand(*parse(line))), expected)

    def test_part1(self):
        self.assertEqual(part2(self.sample.keys()), 525152)
