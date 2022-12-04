import sys

result = 0
for line in sys.stdin.readlines():
    values = list(map(int, line.split()))
    result += max(values) - min(values)
print(result)
