from collections import defaultdict

adapters = []
while True:
    try:
        adapters += [int(input())]
    except:
        break
adapters.sort()

mem = defaultdict(int)
mem[0] = 1

for a in adapters:
    mem[a] = sum([mem[a-1-d] for d in range(3)])
    print(a, mem[a])
