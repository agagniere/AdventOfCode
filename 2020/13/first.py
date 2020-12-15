start = int(input())
bus = [int(ID) for ID in input().split(',') if ID != 'x']

best = min(bus, key=lambda b: b - (start % b))

print(best * (best - (start % best)))
