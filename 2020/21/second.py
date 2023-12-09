import re
from collections import namedtuple

from first import Food, allergen_free_ingredients, parse
from utils import lines


def dangerous_ingredients(suspects: dict[str, set[str]]) -> dict[str, str]:
    result = dict()
    while suspects:
        allergen, ingredient = next(filter(lambda p:len(p[1]) == 1, suspects.items()))
        suspects.pop(allergen)
        result[allergen] = next(iter(ingredient))
        for key, value in suspects.items():
            value -= ingredient
    return result

def part2(lines):
    _, suspects = allergen_free_ingredients(parse(line) for line in lines)
    dangerous = dangerous_ingredients(suspects)
    return [ingredient for allergen, ingredient in sorted(dangerous.items())]

if __name__ == '__main__':
    print(','.join(part2(lines())))

# ------------------------------

from unittest import TestCase

class TestDay21_2(TestCase):
    sample = [
        'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
        'trh fvjkl sbzzf mxmxvkd (contains dairy)',
        'sqjhc fvjkl (contains soy)',
        'sqjhc mxmxvkd sbzzf (contains fish)'
    ]

    def test_dangerous(self):
        expected = {
            'dairy': 'mxmxvkd',
            'fish': 'sqjhc',
            'soy': 'fvjkl'
        }
        _, suspects = allergen_free_ingredients(parse(line) for line in self.sample)
        self.assertEqual(dangerous_ingredients(suspects), expected)

    def test_part2(self):
        expected = ['mxmxvkd','sqjhc','fvjkl']
        self.assertEqual(part2(self.sample), expected)
