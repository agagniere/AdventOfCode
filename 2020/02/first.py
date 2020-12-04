valid_count = 0

for i in range(1000):
    r, c, password = input().split()
    mini, maxi = map(int, r.split('-'))
    c = c[0]
    #print("Letter", c, "from", mini, "to", maxi, "times in", password)
    occurences = password.count(c)
    if mini <= occurences and occurences <= maxi:
        valid_count += 1
print(valid_count)
