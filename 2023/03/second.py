from utils import lines, Point
from collections import defaultdict
from math import prod

board = list(lines())
gears = defaultdict(list)
adjacent = dict()

for y, line in enumerate(board):
    for x, c in enumerate(line):
        if c == '*':
            adjacent |= {neigh: (x,y) for neigh in Point(x, y).neighbors()}

for y, line in enumerate(board):
    number = 0
    gear = None
    for x, c in enumerate(line):
        if c.isdigit():
            number *= 10
            number += ord(c) - ord('0')
            if gear is None and (x,y) in adjacent:
                gear = adjacent[x, y]
        else:
            if gear is not None:
                gears[gear] += [number]
            number = 0
            gear = None
    if gear is not None:
        gears[gear] += [number]

print(sum(prod(gear) for gear in gears.values() if len(gear) > 1))
