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
            print("New :", seen)
        else:
            seen &= set(line)
            print("Inter :", seen)
    elif seen != None:
        print("Final :", seen)
        count += len(seen)
        seen = None
if seen != None:
    print("Final :", seen)
    count += len(seen)
print(count)
