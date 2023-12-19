from collections import OrderedDict, defaultdict

from first import santa_hash


def execute(instructions: list[str]):
    HASHMAP = defaultdict(OrderedDict)
    for instruction in instructions:
        if instruction[-1] == '-':
            label = instruction[:-1]
            box = HASHMAP[santa_hash(label)]
            if label in box:
                box.move_to_end(label)
                box.popitem()
        else:
            label, focal = instruction.split('=')
            HASHMAP[santa_hash(label)][label] = int(focal)
    return sum((h + 1) * sum(slot * focal for slot, (label, focal) in enumerate(box.items(), 1)) for h, box in HASHMAP.items())

if __name__ == '__main__':
    print(execute(input().split(',')))

# ------------------------------

from unittest import TestCase

from first import sample


class TestDay15_1(TestCase):

    def test_execute(self):
        self.assertEqual(execute(sample.split(',')), 145)
