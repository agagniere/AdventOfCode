from collections import Counter

prev = Counter(map(int, input().split(',')))
for _ in range(256):
    current = {8: prev[0]}
    for i in range(8):
        current[i] = prev[i + 1]
    current[6] += prev[0]
    prev = current
print(sum(current.values()))
