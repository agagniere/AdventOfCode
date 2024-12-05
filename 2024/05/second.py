from utils import lines
from collections import defaultdict

rules_after = defaultdict(set)

def reorder(update: list, first: bool = True):
    valid = True
    before = {}
    reordered = [page for page in update]
    for i, page in enumerate(update):
        if rules_after[page] & before.keys():
            m = min(before[other] for other in rules_after[page] & before.keys())
            print(page, "must be before", rules_after[page] & before.keys(), ", index <", m)
            valid = False
            reordered[i] = update[m]
            reordered[m] = page
            return reorder(reordered, False)
        before[page] = i
    return None if first else reordered

for line in lines():
    if not line:
        break
    a, b = map(int, line.split('|'))
    rules_after[a].add(b)

R = 0

for line in lines():
    update = list(map(int, line.split(',')))
    N = reorder(update)
    if N:
        R += N[len(N) // 2]

print(R)
