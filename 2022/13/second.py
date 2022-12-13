from utils import *
from functools import cmp_to_key
from math import prod

dividers = ['[[2]]', '[[6]]']
B = store_nonempty_lines() + dividers
B = list(map(eval, B))
B.sort(key=cmp_to_key(compare), reverse=True)
R = [i + 1 for i, line in enumerate(map(str, B)) if line in dividers]
print(R)
print(prod(R))
