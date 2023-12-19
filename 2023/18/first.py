from collections import deque

from utils import Point, lines

MOVE = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, -1),
    'U': (0, 1)
}

def dig_edge(lines):
    pos = Point(0, 0)
    dug = set([pos])
    for line in lines:
        direction, length, _ = line.split()
        dep = MOVE[direction]
        for _ in range(int(length)):
            pos += dep
            dug.add(pos)
    return dug

def dig_inside(edge, range_x, range_y):
    fringe = deque([Point(range_x.start, range_y.start)])
    seen = set(fringe)
    while fringe:
        P = fringe.popleft()
        for n in P.neighbors():
            if n not in seen and n not in edge and n.x in range_x and n.y in range_y:
                seen.add(n)
                fringe.append(n)
    return len(range_x) * len(range_y) - len(seen)

if __name__ == '__main__':
    edge = dig_edge(lines())
    My = max(map(lambda p:p[1], edge))
    my = min(map(lambda p:p[1], edge))
    Mx = max(map(lambda p:p[0], edge))
    mx = min(map(lambda p:p[0], edge))
    #for y in range(My, my - 1, -1):
    #    print(''.join('O' if (x,y) in edge else ' ' for x in range(mx, Mx + 1)))
    print(dig_inside(edge, range(mx - 1, Mx + 2), range(my - 1, My + 2)))
