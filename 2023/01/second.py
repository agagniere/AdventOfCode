from utils import lines

spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_from_string = {digit: i + 1 for i, digit in enumerate(spelled)}

def extractValue(line: str) -> int:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            for sub in [3,4,5]:
                if line[i:][:sub] in digit_from_string:
                    digits.append(digit_from_string[line[i:][:sub]])
    return 10 * digits[0] + digits[-1]

if __name__ == '__main__':
    print(sum(map(extractValue, lines())))
