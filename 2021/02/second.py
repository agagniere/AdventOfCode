apply = {
    'forward': (lambda p, v : (p[0] + v, p[1] + p[2] * v, p[2])),
    'up'     : (lambda p, v : (p[0], p[1], p[2] - v)),
    'down'   : (lambda p, v : (p[0], p[1], p[2] + v))
}
state = (0, 0, 0)
while True:
    try:
        motion, value = input().split()
    except:
        break
    state = apply[motion](state, int(value))
print(state, state[0] * state[1])
