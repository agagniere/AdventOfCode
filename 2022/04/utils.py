import sys
from itertools import zip_longest

lines = map(str.strip, sys.stdin.readlines())

def create_range(text):
    start, end = map(int, text.split('-'))
    return range(start, end + 1)
