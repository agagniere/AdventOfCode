from utils import *
from functools import cmp_to_key
from math import prod

B = store_nonempty_lines()
B = list(map(eval, B))
R = [i + 1 for i, pair in enumerate(zip(B[::2], B[1::2])) if compare(*pair) > 0]
print(R)
print(sum(R))
