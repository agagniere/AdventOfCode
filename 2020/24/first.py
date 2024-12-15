from utils import lines, Point
from collections import defaultdict

def tokenize(line: str):
    acc = None
    for c in line:
        if c in 'sn':
            acc = c
        else:
            yield acc + c if acc else c
            acc = None

def flip(tiles: dict, instructions: str):
    pos = Point(0,0)
    for token in tokenize(instructions):
        pos = pos.next(token)
    tiles[pos] = not tiles[pos]

def count(tiles: dict):
    return sum(1 for t in tiles.values() if t)

if __name__ == '__main__':
    tiles = defaultdict(bool)
    for line in lines():
        flip(tiles, line)
    print(count(tiles))
