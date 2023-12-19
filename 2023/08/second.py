import re
from math import lcm

from first import navigate, parse
from utils import lines


def ghost_solve(network: map, instructions: str) -> int:
    paths = []
    for node in network:
        if node.endswith('A'):
            paths.append(navigate(network, instructions, node))
    return lcm(*paths)

if __name__ == '__main__':
    instructions = input()
    input()
    network = parse(lines())
    print(ghost_solve(network, instructions))

# ------------------------------

from unittest import TestCase


class TestDay8_2(TestCase):
    def test_solve(self):
        sample = {
            '11A': {'L':'11B', 'R':'XXX'},
            '11B': {'L':'XXX', 'R':'11Z'},
            '11Z': {'L':'11B', 'R':'XXX'},
            '22A': {'L':'22B', 'R':'XXX'},
            '22B': {'L':'22C', 'R':'22C'},
            '22C': {'L':'22Z', 'R':'22Z'},
            '22Z': {'L':'22B', 'R':'22B'},
            'XXX': {'L':'XXX', 'R':'XXX'}
        }
        self.assertEqual(ghost_solve(sample, 'LR'), 6)
