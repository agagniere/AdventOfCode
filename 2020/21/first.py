import re
from collections import namedtuple

from utils import lines

Food = namedtuple('Food', ['allergens', 'ingredients'])

form = re.compile(r'(\w+ )+\(contains (\w+)\)')

def parse(line: str) -> Food:
    ingredients, allergens = line.split('(')
    allergens = allergens.removeprefix('contains ').removesuffix(')')
    return Food(allergens.split(', '),
                set(ingredients.split()))

def allergen_free_ingredients(foods: list[Food]) -> set[str]:
    suspects = {}
    all_ingredients = set()
    for food in foods:
        all_ingredients |= food.ingredients
        for allergen in food.allergens:
            if allergen not in suspects:
                suspects[allergen] = food.ingredients.copy()
            else:
                suspects[allergen] &= food.ingredients
    innocents = all_ingredients
    for ingredients in suspects.values():
        innocents -= ingredients
    return innocents, suspects

def part1(lines):
    foods = [parse(line) for line in lines]
    allergen_free, _ = allergen_free_ingredients(foods)
    result = 0
    for food in foods:
        result += len(allergen_free & food.ingredients)
    return result

if __name__ == '__main__':
    print(part1(lines()))

# ------------------------------

from unittest import TestCase

class TestDay21_1(TestCase):
    cases = {
        'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)': Food(['dairy', 'fish'], {'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}),
        'trh fvjkl sbzzf mxmxvkd (contains dairy)': Food(['dairy'], {'trh', 'fvjkl', 'sbzzf', 'mxmxvkd'}),
        'sqjhc fvjkl (contains soy)': Food(['soy'], {'sqjhc', 'fvjkl'}),
        'sqjhc mxmxvkd sbzzf (contains fish)': Food(['fish'], {'sqjhc', 'mxmxvkd', 'sbzzf'}),
    }

    def test_parse(self):
        for line, expected in self.cases.items():
            with self.subTest(line):
                self.assertEqual(parse(line), expected)

    def test_allergen_free(self):
        self.assertEqual(allergen_free_ingredients(self.cases.values())[0], {'kfcds', 'nhms', 'sbzzf', 'trh'})

    def test_part1(self):
        self.assertEqual(part1(self.cases.keys()), 5)
