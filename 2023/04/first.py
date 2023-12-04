from utils import lines


def toIntegerSet(string: str) -> set[int]:
    "Converts '  1 21 53 59 44 ' to {1, 21, 53, 59, 44}"
    return set(int(x) for x in string.split(' ') if x)

def score(line: str) -> int:
    "Computes the number of points the card is worth"
    want, have = map(toIntegerSet, line.split(':')[1].split('|'))
    win = want & have
    return 1 << (len(win) - 1) if win else 0

if __name__ == '__main__':
    print(sum(map(score, lines())))

# ------------------------------

from unittest import TestCase

class TestDay4_1(TestCase):

    def test_parsing(self):
        cases = {
            '': set(),
            '42': {42},
            '7 2 5': {7, 2, 5},
            '41 48 83 86 17': {41, 48, 83, 86, 17},
            ' 83 86  6 31 17  9 48 53': {83, 86, 6, 31, 17, 9, 48, 53},
            '  1 21 53 59 44 ': {1, 21, 53, 59, 44}
        }
        for input_string, expected_set in cases.items():
            with self.subTest(input_string):
                self.assertEqual(toIntegerSet(input_string), expected_set)

    def test_score(self):
        cases = {
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53': 8,
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19': 2,
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1': 2,
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83': 1,
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36': 0,
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11': 0
        }
        for input_string, expected in cases.items():
            with self.subTest(input_string):
                self.assertEqual(score(input_string), expected)
