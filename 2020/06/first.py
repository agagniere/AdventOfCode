seen = set()
count = 0
#for _ in range(2087):
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
