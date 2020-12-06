target = ('shiny', 'gold')
rule = {}
while True:
    try:
        line = input()
    except:
        break
    outer, inner = line.split(' contain ')
    parent = tuple(outer.split()[:2])
    rule[parent] = []
    if inner[:2] == 'no':
        continue
    for bag in inner.split(','):
        child = tuple(bag.split()[:3])
        rule[parent] += [child]


def sub_bags_in(bag):
    count = 1
    for n, adj, color in rule[bag]:
        count += int(n) * sub_bags_in((adj, color))
    return count

# -1 to exclude the shiny gold bag itself
print(sub_bags_in(target) - 1)
