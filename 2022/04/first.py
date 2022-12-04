def create_range(text):
    start, end = map(int, text.split('-'))
    return range(start, end + 1)

count = 0
while True:
    try:
        A, B = sorted(map(create_range, input().split(',')), key=len)
        if A.start in B and A.stop-1 in B:
            count += 1
    except:
        break
print(count)
