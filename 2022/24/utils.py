from heapq import heappush, heappop

delta_from_facing = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1)
}

class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def distance(self, other): return abs(self.x - other[0]) + abs(self.y - other[1])
    def neighbors(self):
        for f in 'v><^':
            yield self + delta_from_facing[f]
    def getX(self): return self.x
    def getY(self): return self.y
    def __add__(self, other): return Point(self.x + other[0], self.y + other[1])
    def __radd__(self, other): return self + other
    def __sub__(self, other): return Point(self.x - other[0], self.y - other[1])
    def __neg__(self): return Point(-self.x, -self.y)
    def __mul__(self, scalar): return Point(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar): return self * scalar
    def __eq__(self, other): return self.x == other[0] and self.y == other[1]
    def __mod__(self, other): return Point(self.x % other[0], self.y % other[1])
    def __getitem__(self, i): return self.x if i == 0 else self.y
    def __str__(self): return "({}, {})".format(self.x, self.y)
    def __repr__(self): return "({} {})".format(self.x, self.y)
    def __hash__(self): return (self.x, self.y).__hash__()

def lines():
    while True:
        try:
            yield input()
        except:
            break

initial = list(lines())
non_wall = set(Point(x, y) for y, row in enumerate(initial) for x, c in enumerate(row) if c != '#')

wind = [list()]
for y, row in enumerate(initial):
    for x, c in enumerate(row):
        if c in '<>v^':
            wind[0] += [(Point(x, y), c)]

free_tiles = [non_wall - set(w for w,_ in wind[0])]
MAX = 999999

def get_winds(time: int):
    global MAX
    global free_tiles
    while time % MAX >= len(wind):
        wind.append(list())
        for p, f in wind[-2]:
            n = (1, 1) + (((p + delta_from_facing[f]) - (1, 1)) % (len(initial[0]) - 2, len(initial) - 2))
            wind[-1] += [(n, f)]
        if wind[0] == wind[-1]:
            wind.pop()
            MAX = len(wind)
        else:
            free_tiles += [non_wall - set(w for w,_ in wind[-1])]
    return wind[time % MAX]

def get_free_tiles(time: int):
    if time % MAX >= len(free_tiles):
        get_winds(time)
    return free_tiles[time % MAX]

UID = 0
def A_star(start, end, clock = 0):
    heuristic = end.distance
    def new_node(cost, pos):
        global UID
        h = heuristic(pos)
        UID += 1
        return (cost + h, cost, UID, pos)
    seen = set([(start, clock)])
    fringe = [new_node(clock, start)]
    best = 9999999
    count = 0
    while fringe:
        _, time, _, pos = heappop(fringe)
        count += 1
        if pos.distance(end) < best:
            best = pos.distance(end)
            print(f'Closest {best:4} in {time:4} [{UID:10} - {count:10} = {UID-count:12}]')
        free = get_free_tiles(time + 1)
        for n in pos.neighbors():
            if n == end:
                return time + 1
            if n in free and (n, time + 1) not in seen:
                seen.add( (n, time + 1) )
                heappush(fringe, new_node(time + 1, n))
        if pos in free and (pos, time + 1) not in seen:
            seen.add( (pos, time + 1) )
            heappush(fringe, new_node(time + 1, pos))

start = min(free_tiles[0], key = Point.getY)
end = max(free_tiles[0], key = Point.getY)
