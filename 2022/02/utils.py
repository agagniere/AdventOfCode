import sys

lines = map(str.strip, sys.stdin.readlines())

def convert(letter):
    return 'ABCXYZ'.index(letter) % 3

def score(opponent, me):
    return me + 1 + 3 * ((me + 4 - opponent) % 3)
