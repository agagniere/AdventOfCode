def lines():
    while True:
        try:
            yield input()
        except:
            break

board = [list(map(int, row)) for row in lines()]
print('\n'.join(map(str, board)))

step = 0
while True:
    prev = board
    step += 1
    board = [[n + 1 for n in row]for row in  prev]
    flashes = 0
    def flash(x, y):
        global board
        global flashes
        board[y][x] = 0
        flashes += 1
        for i in range(9):
            dx, dy = (i % 3) - 1, i // 3 - 1
            if dx or dy:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and ny < len(board) and nx < len(board[ny]) and board[ny][nx]:
                    board[ny][nx] += 1
                    if board[ny][nx] > 9:
                        flash(nx, ny)
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell > 9:
                flash(x, y)
    if flashes > 20:
        print("After step {}, [{}] :\n{}".format(step, flashes, '\n'.join([''.join(map(lambda x: str(x) if x else f"\033[1;33m{x}\033[0m", row)) for row in board])))
    if flashes == 100:
        print(step)
        break
