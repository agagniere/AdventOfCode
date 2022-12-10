from utils import *

drawing = next(non_empty_line_group(lines()))
stacks = extract_stacks(drawing)

for line in lines():
    count, src, dst = map(int, filter(str.isdigit, line.split()))
    move = stacks[src - 1][-count:]
    del stacks[src - 1][-count:]
    stacks[dst - 1] += reversed(move)

print(''.join([stack[-1] for stack in stacks]))
