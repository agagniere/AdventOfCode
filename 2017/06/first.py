import sys

slots = list(map(int, sys.stdin.read().split()))
print(slots)
seen = set([tuple(slots)])
while True:
    c, i = min((-c, i) for i,c in enumerate(slots))
    slots[i] = 0
    while c:
        i += 1
        i %= len(slots)
        slots[i] += 1
        c += 1
    T = tuple(slots)
    if T in seen:
        break
    seen.add(T)
    print(T)
print(len(seen))
