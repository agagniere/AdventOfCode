def solve(LEN):
    seen = set()
    for i in range(LEN):
        n = int(input())
        for o in seen:
            target = 2020 - (n + o)
            if target in seen:
                return target * o * n
        seen.add(n)

print(solve(200))
