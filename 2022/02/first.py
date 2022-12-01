
def round(other, you):
    o = ord(other) - ord('A')
    y = ord(you) - ord('X')
    return y + 1 + (3 if o == y else 6 * ((o+1)%3==y))

score = 0
while True:
    try:
        other, you = input().split()
    except:
        break
    score += round(other, you)
print(score)
