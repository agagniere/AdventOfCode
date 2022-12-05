from utils import *
from collections import defaultdict

total_cost = defaultdict(int)

def single(line):
    result = set()
    p = Point(0, 0)
    cost = 0
    for direction, steps in map(lambda x: (x[0], int(x[1:])),line.split(',')):
        for _ in range(steps):
            p += delta[direction]
            cost += 1
            result.add(p)
            total_cost[p] += cost
    return result

A, B = map(single, lines)

print(total_cost[min(A & B, key = total_cost.__getitem__)])
