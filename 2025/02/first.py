ranges = [[int(b) for b in r.split('-')] for r in input().split(',')]

invalids = set()
for i in range(1, 10):
    invalids.add(i * 10 + i)
for i in range(10, 100):
    invalids.add(i * 100 + i)
for i in range(100, 1000):
    invalids.add(i * 1000 + i)
for i in range(1000, 10000):
    invalids.add(i * 10000 + i)
for i in range(10000, 100000):
    invalids.add(i * 100000 + i)
print('generated', len(invalids), 'invalid IDs')

result = 0
for L,U in ranges:
    for i in range(L, U+1):
        if i in invalids:
            result += i
            print('found invalid ID', i)
print(result)
