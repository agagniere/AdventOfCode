from utils import lines, Point
from collections import defaultdict
from first import tokenize, flip, count

def next_day(tiles):
    result = defaultdict(bool)
    whites = set()
    for pos, is_black in tiles.items():
        if not is_black:
            continue
        density = 0
        for neigh in pos.neighbors():
            if tiles.get(neigh, False):
                density += 1
            else:
                whites.add(neigh)
        if density in (1, 2):
            result[pos] = True
    for pos in whites:
        density = 0
        for neigh in pos.neighbors():
            if tiles[neigh]:
                density += 1
        if density == 2:
            result[pos] = True
    return result

if __name__ == '__main__':
    tiles = defaultdict(bool)
    for line in lines():
        flip(tiles, line)
    for day in range(100):
        tiles = next_day(tiles)
    print(count(tiles))
