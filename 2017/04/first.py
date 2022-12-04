import sys

def check_line(line):
    words = line.split()
    return len(words) == len(set(words))

print(sum(map(check_line, sys.stdin.readlines())))
