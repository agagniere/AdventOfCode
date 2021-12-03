apply = {
    'forward': (lambda p, v : (p[0] + v, p[1])),
    'up'     : (lambda p, v : (p[0], p[1] - v)),
    'down'   : (lambda p, v : (p[0], p[1] + v))
}
pos = (0, 0)
while True:
    try:
        motion, value = input().split()
    except:
        break
    pos = apply[motion](pos, int(value))
print(pos, pos[0] * pos[1])
