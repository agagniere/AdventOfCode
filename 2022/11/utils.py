import sys
from math import prod
import math

def make_operation(string):
    if string == 'old * old':
        return lambda x: x**2
    _, op, s = string.split()
    k = int(s)
    return {'+': k.__add__, '*': k.__mul__}[op]

class Monkey:

    def __init__(self, ini):
        self.throw = [-1, -1]
        for line in ini:
            key, value = map(str.strip, line.split(':'))
            if key.startswith('Monkey'):
                self.name = int(key.split()[1])
            elif key.startswith('Starting'):
                self.items = list(map(int, value.split(', ')))
            elif key == 'Operation':
                self.operation = make_operation(value.split('=')[1].strip())
            elif key == 'Test':
                self.divisor = int(value.split()[2])
            elif key.startswith('If'):
                self.throw[key.split()[1] == 'true'] = int(value.split()[3])
            else:
                raise Error(f'Unrecognized key : "{key}"')
        self.count = 0
        print('Created :', self)

    def __str__(self):
        return f'({self.name}, {self.divisor:2}, {self.items})'

    def exec(self, monkeys :list, lcm :int, divide :bool):
        for item in self.items:
            self.count += 1
            item = self.operation(item)
            if divide:
                item //= 3
            item %= lcm
            monkeys[self.throw[item % self.divisor == 0]].items.append(item)
        self.items = []

def lines():
    while True:
        try:
            yield input()
        except:
            break

def non_empty_line_group(iterable):
    acc = []
    for line in iterable:
        if line:
            acc.append(line)
        elif acc:
            yield acc
            acc = []
    if acc:
        yield acc

def run_rounds(monkeys: list, n: int, divide: bool = False) -> list:
    lcm = prod(monkey.divisor for monkey in monkeys)
    for _ in range(n):
        for monkey in monkeys:
            monkey.exec(monkeys, lcm, divide)
    return monkeys
