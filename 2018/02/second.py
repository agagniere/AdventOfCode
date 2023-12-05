from utils import lines

def part2_single(a: str, b: str) -> int:
    result = 0
    for c, d in zip(a, b):
        result += c != d
    return result

def part2(lines) -> str:
    for i, a in enumerate(lines):
        for b in lines[:i]:
            if part2_single(a, b) == 1:
                return ''.join(c for k, c in enumerate(a) if b[k] == c)
    return ''

if __name__ == '__main__':
    print(part2(lines()))

# ------------------------------

from unittest import TestCase

class TestDay2(TestCase):

    def test_part2_single(self):
        cases = {
            ('abcde', 'axcye'): 2,
            ('abxde', 'abcye'): 2,
            ('abcde', 'obcda'): 2,
            ('abcce', 'dcbea'): 5,
            ('abcce', 'dccea'): 4,
            ('fghij', 'fguij'): 1,
        }
        for pair, expected in cases.items():
            with self.subTest(pair):
                self.assertEqual(part2_single(*pair), expected)
    def test_part2(self):
        sample = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ]
        self.assertEqual(part2(sample), 'fgij')
