from utils import *

def single(line):
    return score(*map(convert, line.split()))

print(sum(map(single, lines)))
