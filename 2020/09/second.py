#target=127
target = 31161678

# Read input
seq = []
while True:
    try:
        seq += [int(input())]
    except:
        break

sums = [seq]
n = 1
found = False
while not found and n < len(seq):
    print("Sums of", n+1, "elements")
    cur = []
    for i in range(len(sums[-1]) - 1):
        x = sums[-1][i] + seq[i + n]
        cur += [x]
        if x == target:
            subset = seq[i:][:n]
            m = min(subset)
            M = max(subset)
            print(i, i+n, ":", m, '+', M, "=", m + M)
            found = True
            break
    sums += [cur]
    n += 1
