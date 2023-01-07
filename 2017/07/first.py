import sys
import re

parents = set()
not_roots = set()
parse = re.compile(r'(\w+) \(\d+\)( -> ([\w, ]+))?')
for line in map(str.strip, sys.stdin.readlines()):
    node, children = parse.match(line).group(1, 3)
    if children:
        children = children.split(', ')
        not_roots |= set(children)
        parents.add(node)
root = next(iter(parents - not_roots))
print(root)
