from utils import lines, Point
from collections import Counter
from enum import IntEnum, auto
from functools import cache

@cache
def tilt_left(row: str) -> str:
    previous = 0
    result = {}
    for x, c in enumerate(row):
        if c == '#':
            previous = x + 1
            result[x] = c
        elif c == 'O':
            result[previous] = c
            previous += 1
    return ''.join(result.get(x, '.') for x in range(len(row)))

def load_left(col: str) -> int:
    result = 0
    for x, c in enumerate(col):
        if c == 'O':
            result += len(col) - x
    return result

def cycle(lines: list[str], times: int):
    seen = {} # index from state
    store = {} # state from index
    i = 0
    prev = list(reversed([''.join(col) for col in zip(*lines)]))
    while i < times:
        N = [tilt_left(col) for col in prev]
        W = [tilt_left(''.join(row)) for row in zip(*N[::-1])]
        S = [tilt_left(''.join(col)) for col in zip(*W[::-1])]
        E = [tilt_left(''.join(row)) for row in zip(*S[::-1])]
        prev = tuple(''.join(col) for col in zip(*E[::-1]))
        i += 1

        if prev in seen:
            start = seen[prev]
            length = i - seen[prev]
            goal = (times - start) % length
            print(f'Found a loop of length {length}, starting from {start}')
            print(f'The {times}th cycle is at step {goal} of the loop')
            print(f'Therefore it is the same as the {start + goal}th cycle')
            return sum(load_left(col) for col in store[start + goal])
        else:
            seen[prev] = i
            store[i] = prev
    return sum(load_left(col) for col in prev)

if __name__ == '__main__':
    print(cycle(list(lines()), 1000000000))
    print(tilt_left.cache_info())
