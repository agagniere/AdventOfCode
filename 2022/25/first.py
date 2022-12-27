import sys

def from_snafu(s: str) -> int:
    ans = 0
    for c in s:
        ans *= 5
        ans += '=-012'.index(c) - 2
    return ans

def to_snafu(n: int) -> str:
    snafu = []
    while n:
        digit = n % 5
        snafu.append('012=-'[digit])
        n //= 5
        n += (digit > 2)
    return ''.join(reversed(snafu))

print(to_snafu(sum(map(from_snafu, sys.stdin.read().split('\n')))))
