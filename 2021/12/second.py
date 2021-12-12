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


fringe = deque([('start', defaultdict(int), [], None)])
paths = []
while fringe:
    cur, seen, path, small = fringe.popleft()
    seen[cur] += 1
    adj = topo[cur]
    for r in adj:
        if r == 'end':
            paths += [path]
        elif seen[r] < 1 or r.isupper():
            fringe.append((r, seen.copy(), path + [r], small))
        elif small == None and seen[r] < 2 and r not in set(['start', 'end']) and r.islower():
            fringe.append((r, seen.copy(), path + [r], r))

#print('\n'.join([' , '.join(p) for p in paths]))
print(len(paths))
