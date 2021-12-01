from collections import deque

count = 0
current = 0
queue = deque()
while True:
    try:
        v = int(input())
    except:
        break
    prev = current
    current += v
    queue.append(v)
    if len(queue) > 3:
        current -= queue.popleft()
        if prev < current:
            count += 1
print(count)
