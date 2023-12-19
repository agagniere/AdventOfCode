from utils import lines


def extractValue(line):
    digits = list(filter(str.isdigit, line))
    return int(digits[0] + digits[-1])

if __name__ == '__main__':
    print(sum(map(extractValue, lines())))
