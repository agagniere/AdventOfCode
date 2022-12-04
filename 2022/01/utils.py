import sys

lines = map(str.strip, sys.stdin.readlines())

'''
Split list into multiple lists with no empty elements
'''
def split(L :list) -> list:
    acc = []
    for e in L:
        if e:
            acc.append(int(e))
        elif acc:
            yield acc
            acc = []
    if acc:
        yield acc
