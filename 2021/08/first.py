from collections import defaultdict

correct = {
    '0': "abcefg",
    '1': "cf",
    '2': "acdeg",
    '3': "acdfg",
    '4': "bcdf",
    '5': "abdfg",
    '6': "abdefg",
    '7': "acf",
    '8': "abcdefg",
    '9': "abcdfg"
}
by_length = defaultdict(list)
for key, value in correct.items():
    by_length[len(value)] += [key]
unique = {L:D[0] for L, D in by_length.items() if len(D) == 1}

count = 0
while True:
    try:
        line = input()
    except:
        break
    four_output = line.split(' | ')[1].split()
    count += len(list(filter(lambda x: len(x) in unique, four_output)))
print(count)
