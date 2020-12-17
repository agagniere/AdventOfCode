initial = list(map(int, input().split(',')))
i = len(initial) - 1
seen = {c:i for i, c in enumerate(initial[:-1])}
last = initial[-1]
while i < 2019:
    if last in seen:
        cur = i - seen[last]
    else:
        cur = 0
#    print(i + 2, last, cur)
    seen[last] = i
    last = cur
    i += 1

print(last)
