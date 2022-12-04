from utils import *

def single(line):
    H = len(line) // 2
    return priority(common(line[:H], line[H:]))

print(sum(map(single, lines)))
