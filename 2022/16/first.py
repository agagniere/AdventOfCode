from utils import *
from collections import deque

def bfs(start: str, topo: dict, interest: set) -> dict:
    fringe = deque([(0, start)])
    seen = set([start])
    result = {}
    while fringe:
        dist, current = fringe.popleft()
        if dist and current in interest:
            result[current] = dist
        for n in topo[current]:
            if n not in seen:
                seen.add(n)
                fringe.append( (dist + 1, n) )
    return result

topo, rates = parse(lines())
print(len(rates))

valves = [k for k, v in rates.items() if v]
print(len(valves))

useful_topo = {k:bfs(k, topo, set(valves)) for k in valves + ['AA']}

time_limit = 30
fringe = deque([(0, 0, 'AA', set(valves))])
best = 0
while fringe:
    elapsed, released, node, to_open = fringe.popleft()
    #print(f'After {elapsed}: {node} with {released}')
    if not to_open:
        #print(f'Finished opening all valves after {elapsed} minutes with {released}')
        best = max(best, released)
    else:
        found = False
        for neighbor, cost in useful_topo[node].items():
            opened_at = elapsed + cost + 1
            if neighbor in to_open and opened_at < time_limit:
                found = True
                fringe.append( (opened_at,
                                released + (time_limit - opened_at) * rates[neighbor],
                                neighbor,
                                to_open - set([neighbor])) )
        if not found:
            #print(f"Out of time, released {released}:", set(valves) - to_open)
            best = max(best, released)
print(best)
