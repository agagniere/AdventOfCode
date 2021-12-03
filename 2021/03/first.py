def int_from_bl(bl):
    ans = 1 if bl[-1] else 0
    if len(bl) > 1:
        ans += 2 * int_from_bl(bl[:-1])
    return ans

huge = input()
L = len(huge)
C = 1
while True:
    try:
        huge += input()
        C += 1
    except:
        break
stat = [sum(map(int, huge[i::L])) for i in range(L)]
print(stat)
H = C // 2
gamma = int_from_bl([b > H for b in stat])
epsilon = int_from_bl([b <= H for b in stat])
print(gamma, epsilon, gamma * epsilon)
