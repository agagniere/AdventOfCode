from utils import lines
import re

towels = input().split(', ')
expression = re.compile('(' + '|'.join(towels) + ')+')
input()
print(sum(1 for line in lines() if expression.fullmatch(line)))
