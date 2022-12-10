from utils import *

acc = 0
for cycle_index, X in solve(lines()):
    n = cycle_index + 1 # The 1st cycle has index 0
    if (n - 20) % 40 == 0:
        print(n, X)
        acc += n * X
print(acc)
