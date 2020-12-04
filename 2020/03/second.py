board = [input() for _ in range(323)]
total = 1
for offset in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    x = 0
    tree_count = 0
    for row in board[::offset[1]]:
        tree_count += (row[x % len(row)] == '#')
        x += offset[0]
    total *= tree_count
print(total)
