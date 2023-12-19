import re

from utils import lines

form = re.compile(r'^(\w+) = \((\w+), (\w+)\)')

def parse_single(line: str) -> tuple[str]:
    return form.match(line).groups()

def parse(lines) -> dict[str, dict[str, str]]:
    result = dict()
    for line in lines:
        node, left, right = parse_single(line)
        result[node] = {'L': left, 'R': right}
    return result

def navigate(network: dict, instructions: str, start: str = 'AAA') -> int:
    current = start
    steps = 0
    while True:
        for direction in instructions:
            current = network[current][direction]
            steps += 1
            if current[-1] == 'Z':
                return steps

if __name__ == '__main__':
    instructions = input()
    input()
    network = parse(lines())
    print(navigate(network, instructions))

# ------------------------------

from unittest import TestCase


class TestDay8_1(TestCase):
    sample = {
        'AAA = (BBB, BBB)': ('AAA', 'BBB', 'BBB'),
        'BBB = (AAA, ZZZ)': ('BBB', 'AAA', 'ZZZ'),
        'ZZZ = (ZZZ, ZZZ)': ('ZZZ', 'ZZZ', 'ZZZ'),
    }

    sample_map = {
        'AAA': {'L': 'BBB', 'R': 'BBB'},
        'BBB': {'L': 'AAA', 'R': 'ZZZ'},
        'ZZZ': {'L': 'ZZZ', 'R': 'ZZZ'},
    }

    sample_instructions = 'LLR'

    def test_parse_single(self):
        for line, expected in self.sample.items():
            with self.subTest(line):
                self.assertEqual(parse_single(line), expected)

    def test_parse(self):
        self.assertEqual(parse(self.sample.keys()), self.sample_map)

    def test_navigate(self):
        self.assertEqual(navigate(self.sample_map, self.sample_instructions), 6)
