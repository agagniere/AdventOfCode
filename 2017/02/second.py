import sys

result = 0
for line in sys.stdin.readlines():
    values = sorted(map(int, line.split()))
    found = False
    for I in reversed(range(len(values))):
        big = values[I]
        for small in values[:I]:
            if big % small == 0:
                print(f'{big:4} / {small:3} = {big//small:2}')
                result += big // small
                found = True
                break
        if found:
            break
print(result)
