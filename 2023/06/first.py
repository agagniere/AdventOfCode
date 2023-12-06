from math import prod


def parse(line: str) -> list[str]:
    return [int(x) for x in line.split(':')[1].split()]

def simulate(time_limit: int, duration_held: int) -> int:
    remaining = time_limit - duration_held
    return duration_held * remaining

def number_of_ways_to_win(time_limit: int, record: int) -> int:
    return sum([simulate(time_limit, hold) > record for hold in range(time_limit)])

def part1(time_limits: list[int], records: list[int]) -> int:
    return prod(number_of_ways_to_win(limit, record) for limit, record in zip(time_limits, records))

if __name__ == '__main__':
    times = parse(input())
    records = parse(input())
    print(part1(times, records))

# ------------------------------

from unittest import TestCase

class TestDay6_1(TestCase):

    def test_parse(self):
        cases = {
            'Time:      7  15   30': [7, 15, 30],
            'Distance:  9  40  200': [9, 40, 200]
        }
        for string, expected in cases.items():
            with self.subTest(string):
                self.assertEqual(parse(string), expected)

    def test_simulate(self):
        cases = {
            (7, 0): 0,
            (7, 1): 6,
            (7, 2): 10,
            (7, 3): 12,
            (7, 4): 12,
            (7, 5): 10,
            (7, 6): 6,
            (7, 7): 0,
        }
        for pair, expected in cases.items():
            with self.subTest(time_limit=pair[0], button_held_for=pair[1]):
                self.assertEqual(simulate(*pair), expected)

    def test_counter(self):
        cases = {
            (7, 9): 4,
            (15, 40): 8,
            (30, 200): 9,
        }
        for pair, expected in cases.items():
            with self.subTest(time_limit=pair[0], current_record=pair[1]):
                self.assertEqual(number_of_ways_to_win(*pair), expected)

    def test_part1(self):
        times = [7, 15, 30]
        records = [9, 40, 200]
        self.assertEqual(part1(times, records), 288)
