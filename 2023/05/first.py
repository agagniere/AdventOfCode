from collections import defaultdict

from utils import debug, lines


def parser(lines):
    "From an iterable of strings, iterate over the maps described"
    source = None
    destination = None
    conversions = []
    for line in lines:
        if not line:
            if source:
                yield source, destination, conversions
            source = None
            destination = None
            conversions = []
        elif not source:
            source, destination = line.split()[0].split('-to-')
        else:
            destination_start, source_start, length = map(int, line.split())
            delta = destination_start - source_start
            conversions.append((range(source_start, source_start + length), delta))
    if source:
        yield source, destination, conversions

if __name__ == '__main__':
    target = defaultdict(list)
    target['seed'] += map(int, input().split(':')[1].split())

    for domain, codomain, conversions in parser(lines()):
        to_convert = target[domain]
        debug(f'f:  {domain:11} |->', codomain)
        for subdomain, delta in conversions:
            for i, x in reversed(list(enumerate(to_convert))):
                if x in subdomain:
                    debug(f'  {x:13} -->', x + delta)
                    target[codomain].append(x + delta)
                    del to_convert[i]
        debug('remaining:', to_convert, '\n')
        target[codomain] += to_convert

    debug(target['location'])
    print(min(target['location']))
