fuel = 0

while True:
    try:
        mass = int(input())
    except:
        break
    while mass:
        mass = max(0, mass // 3 - 2)
        fuel += mass

print(fuel)
