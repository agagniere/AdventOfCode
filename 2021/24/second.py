def lines():
    while True:
        try:
            yield input()
        except:
            break

smallest = ['?'] * 14
largest = ['?'] * 14
stack = []
for i, line in enumerate(lines()):
    a, b = map(int, line.split())
    if b < 0:
        j, p = stack.pop()
        d = p + b
        largest[j] = min(9, 9 - d)
        largest[i] = min(9, 9 + d)
        smallest[j] = max(1, 1 - d)
        smallest[i] = max(1, 1 + d)
    else:
        stack += [(i, a)]
print("Largest :", ''.join(map(str, largest)))
print("Smallest :", ''.join(map(str, smallest)))
