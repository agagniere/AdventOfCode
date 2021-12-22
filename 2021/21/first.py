i = 0
space = [4, 8]
score = [0, 0]
player = False
while True:
    R = 0
    for _ in range(3):
        R += (i % 100) + 1
        i += 1
    space[player] = ((space[player] - 1 + R) % 10) + 1
    score[player] += space[player]
    if score[player] > 999:
        break
    player = not player

print("Winner is", "12"[player])
L = score[not player]
print(L, i, L * i)
