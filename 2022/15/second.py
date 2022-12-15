from utils import *

def edges(sensor: Point, radius: int):
    for i, y in enumerate(range(sensor.y - radius, sensor.y)):
        yield (sensor.x - i - 1, y)
        yield (sensor.x + i + 1, y)
    for i, y in enumerate(range(sensor.y, sensor.y + radius)):
        yield (sensor.x - radius + i - 1, y)
        yield (sensor.x + radius - i + 1, y)

def is_blindspot(pos, sensors: list) -> bool:
    for S, D in sensors:
        if S.taxi_distance(pos) <= D:
            return False
    return True

sensors, _ = parse(lines())
sensors.sort(key=lambda x:x[1])
max_x = max(p[0].x for p in sensors)
for sensor, radius in sensors:
    for x, y in edges(sensor, radius):
        if x < 0 or x > max_x or y < 0 or y > max_x: continue
        if is_blindspot((x,y), sensors):
            print(x,y)
            print(x * 4000000 + y)
            exit(0)
