from utils import *

def slice_edges(y: int, sensor: Point, radius: int):
    v_dist = abs(sensor.y - y)
    if v_dist > radius:
        return set()
    half = radius - v_dist
    return set(range(sensor.x - half, sensor.x + half + 1))

sensors, beacons = parse(lines())

y = [10, 2000000][len(sensors) > 20]
in_range = set()
for sensor, radius in sensors:
    in_range |= slice_edges(y, sensor, radius)
print(len(in_range - set(b.x for b in beacons if b.y == y)))
