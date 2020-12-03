seen = set()
for i in range(200):
    n = int(input())
    t = 2020 - n
    if t in seen:
        print(t * n)
        break
    seen.add(n)
