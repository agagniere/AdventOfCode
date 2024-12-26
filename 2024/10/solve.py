from utils import lines, Point
from collections import deque, namedtuple, defaultdict

Node = namedtuple('Node', ['position', 'origin'])

def parse(lines):
    heights = {}
    trailheads = []
    peaks = []
    for y, line in enumerate(lines):
        for x, h in enumerate(map(int, line)):
            p = Point(x, y)
            heights[p] = h
            if h == 0:
                trailheads.append(p)
            if h == 9:
                peaks.append(p)
    return heights, trailheads, peaks

def part1(heights, peaks):
    reachable = defaultdict(set)
    score = defaultdict(int)
    fringe = deque(Node(p, p) for p in peaks)
    while fringe:
        pos, origin = fringe.popleft()
        for n in pos.neighbors():
            if n not in heights or heights[n] != heights[pos] - 1 or n in reachable[origin]:
                continue
            reachable[origin].add(n)
            if heights[n] == 0:
                score[n] += 1
            else:
                fringe.append(Node(n, origin))
    return sum(score.values())

def part2(heights, trailheads):
    rating = defaultdict(int)
    fringe = deque(Node(p, p) for p in trailheads)
    while fringe:
        pos, origin = fringe.popleft()
        for n in pos.neighbors():
            if n not in heights or heights[n] != heights[pos] + 1:
                continue
            if heights[n] == 9:
                rating[origin] += 1
            else:
                fringe.append(Node(n, origin))
    return sum(rating.values())



if __name__ == '__main__':
    heights, trailheads, peaks = parse(lines())
    print(part1(heights, peaks))
    print(part2(heights, trailheads))
