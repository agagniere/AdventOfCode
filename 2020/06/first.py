seen = set()
count = 0
while True:
    try:
        line = input()
    except:
        break
    if line:
        seen |= set(line)
    else:
        count += len(seen)
        seen.clear()
print(count)
