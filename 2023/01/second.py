def lines():
    while True:
        try:
            yield input()
        except:
            break

L = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

result = 0
for line in lines():
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            for sub in [3,4,5]:
                if line[i:][:sub] in L:
                    digits.append(L[line[i:][:sub]])
    result += 10 * digits[0] + digits[-1]
print(result)
