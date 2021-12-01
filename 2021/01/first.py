prev = None
count = 0
while True:
    try:
        v = int(input())
    except:
        break
    if prev and v > prev:
        count += 1
    prev = v
print(count)
