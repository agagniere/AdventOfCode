import sys
from itertools import zip_longest

lines = map(str.strip, sys.stdin.readlines())

def priority(c):
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

def common(*sets):
    return next(iter(set.intersection(*map(set, sets))))

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
