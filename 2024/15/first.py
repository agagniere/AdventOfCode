from utils import Point, lines
from collections import defaultdict

EMPTY = 0
WALL = 1
BOX = 2

def direction(move: str):
    return {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1),
    }[move]

def parse(lines):
    board = defaultdict(int)
    robot = None
    M = Point(0, 0)
    for y, line in enumerate(lines):
        print(line)
        if not line:
            M.y = y
            break
        for x, c in enumerate(line):
            if c == '#':
                board[Point(x,y)] = WALL
            elif c == 'O':
                board[Point(x,y)] = BOX
            elif c == '@':
                robot = Point(x, y)
            M.x = max(x, M.x)

    return board, robot, M + (1,0)

def move(board: dict, robot: Point, m: str):
    d = direction(m)
    dest = robot + d
    freespot = dest
    while board[freespot] == BOX:
        freespot += d
    if board[freespot] != WALL:
        if dest != freespot:
            board[freespot] = BOX
        board[dest] = EMPTY
        robot = dest
    return board, robot

if __name__ == '__main__':
    board, robot, bounds = parse(lines())
    for line in lines():
        for m in line:
            board, robot = move(board, robot, m)
    for y in range(bounds.y):
        print(''.join('#' if board[(x,y)] == WALL else
                      'O' if board[(x,y)] == BOX else '.'
                      for x in range(bounds.x)))
    R = 0
    for pos, item in board.items():
        if item == BOX:
            R += pos.y * 100 + pos.x
    print(R)
