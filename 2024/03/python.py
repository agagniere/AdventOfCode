from utils import lines
import re
from math import prod

parse = re.compile(r'mul\((\d+)[,](\d+)\)')
print(sum(sum(prod(map(int, m.groups())) for m in parse.finditer(line)) for line in lines()))
