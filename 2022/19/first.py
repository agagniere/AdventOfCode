from utils import *

ans = 0
B = parse(lines())
for i, b in enumerate(B):
    print(i)
    Q = b.quality_level(24, 7)
    ans += (i + 1) * Q
    print(Q)
print(ans)
