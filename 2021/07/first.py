initial = list(map(int, input().split(',')))
print(min([sum([abs(target - crab) for crab in initial]) for target in range(1, max(initial))]))
