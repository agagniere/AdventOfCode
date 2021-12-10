score_per_char = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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

all_scores = []
for line in lines():
    queue = []
    is_corrupt = False
    for c in line:
        if c in brackets:
            queue.append(brackets[c])
        elif queue and c != queue.pop():
            is_corrupt = True
            break
    if not is_corrupt:
        all_scores += [int(''.join([str(score_per_char[c]) for c in queue[::-1]]), base = 5)]

print(sorted(all_scores)[len(all_scores) // 2])
