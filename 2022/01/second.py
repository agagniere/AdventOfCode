calories = []
current = 0
while True:
    try:
        line = input()
        if not line:
            print(current)
            calories.append(current)
            current = 0
        else:
            current += int(line)
    except:
        break
calories.sort(reverse = True)
print('top3:', calories[:3])
print('->', sum(calories[:3]))
