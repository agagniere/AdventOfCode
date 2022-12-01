def round(other, outcome):
    o = ord(other) - ord('A')
    f = ord(outcome) - ord('X')
    y = (3 + o - 1 + f) % 3
    return y + 1 + (3 if o == y else 6 * ((o+1)%3==y))

score = 0
while True:
    try:
        other, outcome = input().split()
    except:
        break
    score += round(other, outcome)
print(score)
