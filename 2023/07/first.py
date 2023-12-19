from collections import Counter, namedtuple

from utils import lines

Hand = namedtuple('Hand', ['type', 'card_values', 'bid'])

class CamelCards:
    CARDS = "23456789TJQKA"
    VALUE = {c: i for i,c in enumerate(CARDS, 2)}

    @classmethod
    def hand_type(cls, hand: str) -> tuple:
        return tuple(sorted(Counter(hand).values(), reverse=True)[:2])

    @classmethod
    def parse(cls, line: str) -> Hand:
        hand, bid = line.split()
        return Hand(cls.hand_type(hand),
                    [cls.VALUE[card] for card in hand],
                    int(bid))

    @classmethod
    def wins(cls, rank: int, hand: Hand) -> int:
        return rank * hand.bid

    @classmethod
    def total_winnings(cls, lines) -> int:
        hands = sorted(cls.parse(line) for line in lines)
        return sum(cls.wins(i, hand) for i, hand in enumerate(hands, 1))

if __name__ == '__main__':
    print(CamelCards.total_winnings(lines()))

# ------------------------------

from unittest import TestCase


class TestDay7_1(TestCase):

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
            'KTJJT': (2, 2),
            'T55J5': (3, 1),
            'QQQJA': (3, 1)
        }
        for hand, expected in cases.items():
            with self.subTest(hand):
                self.assertEqual(CamelCards.hand_type(hand), expected)

    def test_parse(self):
        cases = {
            '32T3K 765': Hand((2, 1), [3, 2, 10, 3, 13], 765),
            'T55J5 684': Hand((3, 1), [10, 5, 5, 11, 5], 684),
            'KK677 28': Hand((2, 2), [13, 13, 6, 7, 7], 28),
            'KTJJT 220': Hand((2, 2), [13, 10, 11, 11, 10], 220),
            'QQQJA 483': Hand((3, 1), [12, 12, 12, 11, 14], 483),
        }
        for line, expected in cases.items():
            with self.subTest(line):
                self.assertEqual(CamelCards.parse(line), expected)

    def test_part1(self):
        sample = [
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'
        ]
        self.assertEqual(CamelCards.total_winnings(sample), 6440)
