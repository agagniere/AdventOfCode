from utils import *
from collections import deque

def solve(droplets: list) -> int:
    lava = set(droplets)
    border = set()
    for d in droplets:
        border |= set(n for n in d.neighbors() if n not in lava)
    start = min(border, key = Point.getX)
    seen = set([start])
    fringe = deque([start])
    faces = 0
    while fringe:
        current = fringe.popleft()
        for n in current.neighbors():
            if n in lava:
                faces += 1
            elif n in border and n not in seen:
                seen.add(n)
                fringe.append(n)
            else:
                for jump in n.neighbors():
                    if jump in border and jump not in seen:
                        seen.add(jump)
                        fringe.append(jump)
    return faces

print(solve(parse(lines())))
