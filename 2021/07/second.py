def triangular(n):
    return n * (n + 1) // 2

initial = list(map(int, input().split(',')))
print(min([sum([triangular(abs(target - crab)) for crab in initial]) for target in range(1, max(initial))]))
