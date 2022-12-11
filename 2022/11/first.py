from utils import *

monkeys = [Monkey(ini) for ini in non_empty_line_group(lines())]
run_rounds(monkeys, 20, True)
print([m.count for m in monkeys])
print(prod(sorted([m.count for m in monkeys])[-2:]))
