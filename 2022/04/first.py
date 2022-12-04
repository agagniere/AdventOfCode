from utils import *

def single(line):
    A, B = sorted(map(create_range, line.split(',')), key=len)
    return A.start in B and A.stop - 1 in B

print(sum(map(single, lines)))
