from functools import reduce
import heapq

heights = []
while True:
    try:
        line = input()
    except:
        break
    heights += [tuple(map(int, line))]
seen = set()

def bassin(x, y):
    seen.add((x, y))
    result = 1
    if x > 0 and (x - 1, y) not in seen and heights[y][x - 1] < 9:
        result += bassin(x - 1, y)
    if y > 0 and (x, y - 1) not in seen and heights[y - 1][x] < 9:
        result += bassin(x, y - 1)
    if x + 1 < len(heights[y]) and (x + 1, y) not in seen and heights[y][x + 1] < 9:
        result += bassin(x + 1, y)
    if y + 1 < len(heights) and (x, y + 1) not in seen and heights[y + 1][x] < 9:
        result += bassin(x, y + 1)
    return result

bassins = []
for y, row in enumerate(heights):
    for x, cell in enumerate(row):
        if cell < 9 and (x, y) not in seen:
            bassins.append(bassin(x, y))

top3 = heapq.nlargest(3, bassins)
print(top3)
print(reduce(int.__mul__, top3, 1))
