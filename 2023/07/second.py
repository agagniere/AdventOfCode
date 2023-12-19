from collections import Counter

from first import CamelCards, Hand
from utils import lines


class CamelCardsVariant(CamelCards):
    CARDS = "J23456789TQKA"
    VALUE = {c: i for i,c in enumerate(CARDS, 1)}

    @classmethod
    def hand_type(cls, hand: str) -> tuple:
        histogram = Counter(hand)
        jokers = 0

        if 'J' in histogram and histogram['J'] < 5:
            jokers = histogram.pop('J')

        best = sorted(histogram.values(), reverse=True)[:2]
        best[0] += jokers
        return tuple(best)

if __name__ == '__main__':
    print(CamelCardsVariant.total_winnings(lines()))

# ------------------------------

from unittest import TestCase


class TestDay7_2(TestCase):

    def test_hand_type(self):
        cases = {
            'AAAAA': (5, ),
            'AA8AA': (4, 1),
            '23332': (3, 2),
            'TTT98': (3, 1),
            '23432': (2, 2),
            'A23A4': (2, 1),
            '23456': (1, 1),
            '33332': (4, 1),
            '2AAAA': (4, 1),
            '77888': (3, 2),
            '32T3K': (2, 1),
            'KK677': (2, 2),
            'KTJJT': (4, 1),
            'T55J5': (4, 1),
            'QQQJA': (4, 1)
        }
        for hand, expected in cases.items():
            with self.subTest(hand):
                self.assertEqual(CamelCardsVariant.hand_type(hand), expected)

    def test_parse(self):
        cases = {
            '32T3K 765': Hand((2, 1), [3, 2, 10, 3, 12], 765),
            'T55J5 684': Hand((4, 1), [10, 5, 5, 1, 5], 684),
            'KK677 28': Hand((2, 2), [12, 12, 6, 7, 7], 28),
            'KTJJT 220': Hand((4, 1), [12, 10, 1, 1, 10], 220),
            'QQQJA 483': Hand((4, 1), [11, 11, 11, 1, 13], 483),
        }
        for line, expected in cases.items():
            with self.subTest(line):
                self.assertEqual(CamelCardsVariant.parse(line), expected)

    def test_part2(self):
        sample = [
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'
        ]
        self.assertEqual(CamelCardsVariant.total_winnings(sample), 5905)
