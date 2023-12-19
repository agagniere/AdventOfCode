from functools import cache


@cache
def santa_hash(string: str) -> int:
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256
    return result

def part1(line):
    return sum(map(santa_hash, line.split(',')))

if __name__ == '__main__':
    print(part1(input()))

# ------------------------------

from unittest import TestCase

sample = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

class TestDay15_1(TestCase):

    cases = {
        'rn=1': 30,
        'cm-': 253,
        'qp=3': 97,
        'cm=2': 47,
        'qp-': 14,
        'pc=4': 180,
        'ot=9': 9,
        'ab=5': 197,
        'pc-': 48,
        'pc=6': 214,
        'ot=7': 231
    }

    def test_hash(self):
        self.assertEqual(santa_hash('HASH'), 52)
        for string, expected in self.cases.items():
            with self.subTest(string):
                self.assertEqual(santa_hash(string), expected)

    def test_part1(self):
        self.assertEqual(part1(sample), 1320)
