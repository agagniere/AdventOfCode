from utils import lines, debug
from collections import defaultdict
from more_itertools import grouper

from first import parser

class Range:
    def __init__(self, start, one_past_end):
        self.start = start
        self.stop = one_past_end

    def __contains__(self, element):
        return element in range(self.start, self.stop)

    def __and__(self, other):
        if self.start in other or (self.stop - 1) in other or other.start in self:
            return Range(max(self.start, other.start), min(self.stop, other.stop))
        return set()

    def __sub__(self, other):
        if self.start < other.start:
            yield Range(self.start, min(self.stop, other.start))
        if self.stop > other.stop:
            yield Range(max(self.start, other.stop), self.stop)

    def __add__(self, offset):
        return Range(self.start + offset, self.stop + offset)

    def __str__(self):
        return f'[{self.start}, {self.stop}['
    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    target = defaultdict(list)
    for start, length in grouper(map(int, input().split(':')[1].split()), 2, 'strict'):
        target['seed'].append(Range(start, start + length))

    for domain, codomain, conversions in parser(lines()):
        to_convert = target[domain]
        debug(f'f:  {domain:11} |->', codomain)
        for subdomain, delta in conversions:
            i = 0
            while i < len(to_convert):
                subset = to_convert[i]
                inter = subset & subdomain
                if inter:
                    debug(f'  {str(subset):10} -->', [inter + delta] + list(subset - subdomain))
                    target[codomain].append(inter + delta)
                    del to_convert[i]
                    to_convert += subset - subdomain
                else:
                    i += 1

        debug('remaining:', to_convert, '\n')
        target[codomain] += to_convert

    debug(target['location'])
    print(min(map(lambda x: x.start, target['location'])))
