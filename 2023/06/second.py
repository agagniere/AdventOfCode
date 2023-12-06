from first import simulate, number_of_ways_to_win


def parse(line: str) -> list[str]:
    return int(''.join(filter(str.isdigit, line)))

if __name__ == '__main__':
    time = parse(input())
    record = parse(input())
    print(number_of_ways_to_win(time, record))

# ------------------------------

from unittest import TestCase

class TestDay6_2(TestCase):

    def test_parse(self):
        cases = {
            'Time:      7  15   30': 71530,
            'Distance:  9  40  200': 940200
        }
        for string, expected in cases.items():
            with self.subTest(string):
                self.assertEqual(parse(string), expected)

    def test_part1(self):
        time = 71530
        record = 940200
        self.assertEqual(number_of_ways_to_win(time, record), 71503)
