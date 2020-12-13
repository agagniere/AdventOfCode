seen = None
count = 0
while True:
    try:
        line = input()
    except:
        break
    if line:
        if seen == None:
            seen = set(line)
        else:
            seen &= set(line)
    elif seen != None:
        count += len(seen)
        seen = None
if seen != None:
    count += len(seen)
print(count)
