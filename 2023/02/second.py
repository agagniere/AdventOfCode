from collections import defaultdict
from math import prod

from utils import lines


def power(line):
    game, draws = line.split(': ')
    maximum = defaultdict(int)
    for draw in draws.split('; '):
        for group in draw.split(', '):
            count, color = group.split(' ')
            count = int(count)
            maximum[color] = max(maximum[color], count)
    return prod(maximum.values())

if __name__ == '__main__':
    print(sum(map(power, lines())))
