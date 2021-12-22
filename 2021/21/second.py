from collections import deque, Counter

todo = deque()
todo.append((False, (0, 0), (1, 0), 1))
count = [0, 0]
rolls = Counter([3 + sum((i, j, k)) for i in range(3) for j in range(3) for k in range(3)])

while todo:
    player, score, space, univ = todo.popleft()
    for roll, mul in rolls.items():
        sp = (space[0] + roll) % 10
        sc = score[0] + sp + 1
        if sc > 20:
            count[player] += univ * mul
        else:
            todo.append((not player, (score[1], sc), (space[1], sp), univ * mul))
print(count[0])
print(count[1])
print(max(count))
