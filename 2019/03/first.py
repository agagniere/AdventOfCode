from utils import *

def single(line):
    result = set()
    p = Point(0, 0)
    for direction, steps in map(lambda x: (x[0], int(x[1:])),line.split(',')):
        for _ in range(steps):
            p += delta[direction]
            result.add(p)
    return result

A, B = map(single, lines)

print(min(A & B, key=Point.module).module())
