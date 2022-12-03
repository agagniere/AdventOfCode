def priority(c):
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

result = 0
while True:
    try:
        A = set(input())
        B = set(input())
        C = set(input())
    except:
        break
    common = next(iter(A & B & C))
    print(common)
    result += priority(common)
print(result)
