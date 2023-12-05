def lines():
    while True:
        try:
            yield input()
        except:
            break

def tuple_sum(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))

# ------------------------------

from unittest import TestCase

class TestDay2_utils(TestCase):

    def test_tuple_sum(self):
        cases = {
            ((1, 2), (3, 4)): (4, 6),
            ((True, False), (True, True)): (2, 1),
            ((7, 6, 5, 4), (2, 0, 1, 3)): (9, 6, 6, 7)
        }
        for pair, expected in cases.items():
            with self.subTest(input=pair, expected=expected):
                self.assertEqual(tuple_sum(*pair), expected)
