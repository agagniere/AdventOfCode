from utils import *

for cycle, X in solve(lines()):
    cursor = cycle % 40
    print(' #'[abs(X - cursor) <= 1],
          end = ['', '\n'][cursor == 39])
