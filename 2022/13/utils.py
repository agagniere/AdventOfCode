def lines():
    while True:
        try:
            yield input()
        except:
            break

def store_nonempty_lines():
    return [line for line in lines() if line]

def compare(A, B):
    if type(A) != type(B):
        if type(A) == int:
            return compare([A], B)
        return compare(A, [B])
    if type(A) == int:
        return 1 if A < B else -1 if A > B else 0
    for a, b in zip(A, B):
        R = compare(a, b)
        if R != 0:
            return R
    return compare(len(A), len(B))
