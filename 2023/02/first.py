from utils import lines

threshold = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_possible(line):
    game, draws = line.split(': ')
    for draw in draws.split('; '):
        for group in draw.split(', '):
            count, color = group.split(' ')
            count = int(count)
            if count > threshold[color]:
                return False
    return True

if __name__ == '__main__':
    print(sum([i + 1 for i, line in enumerate(lines()) if is_possible(line)]))
