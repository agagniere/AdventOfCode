from utils import *

print(sum([d.size for d in tree(lines()).values() if d.size <= 100000]))
