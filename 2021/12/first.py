from collections import defaultdict, deque

def lines():
    while True:
        try:
            yield input()
        except:
            break

topo = defaultdict(list)

for line in lines():
    a, b = line.split('-')
    topo[a] += [b]
    topo[b] += [a]


fringe = deque([('start', defaultdict(int), [])])
paths = []
while fringe:
    cur, seen, path = fringe.popleft()
    seen[cur] += 1
    adj = topo[cur]
    for r in adj:
        if r == 'end':
            paths += [path]
        elif seen[r] < 1 or r.isupper():
            fringe.append((r, seen.copy(), path + [r]))
print('\n'.join([' , '.join(p) for p in paths]))
print(len(paths))
