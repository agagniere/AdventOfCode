from collections import Counter, defaultdict

def lines():
    while True:
        try:
            yield input()
        except:
            break

polymer = input()
input()
freq = Counter(polymer)
pairs = defaultdict(int)
for a, b in zip(polymer[:-1], polymer[1:]):
    pairs[a + b] += 1

instructions = []
for line in lines():
    pair, new = line.split(' -> ')
    instructions += [(pair, new)]

for step in range(40):
    next_pairs = pairs.copy()
    for pair, new in instructions:
        if pairs[pair]:
            next_pairs[pair] -= pairs[pair]
            freq[new] += pairs[pair]
            a, b = pair
            next_pairs[a + new] += pairs[pair]
            next_pairs[new + b] += pairs[pair]
    pairs = next_pairs

R = sorted(freq.values())
print(R[-1] - R[0])
