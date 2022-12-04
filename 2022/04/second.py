def create_range(text):
    start, end = map(int, text.split('-'))
    return range(start, end + 1)

count = 0
while True:
    try:
        A, B = sorted(map(create_range, input().split(',')), key=lambda x:x.start)
        if B.start < A.stop:
            count += 1
    except:
        break
print(count)
