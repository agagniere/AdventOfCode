from utils import *

def sensors_in_range(p, sensors: list) -> int:
    result = 0
    for S, D in sensors:
        if S.taxi_distance(p) <= D:
            result += 1
    return result

sensors, _ = parse(lines())
L = 20
#L = 4000000
print(sensors)
for y in range(-L//2, L * 3 // 2, L // 20):
    print(''.join(['  ', '. ', '..', '::', ';;', '||', '[]'][sensors_in_range( (x,y), sensors)] for x in range(-L//2, L * 3 // 2, L // 20)))
