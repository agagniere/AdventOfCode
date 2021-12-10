score_per_char = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def lines():
    while True:
        try:
            yield input()
        except:
            break

total = 0
for line in lines():
    queue = []
    for c in line:
        if c in brackets:
            queue.append(brackets[c])
        elif queue and c != queue.pop():
            total += score_per_char[c]
print(total)
