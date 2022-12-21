from utils import *

def parse(iterable):
    constant = {}
    queue = deque(iterable)
    print(len(queue))
    while queue:
        line = queue.popleft()
        key, value = line.split(': ')
        if value.isdigit():
            constant[key] = int(value)
        else:
            a, op, b = value.split()
            if a in constant and b in constant:
                constant[key] = do_op[op](constant[a], constant[b])
            else:
                queue.append(line)
    return constant

print(parse(lines())['root'])
