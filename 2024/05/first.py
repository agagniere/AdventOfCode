from utils import lines
from collections import defaultdict

#rules_before = defaultdict(set)
rules_after = defaultdict(set)

for line in lines():
    if not line:
        break
    a, b = map(int, line.split('|'))
    rules_after[a].add(b)
    #rules_before[b].add(a)

R = 0

for line in lines():
    update = list(map(int, line.split(',')))
    valid = True
    before = set()
    #after = set(update)
    for page in update:
        #after.remove(page)
        if rules_after[page] & before: # or rules_before[page] & after:
            valid = False
            break
        before.add(page)
    if valid:
        R += update[len(update) // 2]

print(R)
