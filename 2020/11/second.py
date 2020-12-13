
def visible(board, x, y):
    res = ""
    for i in range(9):
        if i == 4:
            continue
        dx = (i % 3) - 1
        dy = i // 3 - 1
        tx, ty = x + dx, y + dy
        while ty in range(len(board)) and tx in range(len(board[0])) and board[ty][tx] == '.':
            tx += dx
            ty += dy
        if ty in range(len(board)) and tx in range(len(board[0])):
            res += board[ty][tx]
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
                adj = visible(previous, x, y)
                if not '#' in adj:
                    c = '#'
                elif adj.count('#') >= 5:
                    c = 'L'
            nrow += c
        board += [nrow]
    print('-' * 50)
    print('\n'.join(board))
print('---- END ----')
print(sum([row.count('#') for row in board]))
