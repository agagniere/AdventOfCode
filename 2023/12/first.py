from functools import cache

from utils import lines

# Constants

OPERATIONAL = '.'
BROKEN = '#'
UNKNOWN = '?'

DOUBT = set([BROKEN, UNKNOWN])

# Functions

def parse(line: str) -> (str, tuple[int]):
    springs, groups = line.split()
    return springs, tuple(int(g) for g in groups.split(','))

@cache
def count_arrangements(springs: str, groups: tuple) -> int:
    if len(groups) == 0:
        return BROKEN not in springs

    skip = 0
    while skip < len(springs) and springs[skip] == OPERATIONAL:
        skip += 1
    if skip == len(springs):
        return 0

    # If we have a broken spring, we MUST consume the first group
    end = skip
    while end < len(springs) and end - skip < groups[0] and springs[end] in DOUBT:
        end += 1
    if end == len(springs):
        broken = len(groups) == 1 and end - skip == groups[0]
    elif end - skip != groups[0] or springs[end] == BROKEN:
        broken = 0
    else:
        broken = count_arrangements(springs[end + 1:], groups[1:])
    if springs[skip] == BROKEN:
        return broken

    return broken + count_arrangements(springs[skip + 1:], groups)

def part1(lines) -> int:
    return sum(count_arrangements(*parse(line)) for line in lines)

# Entrypoint

if __name__ == '__main__':
    print(part1(lines()))

# ------------------------------

from unittest import TestCase


class TestDay12_1(TestCase):

    def test_single(self):
        cases = [
            ('# 1', 1),
            ('.# 1', 1),
            ('#. 1', 1),
            ('## 2', 1),
            ('#.#.### 1,1,3', 1),
            ('.#...#....###. 1,1,3', 1),
            ('.#.###.#.###### 1,3,1,6', 1),
            ('####.#...#... 4,1,1', 1),
            ('#....######..#####. 1,6,5', 1),
            ('.###.##....# 3,2,1', 1),
            ('? 1', 1),
            ('?. 1', 1),
            ('?# 1', 1),
            ('#? 1', 1),
            ('?? 1', 2),
            ('####? 5', 1),
            ('?#### 5', 1),
            ('?###? 5', 1),
            ('?#?#? 5', 1),
            ('?#??? 5', 1),
            ('????? 5', 1),
            ('.?# 1', 1),
            ('.?# 2', 1),
            ('# 1', 1),
            ('#?# 1,1', 1),
            ('#.? 1,1', 1),
            ('?.? 1,1', 1),
            ('#?? 1,1', 1),
            ('??# 1,1', 1),
            ('??? 1,1', 1),
            ('???.### 1,1,3', 1),
            ('.??..??...?##. 1,1,3', 4),
            ('?#?#?#?#?#?#?#? 1,3,1,6', 1),
            ('????.#...#... 4,1,1', 1),
            ('????.######..#####. 1,6,5', 4),
            ('???? 1', 4),
            ('##.???? 2,1', 4),
            ('##????? 2,1', 4),
            ('##.??? 2,1', 3),
            ('##???? 2,1', 3),
            ('##.?? 2,1', 2),
            ('##??? 2,1', 2),
            ('##.? 2,1', 1),
            ('##?? 2,1', 1),
            ('#??? 2,1', 1),
            ('.??? 2,1', 0),
            ('???? 2,1', 1),
            ('.???? 2,1', 1),
            ('#???? 2,1', 2),
            ('????? 2,1', 3),
            ('.????? 2,1', 3),
            ('#????? 2,1', 3),
            ('?????? 2,1', 6),
            ('.?????? 2,1', 6),
            ('#?????? 2,1', 4),
            ('??????? 2,1', 10),
            ('?###???????? 3,2,1', 10),
            ('???.###????.### 1,1,3,1,1,3', 1),
            ('???.###????.###????.### 1,1,3,1,1,3,1,1,3', 1)
        ]
        for line, expected in cases:
            with self.subTest(line):
                self.assertEqual(count_arrangements(*parse(line)), expected)

    def test_part1(self):
        sample = [
            '???.### 1,1,3',
            '.??..??...?##. 1,1,3',
            '?#?#?#?#?#?#?#? 1,3,1,6',
            '????.#...#... 4,1,1',
            '????.######..#####. 1,6,5',
            '?###???????? 3,2,1'
        ]
        self.assertEqual(part1(sample), 21)
