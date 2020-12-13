import math

do_op = {
    'N':(lambda p,w,a: (p, w + a * 1j)),
    'S':(lambda p,w,a: (p, w - a * 1j)),
    'E':(lambda p,w,a: (p, w + a)),
    'W':(lambda p,w,a: (p, w - a)),
    'L':(lambda p,w,a: (p, w * 1j ** (a // 90))),
    'R':(lambda p,w,a: (p, w * 1j ** (-a // 90))),
    'F':(lambda p,w,a: (p + w * a, w)),
}

ship = 0
way = 10 + 1j

while True:
    try:
        line = input()
    except:
        break
    action = line[0]
    arg = int(line[1:])
    ship, way = do_op[action](ship, way, arg)
    #print(ship, way)

print(abs(ship.real) + abs(ship.imag))
