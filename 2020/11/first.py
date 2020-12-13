
def adjacents(board, x, y):
    res = ""
    if y > 0:
        res += board[y-1][max(x-1,0):x+2]
    if x > 0:
        res += board[y][x-1]
    if x + 1 < len(board[y]):
        res += board[y][x+1]
    if y + 1 < len(board):
        res += board[y+1][max(x-1,0):x+2]
    #print(x, y, res)
    return res

board = []

while True:
    try:
        board += [input()]
    except:
        break

previous = []
while previous != board:
    previous = board
    board = []
    for y, row in enumerate(previous):
        nrow = ""
        for x, c in enumerate(row):
            if c in "L#":
                adj = adjacents(previous, x, y)
                if not '#' in adj:
                    c = '#'
                elif adj.count('#') >= 4:
                    c = 'L'
            nrow += c
        board += [nrow]
    print('-' * 50)
    print('\n'.join(board))
print('---- END ----')
print(sum([row.count('#') for row in board]))
