import sys

acc = 0
for line in sys.stdin.readlines():
    n = 0
    for c in line.strip():
        n *= 5
        n += '=-012'.index(c) - 2
    print(n)
    acc += n
print(acc)

def to_snafu(n):
    snafu = []
    while n:
        d = n % 5
        snafu += ['012=-'[d]]
        n //= 5
        n += d > 2
    return ''.join(reversed(snafu))
print(to_snafu(acc))
