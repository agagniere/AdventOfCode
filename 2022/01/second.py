from utils import *

print(sum(sorted(map(sum, split(lines)))[-3:]))
