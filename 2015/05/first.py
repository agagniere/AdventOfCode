import re

count = 0
while True:
    try:
        line = input()
    except:
        break
    if True in [no in line for no in ["ab", "cd", "pq", "xy"]]:
        continue
    if sum([line.count(v) for v in "aeiou"]) < 3:
        continue
    if re.search(r'([a-z])\1', line) != None:
        count += 1

print(count)
