from utils import Point, lines
from collections import defaultdict

EMPTY = 0
WALL = 1
BOX_LEFT = 2
BOX_RIGHT = 3

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
        #print(line)
        if not line:
            M.y = y
            break
        for x, c in enumerate(line):
            P = Point(2*x, y)
            if c == '#':
                board[P] = WALL
                board[P + (1, 0)] = WALL
            elif c == 'O':
                board[P] = BOX_LEFT
                board[P + (1, 0)] = BOX_RIGHT
            elif c == '@':
                robot = P
        M.x = max(M.x, P.x)
    return board, robot, M + (1,0)

BOX_PART = set([BOX_LEFT, BOX_RIGHT])

def move(board: dict, robot: Point, m: str):
    d = direction(m)
    dest = robot + d
    to_move = []
    freespots = [dest]

    while True:
        obs = set(board[s] for s in freespots)
        if WALL in obs:
            return board, robot
        elif BOX_PART & obs:
            match m:
                case '<':
                    for f in freespots:
                        to_move += [f, f + (-1, 0)]
                    freespots = [f + (-2, 0) for f in freespots]
                case '>':
                    for f in freespots:
                        to_move += [f, f + (1, 0)]
                    freespots = [f + (2, 0) for f in freespots]
                case '^':
                    nf = []
                    for f in freespots:
                        if board[f] == BOX_LEFT and f + (0, -1) not in nf:
                            to_move += [f, f + (1, 0)]
                            nf += [f + (0, -1), f + (1, -1)]
                        elif board[f] == BOX_RIGHT and f + (0, -1) not in nf:
                            to_move += [f, f + (-1, 0)]
                            nf += [f + (0, -1), f + (-1, -1)]
                    freespots = nf
                case 'v':
                    nf = []
                    for f in freespots:
                        if board[f] == BOX_LEFT and f + (0, 1) not in nf:
                            to_move += [f, f + (1, 0)]
                            nf += [f + (0, 1), f + (1, 1)]
                        elif board[f] == BOX_RIGHT and f + (0, 1) not in nf:
                            to_move += [f, f + (-1, 0)]
                            nf += [f + (0, 1), f + (-1, 1)]
                    freespots = nf
        else:
            for p in reversed(to_move):
                board[p+d] = board[p]
                board[p] = EMPTY
            return board, robot + d

if __name__ == '__main__':
    board, robot, bounds = parse(lines())
    for line in lines():
        for m in line:
            board, robot = move(board, robot, m)
    # for y in range(bounds.y):
    #     print(''.join('#' if board[(x,y)] == WALL else
    #                   '[' if board[(x,y)] == BOX_LEFT else
    #                   ']' if board[(x,y)] == BOX_RIGHT else '.'
    #                   for x in range(bounds.x)))
    R = 0
    for pos, item in board.items():
        if item == BOX_LEFT:
            R += pos.y * 100 + pos.x
    print(R)
