from utils import *

dirs = tree(lines())
capacity = 70000000
wanted_free = 30000000
used = dirs['/'].size
free = capacity - used
need_to_remove = wanted_free - free
print(min([d.size for d in dirs.values() if d.size >= need_to_remove]))
