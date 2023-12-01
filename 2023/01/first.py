def lines():
    while True:
        try:
            yield input()
        except:
            break

result = 0
for line in lines():
    digits = list(filter(str.isdigit, line))
    result += int(digits[0] + digits[-1])
print(result)
