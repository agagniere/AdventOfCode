import math

def lines():
    while True:
        try:
            yield input()
        except:
            break

def solve(program :list):
    X = 1
    cycles = 0
    for line in program:
        yield cycles, X
        if line != 'noop':
            cycles += 1
            yield cycles, X
            X += int(line.split()[1])
        cycles += 1
