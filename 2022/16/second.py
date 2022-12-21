from utils import *
from collections import deque
from heapq import heappop, heappush

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
#print(useful_topo)

time_limit = 26

def potential(opened_at, rate):
    return rate * (time_limit - opened_at)

def to_release(clock, costs):
    def inner(node):
        return potential(clock + costs[node] + 1, rates[node])
    return inner

fringe = [(len(valves), 0, 0, 0, 0, 'AA', 0, 'AA', set(valves))]
best = 0
count = 0
while fringe:
    _, _, _, released, my_clock, my_pos, el_clock, el_pos, to_open = heappop(fringe) # fringe.popleft()
    count += 1
    #print(f'Released {released}: I reached {my_pos} at {my_clock}, elphant reached {el_pos} at {el_clock}')
    if not to_open:
        #print(f'Finished opening all valves after {max(my_clock, el_clock)} minutes with {released}')
        if released > best:
            print(count, released)
        best = max(best, released)
    else:
        found = False
        my_potential = to_release(my_clock, useful_topo[my_pos])
        el_potential = to_release(el_clock, useful_topo[el_pos])

        #el_best = max(to_open, key = el_potential)
        for my_best in to_open: #sorted(to_open, key = my_potential, reverse=True)[:]:
            opened_at = my_clock + useful_topo[my_pos][my_best] + 1
            if opened_at < time_limit:
                found = True
                # fringe.append(
                heappush(fringe,
                    (max(opened_at, el_clock) + 2*len(to_open),
                     #+ min(min((useful_topo[pos][d] for d in to_open if d != pos), default=0) for pos in [my_best, el_pos]),
                     max(opened_at, el_clock),
                     -released - potential(opened_at, rates[my_best]),
                     released + potential(opened_at, rates[my_best]),
                     opened_at,
                     my_best,
                     el_clock,
                     el_pos,
                     to_open - set([my_best]))
                )
        for el_best in to_open: #sorted(to_open, key = el_potential, reverse=True)[:]:
            opened_at = el_clock + useful_topo[el_pos][el_best] + 1
            if opened_at < time_limit:
                found = True
                # fringe.append(
                heappush(fringe,
                    (max(opened_at, my_clock) + 2*len(to_open),
                     #+ min(min((useful_topo[pos][d] for d in to_open if d != pos), default=0) for pos in [el_best, my_pos]),
                     max(opened_at, my_clock),
                     -released - potential(opened_at, rates[el_best]),
                     released + potential(opened_at, rates[el_best]),
                     my_clock,
                     my_pos,
                     opened_at,
                     el_best,
                     to_open - set([el_best]))
                )
        if not found:
            #print(f'Out of time, with {released}')
            if released > best:
                print(count, released)
            best = max(best, released)
print(count)
print(best)
