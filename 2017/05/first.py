import sys

prog = list(map(int, sys.stdin.readlines()))
i = 0
count = 0
while i < len(prog):
    count += 1
    prev = i
    i += prog[i]
    prog[prev] += 1
print(count)
