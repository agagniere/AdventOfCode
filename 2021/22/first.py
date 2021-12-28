#from collections import defaultdict

on = set()

def lines():
    while True:
        try:
            yield input()
        except:
            break

for line in lines():
    ins, rest = line.split()
    bounds = [list(map(int, d[2:].split('..'))) for d in rest.split(',')]
    skip = False
    for b in bounds:
        if b[1] < -50 or 50 < b[0]:
            skip = True
        b[0] = max(-50, b[0])
        b[1] = min(50, b[1])
    print(ins, bounds, skip)
    if skip:
        continue
    for x in range(bounds[0][0], bounds[0][1] + 1):
        for y in range(bounds[1][0], bounds[1][1] + 1):
            for z in range(bounds[2][0], bounds[2][1] + 1):
                if abs(x) < 51 and abs(y) < 51 and abs(z) < 51:
                    if ins == "on":
                        on.add((x, y, z))
                    elif (x, y, z) in on:
                        on.remove((x, y, z))
print(len(on))
