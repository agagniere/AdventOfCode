heights = []
while True:
    try:
        line = input()
    except:
        break
    heights += [tuple(map(int, line))]

total = 0
for y, row in enumerate(heights):
    for x, cell in enumerate(row):
        if (x == 0 or cell < row[x - 1]) and (x + 1 == len(row) or cell < row[x + 1]) and (y == 0 or cell < heights[y - 1][x]) and (y + 1 == len(heights) or cell < heights[y + 1][x]):
            total += 1 + cell
print(total)
