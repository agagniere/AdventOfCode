from utils import *

def single(line):
    opponent, outcome = map(convert, line.split())
    return score(opponent, (2 + opponent + outcome) % 3)

print(sum(map(single, lines)))
