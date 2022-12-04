from utils import *

def single(line):
    A, B = sorted(map(create_range, line.split(',')), key=lambda x:x.start)
    return B.start < A.stop

print(sum(map(single, lines)))
