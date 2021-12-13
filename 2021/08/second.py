from collections import defaultdict

def common(a, b):
    return len(set(a) & set(b))

def sort_strings(strings):
    result = []
    for string in strings:
        result += [''.join(sorted(string))]
    return result

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

common_matrix = {d: {o: common(D, O) for o, O in correct.items()} for d, D in correct.items()}
by_common = {d: defaultdict(set) for d in correct}
for d, in_common in common_matrix.items():
    for o, c in in_common.items():
        by_common[d][c].add(o)

total = 0
while True:
    try:
        line = input()
    except:
        break
    ten_figures, four_output = [sort_strings(half.split()) for half in line.split(' | ')]
    digit_from_figure = {figure: set(by_length[len(figure)]) for figure in ten_figures}
    figure_from_digit = {by_length[len(figure)][0]: figure for figure in ten_figures if len(by_length[len(figure)]) == 1}
    for figure, candidates in filter(lambda kv: len(kv[1]) > 1, digit_from_figure.items()):
        for digit, other in figure_from_digit.items():
            candidates &= by_common[digit][common(figure, other)]
        figure_from_digit[next(iter(candidates))] = figure
    total += int(''.join([next(iter(digit_from_figure[figure])) for figure in four_output]))
print(total)
