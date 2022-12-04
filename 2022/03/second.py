from utils import *

def three(lines):
    return priority(common(*lines))

print(sum(map(three, grouper(lines, 3))))
