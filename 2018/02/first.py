from collections import Counter
from math import prod
from functools import reduce

from utils import lines, tuple_sum

def part1_single(line: str) -> (bool, bool):
    inverse = {v:k for k,v in Counter(line).items()}
    return 2 in inverse, 3 in inverse

def part1(lines) -> int:
    return prod(reduce(tuple_sum, map(part1_single, lines)))

if __name__ == '__main__':
    print(part1(lines()))

# ------------------------------

from unittest import TestCase

class TestDay2_1(TestCase):

    def test_part1(self):
        cases = {
            'abcdef': (False, False),
            'bababc': (True, True),
            'abbcde': (True, False),
            'abcccd': (False, True),
            'aabcdd': (True, False),
            'abcdee': (True, False),
            'ababab': (False, True),
        }
        for string, expected in cases.items():
            with self.subTest(input=string, expected=expected):
                self.assertEqual(part1_single(string), expected)
        self.assertEqual(part1(cases.keys()), 12)
