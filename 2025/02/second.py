invalids = set()
for i in range(1, 10):
    invalids.add(i * 11)
    invalids.add(i * 111)
    invalids.add(i * 1111)
    invalids.add(i * 11111)
    invalids.add(i * 111111)
    invalids.add(i * 1111111)
    invalids.add(i * 11111111)
    invalids.add(i * 111111111)
    invalids.add(i * 1111111111)
for i in range(10, 100):
    invalids.add(i * 101)
    invalids.add(i * 10101)
    invalids.add(i * 1010101)
    invalids.add(i * 101010101)
for i in range(100, 1000):
    invalids.add(i * 1001)
    invalids.add(i * 1001001)
for i in range(1000, 10000):
    invalids.add(i * 10001)
for i in range(10000, 100000):
    invalids.add(i * 100001)
print('generated', len(invalids), 'invalid IDs')

ranges = [[int(b) for b in r.split('-')] for r in input().split(',')]

result = 0
for L,U in ranges:
    for i in range(L, U+1):
        if i in invalids:
            result += i
print(result)
