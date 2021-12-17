x_limits, y_limits = [tuple(map(int, s.rstrip(',').split('=')[1].split('..'))) for s in input().split()[2:]]

best = -42
best_highest = -42
for initial_vy in range(200):
    vy = initial_vy
    y = 0
    highest = 0
    while vy > 0:
        y += vy
        vy -= 1
    highest = y
    while y > max(y_limits):
        y += vy
        vy -= 1
    if y >= min(y_limits):
        best = initial_vy
        best_highest = highest
print(best, best_highest)
