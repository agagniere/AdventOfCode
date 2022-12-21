from utils import *

def parse(iterable):
    constant = {}
    equation = {'humn': None}
    queue = deque(iterable)
    print(len(queue))
    while queue:
        line = queue.popleft()
        key, value = line.split(': ')
        if key == 'humn':
            continue
        if value.isdigit():
            constant[key] = int(value)
        else:
            a, op, b = value.split()
            if a in constant and b in constant:
                constant[key] = do_op[op](constant[a], constant[b])
            elif (a not in constant and a not in equation) or (b not in constant and b not in equation):
                queue.append(line)
            else:
                equation[key] = op, constant.get(a, a), constant.get(b, b)
    return equation

tree = parse(lines())
print(len(tree))

order = []
ptr = 'root'
while True:
    _, a, b = tree[ptr]
    ptr = a if isinstance(b, int) else b
    order += [ptr]
    if not tree[ptr]:
        break
print(order)

equation = []
rest = deque()
for ptr in order[:-1]:
    op, a, b = tree[ptr]
    if isinstance(b, int):
        equation += ['(']
        rest.appendleft(f') {op} {b}')
    else:
        equation += [f'{a} {op} (']
        rest.appendleft(')')
equation = ''.join(equation + ['x'] + list(rest))
print(equation)

goal = tree['root'][1] if isinstance(tree['root'][1], int) else tree['root'][2]
print(goal)

m = 0
M = 1000 ** 5

while m != M:
    x = m
    v_m = abs(goal - eval(equation))
    x = M
    v_M = abs(goal - eval(equation))
    if v_m < v_M:
        M = (m + M) // 2
    else:
        m = (m + M) // 2
print(m)
