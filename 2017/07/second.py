from collections import Counter, defaultdict
import sys
import re

topo = {}
weights = {}
not_roots = set()
parse = re.compile(r'(\w+) \((\d+)\)( -> ([\w, ]+))?')
for line in map(str.strip, sys.stdin.readlines()):
    node, weight, children = parse.match(line).group(1, 2, 4)
    if children:
        children = children.split(', ')
        not_roots |= set(children)
        topo[node] = children
    weights[node] = int(weight)

def get_weight(node):
    if node not in topo:
        return weights[node]
    carried = defaultdict(list)
    for child in topo[node]:
        carried[get_weight(child)].append(child)
    if len(carried) == 1:
        W, C = next(iter(carried.items()))
        return weights[node] + W * len(C)
    nominal_weight = max(carried, key = lambda x: len(carried[x]))
    wrong_weight   = min(carried, key = lambda x: len(carried[x]))
    to_correct = carried[wrong_weight][0]
    corrected = weights[to_correct] + nominal_weight - wrong_weight
    print(corrected)
    exit(0)

root = next(iter(set(topo.keys()) - not_roots))
get_weight(root)
