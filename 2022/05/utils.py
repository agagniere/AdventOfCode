def lines():
    while True:
        try:
            yield input()
        except:
            break

def non_empty_line_group(iterable):
    acc = []
    for line in iterable:
        if line:
            acc.append(line)
        elif acc:
            yield acc
            acc = []
    if acc:
        yield acc

def extract_stacks(drawing):
    stacks = [list() for _ in drawing[0][::4]]
    for col, stack in filter(lambda p:p[1].isdigit(), enumerate(drawing[-1])):
        stacks[int(stack) - 1] = [row[col] for row in reversed(drawing[:-1]) if row[col].isalpha()]
    return stacks
