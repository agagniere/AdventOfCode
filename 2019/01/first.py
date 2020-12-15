fuel = 0

while True:
    try:
        fuel += int(input()) // 3 - 2
    except:
        break

print(fuel)
