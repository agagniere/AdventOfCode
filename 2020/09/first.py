sequence = []
#i = 0
while True:
    try:
        current = int(input())
    except:
        break
    #i += 1
    if len(sequence) <= 25:
        sequence += [current]
        continue
    sliding = sequence[-25:]
    seen = set()
    ok = False
    for s in sliding:
        if current - s in seen:
            ok = True
            break
        seen.add(s)
    if not ok:
        print(current)
        break
    sequence += [current]
