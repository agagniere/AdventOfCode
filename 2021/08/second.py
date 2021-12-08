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
translate = {value: key for key, value in correct.items()}
by_length = defaultdict(list)
for key, value in correct.items():
    by_length[len(value)] += [key]
unique = {L:D[0] for L, D in by_length.items() if len(D) == 1}

def common(a, b):
    return len(set(a) & set(b))

total = 0
while True:
    try:
        line = input()
    except:
        break
    halves = line.split(' | ')
    ten_digits = halves[0].split()
    four_output = halves[1].split()

    local_translate = {}
    local = {}
    for D in ten_digits:
        d = ''.join(sorted(D))
        if len(d) in unique:
            local_translate[d] = unique[len(d)]
            local[unique[len(d)]] = d
    for D in ten_digits:
        d = ''.join(sorted(D))
        if d not in local_translate:
            r = None
            if len(d) == 5:
                if common(d, local['1']) == 2:
                    r = '3'
                elif common(d, local['4']) == 3:
                    r = '5'
                else:
                    r = '2'
            if len(d) == 6:
                if common(d, local['1']) == 1:
                    r = '6'
                elif common(d, local['4']) == 3:
                    r = '0'
                else:
                    r = '9'
            if r:
                local_translate[d] = r
                local[r] = d
    res = ''.join([local_translate.get(''.join(sorted(n)), '?') for n in four_output])
    print(res)
    total += int(res)
print(total)
