target = ('shiny', 'gold')
reverse = {}
while True:
    try:
        line = input()
    except:
        break
    outer, inner = line.split(' contain ')
    parent = tuple(outer.split()[:2])
    if inner[:2] == 'no':
        continue
    for bag in inner.split(','):
        child = tuple(bag.split()[1:3])
        reverse[child] = set([parent]) | reverse.get(child, set())

seen = set()
valid = reverse[target]
while valid - seen:
    next_level = set()
    for bag in filter(lambda x: x not in seen, valid):
        next_level |= reverse.get(bag, set())
    seen |= valid
    valid |= next_level

print(len(valid))
