board = [input() for _ in range(323)]
x = 0
tree_count = 0
for row in board:
    tree_count += (row[x % len(row)] == '#')
    x += 3
print(tree_count)
