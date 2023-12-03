def lines():
    while True:
        try:
            yield input()
        except:
            break

def find_duplicate(changes: list[int]):
    seen = set()
    freq = 0
    while True:
        for change in changes:
            if freq in seen:
                return freq
            seen.add(freq)
            freq += change


changes = [int(line) for line in lines()]

print('Resulting frequency:', sum(changes))
print('First repeated frequency:', find_duplicate(changes))
