def lines():
    while True:
        try:
            yield input()
        except:
            break

board = [list(map(int, row)) for row in lines()]
print("Before any steps:\n{}".format('\n'.join([''.join(map(str, row)) for row in board])))

total = 0
step = 0
while step < 100:
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
    total += flashes
    if step < 10 or step % 10 == 0:
        print("After step {}, [{}] :\n{}".format(step, flashes, '\n'.join([''.join(map(lambda x: str(x) if x else f"\033[1;33m{x}\033[0m", row)) for row in board])))
print(total)
