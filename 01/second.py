seen = set()
sums = {}
for i in range(199):
    n = int(input())
    t = 2020 - n
    if t in sums:
        a = t - sums[t]
        b = t - a
        print(a * b * n)
        break
    for o in seen:
        sums[n + o] = n
    seen.add(n)
print(seen)
