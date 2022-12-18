from utils import *

def solve(droplets: list) -> int:
    lava = set(droplets)
    faces = 0
    for d in droplets:
        faces += 6 - sum(1 for n in d.neighbors() if n in lava)
    return faces

print(solve(parse(lines())))
