valid_count = 0

for i in range(1000):
    r, c, pwd = input().split()
    p, q = map(lambda s: int(s) - 1, r.split('-'))
    c = c[0]
    if (c == pwd[p] or c == pwd[q]) and pwd[p] != pwd[q]:
        valid_count += 1
    #print("The letter {} is {} or {} but not both : {}".format(c, pwd[p], pwd[q], c in pwd[p]+pwd[q] and len(set([c, pwd[p], pwd[q]])) == 2))

print(valid_count)
