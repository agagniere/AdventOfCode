def priority(c):
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

result = 0
while True:
    try:
        line = input()
    except:
        break
    H = len(line) // 2
    first = set(line[:H])
    second = set(line[H:])
    common = next(iter(first & second))
    print(common)
    result += priority(common)
print(result)
