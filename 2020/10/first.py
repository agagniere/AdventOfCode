#adapters = set()
adapters = []
while True:
    try:
        #adapters.add(int(input()))
        adapters += [int(input())]
    except:
        break
adapters.sort()

jumps = [0, 0, 1] # from last to target : jump of 3
jumps[adapters[0] - 1] += 1 # from 0 to first
for i, current in enumerate(adapters[:-1]):
    jumps[adapters[i+1] - current - 1] += 1

print(jumps)
print(jumps[0] * jumps[2])
