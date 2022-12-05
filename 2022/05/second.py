from utils import *

drawing = []
for line in lines():
    drawing += [line]
    if not '[' in line:
        break
print('\n'.join(drawing))

stacks = [list() for _ in drawing[0][::4]]
for col, stack in filter(lambda p:p[1].isdigit(), enumerate(drawing[-1])):
    stacks[int(stack) - 1] = [row[col] for row in reversed(drawing[:-1]) if row[col].isalpha()]

for line in lines():
    if not line:
        continue
    *count, src, dst = filter(str.isdigit, line)
    count, src, dst = map(int, [''.join(count), src, dst])
    move = stacks[src - 1][-count:]
    del stacks[src - 1][-count:]
    stacks[dst - 1] += move
    #print('------')
    #for s in stacks:
    #    print('[' + '] ['.join(s) + ']')

print(''.join([stack[-1] for stack in stacks]))
